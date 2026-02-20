# Why terminal 3 for MetaMask
## A Strategic Identity Infrastructure Partnership

**Prepared for:** MetaMask Leadership
**From:** terminal 3 Product
**Date:** February 20, 2026

---

## The Decision

MetaMask is choosing its identity infrastructure partner -- not just a KYC vendor. This decision will define how MetaMask handles user identity, authentication, compliance, and payment routing across every product line for the next 3-5 years.

This document explains why terminal 3 is the right choice, how it compares directly against idOS (the alternative under evaluation), and what MetaMask risks by choosing a narrower solution.

---

## What MetaMask Needs (In Your Own Words)

From our working sessions, MetaMask has articulated a clear vision:

- **A unified "MetaMask ID"** that works across all products -- on-ramp, card, trading, equities, perps, prediction markets
- **Reusable KYC** so users verify once and never again across providers
- **Privacy-preserving** identity that aligns with MetaMask's Web3 philosophy
- **No backend dependency** -- the solution must work with MetaMask's frontend-only architecture
- **Reduced friction** where users currently KYC multiple times across Transak, MoonPay, and future services
- **A path to becoming like Coinbase/Kraken/Robinhood** (unified experience) while remaining Web3-native

This is not a KYC problem. This is an identity infrastructure problem. The choice of partner determines whether MetaMask can deliver on this vision or not.

---

## What terminal 3 Delivers

### 1. Unified Authentication + Identity (One Integration, All Products)

terminal 3 provides both **authentication** (login, session management, SSO) and **identity verification** (KYC L1/L2/L3, credential issuance, VP sharing) in a single integration.

**What this means for MetaMask:**
- Users log in once via terminal 3 and are authenticated across all MetaMask products
- The same identity serves on-ramp (Transak), card (future bank partner), trading, and any new product line
- MetaMask gets its "MetaMask ID" without building backend identity infrastructure
- One SDK to integrate. One vendor to audit. One relationship to manage.

**How idOS compares:**
idOS is a credential storage network. It does not provide authentication, login, session management, or SSO. If MetaMask chose idOS, it would still need to source and integrate a separate authentication provider, build custom session management, and stitch together login + identity across products manually. idOS solves one piece of the puzzle. terminal 3 solves the whole picture.

### 2. Smart Verifiable Credentials + Ongoing Compliance Monitoring

terminal 3 issues **Smart Verifiable Credentials (Smart VCs)** -- living credentials that can be refreshed, revoked, and re-verified over time. This is not static storage. This is compliance as a continuous process.

**What Smart VCs deliver for MetaMask:**
- **Sanctions and PEP screening:** At onboarding AND on an ongoing basis. terminal 3 screens users against global sanctions lists and politically exposed person (PEP) databases -- built into the platform, not a one-time check.
- **Scheduled re-verification:** Smart VCs are refreshed on a configurable schedule (e.g., every 12 months). terminal 3 prompts re-verification and reruns key checks. Credentials that fail re-certification are automatically flagged or suspended.
- **Event-driven re-verification:** When conditions change (new jurisdiction activated, risk threshold crossed), terminal 3 triggers targeted re-verification without requiring a full KYC restart.
- **Real-time revocation:** If a user is flagged post-verification (sanctions hit, fraud detected), their Smart VC is revoked via the DID registry. Every verifier (Transak, card providers, future partners) checks revocation status before accepting a credential.
- **Cross-provider risk intelligence:** When a user verified through Transak later tries the MetaMask card, terminal 3 carries their verified identity AND Smart VC status across. A user with 5 successful orders and an active Smart VC is a demonstrably lower risk.
- **Conversion optimization:** Returning verified users with valid Smart VCs skip KYC entirely -- zero friction.

**How idOS compares:**
idOS stores encrypted credentials at the point of issuance -- a snapshot frozen in time. There is no scheduled re-verification, no event-driven refresh, no sanctions monitoring after initial issuance, and no mechanism to revoke a compromised credential across all consumers simultaneously. If a credential is issued on Monday and the user's identity is compromised on Tuesday, every app consuming that idOS credential must independently discover and handle the problem. With terminal 3's Smart VCs, one revocation propagates to all verifiers instantly via the DID registry.

**Why this matters now:**
The recent Onfido fraud incident demonstrated that static, point-in-time KYC is insufficient. Sophisticated fraud using stolen identities requires ongoing monitoring. Smart VCs are specifically designed for this.

### 3. Provider-Agnostic Architecture

terminal 3 orchestrates across KYC providers (Veriff, Onfido, Sumsub, and others) without changing MetaMask's integration.

**What this means for MetaMask:**
- If a KYC provider fails (as Onfido recently did), terminal 3 can switch to an alternative provider without any change to MetaMask's frontend or integration
- As MetaMask expands to new regions, terminal 3 activates the best local KYC provider for each jurisdiction
- MetaMask's security team audits one SDK, not multiple vendor integrations

