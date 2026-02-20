# MetaMask x terminal 3 x Transak
## End-to-End Product Requirements Document

**Author:** Janani G, Head of Product — terminal 3
**Prepared by:** Janet ✦ (Lead PM)
**Date:** February 20, 2026
**Status:** Draft v1
**Classification:** Confidential

---

## 1. Executive Summary

MetaMask needs an identity and orchestration layer. It operates as a frontend-only wallet with no backend infrastructure -- no KYC state management, no provider routing, no identity persistence. terminal 3 fills this gap.

This PRD defines the end-to-end integration between **MetaMask** (wallet frontend), **terminal 3** (identity orchestration), and **Transak** (fiat on-ramp) -- from the moment a user clicks "Buy" in MetaMask to the moment crypto lands in their wallet.

**Core proposition:** terminal 3 is the invisible infrastructure that makes MetaMask's identity and compliance requirements work seamlessly, starting with Transak and scaling to any provider.

---

## 2. Problem Statement

| Stakeholder | Problem |
|---|---|
| **MetaMask** | No backend. Cannot store user data, manage KYC state, or make routing decisions. Every provider integration is bespoke. Users re-verify for every provider. |
| **Transak** | Receives unstructured, incomplete user data. High drop-off during KYC. No session continuity -- returning users start from zero. |
| **End User** | Verifies identity repeatedly. Fragmented experience across providers. No portable identity. |

**terminal 3 solves all three simultaneously** by sitting between MetaMask and its service providers as a stateful identity orchestration layer.

---

## 3. System Architecture

### 3.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          END USER                                   │
│                     (MetaMask Wallet)                               │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       METAMASK FRONTEND                             │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐  │
│  │  Buy/Sell    │  │  Wallet      │  │  Consent &               │  │
│  │  Intent UI   │  │  Connection  │  │  Authorization UI        │  │
│  └──────┬───────┘  └──────────────┘  └──────────────────────────┘  │
│         │                                                           │
│         │  SDK / API call                                           │
└─────────┼───────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      TERMINAL 3 LAYER                               │
│                  (Identity Orchestration)                            │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                    API GATEWAY                                 │ │
│  │         Authentication · Rate Limiting · Logging               │ │
│  └────────────────────────┬───────────────────────────────────────┘ │
│                           │                                         │
│  ┌────────────┐  ┌────────┴───────┐  ┌──────────────┐             │
│  │  SESSION    │  │  IDENTITY      │  │  POLICY      │             │
│  │  MANAGER    │  │  MANAGER       │  │  ENGINE      │             │
│  │             │  │                │  │              │             │
│  │ • Session   │  │ • KYC state    │  │ • Threshold  │             │
│  │   creation  │  │ • Credential   │  │   rules      │             │
│  │ • State     │  │   storage      │  │ • Jurisdic-  │             │
│  │   persist.  │  │ • Level mgmt   │  │   tion rules │             │
│  │ • Wallet    │  │ • Verification │  │ • Anti-gaming│             │
│  │   linking   │  │   orchestrate  │  │ • FX buffer  │             │
│  └──────┬─────┘  └────────┬───────┘  └──────┬───────┘             │
│         │                 │                  │                      │
│  ┌──────┴─────────────────┴──────────────────┴───────┐             │
│  │              PROVIDER ROUTER                       │             │
│  │                                                    │             │
│  │  • Provider selection (declared / smart)            │             │
│  │  • Payload construction per provider spec          │             │
│  │  • Credential mapping (t3 levels → provider reqs)  │             │
│  │  • Fallback routing on failure                     │             │
│  └───────────┬──────────────┬──────────────┬─────────┘             │
│              │              │              │                        │
│  ┌───────────┴──┐  ┌───────┴──────┐  ┌────┴─────────┐            │
│  │  AUDIT LOG   │  │  CREDENTIAL  │  │  ANALYTICS   │            │
│  │              │  │  STORE (TEE) │  │              │            │
│  │ • Who        │  │              │  │ • Conversion │            │
│  │ • What       │  │ • SD-JWT     │  │ • Drop-off   │            │
│  │ • When       │  │ • mDoc       │  │ • Provider   │            │
│  │ • Decision   │  │ • Atomized   │  │   perf.      │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                     │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   TRANSAK    │  │   MOONPAY    │  │   FUTURE     │
│              │  │              │  │   PROVIDERS  │
│  On-ramp /   │  │  On-ramp /   │  │              │
│  Off-ramp    │  │  Off-ramp    │  │              │
│              │  │              │  │              │
│  Receives:   │  │  Receives:   │  │  Receives:   │
│  Structured  │  │  Structured  │  │  Structured  │
│  identity    │  │  identity    │  │  identity    │
│  object      │  │  object      │  │  object      │
└──────────────┘  └──────────────┘  └──────────────┘
```

### 3.2 Component Definitions

| Component | Responsibility | Key Interfaces |
|---|---|---|
| **API Gateway** | Authentication, rate limiting, request validation, API versioning | MetaMask SDK → terminal 3 API |
| **Session Manager** | Creates and persists user sessions. Links wallet addresses to identity sessions. Handles returning user detection. | Reads/writes session store |
| **Identity Manager** | Owns user KYC state. Manages credential lifecycle (issuance, storage, expiry, revocation). Orchestrates verification flows. | Credential Store (TEE), verification providers |
| **Policy Engine** | Evaluates transaction context against rules. Determines required KYC level. Enforces thresholds, jurisdiction rules, anti-gaming controls. | Identity Manager, Provider Router |
| **Provider Router** | Selects target provider. Constructs provider-specific payload from standardized identity object. Handles failover. | Provider APIs (Transak, MoonPay, etc.) |
| **Credential Store** | TEE-protected storage for verified credentials. SD-JWT and mDoc format. Atomized -- user controls which fields are shared. | Identity Manager |
| **Audit Log** | Immutable record of all identity decisions, verifications, routing choices. Compliance-ready. | All components write to audit log |
| **Analytics** | Conversion tracking, drop-off analysis, provider performance metrics. | All components emit events |

---

## 4. User Flows

### 4.1 Flow 1: New User — Sub-Threshold Buy (< $150)

```
User clicks "Buy" in MetaMask
        │
        ▼
