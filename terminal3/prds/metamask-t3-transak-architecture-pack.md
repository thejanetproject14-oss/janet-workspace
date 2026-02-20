# MetaMask x terminal 3 x Transak
## 80/20 Architecture & Security Pack

**Author:** Janani G, Head of Product -- terminal 3
**Prepared by:** Janet ✦ (Lead PM)
**Date:** February 20, 2026
**Purpose:** Security-ready architecture pack for MetaMask security & engineering review
**Scope:** Native Flow (Deposit) -- US & EU via Transak
**Status:** Draft for MetaMask review

---

## 1. System Overview

### 1.1 High-Level Data Flow

```
USER (MetaMask Wallet)
    │
    │ [1] User taps Deposit
    ▼
METAMASK FRONTEND (no backend)
    │
    │ [2] Invocation: app_id, env, country, amount?, theme, provider
    ▼
TERMINAL 3 (Identity Orchestration Layer)
    │
    ├── [3] Login: email + OTP
    ├── [4] KYC L1/L2 via Veriff
    ├── [5] VC issuance (SD-JWT)
    ├── [6] VP generation (OID4VP)
    │
    │ [7] VP + auth handoff
    ▼
TRANSAK (On-ramp Provider)
    │
    │ [8] Payment processing
    │ [9] Crypto fulfillment
    │
    │ [10] Order status (polled by MetaMask)
    ▼
USER (crypto in wallet)
```

### 1.2 Roles & Responsibilities

| Party | Owns | Does NOT Own |
|---|---|---|
| **MetaMask** | Frontend UX, user consent, wallet connection, order status polling | Backend, KYC state, identity storage, provider routing |
| **terminal 3** | Authentication, KYC orchestration, VC issuance, VP generation, DID registry, revocation, regulatory vault, duplicate identity prevention | Payment processing, fiat handling, crypto fulfillment |
| **Transak** | Payment processing, fiat-to-crypto execution, settlement, compliance (as licensed entity) | KYC collection (delegated to terminal 3), user authentication |

---

## 2. Per-API-Call System Diagram

### Step 1: MetaMask Invocation → terminal 3

```
METAMASK                              TERMINAL 3
   │                                      │
   │  POST /v1/sessions/create            │
   │  ──────────────────────────────►     │
   │  {                                    │
   │    app_id: "metamask",                │
   │    env: "production",                 │
   │    country: "US",                     │
   │    amount: 500 (optional),            │
   │    currency: "USD" (optional),        │
   │    theme: "dark",                     │
   │    provider: "transak"                │
   │  }                                    │
   │                                      │
   │  ◄──────────────────────────────     │
   │  200 OK                               │
   │  {                                    │
   │    session_id: "t3_sess_xxx",         │
   │    required_level: "L2",              │
   │    action: "login",                   │
   │    login_url: "https://..."           │
   │  }                                    │
   │                                      │
```

**Security notes:**
- If `amount` is missing, terminal 3 conservatively assumes L2 KYC required
- Country is validated against IP (but MetaMask explicit param takes precedence)
- `app_id` + `env` used for client authentication
- Session expires after configurable TTL

### Step 2: User Login (Email + OTP)

```
USER                    TERMINAL 3
  │                         │
  │  [UI: Enter email]      │
  │                         │
  │  POST /v1/auth/login    │
  │  ──────────────────►   │
  │  { email: "user@..." }  │
  │                         │── Generate OTP
  │                         │── Send OTP to email
  │  ◄──────────────────   │
  │  { status: "otp_sent" } │
  │                         │
  │  POST /v1/auth/verify   │
  │  ──────────────────►   │
  │  { email, otp: "123456"}│
  │                         │── Verify OTP
  │                         │── Create/lookup account
  │                         │── Check: account exists? KYC status?
  │  ◄──────────────────   │
  │  {                      │
  │    user_id: "t3_xxx",   │
  │    auth_token: "jwt...",│
  │    kyc_status: "none",  │  ← or "L1", "L2"
  │    next_action: "kyc"   │  ← or "vp_share" if already verified
  │  }                      │
  │                         │
```

**Security notes:**
- OTP: 6-digit, 5-minute expiry, 3 max attempts
- Auth token: JWT, short-lived, signed by terminal 3
- If account exists with completed KYC → skip to VP sharing (zero-friction return)
- If KYC abandoned previously → restart from beginning