**How idOS compares:**
idOS depends entirely on the quality of whichever issuer created the credential. If the issuer fails (as Onfido recently did), the credential is permanently compromised. There is no orchestration layer to reroute, no ability to switch providers, and no way to re-verify affected users without starting from scratch. With terminal 3, a provider switch is a configuration change. With idOS, it is a re-architecture.

### 4. Compliance as Infrastructure (Not an Afterthought)

terminal 3 builds compliance into the network layer, not the application layer.

**What this means for MetaMask:**
- **Unified audit trail:** A single compliance authority can oversee and audit identity operations across all of MetaMask's providers and product lines -- not siloed per app
- **Regulatory Vault:** Sensitive artifacts (liveness video, document images) are stored in a jurisdiction-aware encrypted vault, accessible to regulators on demand without exposing PII to providers
- **DID Registry + Revocation:** Verifiers (Transak, card providers, future partners) can check credential validity in real-time without accessing underlying personal data
- **Duplicate identity prevention:** Built-in detection prevents the same government ID from creating multiple accounts -- configurable per client

**How idOS compares:**
In idOS, compliance is handled at the application layer -- each app that consumes idOS credentials is responsible for its own regulatory checks, audit trails, and reporting. This means every new MetaMask product line (on-ramp, card, trading) must independently build compliance logic. There is no network-level compliance authority and no unified audit view across providers. terminal 3 flips this: compliance is a built-in network role. A regulator or compliance officer gets a verified view across all of MetaMask's identity operations without each product rebuilding it from scratch.

### 5. PCI DSS Certification and Payment Routing Readiness

terminal 3 is on track for PCI DSS certification, positioning it to handle sensitive payment data alongside identity.

**What this means for MetaMask:**
- As MetaMask expands into card products, trading, and cross-border payments, terminal 3 can serve as both the identity layer AND the payment data orchestration layer
- One partner that grows with MetaMask across the full product roadmap -- from "who is this user" to "how does this user pay"
- Reduces the number of touchpoints handling sensitive financial data, simplifying MetaMask's security surface

**How idOS compares:**
idOS is a credential storage network with zero payment capability. It has no path to PCI DSS, no ability to handle card data, and no role in payment orchestration. As MetaMask scales into cards, trading, and cross-border payments, idOS remains frozen as a KYC storage layer while MetaMask must source and integrate separate payment infrastructure from scratch.

terminal 3 converges identity and payment data handling into a single infrastructure partner -- fewer vendors, fewer audits, smaller security surface.

### 6. A Richer Data Ecosystem (Beyond KYC)

terminal 3's architecture supports multiple participant types beyond the basic user-verifier-consumer model.

**What this means for MetaMask:**
- **Data providers** (banks, telcos, credit bureaus) can plug directly into terminal 3 as verified data sources -- enabling richer identity signals beyond basic KYC
- **Node operators** run infrastructure independently of data providers, creating separation of concerns and reducing trust requirements
- **Richer data types:** Income history, professional credentials, transaction data, and credit signals can flow through terminal 3 under user consent -- enabling MetaMask to offer premium financial products that require more than just "did this person pass KYC"

**How idOS compares:**
idOS operates a three-party model: user, KYC verifier, and consuming app. That is the entire ecosystem. There is no mechanism for banks, telcos, or credit bureaus to participate as data providers. The only data that flows through idOS is a credential -- a binary signal that someone passed KYC. terminal 3's multi-participant architecture (users, verifiers, data providers, node operators, compliance authorities) was designed from the ground up for the kind of rich data economy MetaMask needs to power premium financial products.

**The long-term picture:**
MetaMask's vision of becoming a unified financial platform (like Coinbase but Web3-native) requires identity signals that go far beyond document verification. terminal 3's ecosystem is built for this. idOS's three-party credential vault is not.

---

## Head-to-Head: terminal 3 vs idOS

| Capability | terminal 3 | idOS |
|---|---|---|
| **Authentication (login, SSO)** | ✅ Unified auth across all MetaMask products | ❌ Not offered -- MetaMask needs a separate auth provider |
| **KYC orchestration** | ✅ Provider-agnostic (Veriff, Onfido, Sumsub) | ⚠️ Depends on individual issuers -- no switching capability |
| **Live risk intelligence** | ✅ Real-time APIs, cross-provider signals | ❌ Static snapshots only -- no post-issuance monitoring |
| **Session persistence** | ✅ Returning users skip KYC entirely | ❌ Re-decrypt and re-share for every session |
| **Compliance infrastructure** | ✅ Network-level: unified audits, regulatory vault, DID registry | ❌ App-level: each product builds its own compliance |
| **Duplicate identity prevention** | ✅ Built-in, configurable per client | ❌ Not a network feature |
| **PCI DSS / payment routing** | ✅ Certification in progress | ❌ No payment capability |
| **Data ecosystem** | ✅ Multi-participant: banks, telcos, credit bureaus as data providers | ❌ Three-party only: user, verifier, consumer |
| **Integration complexity** | Standard REST APIs -- works with MetaMask's no-backend architecture | Requires blockchain node integration, client-side encryption, wallet signatures |
| **KYA (agent identity)** | On roadmap -- architecturally planned | ❌ Not offered |
| **Enterprise SLAs** | ✅ 99.9% uptime, dedicated support | ❌ Decentralized protocol -- community support, no guaranteed response times |