MetaMask captures intent
(amount, currency, crypto)
        │
        ▼
MetaMask calls terminal 3 API
POST /v1/sessions/create
{wallet, intent, provider: "transak"}
        │
        ▼
terminal 3 Session Manager
• Creates session
• Checks: returning user? → NO (new wallet)
• Assigns KYC level: L0
        │
        ▼
terminal 3 Policy Engine evaluates:
• Amount: $80 (sub-threshold)
• Required level: L1 (self-declared)
• Current level: L0
• Decision: UPGRADE_REQUIRED → L1
        │
        ▼
terminal 3 → MetaMask:
{action: "collect", fields: ["name", "email", "country"]}
        │
        ▼
MetaMask shows consent + collection UI
User enters: name, email, country
        │
        ▼
MetaMask sends to terminal 3
POST /v1/identity/update
{session_id, fields: {name, email, country}}
        │
        ▼
terminal 3 Identity Manager:
• Stores L1 credential
• Updates KYC level: L1
        │
        ▼
terminal 3 Policy Engine re-evaluates:
• Required: L1 ✓
• Decision: ALLOW
        │
        ▼
terminal 3 Provider Router:
• Provider: Transak (declared)
• Constructs Transak payload with L1 fields
• Generates Transak session URL
        │
        ▼
terminal 3 → MetaMask:
{action: "redirect", url: "transak.com/widget?...", session: "t3_xxx"}
        │
        ▼
User completes purchase in Transak widget
(payment method → fiat → crypto → wallet)
        │
        ▼
Transak webhook → terminal 3
{status: "completed", tx_hash: "0x..."}
        │
        ▼