**Decision point:**
```
IF account_exists AND kyc_complete AND credential_valid
  → Skip to Step 5 (VP generation)
IF account_exists AND kyc_incomplete
  → Resume from KYC step
IF new_account
  → Proceed to Step 3 (KYC)
```

### Step 3: KYC Level 1 (USA)

```
USER                    TERMINAL 3              VERIFF
  │                         │                      │
  │  [UI: Country of        │                      │
  │   Residence selection]  │                      │
  │                         │                      │
  │  POST /v1/kyc/l1        │                      │
  │  ──────────────────►   │                      │
  │  {                      │                      │
  │    first_name,          │                      │
  │    last_name,           │                      │
  │    phone,               │                      │
  │    dob,                 │                      │
  │    ssn,                 │                      │
  │    address: {           │                      │
  │      line1, line2,      │                      │
  │      city, state,       │                      │
  │      zip, country       │                      │
  │    }                    │                      │
  │  }                      │                      │
  │                         │── SSN + Name match ──►│
  │                         │◄── Match result ─────│
  │                         │                      │
  │                         │── Duplicate check     │
  │                         │   (internal)          │
  │                         │                      │
  │  ◄──────────────────   │                      │
  │  {                      │                      │
  │    kyc_level: "L1",     │                      │
  │    next_action: "l2"    │  ← if amount > $150  │
  │    OR "vp_share"        │  ← if amount <= $150 │
  │  }                      │                      │
```

**Validation rules:**
- `residence_country == "US"` AND `document_country == "US"` → proceed
- `residence_country != "US"` → block (not supported in Phase 1)
- `residence_country == "US"` AND `document_country != "US"` → can proceed
- Check against Transak blacklist countries
- Duplicate identity check: same SSN cannot create multiple terminal 3 accounts

**Decision point:**
```
IF amount IS NULL OR amount > 150
  → Require L2 KYC (Step 4)
IF amount <= 150
  → L1 sufficient, proceed to VP (Step 5)
```

### Step 4: KYC Level 2 (Document + Liveness)

```
USER                    TERMINAL 3              VERIFF
  │                         │                      │
  │  [UI: Veriff embedded   │                      │
  │   document upload +     │                      │
  │   liveness check]       │                      │
  │                         │                      │
  │  ── Veriff SDK flow ──────────────────────────►│
  │                         │                      │── Doc verification
  │                         │                      │── Liveness check
  │                         │                      │── Extract: name, DOB,
  │                         │                      │   doc number, expiry,
  │                         │                      │   country, sex, etc.
  │                         │◄── Webhook: result ──│
  │                         │                      │
  │                         │── Validate:           │
  │                         │   doc_country == entered_country?
  │                         │   name matches L1 data?
  │                         │                      │
  │                         │── Store in Regulatory Vault:
  │                         │   • Liveness video
  │                         │   • Passport image
  │                         │   • Portrait image
  │                         │                      │
  │  ◄──────────────────   │                      │
  │  {                      │                      │
  │    kyc_level: "L2",     │                      │
  │    next_action:         │                      │
  │      "vp_share"         │                      │
  │  }                      │                      │
```

**Accepted documents:** National ID, Passport, Driver's License
**Rejection rules:**
- If passport issuing country != entered document country → reject with error, redirect to re-do KYC
- If liveness fails → reject, allow retry

**Regulatory Vault storage (per jurisdiction rules):**
- Liveness check video
- Passport/ID image
- Portrait image
- Retention: per local regulation (varies by jurisdiction)

### Step 5: Verifiable Credential Issuance

```
TERMINAL 3 (internal)
  │
  │── Issue VC: Email + Phone (SD-JWT)
  │   {
  │     type: "EmailPhoneCredential",
  │     email: "user@..." (verified),
  │     phone: "+1..." (unverified),
  │     signed_by: "terminal3"
  │   }
  │
  │── Issue VC: KYC (SD-JWT)
  │   {
  │     type: "KYCCredential",
  │     kyc_level: 2,
  │     first_name, last_name, dob,
  │     doc_number, doc_type, doc_expiry,
  │     doc_country, sex, birth_place,
  │     address: { street, city, country, postcode },
  │     portrait_image_hash,
  │     signed_by: "terminal3",
  │     on_behalf_of: "veriff",
  │     verified_at: "2026-02-20T...",
  │     expires_at: "2027-02-20T..."
  │   }
  │
  │── Register DID
  │   {
  │     did: "did:t3:user_xxx",
  │     status: "active",
  │     issuer: "terminal3",
  │     revocation_status: "valid"
  │   }
  │
```

