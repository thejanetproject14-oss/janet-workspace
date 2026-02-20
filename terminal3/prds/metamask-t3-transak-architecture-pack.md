# MetaMask x Terminal 3 x Transak
## 80/20 Architecture & Security Pack

**Author:** Janani G, Head of Product -- Terminal 3
**Prepared by:** Janet ✦ (Lead PM)
**Date:** February 20, 2026
**Purpose:** Security-ready architecture pack for MetaMask security & engineering review
**Scope:** Native Flow (Deposit) -- US & EU via Transak
**Status:** Draft for MetaMask review

---

## Document Accuracy Notes

**This document represents proposed architecture. Diagrams show illustrative flows. Actual API contracts, VC schemas, and integration patterns to be finalized during engineering alignment sessions with MetaMask and Transak.**

Features marked as [PROPOSED], [PLANNED], or [TBC] are not currently implemented and require engineering development or partner alignment before availability.

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
    │ [2] SDK Invocation: app_id, env, country, amount?, theme, provider
    ▼
TERMINAL 3 (Identity Routing & Orchestration Layer)
    │
    ├── [3] Login: email + OTP [PHONE PLANNED]
    ├── [4] KYC L1/L2/L3 via Veriff
    ├── [5] VC issuance (SD-JWT)
    ├── [6] VP generation [PROPOSED OID4VP mechanism]
    │
    │ [7] VP + auth handoff
    ▼
