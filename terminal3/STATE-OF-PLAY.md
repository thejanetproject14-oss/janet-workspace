# terminal 3: State of Play
> Last updated: Feb 20, 2026 by Janet ✦
> This is the single source of truth. Janet maintains this after every context update.

---

## MetaMask Partnership

### Status: IN PROGRESS -- HIGH PRIORITY
- **Product lead at MetaMask:** Lorenzo Santos
- **terminal 3 product lead:** Janani Gopalakrishnan (Sunshine)
- **MSA status:** Pending signature -- THIS IS THE CRITICAL PATH BLOCKER
- **Target go-live:** March 31, 2026 (testing) → April 15-16 (rollout)
- **Scope:** Native Flow (Deposit) for US & EU via Transak -- Mobile + Browser

### What MetaMask Wants (In Their Words)
- A unified "MetaMask ID" across all products (on-ramp, card, trading, equities/perps)
- Reusable KYC -- users verify once, never again across providers
- Privacy-preserving identity aligned with Web3 philosophy
- No backend dependency -- solution must work frontend-only
- Reduced friction -- users currently KYC multiple times across providers
- Path to becoming like Coinbase/Kraken/Robinhood but Web3-native

### What MetaMask Needs From Us NOW
1. Per-API-call system diagram ✅ (delivered in architecture pack)
2. Data-flow diagrams for security review ✅ (delivered)
3. 80/20 architecture pack for security team ✅ (delivered)
4. Orchestration decision logic ✅ (delivered)
5. Off-happy-path flows (edge cases, failures, retries) ✅ (delivered)

### Three Threats to the Deal
1. **Platform fee perception** -- caught MetaMask leadership off guard 2 weeks ago. Triggered competitive review.
2. **idOS competitive check** -- leadership doing due diligence. Lorenzo is sympathetic to terminal 3.
3. **zkMe smear campaign** -- baseless legal dispute claims + humanity protocol bot allegations. Being addressed by Malcolm/Gary/legal.

### Transak Relationship
- MetaMask introduced terminal 3 to Transak
- 3-way kickoff call happened Feb 9 (Lorenzo, Janani, Amit from Transak)
- Transak has Auth Reliance (live) and KYC Reliance (coming soon, going provider-agnostic)
- Transak product lead: Amit Rath
- MetaMask bears cost of auth + KYC
- Transak effort is minimal -- primarily VP acceptance via Verifier SDK
- Need compliance teams to align on tripartite agreement

### Meld Risk
- MetaMask exploring Meld as long-term orchestration layer
- Concerns about single point of failure work in terminal 3's favor (fallback/complement)

---

## terminal 3 Technical Capabilities (What's Real)

### LIVE and Shipping
- **KYC orchestration** -- live, provider-agnostic (Veriff currently)
- **SD-JWT credentials** -- live, selective disclosure
- **TEE storage** -- live, encrypted at rest
- **Smart Verifiable Credentials** -- live (documented in OSN KYB reference)
  - Scheduled re-verification (configurable refresh cycles)
  - Event-driven re-verification
  - Sanctions/PEP screening (ongoing, not one-time)
  - Real-time revocation via DID registry
- **Regulatory Vault** -- live (secure encrypted storage, audit logging)
- **DID Registry + Revocation** -- live
- **OID4VP** -- live (VP generation and sharing)
- **Verifier SDK** -- live (for consumers like Transak)
- **Duplicate identity prevention** -- being built
- **Authentication (email + OTP)** -- live

### ON ROADMAP (Not Yet Built)
- **KYA (Know Your Agent)** -- designed but not built
- **PCI DSS certification** -- in progress
- **Smart routing** (intent-based provider selection) -- future
- **Device/behavioral signals** -- future

---

## Competitive Landscape

### idOS
- Decentralized identity storage on Kwil blockchain + Arbitrum Orbit L2
- Consortium backed: Arbitrum, Circle, Ripple, NEAR
- Self-custody model -- user-controlled encryption
- **Key weakness for MetaMask:** Storage primitive only, no auth, no orchestration, no ongoing monitoring, no payment capability
- **Positioning:** terminal 3 is identity infrastructure (auth + KYC + compliance + payment routing). idOS is credential storage.
- No confirmed integration with MetaMask -- competitive check only

### zkMe
- Hong Kong-based company, known industry agitator
- Making baseless claims about legal disputes with terminal 3
- Also targeting Humanity Protocol with bot allegations
- terminal 3 has ZERO legal disputes, commercial relationships, or partner overlap with zkMe
- Being handled by Malcolm, Gary, and legal team

---

## Key People

### terminal 3
- **Janani Gopalakrishnan** -- Head of Product (Sunshine)
- **Malcolm Ong** -- Co-founder/leadership
- **Gary** -- Co-founder/leadership
- **Truong Nguyen** -- BE Engineer
- **Edward Fu** -- BE Engineer
- **Phuc Hoang** -- BE Engineer
- **Quang Tran** -- FE Engineer
- **Matthew Torres** -- FE Engineer
- **Ruby Wu** -- Designer
- **Micho Gunawan** -- Designer
- **Joey** -- Legal coordination
- **Charmaine** -- Business development
- **Lauren** -- Marketing/LinkedIn
- **Nathan** -- Former IMDA digital lead, now at terminal 3

### MetaMask
- **Lorenzo Santos** -- Product Manager (weekly sync with Janani)
- **Alex** -- Business lead (dealt with pricing issue)

### Transak
- **Amit Rath** -- Product lead (4 years at Transak, handles frontend + fiat/order team)

### Customer References Available
- **IMDA** (Singapore regulator) -- pilot relationship
- **DNP** (Japan) -- deepening technical relationship, regulated KYC credentials
- **Humanity Protocol** -- former client (ended Dec 2025), can serve as reference
- **Open Campus** -- former client (ended Dec 2025)

---

## Key Dates
- **Feb 20, 2026** -- All deliverables shipped (competitive analysis, E2E PRD, architecture pack, value proposition)
- **Feb 24-28** -- DNP Japan market testing
- **End of Feb** -- MetaMask needs to close competitive analysis
- **Mar 31** -- Target testing go-live for MetaMask integration
- **Apr 15-16** -- Target production rollout

---

## Source Files Index
| File | Contents |
|---|---|
| `source/metamask-master-prd-raw.md` | Full master PRD + meeting transcripts (Feb 6, Feb 9, Feb 20 calls) |
| `source/qa-context-feb20.md` | Q&A answers from Sunshine's colleague (Dolphin) |
| `source/kyb-osn-reference.md` | OSN KYB doc -- proves Smart VC + ongoing compliance capabilities |
