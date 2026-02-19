# MetaMask x terminal 3 x Transak
## Integration Architecture Proposal -- Pre-Alignment Document

**Prepared by:** terminal 3 Product
**Date:** February 19, 2026
**Status:** Draft for internal review, then Transak working session
**Classification:** Confidential

---

## 1. Executive Summary

terminal 3 proposes to serve as the **identity orchestration layer** between MetaMask and Transak (and future on-ramp/off-ramp providers). MetaMask operates frontend-only with no backend infrastructure. terminal 3 fills that gap: owning KYC state, routing logic, threshold enforcement, and user identity persistence.

This document outlines the integration architecture, KYC tiering framework, routing strategy, and open decision points requiring alignment with Transak before development begins.

---

## 2. Architecture Overview

```
┌──────────────┐     ┌───────────────────────────────────┐     ┌──────────────┐
│              │     │         terminal 3                 │     │              │
│   MetaMask   │────▶│                                   │────▶│   Transak    │
│  (frontend)  │     │  ┌─────────────┐ ┌─────────────┐  │     │  (on-ramp)   │
│              │◀────│  │ KYC State   │ │ Policy      │  │◀────│              │
│  No backend  │     │  │ Manager     │ │ Engine      │  │     │              │
│  No storage  │     │  └─────────────┘ └─────────────┘  │     └──────────────┘
│              │     │  ┌─────────────┐ ┌─────────────┐  │     ┌──────────────┐
└──────────────┘     │  │ Threshold   │ │ Provider    │  │────▶│  MoonPay     │
                     │  │ Engine      │ │ Router      │  │     │  Ramp        │
                     │  └─────────────┘ └─────────────┘  │     │  Others...   │
                     │  ┌─────────────┐                  │     └──────────────┘
                     │  │ Audit Log   │                  │
                     │  └─────────────┘                  │
                     └───────────────────────────────────┘
```

**terminal 3 owns:**
- User identity state (KYC level achieved, credentials held)
- Routing decisions (which provider, which flow)
- Threshold enforcement (amount-based, jurisdiction-based)
- Session continuity (user returns, no re-verification)
- Audit trail (who verified what, when, to what level)

**MetaMask owns:**
- Frontend UX
- User consent flows
- Wallet connection

**Transak owns:**
- Fiat on-ramp/off-ramp execution
- Payment processing
- Local payment method support
- Provider-side compliance obligations

---

## 3. Routing Strategy

### Recommendation: Hybrid Model (Option A now, Option B roadmap)

| | Option A: Provider-Declared | Option B: Smart Routing | Hybrid |
|---|---|---|---|
| **MetaMask sends** | provider = "Transak" | intent + currency + amount | Provider-declared now; intent-based later |
| **terminal 3 decides** | KYC level, payload shape | Provider + KYC + payload | Progressively more |
| **Transak impact** | Low -- they're always selected | Medium -- may not be selected | Low now, medium later |
| **Scalability** | Limited | High | High (phased) |
| **Time to ship** | Fast | Slow (needs routing logic + provider scoring) | Fast start, iterate |

**Rationale:**

Phase 1 (now): MetaMask declares `provider = "Transak"`. terminal 3 handles KYC gating and payload construction. This ships fast and proves the integration.

Phase 2 (Q3+): terminal 3 accepts intent-based requests (`buy`, `sell`, currency, amount) and routes to the optimal provider based on: jurisdiction, fee structure, KYC friction, success rate, liquidity.

**Decision point for Transak:** Are they comfortable with terminal 3 owning routing in Phase 2? This is a strategic conversation -- Transak may want guaranteed traffic vs. competitive routing.

---

## 4. KYC Tier Framework

### 4.1 Standardized Levels

| Level | Name | Data Collected | Verification | Typical Threshold |
|---|---|---|---|---|
| **L0** | Anonymous | Wallet address only | None | View-only / quotes |
| **L1** | Self-Declared | Name, email, country | User-input, no verification | < $150 equivalent |
| **L2** | Verified | L1 + government ID + liveness | Document verification + biometric | $150 -- $10,000 equivalent |
| **L3** | Enhanced | L2 + proof of address + source of funds | Full EDD | > $10,000 equivalent |

### 4.2 Design Principles

- **Levels are provider-agnostic.** The same L1 credential works for Transak, MoonPay, or any future provider.
- **Levels are persistent.** A user verified to L2 stays at L2 across sessions. No re-verification unless credentials expire or regulations change.
- **Levels are progressive.** Users upgrade only when needed. L1 for small buys, prompted to L2 only at threshold.
- **Levels map to provider requirements.** terminal 3 maintains a mapping table per provider per jurisdiction.

### 4.3 Provider Mapping (Transak -- to be confirmed)

| Transak Requirement | terminal 3 Level | Notes |
|---|---|---|
| Sub-$150, user-input only | L1 | terminal 3 sends name + email + country |
| Above threshold, KYC required | L2 | Two integration modes (see Section 5) |
| High-value / EDD triggers | L3 | Rare; regulatory edge cases |