TRANSAK (On-ramp Provider)
    │
    │ [8] Payment processing
    │ [9] Crypto fulfillment
    │ [10] Order status [TBC -- align with Transak's existing pattern]
    ▼
USER (crypto in wallet)
```

### 1.2 Roles & Responsibilities

| Party | Owns | Does NOT Own |
|---|---|---|
| **MetaMask** | Frontend UX, user consent, wallet connection, Terminal 3 SDK integration | Backend, KYC state, identity storage, provider routing |
| **Terminal 3** | Authentication, KYC orchestration & routing, VC issuance, VP generation, DID registry, revocation, regulatory vault, duplicate identity prevention [PLANNED] | Payment processing, fiat handling, crypto fulfillment |
| **Transak** | Payment processing, fiat-to-crypto execution, settlement, compliance (as licensed entity) | KYC collection (delegated to Terminal 3), user authentication |

---

## 2. Per-API-Call System Diagram

### Step 1: MetaMask SDK Invocation → Terminal 3

```
METAMASK FRONTEND                     TERMINAL 3
   │                                      │
   │  Terminal 3 SDK.initialize()         │
   │  ──────────────────────────────►     │
   │  {                                    │
   │    app_id: "metamask",                │
   │    env: "production",                 │
   │    country: "US",                     │
   │    amount: 500,                       │
   │    currency: "USD",                   │
   │    theme: "dark",                     │
   │    provider: "transak"                │
   │  }                                    │
   │                                      │── Internal session creation
   │                                      │   (MetaMask does NOT receive
   │                                      │    raw session details)
   │  ◄──────────────────────────────     │
   │  SDK Response (internal routing)     │
   │  {                                    │
   │    required_level: "L2",              │
   │    action: "login"                    │
   │  }                                    │
   │                                      │
```

**Security notes:**
- Integration is via Terminal 3 SDK embedded in MetaMask's frontend, not direct API calls
- SDK handles session creation internally
- If `amount` is missing, Terminal 3 conservatively assumes L2 KYC required
- Country is validated against IP (but MetaMask explicit param takes precedence)
- `app_id` + `env` used for client authentication
- Session expires after configurable TTL

### Step 2: User Login (Email OTP + [PLANNED] Phone OTP) -- Account Creation

```
USER                    TERMINAL 3
  │                         │
  │  [UI: Enter email]      │
  │                         │
  │  Email verification     │
  │  ──────────────────►   │
  │  { email: "user@..." }  │
  │                         │── Generate OTP
  │                         │── Send OTP to email
  │  ◄──────────────────   │
  │  { status: "otp_sent" } │
  │                         │
  │  OTP verification       │
  │  ──────────────────►   │
  │  { email, otp: "123456"}│
  │                         │── Verify OTP (3 min expiry)
  │                         │── Create/lookup account
  │                         │── Create DID if new account
  │                         │── Issue Email VC
  │  ◄──────────────────   │
  │  {                      │
  │    user_id: "t3_xxx",   │
  │    kyc_status: "none",  │  ← or "L1", "L2"
  │    next_action: "kyc"   │  ← or "vp_share" if already verified
  │  }                      │  (SDK handles internal routing)
  │                         │
```

**Security notes:**
- OTP: 6-digit, **3-minute expiry** (not 5 minutes), 3 max attempts
- Terminal 3 does **NOT currently issue short-lived JWTs**
- **Phone verification is [PLANNED] -- not currently implemented**
- **DID creation happens at account creation (this step), not after KYC**
- **Email VC is issued upon email verification at this step**
- **API URLs and input/return formats shown are ILLUSTRATIVE of internal logic, not actual API contracts**
- **Note: Actual API contracts to be finalized during engineering alignment**

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
  │  L1 KYC Data Collection │                      │
  │  ──────────────────►   │                      │
  │  {                      │                      │
  │    first_name,          │  (user-provided,     │
  │    last_name,           │   unverified)        │
  │    phone,               │                      │
  │    dob,                 │                      │
  │    ssn,                 │                      │
  │    address: {           │                      │
  │      line1, line2,      │                      │
  │      city, state,       │                      │
  │      zip, country       │                      │
  │    }                    │                      │
  │  }                      │                      │
  │                         │── SSN + Name match ──►│ [TBC -- needs verification 
  │                         │   (for verification) │   that Veriff supports this]
  │                         │◄── Match result ─────│
  │                         │                      │
  │                         │── Duplicate check     │ [PLANNED -- not currently
  │                         │   (internal)          │  implemented]
  │                         │                      │
  │  ◄──────────────────   │                      │
  │  Internal routing to    │                      │
  │  L2 or VP sharing       │                      │
  │  (user doesn't receive  │                      │
  │  KYC level directly)    │                      │
```

**Validation rules:**
- `residence_country == "US"` AND `document_country == "US"` → proceed
- `residence_country != "US"` → block (not supported in Phase 1)
- `residence_country == "US"` AND `document_country != "US"` → can proceed
- Check against Transak blacklist countries
- [PLANNED] Duplicate identity check: same SSN cannot create multiple Terminal 3 accounts

**Data Flow Notes:**
- For L1 KYC data: distinguish between "collected" (user-provided, unverified) and "verified" (checked against a source)
- Not all L1 fields are verified -- some are self-declared
- SDK handles routing internally; user doesn't receive KYC level directly

**Decision point -- KYC Level Routing:**
Terminal 3 handles KYC level routing based on the following inputs: **provider**, **amount**, **payment method type**, and **currency**. The $150 USD Level 1 limit is per transaction, with additional daily, monthly, and yearly cumulative limits for Level 1 KYC.

```
IF amount IS NULL OR amount exceeds L1 threshold for given provider/method
  → Require L2 KYC (Step 4)
IF amount <= L1 threshold AND within cumulative limits
  → L1 sufficient, proceed to VP (Step 5)
IF payment method requires L2 regardless (e.g., ACH bank transfer)
  → Require L2 KYC (Step 4)
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
  │                         │── [PROPOSED validation rule]:
  │                         │   doc_country == user_input_country?
  │                         │   name matches L1 data?
  │                         │                      │
  │                         │── Store in Regulatory Vault:
  │                         │   • Liveness video
  │                         │   • Passport image
  │                         │   • Portrait image
  │                         │                      │
  │  ◄──────────────────   │                      │
  │  Internal routing to    │                      │
  │  VP sharing             │                      │
```

**Accepted documents:** National ID, Passport, Driver's License

**[PROPOSED validation rule] Document country vs user input country validation: NOT currently implemented**

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
  │── Email VC (already issued at Step 2):
  │   {
  │     type: "EmailCredential",
  │     email: "user@..." (verified),
  │     signed_by: "Terminal 3"
  │   }
  │
  │── [PLANNED] Phone VC:
  │   {
  │     type: "PhoneCredential", 
  │     phone: "+1..." (verified),
  │     signed_by: "Terminal 3"
  │   }
  │
  │── Issue VC: KYC (SD-JWT) [ILLUSTRATIVE FORMAT]:
  │   {
  │     type: "KYCCredential",
  │     kyc_level: 2,
  │     first_name, last_name, dob,
  │     doc_number, doc_type, doc_expiry,
  │     doc_country, sex, birth_place,
  │     address: { street, city, country, postcode },
  │     portrait_image_hash,
  │     signed_by: "Terminal 3",
  │     on_behalf_of: "veriff",
  │     verified_at: "2026-02-20T...",
  │     expires_at: "2027-02-20T..."
  │   }
  │
  │── DID (already created at Step 2):
  │   {
  │     did: "did:t3:user_xxx",
  │     status: "active",
  │     issuer: "Terminal 3",
  │     revocation_status: "valid"
  │   }
  │
```

**Important Notes:**
- **DID creation happens at Step 2 (account creation), not here**
- **Email VC is issued at Step 2 when email is verified** 
- **Phone VC: [PLANNED -- pending phone verification implementation]**
- **VC schema is illustrative. Actual fields and format to be confirmed with engineering.**
- **VC format:** SD-JWT (selective disclosure)
- **Signing:** Terminal 3 signs on behalf of Veriff

### Step 6: VP Sharing with Transak [PROPOSED OID4VP mechanism]

```
TRANSAK                 TERMINAL 3              USER
  │                         │                      │
  │  [PROPOSED -- subject to│                      │
  │   Transak engineering   │                      │
  │   alignment]            │                      │
  │                         │                      │
  │  OID4VP Request         │                      │
  │  [TBC mechanism]        │                      │
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

**Important Notes:**
- **Terminal 3 handles VP generation and sharing**
- **The mechanism (whether Transak sends an OID4VP request or Terminal 3 pushes the VP) is [TBC with Transak]**
- **The entire OID4VP mechanism is [PROPOSED -- subject to Transak engineering alignment]**

**Transak verification:**
- Uses Terminal 3 Verifier SDK
- Checks: VP signature valid? Issuer trusted? Credential expired? Revoked?
- Reference: Terminal 3 OID4VP spec (https://docs.terminal3.io/api-reference/openid4vp-vc/openid4vp/authorization)

**Post-VP Flow -- Order Status:**

Terminal 3 handles ALL KYC routing and step-up BEFORE sharing the VP. Post-VP flow covers only order status (how Terminal 3 learns the order completed).

**Order Status Mechanism [TBC -- align with Transak's existing pattern]:**

```
TRANSAK                 TERMINAL 3
  │                         │
  │── Order Status Update   │
  │   [TBC mechanism]       │
  │  ──────────────────►   │
  │  { order_id, status:    │
  │    "confirmed" }        │
  │                         │── Log order status
  │                         │
  │── Order Completion      │
  │  ──────────────────►   │
  │  { order_id, status:    │
  │    "completed",         │
  │    tx_hash: "0x..." }   │
  │                         │── Log completion
  │                         │
```

### Step 7: Transak SSO + Order Execution

```
USER                    TERMINAL 3              TRANSAK
  │                         │                      │
  │                         │── Auth Reliance ─────►│
  │                         │   (Terminal 3 completes│
  │                         │    KYC, generates VP,   │
  │                         │    hands off auth +     │
  │                         │    VP data)            │
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

| Data Element | MetaMask | Terminal 3 | Transak | Regulatory Vault |
|---|---|---|---|---|
| Wallet address | ✅ has | ✅ has | ✅ receives | — |
| Email | — | ✅ verified | ✅ receives via VP | — |
| Phone | — | ✅ collected + verified [PLANNED] | ✅ receives via VP [PLANNED] | — |
| First/Last Name | — | ✅ collected + verified | ✅ receives via VP | — |
| DOB | — | ✅ collected + verified | ✅ receives via VP | — |
| SSN | — | ✅ collected (L1 match check) | ❌ NOT shared | — |
| Address | — | ✅ collected | ✅ receives via VP | — |
| Passport image | — | ❌ not retained long-term | ❌ NOT shared | ✅ stored |
| Portrait image | — | ❌ not retained long-term | ❌ NOT shared | ✅ stored |
| Liveness video | — | ❌ not retained long-term | ❌ NOT shared | ✅ stored |
| KYC level/status | — | ✅ owns | ✅ receives via VP | — |
| Order data | ✅ polls status | ✅ receives via webhook/polling | ✅ owns | — |

### 3.2 Data Encryption & Storage

| Storage | Method | Access Control |
|---|---|---|
| **Terminal 3 Credential Store** | Encrypted at rest (standard encryption) | Terminal 3 internal only |
| **SD-JWT Credentials** | Signed, selective disclosure | User-consented sharing only |
| **Regulatory Vault** | Encrypted, jurisdiction-aware retention | Regulatory authorities on demand |
| **DID Registry** | Public metadata (no PII) | Verifiers can check status |

**Note:** TEE-based storage planned with Trinity architecture migration [timeline TBC]. Current state uses encrypted at rest (standard encryption).

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
[Create account + DID]   [Resume KYC]
[Issue Email VC]
  │
  ▼
[Collect L1: name, phone, DOB, SSN, address]
  │
  ▼
[SSN + Name match via Veriff]──FAIL──► REJECT + error
  │ [TBC -- needs verification that Veriff supports this]
  PASS
  │
  ▼
[Duplicate identity check]──DUPLICATE──► BLOCK + error
  │ [PLANNED -- not currently implemented]
  PASS
  │
  ▼
[Evaluate: provider + amount + payment method + currency]
  │
  ▼
[Exceeds L1 threshold?]──YES──►[L2 Required]
  │                                │
  NO                               │
  │                                │
  ▼                                │
[Within cumulative limits?]        │
  │       │                        │
  YES     NO                       │
  │       │                        │
  ▼       ▼                        │
[L1 ok] [L2 Required]             │
  │       │                        │
  ▼       ▼◄───────────────────────┘
VP SHARE  [Veriff: doc upload + liveness]
              │
              ▼
          [Doc country == entered country?]──NO──► REJECT + retry
              │ [PROPOSED validation rule -- not currently implemented]
              YES
              │
              ▼
          [Issue KYC VC + store in Regulatory Vault]
              │
              ▼
          VP SHARE → TRANSAK
```

### 4.2 Provider Routing (Phase 1: Declared)

```
Phase 1: provider = "transak" (declared by MetaMask)
  Terminal 3 role: KYC routing + gating + VP construction
  Routing inputs: provider, amount, payment method type, currency

Phase 2+: intent-based routing (future)
  Terminal 3 role: provider selection + KYC routing + gating + VP construction
```

---

## 5. Edge Cases & Off-Happy-Path Flows

### 5.1 Failure Scenarios

| Scenario | Behavior | User Experience |
|---|---|---|
| **OTP expired** | OTP invalid after 3 min | "Code expired. Request a new one." |
| **OTP max attempts** | 3 failed attempts | "Too many attempts. Please wait 30 minutes." |
| **SSN match fails** | Veriff SSN+name mismatch | "Information doesn't match records. Please check and retry." |
| **Duplicate SSN [PLANNED]** | Same SSN already in system | "This identity is already registered. Please login instead." |
| **Veriff doc rejection** | Document unreadable / fake | "Document could not be verified. Please try again with a clearer image." |
| **Liveness failure** | Biometric check fails | "Face verification failed. Please try again in good lighting." |
| **Doc country mismatch [PROPOSED]** | Passport country != entered country | "Passport does not match selected country. Please re-do KYC." |
| **KYC abandoned mid-flow** | User closes before completing | Next visit: restart KYC from beginning |
| **VP sharing declined** | User refuses consent | Cannot proceed to Transak. Show explanation. |
| **Transak rejects VP** | VP verification fails | Terminal 3 logs error. User shown retry option. |
| **Transak order fails** | Payment processing error | Handled by Transak UX. Terminal 3 not involved. |
| **Network timeout** | Any API call times out | Retry with exponential backoff. Max 3 retries. |

### 5.2 Step-Up Scenarios

| Trigger | Action |
|---|---|
| User at L1 attempts transaction exceeding L1 threshold | Prompt L2 KYC (doc + liveness) |
| User at L1/L2, Transak requests additional info [TBC mechanism] | Terminal 3 collects and issues updated VP |
| ACH bank transfer (any amount) | Require L2 regardless of amount |
| Credential expired (>12 months) | Prompt re-verification |
| Revoked credential | Block + prompt re-verification |

### 5.3 Manual Review

| Scenario | Owner | Process |
|---|---|---|
| Veriff flags for manual review | Veriff | Async review. User notified when complete. |
| Fraud suspicion (duplicate patterns) [PLANNED] | Terminal 3 | Internal review. User blocked pending investigation. |
| Regulatory request for Vault data | Terminal 3 | Compliance team provides encrypted access. |

---

## 6. SDK & Integration Points

### 6.1 Terminal 3 → MetaMask
- **Integration method:** Terminal 3 SDK embedded in MetaMask's frontend
- **Auth:** SDK-based, frontend-initiated
- **Data flow:** MetaMask SDK invocation → Terminal 3 internal session → KYC flow → VP sharing with Transak

### 6.2 Terminal 3 → Transak
- **VP sharing:** [PROPOSED OID4VP mechanism -- subject to Transak engineering alignment]
- **Auth handoff:** Transak Auth Reliance product (email-based)
- **Verification:** Verifier SDK provided to Transak for VP validation
- **DID registry:** Public endpoint for Transak to check issuer + revocation

### 6.3 Transak → Terminal 3
- **Order status:** [TBC -- align with Transak's existing pattern]
- **Step-up KYC:** [TBC mechanism for additional data requests]
- **Order completion:** Status notification confirms final status + tx_hash

### 6.4 Transak → MetaMask
- **Order status:** Polling (GET every 10s, existing pattern)
- **No Terminal 3 involvement** in MetaMask-facing order status polling

### 6.5 SDKs Provided by Terminal 3
| SDK | Purpose | Consumer |
|---|---|---|
| **Verifier SDK** | Validate VP signature, issuer, expiry, revocation | Transak |
| **Identity SDK** | Login + KYC flow (embedded) | MetaMask frontend |

**Security team benefit:** Only ONE SDK to audit (Terminal 3 Identity SDK) for the MetaMask integration. Transak audits the Verifier SDK separately.

---

## 7. Security Checklist

| Item | Status | Notes |
|---|---|---|
| Data at rest encryption | ✅ Encrypted at rest | Credential store (TEE planned with Trinity) |
| Data in transit encryption | ✅ TLS 1.3 | All API calls |
| PII minimization | ✅ Selective disclosure | SD-JWT reveals only requested fields |
| SSN handling | ✅ Hash after match | Raw SSN not stored |
| Biometric data | ✅ Regulatory Vault | Not shared with Transak |
| Credential revocation | ✅ DID registry | Real-time revocation checking |
| Duplicate identity prevention | [PLANNED] Built-in | Configurable per client |
| GDPR right to be forgotten | ✅ Supported | User can revoke credentials + request deletion |
| Audit trail | ✅ Immutable log | 7-year retention |
| SOC 2 compliance | ℹ️ Transak is SOC 2 compliant | Terminal 3 status: confirm |
| Rate limiting | ✅ API gateway | Per-client, per-endpoint |
| Fraud detection | ✅ Document checks | [PLANNED] device ID, VPN checks, behavioral signals |

---

## 8. Open Items for Security Review

| # | Item | Question for MetaMask Security |
|---|---|---|
| 1 | SDK integration | Terminal 3 Identity SDK -- what level of audit does MetaMask security require? |
| 2 | Session TTL | What is acceptable session duration for SDK-based sessions? |
| 3 | MetaMask SDK auth | How does Terminal 3 validate the SDK invocation is from MetaMask? App ID + env sufficient? |
| 4 | Consent UX | Does MetaMask security need to review the VP consent screen? |
| 5 | Device signals | Which signals can MetaMask pass to Terminal 3 for fraud detection? |
| 6 | OID4VP mechanism | Preference for Terminal 3-initiated VP sharing vs Transak OID4VP request pattern? |
| 7 | Regulatory Vault access | What is MetaMask's expectation for regulatory access to Vault data? |
| 8 | Incident response | What is the expected SLA for identity-related incident notification? |

---

*This document is designed as an 80/20 architecture pack: sufficient detail for MetaMask security to begin review without requiring piecemeal Q&A. All architecture decisions are proposals pending joint alignment.*