terminal 3 → MetaMask:
{status: "completed", tx_hash: "0x..."}
```

**Time to purchase:** ~2 minutes (name + email + payment)
**KYC friction:** Minimal (3 fields, no verification)

---

### 4.2 Flow 2: New User — Above Threshold ($500 buy)

```
User clicks "Buy $500 ETH" in MetaMask
        │
        ▼
MetaMask → terminal 3 API
POST /v1/sessions/create
{wallet, intent: {amount: 500, currency: "USD", crypto: "ETH"}}
        │
        ▼
terminal 3 Policy Engine:
• Amount: $500 (above $150 threshold)
• Required level: L2 (verified)
• Current level: L0
• Decision: UPGRADE_REQUIRED → L2
        │
        ▼
terminal 3 → MetaMask:
{action: "verify", level: "L2",
 steps: ["collect_info", "document_upload", "liveness_check"]}
        │
        ▼
[MODE 1 - Phase 1]                    [MODE 2 - Phase 2]
MetaMask collects L1 fields            MetaMask collects L1 fields
terminal 3 stores L1                   terminal 3 stores L1
Redirect to Transak widget             terminal 3 triggers verification:
Transak handles L2 verification        • Document upload (passport/ID)
(document + liveness in-widget)        • Liveness check (biometric)
                                       • Verification via provider (Onfido/Jumio)
                                       terminal 3 stores L2 credential
                                       Transak trusts terminal 3 L2 ✓
                                       No re-verification needed
        │
        ▼
Purchase completes (same as Flow 1 from here)
```

---

### 4.3 Flow 3: Returning User

```
User returns to MetaMask, clicks "Buy"
        │
        ▼
MetaMask → terminal 3 API
POST /v1/sessions/create
{wallet: "0xABC..."}
        │
        ▼
terminal 3 Session Manager:
• Wallet lookup: MATCH FOUND
• Existing session: user_id = t3_xyz
• Current KYC level: L2 (verified 30 days ago)
• Credential status: VALID (expires in 335 days)
        │
        ▼
terminal 3 Policy Engine:
• Amount: $300
• Required: L2
• Current: L2 ✓
• Credential valid ✓
• Decision: ALLOW (no additional verification)
        │
        ▼
terminal 3 Provider Router:
• Pre-populates Transak with verified data
• Generates Transak session URL
        │
        ▼
terminal 3 → MetaMask:
{action: "redirect", url: "transak.com/widget?...",
 user: {name: "...", verified: true}}
        │
        ▼
User goes straight to payment
(no KYC step -- already verified)
```

**Time to purchase:** ~30 seconds
**KYC friction:** Zero
**This is the killer UX advantage.** No other solution gives MetaMask this today.

---

### 4.4 Flow 4: Multi-Provider (Phase 2 -- Smart Routing)

```
User clicks "Buy $200 ETH" in MetaMask
        │
        ▼
MetaMask → terminal 3 API
POST /v1/sessions/create
{wallet, intent: {amount: 200, currency: "USD", crypto: "ETH"}}
        │
        ▼
terminal 3 Provider Router evaluates:
┌──────────────────────────────────────────────┐
│  Provider Scoring (user in Singapore)         │
│                                               │
│  Transak:  fee 1.5% │ KYC: L1 ok │ score: 87 │
│  MoonPay:  fee 2.0% │ KYC: L2 req│ score: 72 │
│  Ramp:     fee 1.8% │ KYC: L1 ok │ score: 80 │
│                                               │
│  Winner: Transak (lowest fee, L1 sufficient)  │
└──────────────────────────────────────────────┘
        │
        ▼
