# Sumsub vs terminal 3: Why They're Not Competitors
**For: Joey Liu → Desmond's PM**
**Date: Feb 25, 2026**
**Author: Janani Gopalakrishnan**

---

## TL;DR

Sumsub is a KYC vendor adding blockchain attestations as a feature. terminal 3 is identity infrastructure that services like Sumsub would plug into. They operate at different layers of the stack.

---

## What Sumsub Is Doing

Sumsub is a traditional KYC/AML provider that has recently added on-chain identity attestations:

- **BNB Chain** -- via BNB Attestation Service (BAS). Users complete Sumsub KYC → receive an on-chain attestation tied to their wallet.
- **Solana** -- via Solana Attestation Service (SAS). Same model, different chain.
- **"Verify once, reuse"** via Sumsub ID -- but Sumsub remains the centralized trust anchor. They are both the issuer AND verifier.

This is a KYC company bolting chain receipts onto its existing product. The user doesn't control the credential -- Sumsub does.

---

## Where terminal 3 Is Fundamentally Different

| Dimension | Sumsub | terminal 3 |
|-----------|--------|------------|
| **What it is** | KYC vendor + chain attestation feature | Identity infrastructure layer |
| **Standards** | Proprietary (BAS, SAS) -- chain-locked | W3C VCs, SD-JWT, mDoc, OID4VP -- portable |
| **User control** | Sumsub holds data, issues proofs on user's behalf | User holds credentials, selectively discloses via TEE |
| **Scope** | KYC/AML verification only | Any credential: payments, authorization, regulatory, agent identity (KYA) |
| **Storage** | Centralized (Sumsub servers) | Atomized, TEE-encrypted, regulatory vault |
| **Auth** | None (relies on client's auth) | Full auth layer (email+OTP, SSO SDK) |
| **Orchestration** | Single provider (Sumsub = the KYC) | Provider-agnostic orchestration (Veriff today, any provider tomorrow) |
| **Compliance model** | One-time verification | Smart VCs: scheduled re-verification, event-driven triggers, ongoing sanctions/PEP screening |
| **Enterprise partners** | dApps needing basic KYC | MetaMask, Mastercard, Visa, IMDA, DNP |

---

## The Stack Analogy

Think of it as cloud infrastructure vs a SaaS app:

- **terminal 3 = AWS** -- provides the identity primitives (auth, credential issuance, storage, presentation, compliance) that any application can build on.
- **Sumsub = a SaaS tool running on AWS** -- it does one thing well (KYC verification) and could theoretically use terminal 3's infrastructure to issue and store credentials.

Sumsub adding BNB/Solana attestations is like a SaaS company adding an API endpoint. It doesn't make them infrastructure.

---

## Why This Matters for Desmond

1. **No overlap in buyer persona.** terminal 3 sells to platforms building identity-native products (MetaMask, payment networks). Sumsub sells to apps that need a KYC checkbox.

2. **No overlap in technical scope.** Sumsub can't do auth, can't do selective disclosure, can't do regulatory vault, can't do cross-ecosystem credential portability. These are terminal 3's core.

3. **Sumsub validates the market, not the competition.** The fact that KYC vendors are racing to add on-chain attestations proves the market terminal 3 is building for. But their approach (proprietary, chain-specific, centralized) is exactly what terminal 3's standards-based architecture solves.

---

## References

- [Sumsub x BNB Attestation Service](https://sumsub.com/newsroom/sumsub-partners-with-binances-bnb-attestation-service-to-streamline-web3-identity-verification/)
- [Sumsub x Solana Attestation Service](https://sumsub.com/newsroom/sumsub-and-solana-debut-on-chain-identity-attestations-at-accelerate-new-york/)