**Questions for Transak:**
1. Is $150 a global threshold or jurisdiction-specific?
2. Is it per-transaction or rolling (24h / 30d)?
3. What fields constitute "minimal user input" for sub-threshold?
4. Do you accept terminal 3 as a trusted KYC source at L2, or do you always re-verify?

---

## 5. Integration Modes

### Mode 1: Minimal Pass-Through

```
User ──▶ MetaMask ──▶ terminal 3 (L1 data) ──▶ Transak
                                                   │
                                          Transak collects remaining
                                          KYC if needed (in-widget)
```

- terminal 3 sends: name, email, country, wallet address
- Transak handles: additional KYC collection if amount exceeds threshold
- terminal 3 role: session management, state persistence, pre-population

**Pros:** Faster to ship. Less liability for terminal 3. Transak keeps control of their compliance.
**Cons:** Fragmented UX (user enters data in two places). terminal 3 doesn't own the full identity picture. Less leverage for multi-provider play.

### Mode 2: Full Verified Profile

```
User ──▶ MetaMask ──▶ terminal 3 (L2 verified) ──▶ Transak
                           │                          │
                    terminal 3 verifies          Transak trusts
                    (ID + liveness)              terminal 3 KYC
```

- terminal 3 sends: verified identity object (name, DOB, nationality, ID document hash, liveness confirmation, verification timestamp)
- Transak accepts: terminal 3 as trusted KYC provider, skips own verification
- terminal 3 role: full identity orchestration, single verification across all providers

**Pros:** Seamless UX. Single verification. terminal 3 becomes the identity layer (strategic positioning). Reusable across providers.
**Cons:** Requires trust agreement with Transak. Liability sits with terminal 3 for verification quality. Longer to negotiate and build.

### Recommendation

**Ship Mode 1 first.** Prove the integration. Measure conversion. Then negotiate Mode 2 with Transak using data: "X% of users drop off during your KYC step. Here's how Mode 2 fixes that."

Mode 2 is the strategic endgame. Mode 1 is the pragmatic start.

---

## 6. Threshold Enforcement

### 6.1 Architecture

```
┌─────────────────────────────────────────┐
│           Policy Engine                  │
│                                          │
│  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │ Threshold │  │ Jurisd.  │  │ Anti-  │ │
│  │ Rules    │  │ Rules    │  │ Gaming │ │
│  └──────────┘  └──────────┘  └────────┘ │
│                                          │
│  Input: amount, currency, user_country,  │
│         user_kyc_level, tx_history       │
│                                          │
│  Output: ALLOW / UPGRADE_REQUIRED /      │
│          BLOCK + required_level          │
└─────────────────────────────────────────┘
```

### 6.2 Threshold Denomination

**Recommendation:** USD-denominated internally, converted at evaluation time.