User is routed to Transak automatically
(or shown choice with recommendation)
```

---

## 5. KYC Tier Framework

### 5.1 Standardized Levels

| Level | Name | Data | Verification | Threshold |
|---|---|---|---|---|
| **L0** | Anonymous | Wallet address | None | Quotes only |
| **L1** | Self-Declared | Name, email, country | User input, unverified | < $150 |
| **L2** | Verified | L1 + gov ID + liveness | Document AI + biometric | $150 -- $10,000 |
| **L3** | Enhanced | L2 + proof of address + source of funds | Full EDD | > $10,000 |

### 5.2 Credential Persistence

- Credentials are stored in terminal 3's TEE-protected credential store
- Format: SD-JWT (selective disclosure) for maximum interoperability
- Expiry: 12 months for L2, 6 months for L3 (configurable per jurisdiction)
- User can revoke at any time (GDPR Article 17 compliant)
- Same credential works across ALL providers -- verify once, use everywhere

### 5.3 Standardized Identity Object

```json
{
  "schema": "terminal3.identity.v1",
  "user_id": "t3_uuid_xxx",
  "kyc_level": 2,
  "verified_at": "2026-02-20T10:00:00Z",
  "expires_at": "2027-02-20T10:00:00Z",
  "jurisdiction": "SG",
  "fields": {
    "full_name": "...",
    "date_of_birth": "YYYY-MM-DD",
    "nationality": "SG",
    "email": "user@email.com",
    "country_of_residence": "SG",
    "id_document": {
      "type": "passport",
      "issuing_country": "SG",
      "verified": true,
      "verification_method": "document_ai + liveness",
      "document_hash": "sha256:abc..."
    }
  },
  "wallet_addresses": ["0xABC..."],
  "verification_provider": "terminal3",
  "audit_ref": "t3_audit_xxx",
  "selective_disclosure": true
}
```

---

## 6. API Specification

### 6.1 MetaMask → terminal 3

#### Create Session
```
POST /v1/sessions
Authorization: Bearer {metamask_api_key}

Request:
{
  "wallet_address": "0xABC...",
  "chain_id": 1,
  "intent": {
    "action": "buy",
    "fiat_currency": "USD",
    "fiat_amount": 500,
    "crypto_currency": "ETH"
  },
  "provider": "transak",          // Phase 1: declared
  "locale": "en-SG",
  "client_metadata": {
    "app_version": "12.0.0",
    "platform": "extension"
  }
}

Response:
{
  "session_id": "t3_sess_xxx",
  "user_id": "t3_user_xxx",
  "kyc_level": 0,
  "required_level": 2,
  "action": "upgrade",
  "upgrade_steps": [
    {
      "step": "collect",
      "fields": ["full_name", "email", "country_of_residence"],
      "target_level": 1
    },
    {
      "step": "verify",
      "methods": ["document_upload", "liveness"],
      "target_level": 2,
      "provider_url": "https://verify.terminal3.io/session/xxx"
    }
  ]
}
```

#### Update Identity
```
POST /v1/sessions/{session_id}/identity
Authorization: Bearer {metamask_api_key}

Request:
{
  "fields": {
    "full_name": "Jane Doe",
    "email": "jane@email.com",
    "country_of_residence": "SG"
  }
}

Response:
{
  "kyc_level": 1,
  "status": "updated",
  "next_action": "verify"    // or "route" if L1 sufficient
}
```

#### Get Routing Decision
```
POST /v1/sessions/{session_id}/route
Authorization: Bearer {metamask_api_key}

Response:
{
  "provider": "transak",
  "action": "redirect",
  "redirect_url": "https://global.transak.com/?apiKey=...&userData=...",
  "prefilled_fields": {
    "firstName": "Jane",
    "lastName": "Doe",
    "email": "jane@email.com"
  },
  "session_token": "t3_route_xxx",
  "expires_at": "2026-02-20T11:00:00Z"
}
```

### 6.2 terminal 3 → Transak

#### Initiate Transaction (Transak Partner API)
```
POST /v1/partner/transactions
Authorization: Bearer {t3_partner_key}

Request:
{
  "partner_session_id": "t3_sess_xxx",
  "user_data": {
    "firstName": "Jane",
    "lastName": "Doe",
    "email": "jane@email.com",
    "country": "SG",
    "kyc_verified": true,           // Mode 2 only
    "kyc_level": "L2",              // Mode 2 only
    "verification_ref": "t3_xxx"    // Mode 2 only
  },
  "transaction": {
    "fiat_currency": "USD",
    "fiat_amount": 500,
    "crypto_currency": "ETH",
    "wallet_address": "0xABC...",
    "network": "ethereum"
  }
}
```

### 6.3 Transak → terminal 3 (Webhooks)

```
POST /v1/webhooks/transak
X-Transak-Signature: {hmac_signature}

