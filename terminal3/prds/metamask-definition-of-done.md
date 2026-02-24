# MetaMask Integration: Definition of Done
**Date: Feb 25, 2026**
**Author: Janani Gopalakrishnan**
**Status: DRAFT -- pending team review**

---

## Purpose

Define clear completion criteria for the MetaMask x terminal 3 integration. This DoD covers what "done" means for Phase 1 (Native Deposit Flow via Transak) across technical, commercial, and operational dimensions.

---

## Phase 1 Scope Recap

**What:** Unified MetaMask ID for KYC across on-ramp providers, starting with Transak (US & EU, Mobile + Browser).

**How:** terminal 3 provides auth + KYC orchestration + credential storage. Users verify once via terminal 3, credential is presented to Transak via Verifier SDK. MetaMask bears cost.

---

## Technical DoD

### Auth Layer
- [ ] SSO SDK integrated -- MetaMask owns auth UX, terminal 3 runs identity backend
- [ ] Auth flow works for both Mobile (React Native) and Browser Extension
- [ ] Session management and token lifecycle defined and tested
- [ ] Fallback handling: what happens when auth fails, times out, or user abandons

### KYC Flow
- [ ] User completes KYC via terminal 3 orchestration (Veriff as provider)
- [ ] KYC result stored as SD-JWT Verifiable Credential in TEE
- [ ] Credential includes: verification status, jurisdiction, provider, timestamp, expiry
- [ ] Duplicate identity check functional (same user, multiple wallets)
- [ ] KYC decision logic implemented (4-5 variable types per MetaMask requirements)

### Credential Presentation
- [ ] Transak can request and verify credential via Verifier SDK
- [ ] Selective disclosure works -- Transak sees only what's needed (no full PII leak)
- [ ] OID4VP flow tested end-to-end
- [ ] Re-presentation works without user re-doing KYC

### Smart VC Compliance
- [ ] Scheduled re-verification configured (cadence TBD with MetaMask compliance)
- [ ] Sanctions/PEP screening running on ongoing basis (not just at issuance)
- [ ] Revocation mechanism tested -- credential can be revoked via DID registry
- [ ] Event-driven re-verification triggers defined

### Storage & Regulatory
- [ ] User PII stored in TEE-encrypted atomized storage
- [ ] Regulatory vault operational -- audit logs, data retention, access controls
- [ ] Data controller vs processor roles clarified in MSA (Malcolm to confirm)
- [ ] Subnet model scoped if MetaMask requires dedicated storage nodes

### Edge Cases & Error Handling
- [ ] User abandons mid-KYC -- state recovery or clean restart
- [ ] KYC rejected -- user can retry with same or different provider
- [ ] Credential expired -- re-verification flow without full re-KYC
- [ ] Network failures -- graceful degradation on both mobile and browser
- [ ] Transak VP request fails -- retry logic and error messaging

---

## Commercial DoD

- [ ] MSA signed by both parties (**CRITICAL PATH BLOCKER**)
- [ ] Pricing model agreed -- per-verification, per-auth, or bundled
- [ ] Tripartite agreement with Transak aligned (compliance teams)
- [ ] Platform fee structure resolved (flagged 2 weeks ago with MetaMask leadership)
- [ ] Data processing agreement in place (GDPR, data residency requirements)

---

## Operational DoD

- [ ] Monitoring and alerting configured for auth + KYC flows
- [ ] SLA defined: uptime, response time, support escalation path
- [ ] L3 support model defined (who handles what when things break)
- [ ] Runbook for common failure scenarios documented
- [ ] Load testing completed for projected MetaMask user volumes

---

## Integration Testing DoD

- [ ] E2E happy path tested: signup → KYC → credential issuance → Transak VP → on-ramp
- [ ] E2E unhappy paths tested (see edge cases above)
- [ ] Mobile (iOS + Android) tested
- [ ] Browser extension tested
- [ ] Performance benchmarks met (latency targets TBD)
- [ ] Security review passed by MetaMask security team (architecture pack delivered ✅)

---

## Go-Live Criteria

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| MSA signed | ASAP | ⏳ Pending |
| Security review passed | Mar 2026 | 📄 Docs delivered, review in progress |
| E2E testing complete | Mar 31, 2026 | 🔜 |
| Staging deployment | Apr 1-14, 2026 | -- |
| Production rollout | Apr 15-16, 2026 | -- |

---

## Open Questions (Pending Alex Huddle -- Feb 25)

1. **"Modular auth" -- which interpretation?**
   - Hard (MetaMask uses Web3Auth, T3 out of auth loop) → Non-starter for T3
   - Light/Helpling model (MetaMask owns UX, T3 runs backend via SSO SDK) → Acceptable
   
2. **"Own storage" -- what do they mean?**
   - Hold PII themselves? → Data controller implications, regulatory burden shifts
   - Dedicated infra? → Subnet model works, T3 stays in the stack

3. **Data split model?**
   - MetaMask holds KYC verification status, T3 holds PII → possible middle ground

4. **Vendor lock-in concern scope** -- is this about exit rights, data portability, or pricing leverage?

---

## Strategic Guardrails

Per internal alignment (Feb 24, Malcolm + team):

- **Auth is non-negotiable.** Without auth, T3 becomes a replaceable KYC vendor. Auth is the door to being the source of truth.
- **Storage = compliance, not just a database.** Giving up storage means giving up regulatory vault, data processing responsibility, and a core differentiator vs IDOS/ZKME.
- **Goal:** A proposal that gives MetaMask comfort (not trapped) while keeping T3 in the critical path (not replaceable).

> "The hook for us is to be the source of truth. When we're the source of truth, we're the sun in the universe." -- Malcolm Ong