**VC format:** SD-JWT (selective disclosure)
**Signing:** terminal 3 signs on behalf of Veriff
**DID registry:** Enables verifiers to check issuer authenticity + revocation status

### Step 6: VP Sharing with Transak (OID4VP)

```
TRANSAK                 TERMINAL 3              USER
  │                         │                      │
  │  OID4VP Request         │                      │
  │  ──────────────────►   │                      │
  │  {                      │                      │
  │    requested_fields: [  │                      │
  │      first_name,        │                      │
  │      last_name,         │                      │
  │      email,             │                      │
  │      phone,             │                      │
  │      billing_address,   │                      │
  │      doc_verification,  │                      │
  │      liveness           │                      │
  │    ]                    │                      │
  │  }                      │                      │
  │                         │── [UI: Consent screen]│
  │                         │   "Share with Transak:│
  │                         │    name, email, ..."  │
  │                         │  ◄── User consents ──│
  │                         │                      │
  │                         │── Generate VP          │
  │                         │   (selective disclosure│
  │                         │    of requested fields)│
  │  ◄──────────────────   │                      │
  │  VP (SD-JWT)            │                      │
  │  {                      │                      │
  │    holder: "did:t3:xxx",│                      │
  │    disclosed: {         │                      │
  │      first_name: "...", │                      │
  │      last_name: "...",  │                      │
  │      email: "...",      │                      │
  │      ...                │                      │
  │    },                   │                      │
  │    signature: "..."     │                      │
  │  }                      │                      │
  │                         │                      │
  │── Verify VP using        │                      │
  │   Verifier SDK           │                      │
  │   (check signature,      │                      │
  │    issuer, expiry,        │                      │
  │    revocation via DID)    │                      │
  │                         │                      │
```