{
  "event": "ORDER_COMPLETED",
  "data": {
    "partner_session_id": "t3_sess_xxx",
    "order_id": "transak_order_xxx",
    "status": "COMPLETED",
    "fiat_amount": 500,
    "fiat_currency": "USD",
    "crypto_amount": 0.18,
    "crypto_currency": "ETH",
    "tx_hash": "0xDEF...",
    "completed_at": "2026-02-20T10:15:00Z"
  }
}
```

---

## 7. Policy Engine -- Threshold & Compliance

### 7.1 Threshold Rules

```
RULE: standard_threshold
  IF amount_usd < 150
    THEN required_level = L1
  IF amount_usd >= 150 AND amount_usd < 10000
    THEN required_level = L2
  IF amount_usd >= 10000
    THEN required_level = L3

RULE: rolling_aggregation
  IF sum(transactions, 24h) > 150
    THEN required_level = L2
  IF sum(transactions, 30d) > 10000
    THEN required_level = L3

RULE: jurisdiction_override
  IF country IN [US, UK, DE, FR, SG]
    THEN apply local_threshold_rules
  IF country IN [sanctioned_list]
    THEN BLOCK
```

### 7.2 Anti-Gaming Controls

| Risk | Detection | Response |
|---|---|---|
| **Structuring** | Rolling 24h/7d/30d aggregation | Auto-upgrade KYC requirement |
| **Multi-wallet splitting** | Same L1 identity across wallets | Aggregate across linked wallets |
| **Rapid re-attempts** | >3 attempts in 1 hour | Cooldown (30 min) |
| **Currency arbitrage** | USD-equivalent normalization | All thresholds in USD-equivalent |

---

## 8. Data Architecture

### 8.1 Storage Boundaries

| Data | Stored By | Format | Retention |
|---|---|---|---|
| Wallet address | terminal 3 | Plaintext | Session lifetime |
| KYC level + status | terminal 3 | Encrypted at rest | Until credential expiry |
| Identity fields (L1) | terminal 3 | Encrypted (TEE) | Until user revokes or 12 months |
| Identity fields (L2) | terminal 3 | SD-JWT in TEE | Until user revokes or 12 months |
| Document images | terminal 3 (Mode 2) | Encrypted, atomized | 30 days post-verification, then hash-only |
| Transaction history | terminal 3 | Encrypted | 5 years (regulatory) |
| Audit trail | terminal 3 | Immutable log | 7 years (regulatory) |

### 8.2 Data Flow Diagram

```
MetaMask                    terminal 3                      Transak
   │                            │                              │
   │── wallet + intent ────────▶│                              │
   │                            │── session created            │
   │◀── collect fields ────────│                              │
   │                            │                              │
   │── name, email, country ──▶│                              │
   │                            │── L1 stored (TEE)            │
   │                            │── policy evaluated           │
   │                            │                              │
   │                            │── structured payload ───────▶│
   │                            │                              │── payment processed
   │                            │◀── webhook (completed) ─────│
   │◀── tx confirmed ──────────│                              │
   │                            │── audit log written          │
   │                            │                              │