---

## The Platform Fee: An Investment, Not a Cost

MetaMask leadership has raised the platform fee as a concern. Here is why it delivers outsized value:

### What the platform fee pays for:

| Capability | Included | Without terminal 3, MetaMask would need to... |
|---|---|---|
| Unified auth + identity | ✅ | Integrate 2-3 separate vendors + build session management |
| Live risk intelligence | ✅ | Build and maintain an internal risk engine |
| Cross-provider user history | ✅ | Build a custom data warehouse + integration per provider |
| Session persistence (returning users) | ✅ | Build user state management without a backend |
| Provider switching (Onfido → Veriff) | ✅ | Re-integrate each provider separately |
| Compliance infrastructure | ✅ | Build audit trails, regulatory vault, DID registry from scratch |
| Duplicate identity prevention | ✅ | Build internal dedup logic + cross-reference systems |
| PCI DSS payment routing (upcoming) | ✅ | Engage a separate payment processor |

### The ROI equation:

**Without terminal 3:**
MetaMask integrates a free or low-cost credential storage solution. Result: each new product line (card, trading, cross-border) requires a separate identity integration, separate compliance build, separate auth system. Engineering cost compounds with every product launch.

**With terminal 3:**
MetaMask integrates once. Every new product line inherits identity, auth, compliance, and risk intelligence from day one. Engineering cost is flat.

The platform fee is the difference between building identity infrastructure internally (months of engineering per product) and inheriting it from a dedicated partner (weeks of integration, once).

---

## What MetaMask Loses by Choosing a Narrower Solution

This is not about terminal 3 vs. a specific competitor. It is about what MetaMask gives up by choosing a solution that only solves credential storage:

1. **No unified auth.** MetaMask still needs to solve login, session management, and cross-product identity separately.

2. **No live intelligence.** A static credential cannot detect post-verification fraud, sanctions changes, or behavioral anomalies. The Onfido incident showed why this matters.

3. **No cross-provider history.** When a user moves from Transak to the card product, a storage-only solution cannot carry risk context across. terminal 3 can.

4. **No compliance infrastructure.** Every product line builds its own audit trails, regulatory reporting, and revocation logic. With terminal 3, it is inherited.

5. **No path to payment routing.** As MetaMask expands into financial products requiring PCI DSS, a storage solution cannot grow with it. terminal 3 can.

6. **No ecosystem for richer data.** If MetaMask wants to offer premium financial products (credit, lending, insurance), it needs identity signals beyond basic KYC -- income, credit scores, professional credentials. A credential vault cannot source these. terminal 3's data provider model can.

7. **Integration complexity multiplies.** Each new provider, each new product, each new region requires a new integration. With terminal 3, these are configuration changes, not engineering projects.

---

## Timeline and Readiness

| Milestone | Date | Status |
|---|---|---|
| Architecture alignment | Feb 2026 | ✅ In progress |
| PRD + security pack delivered | Feb 20, 2026 | ✅ Delivered |
| MSA signature | Pending | ⏳ Blocker for Transak engineering |
| Transak engineering alignment | Late Feb | Ready when MSA clears |
| Engineering build | Mar 2026 | terminal 3 ready to begin |
| Go-live (testing) | Mar 31, 2026 | Target confirmed |
| Production rollout | Apr 15-16, 2026 | Target confirmed |

terminal 3's engineering team is ready. KYC infrastructure (Veriff integration, SD-JWT, TEE storage, OID4VP) is live. The integration effort on Transak's side is minimal -- primarily accepting VPs via their Auth Reliance product plus implementing the Verifier SDK.

The critical path is the MSA. Once signed, engineering kickoff can happen within days.

---

## Recommendation

terminal 3 is not the cheapest option. It is the option that scales.

MetaMask's ambition is to become the unified gateway to Web3 finance -- on-ramp, card, trading, lending, and beyond. That ambition requires identity infrastructure, not identity storage.

Choosing terminal 3 means MetaMask integrates once and inherits identity, authentication, compliance, risk intelligence, and payment routing readiness across every product it launches for the next 3-5 years.

Choosing a narrower solution means MetaMask solves KYC today and rebuilds identity infrastructure for every product that follows.

The platform fee is the cost of not having to build this internally. The value is compounding.

---

*terminal 3 -- Identity infrastructure for the next generation of finance.*