**Transak verification:**
- Uses terminal 3 Verifier SDK
- Checks: VP signature valid? Issuer trusted? Credential expired? Revoked?
- Reference: terminal 3 OID4VP spec (https://docs.terminal3.io/api-reference/openid4vp-vc/openid4vp/authorization)

### Step 7: Transak SSO + Order Execution

```
USER                    TERMINAL 3              TRANSAK
  │                         │                      │
  │                         │── Auth Reliance ─────►│
  │                         │   (user auth token +  │
  │                         │    verified email)     │
  │                         │                      │── Create/login user
  │                         │                      │── Accept VP data
  │                         │                      │
  │  ◄── Redirect to Transak payment flow ────────│
  │                                                │
  │  [User completes payment: card, bank, etc.]    │
  │  ──────────────────────────────────────────►  │
  │                                                │── Process payment
  │                                                │── Fulfill crypto
  │                                                │
```

### Step 8: Order Status (Polling)

```
METAMASK                                    TRANSAK
  │                                            │
  │  GET /v1/orders/{order_id}/status          │
  │  ──────────────────────────────────────►  │
  │  (every 10 seconds)                        │
  │                                            │
  │  ◄──────────────────────────────────────  │
  │  { status: "PROCESSING" | "COMPLETED" |    │
  │    "FAILED", tx_hash: "0x..." }            │
  │                                            │
```

**Note:** MetaMask currently uses polling (no webhook capability due to no backend). This is acceptable for MVP. Webhook-based notification is a future optimization.

---

## 3. Data Flow & Security Matrix

### 3.1 What Data Goes Where

| Data Element | MetaMask | terminal 3 | Transak | Regulatory Vault |
|---|---|---|---|---|
| Wallet address | ✅ has | ✅ has | ✅ receives | — |
| Email | — | ✅ verified | ✅ receives via VP | — |
| Phone | — | ✅ collected (unverified) | ✅ receives via VP | — |
| First/Last Name | — | ✅ collected + verified | ✅ receives via VP | — |
| DOB | — | ✅ collected + verified | ✅ receives via VP | — |
| SSN | — | ✅ collected (L1 match check) | ❌ NOT shared | — |
| Address | — | ✅ collected | ✅ receives via VP | — |
| Passport image | — | ❌ not retained long-term | ❌ NOT shared | ✅ stored |
| Portrait image | — | ❌ not retained long-term | ❌ NOT shared | ✅ stored |
| Liveness video | — | ❌ not retained long-term | ❌ NOT shared | ✅ stored |
| KYC level/status | — | ✅ owns | ✅ receives via VP | — |
| Order data | ✅ polls status | ❌ not in MVP | ✅ owns | — |

### 3.2 Data Encryption & Storage

| Storage | Method | Access Control |
|---|---|---|
| **terminal 3 Credential Store** | TEE-protected, encrypted at rest | terminal 3 internal only |
| **SD-JWT Credentials** | Signed, selective disclosure | User-consented sharing only |
| **Regulatory Vault** | Encrypted, jurisdiction-aware retention | Regulatory authorities on demand |
| **DID Registry** | Public metadata (no PII) | Verifiers can check status |

### 3.3 Data Retention

| Data Type | Retention Policy |
|---|---|
| Email, phone, name, address | Until credential expiry (12 months) or user revocation |
| SSN | Hashed after L1 match verification. Raw SSN NOT stored. |
| Document images | Regulatory Vault only -- 30 days post-verification, then hash-only |
| Liveness video | Regulatory Vault only -- per jurisdiction retention rules |
| KYC credentials (SD-JWT) | 12 months (L2), renewable |
| Audit trail | 7 years (regulatory compliance) |

---

## 4. Orchestration Decision Logic

### 4.1 KYC Level Decision Tree

```
START
  │
  ▼
[Country == US and not NY?]──NO──► BLOCK (not supported)
  │
  YES
  │
  ▼
[Account exists?]──YES──►[KYC complete and valid?]──YES──► SKIP TO VP SHARE
  │                          │
  NO                         NO
  │                          │
  ▼                          ▼
[Create account]         [Resume KYC]
  │
  ▼
[Collect L1: name, phone, DOB, SSN, address]
  │
  ▼
[SSN + Name match via Veriff]──FAIL──► REJECT + error
  │
  PASS
  │
  ▼
[Duplicate identity check]──DUPLICATE──► BLOCK + error
  │
  PASS
  │
  ▼
[Amount provided?]
  │           │
  YES         NO
  │           │
  ▼           ▼
[Amount > $150?]  [Assume L2 required]
  │       │              │
  YES     NO             │
  │       │              │
  ▼       ▼              │
[L2]   [L1 sufficient]   │
  │       │              │
  │       ▼              │
  │    VP SHARE          │
  │                      │
  ▼◄─────────────────────┘
[Veriff: doc upload + liveness]
  │
  ▼
[Doc country == entered country?]──NO──► REJECT + retry
  │
  YES
  │
  ▼
[Issue VCs + store in Regulatory Vault]
  │
  ▼
VP SHARE → TRANSAK
```

### 4.2 Provider Routing (Phase 1: Declared)

```
Phase 1: provider = "transak" (declared by MetaMask)
  terminal 3 role: KYC gating + VP construction

Phase 2+: intent-based routing (future)
  terminal 3 role: provider selection + KYC gating + VP construction
```

---

## 5. Edge Cases & Off-Happy-Path Flows

### 5.1 Failure Scenarios

| Scenario | Behavior | User Experience |
|---|---|---|
| **OTP expired** | OTP invalid after 5 min | "Code expired. Request a new one." |
| **OTP max attempts** | 3 failed attempts | "Too many attempts. Please wait 30 minutes." |
| **SSN match fails** | Veriff SSN+name mismatch | "Information doesn't match records. Please check and retry." |
| **Duplicate SSN** | Same SSN already in system | "This identity is already registered. Please login instead." |
| **Veriff doc rejection** | Document unreadable / fake | "Document could not be verified. Please try again with a clearer image." |
| **Liveness failure** | Biometric check fails | "Face verification failed. Please try again in good lighting." |
| **Doc country mismatch** | Passport country != entered country | "Passport does not match selected country. Please re-do KYC." |
| **KYC abandoned mid-flow** | User closes before completing | Next visit: restart KYC from beginning |
| **VP sharing declined** | User refuses consent | Cannot proceed to Transak. Show explanation. |
| **Transak rejects VP** | VP verification fails | terminal 3 logs error. User shown retry option. |
| **Transak order fails** | Payment processing error | Handled by Transak UX. terminal 3 not involved. |
| **Network timeout** | Any API call times out | Retry with exponential backoff. Max 3 retries. |

### 5.2 Step-Up Scenarios

| Trigger | Action |
|---|---|
| User at L1 attempts transaction > $150 | Prompt L2 KYC (doc + liveness) |
| User at L1/L2, Transak requests additional info | terminal 3 collects and issues updated VP |
| ACH bank transfer (any amount) | Require L2 regardless of amount |
| Credential expired (>12 months) | Prompt re-verification |
| Revoked credential | Block + prompt re-verification |

### 5.3 Manual Review

| Scenario | Owner | Process |
|---|---|---|
| Veriff flags for manual review | Veriff | Async review. User notified when complete. |
| Fraud suspicion (duplicate patterns) | terminal 3 | Internal review. User blocked pending investigation. |
| Regulatory request for Vault data | terminal 3 | Compliance team provides encrypted access. |

---

## 6. SDK & Integration Points

### 6.1 terminal 3 → MetaMask
- **Integration method:** SDK or URL-based (no MetaMask backend needed)
- **Auth:** Token-based, frontend-initiated
- **Data flow:** MetaMask invocation params → terminal 3 session → KYC flow → redirect to Transak

### 6.2 terminal 3 → Transak
- **VP sharing:** OID4VP (terminal 3 spec)
- **Auth handoff:** Transak Auth Reliance product (email-based)
- **Verification:** Verifier SDK provided to Transak for VP validation
- **DID registry:** Public endpoint for Transak to check issuer + revocation

### 6.3 Transak → MetaMask
- **Order status:** Polling (GET every 10s, existing pattern)
- **No terminal 3 involvement** in order execution or settlement

### 6.4 SDKs Provided by terminal 3
| SDK | Purpose | Consumer |
|---|---|---|
| **Verifier SDK** | Validate VP signature, issuer, expiry, revocation | Transak |
| **Identity SDK** | Login + KYC flow (embedded or redirect) | MetaMask frontend |

**Security team benefit:** Only ONE SDK to audit (terminal 3 Identity SDK) for the MetaMask integration. Transak audits the Verifier SDK separately.

---

## 7. Security Checklist

| Item | Status | Notes |
|---|---|---|
| Data at rest encryption | ✅ TEE-protected | Credential store |
| Data in transit encryption | ✅ TLS 1.3 | All API calls |
| PII minimization | ✅ Selective disclosure | SD-JWT reveals only requested fields |
| SSN handling | ✅ Hash after match | Raw SSN not stored |
| Biometric data | ✅ Regulatory Vault | Not shared with Transak |
| Credential revocation | ✅ DID registry | Real-time revocation checking |
| Duplicate identity prevention | ✅ Built-in | Configurable per client |
| GDPR right to be forgotten | ✅ Supported | User can revoke credentials + request deletion |
| Audit trail | ✅ Immutable log | 7-year retention |
| SOC 2 compliance | ℹ️ Transak is SOC 2 compliant | terminal 3 status: confirm |
| Rate limiting | ✅ API gateway | Per-client, per-endpoint |
| Fraud detection | ✅ Duplicate SSN, document checks | Future: device ID, VPN checks, behavioral signals |

---

## 8. Open Items for Security Review

| # | Item | Question for MetaMask Security |
|---|---|---|
| 1 | Auth token format | JWT acceptable? Preferred signing algorithm? |
| 2 | Session TTL | What is acceptable session duration? |
| 3 | MetaMask invocation auth | How does terminal 3 validate the invocation is from MetaMask? App ID + env sufficient? |
| 4 | Consent UX | Does MetaMask security need to review the VP consent screen? |
| 5 | Device signals | MetaMask mentioned device ID and VPN checks. Which signals can MetaMask pass to terminal 3? |
| 6 | SDK audit scope | terminal 3 Identity SDK -- what level of audit does MetaMask security require? |
| 7 | Regulatory Vault access | What is MetaMask's expectation for regulatory access to Vault data? |
| 8 | Incident response | What is the expected SLA for identity-related incident notification? |

---

*This document is designed as an 80/20 architecture pack: sufficient detail for MetaMask security to begin review without requiring piecemeal Q&A. All architecture decisions are proposals pending joint alignment.*