```

**Key principle:** MetaMask never stores identity data. Transak receives only what it needs. terminal 3 is the single source of truth.

---

## 9. Phased Delivery

### Phase 1: Mode 1 -- Minimal Pass-Through (8 weeks)

| Week | Milestone | Owner |
|---|---|---|
| 1-2 | API spec finalized, Transak alignment | terminal 3 + Transak |
| 3-4 | Session Manager + Identity Manager (L0/L1) | terminal 3 Eng |
| 5-6 | Provider Router (Transak integration) | terminal 3 + Transak Eng |
| 7 | Policy Engine (basic thresholds) | terminal 3 Eng |
| 8 | Integration testing + MetaMask SDK | All parties |

**Deliverables:**
- User can buy crypto via MetaMask → terminal 3 → Transak
- Sub-threshold: L1 self-declared, pre-populated in Transak
- Above-threshold: Transak handles KYC in-widget
- Returning user: session persistence, no re-entry of L1 data

### Phase 2: Mode 2 -- Full Verified Profile (12 weeks after Phase 1)

| Week | Milestone |
|---|---|
| 1-3 | Verification provider integration (Onfido/Jumio) |
| 4-6 | L2 credential issuance + TEE storage |
| 7-8 | Transak trust agreement + API integration for pre-verified users |
| 9-10 | SD-JWT selective disclosure implementation |
| 11-12 | Full E2E testing + compliance review |

**Deliverables:**
- terminal 3 verifies users to L2 (document + liveness)
- Transak trusts terminal 3 KYC -- no re-verification
- Single verification works across multiple providers
- Returning user at L2: zero-friction purchase

### Phase 3: Smart Routing + Multi-Provider (ongoing)

- Provider scoring algorithm
- MoonPay, Ramp integration
- Intent-based routing (no declared provider)
- Conversion optimization

---

## 10. Success Metrics

| Metric | Phase 1 Target | Phase 2 Target |
|---|---|---|
| **Conversion rate** (intent → completed purchase) | 45% | 65% |
| **Time to first purchase** (new user) | < 5 min | < 3 min |
| **Time to purchase** (returning user) | < 1 min | < 30 sec |
| **KYC drop-off rate** | < 30% | < 15% |
| **Returning user re-verification rate** | 0% (L1) | 0% (L1+L2) |
| **Provider routing accuracy** | N/A (declared) | > 90% optimal |

---

## 11. Open Questions

| # | Question | Needs Input From | Priority |
|---|---|---|---|
| 1 | Transak threshold: $150 global or jurisdiction-specific? | Transak | P0 |
| 2 | Per-transaction or rolling window? | Transak | P0 |
| 3 | Transak API: can we pre-populate user data via partner API? | Transak Eng | P0 |
| 4 | MetaMask SDK: existing on-ramp SDK or new integration? | MetaMask Eng | P0 |
| 5 | Transak willingness to trust terminal 3 KYC (Mode 2)? | Transak Compliance | P1 |
| 6 | Data residency requirements by jurisdiction? | Legal | P1 |
| 7 | Verification provider preference (Onfido, Jumio, other)? | terminal 3 Eng | P1 |
| 8 | MetaMask consent UX: who builds the UI? | MetaMask Product | P1 |

---

## 12. Risks

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Transak rejects Mode 2 trust model | Stuck on Mode 1 | Medium | Ship Mode 1 with conversion data to build the case |
| MetaMask changes SDK architecture | Integration rework | Low | Abstract interface layer |
| Regulatory divergence across jurisdictions | Complex policy engine | High | Jurisdiction-aware from day 1 |
| idOS or competitor captures MetaMask | Existential for this integration | Medium | Move fast, ship Phase 1, prove value with data |
| FX volatility at threshold boundaries | Edge case UX failures | Low-Medium | 5% buffer below thresholds |

---

## 13. Appendix: Why terminal 3 (Not Build In-House or Competitor)

| Dimension | Build In-House (MetaMask) | idOS | terminal 3 |
|---|---|---|---|
| **Architecture fit** | Requires building backend -- against MetaMask philosophy | Decentralized -- complex integration | Orchestration layer -- clean API, no backend needed |
| **Time to ship** | 12-18 months | Unknown | 8 weeks (Phase 1) |
| **Identity persistence** | Would need to build from scratch | On-chain -- privacy concerns | TEE-protected, SD-JWT, GDPR compliant |
| **Multi-provider routing** | Bespoke per provider | Not core focus | Core architecture -- built for this |
| **Agent authorization (KYA)** | Not on roadmap | Not offered | Native capability -- future-proof |
| **Compliance** | New liability for MetaMask | Early stage | Enterprise-grade, audit-ready |

---

*This document is a working draft. All timelines and specifications are proposals pending alignment with MetaMask and Transak engineering teams.*