- All thresholds stored in USD
- FX conversion at time of transaction using a reliable rate source (e.g., ECB, Transak's own rates, or aggregated)
- Buffer margin of 5% below threshold to account for FX fluctuation (e.g., trigger at $142.50 instead of $150)
- Provider-specific overrides where local regulation mandates local currency thresholds

**Decision point for Transak:** Do they apply thresholds in USD or local currency? Who is the FX source of truth?

### 6.3 Anti-Gaming Controls

| Risk | Mitigation |
|---|---|
| Structuring (multiple sub-threshold txns) | Rolling window aggregation (24h, 7d, 30d). Configurable per jurisdiction. |
| Multi-wallet splitting | Tie KYC identity to multiple wallets. If same L1 identity, aggregate across wallets. |
| Currency arbitrage (use weak currency to stay under threshold) | USD-equivalent normalization for all threshold checks. |
| Rapid re-attempts after block | Rate limiting + cooldown period before retry. |

**Question for Transak:** Do you run your own anti-structuring checks, or do you expect the orchestration layer to handle this?

---

## 7. Standardized Identity Object

The credential terminal 3 passes to any provider:

```json
{
  "schema": "terminal3.identity.v1",
  "user_id": "t3_uuid",
  "kyc_level": 2,
  "verified_at": "2026-02-19T10:00:00Z",
  "expires_at": "2027-02-19T10:00:00Z",
  "jurisdiction": "SG",
  "fields": {
    "full_name": "...",
    "date_of_birth": "...",
    "nationality": "...",
    "email": "...",
    "country_of_residence": "...",
    "id_document": {
      "type": "passport",
      "issuing_country": "SG",
      "verified": true,
      "verification_method": "document_ai + liveness",
      "document_hash": "sha256:..."
    }
  },
  "wallet_addresses": ["0x..."],
  "verification_provider": "terminal3",
  "audit_ref": "t3_audit_abc123"
}
```

This object is:
- **Provider-agnostic** -- same structure sent to Transak, MoonPay, or anyone
- **Versionable** -- `schema` field enables backwards-compatible evolution
- **Auditable** -- `audit_ref` links to terminal 3's internal verification record
- **Selective** -- fields can be omitted based on provider requirements (SD-JWT compatible)

---

## 8. Compliance & Liability Matrix

| Responsibility | Mode 1 | Mode 2 |
|---|---|---|
| **KYC collection** | Shared (terminal 3 = L1, Transak = L2) | terminal 3 |
| **KYC verification** | Transak | terminal 3 |
| **Verification accuracy liability** | Transak | terminal 3 (requires insurance / indemnity) |
| **AML screening** | Transak | Shared (terminal 3 screens, Transak validates) |
| **Threshold enforcement** | terminal 3 (gating) + Transak (own checks) | terminal 3 (primary) + Transak (secondary) |
| **Data retention** | Both (own data) | terminal 3 (primary), Transak (reference) |
| **Regulatory reporting** | Transak (as licensed entity) | Transak (as licensed entity) + terminal 3 (as data processor) |
| **Audit trail** | Fragmented | Unified (terminal 3 audit log) |

**Key risk in Mode 2:** terminal 3 assumes verification liability. This requires:
- Clear contractual indemnification
- Insurance coverage for verification errors
- Regular audit of verification accuracy rates
- Defined SLA for verification quality (e.g., <0.1% false positive rate)

---

## 9. Decision Matrix -- Requires Alignment

| # | Decision | Options | Recommendation | Needs Input From |
|---|---|---|---|---|
| 1 | Routing model | Provider-declared vs. Smart routing | Hybrid (declared now, smart later) | Transak + MetaMask |
| 2 | Integration mode at launch | Mode 1 (minimal) vs. Mode 2 (full) | Mode 1 | Transak |
| 3 | Threshold denomination | USD vs. local currency | USD-normalized | Transak |
| 4 | Threshold window | Per-tx vs. rolling | Rolling 24h (confirm with Transak) | Transak |
| 5 | KYC trust model | Transak re-verifies vs. trusts terminal 3 | Re-verifies (Mode 1), trust later (Mode 2) | Transak compliance |
| 6 | Anti-gaming ownership | terminal 3 vs. Transak vs. shared | Shared (terminal 3 gates, Transak validates) | Transak |
| 7 | FX rate source | Transak rates vs. independent | Align on single source | Transak |
| 8 | Data residency | Where is KYC data stored? | terminal 3 infra (jurisdiction-aware) | Legal / Transak |

---

## 10. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Transak rejects Mode 2 trust model | Stuck on Mode 1 permanently; limits multi-provider play | Medium | Ship Mode 1 with conversion data to build the case |
| Threshold gaming via structuring | Regulatory exposure | Medium | Rolling window aggregation + cross-wallet identity linking |
| FX volatility causes threshold edge cases | Users blocked unexpectedly OR slip through | Low-Medium | 5% buffer + clear user communication on equivalent thresholds |
| MetaMask changes frontend architecture | Integration breaks | Low | Abstract MetaMask interface layer; don't couple to their implementation |
| Regulatory divergence across jurisdictions | Single threshold model doesn't hold | High | Jurisdiction-aware policy engine from day 1 (not bolt-on) |
| KYC credential expiry mid-transaction | UX failure | Low | Pre-check expiry before routing; graceful upgrade prompt |

---

## 11. Questions for Transak

### Thresholds
1. Is the $150 threshold global, or does it vary by jurisdiction/currency?
2. Per-transaction or rolling window? If rolling, what window?
3. Who is the FX source of truth for threshold conversion?
4. Do you apply your own anti-structuring checks?

### KYC
5. What constitutes "minimal user input" for sub-threshold? Exact field list?
6. Would you accept terminal 3 as a trusted KYC provider (Mode 2)? What would that require?
7. What is your KYC credential expiry policy?
8. Do you support receiving pre-verified identity objects via API (vs. widget-based collection)?

### Integration
9. Do you prefer Mode 1 or Mode 2 at launch?
10. What is your API capability for receiving structured identity payloads?
11. Do you support webhook callbacks for KYC status changes on your side?
12. Can we white-label or embed your flow, or must it be redirect-based?

### Commercial
13. How do you view terminal 3's role in a multi-provider routing scenario?
14. Are there volume commitments or exclusivity expectations?
15. What is your timeline for technical integration kickoff?

---

## 12. Proposed Next Steps

| Step | Owner | Timeline |
|---|---|---|
| Internal review of this document | terminal 3 Product | By Feb 21 |
| Share with Transak for pre-read | terminal 3 Product | Feb 24 |
| Working session with Transak | terminal 3 + Transak | Week of Feb 24-28 |
| Align on Mode 1 spec | Both | By Mar 7 |
| API spec exchange | Both (engineering) | By Mar 14 |
| Development kickoff | Both | Mar 17 |
| Mode 1 integration complete | Both | Target: Apr 30 |

---

*This document is a working draft for alignment purposes. All architectural decisions are proposals pending joint review with Transak.*
