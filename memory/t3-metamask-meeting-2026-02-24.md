# MetaMask Discussion -- Meeting Notes
**Date:** Feb 24, 2026
**Participants:** Janani (T3), Amit, Malcolm Ong, Joey Liu, Edward Fu

---

## Context
MetaMask sent async message asking about a "modular integration" -- wanting to potentially own auth and user storage while using T3 as part of their KYC management infra layer. This call was to align internally on how to respond.

## Key Decisions & Positions

### Auth -- NON-NEGOTIABLE (Malcolm's position, team aligned)
- Auth is T3's hook. Without it, T3 becomes just a KYC vendor (commodity, replaceable by Sumsub etc.)
- If T3 gives away both auth AND storage, there's no stickiness. DIDs + VCs are open standards, KYC is KYC -- T3's value is the **glue** of all these combined.
- **Two interpretations of "modular auth":**
  1. **Hard:** MetaMask uses Web3Auth entirely, T3 out of the auth loop (BAD)
  2. **Light (Helpling model):** MetaMask owns auth UX/experience, T3 runs identity backend via SSO SDK (ACCEPTABLE -- already working with Helpling this way)

### Why MetaMask Wants Own Auth (Malcolm's hypothesis)
- Web3Auth was acquired by ConsenSys/MetaMask. The founder is on the Linea team.
- They literally have an auth company in-house -- likely the driver behind "we want to own auth."

### Storage -- More Complex Than "Just a Database"
- Initially team thought giving up storage was OK. **Malcolm corrected:** storage isn't just a database -- it's compliance, data processing responsibility, regulatory vault.
- T3's storage is twofold: (1) decentralized/self-sovereign/privacy-preserving, (2) regulatory vault for compliance. This combo is a key differentiator vs IDOS, ZKME (pure Web3).
- **Subnet model proposed:** Spin up dedicated storage nodes for MetaMask (pseudo on-prem). They get semi-control over their data, T3 stays in the infrastructure. Like providing physical servers.

### What MetaMask Actually Wants (Team's Read)
- **Janani's gauge:** Likely about reducing vendor lock-in risk. "What if we make a wrong decision?" They want an exit path, not necessarily to build everything themselves.
- **Possible data split:** MetaMask holds KYC verification status, T3 holds PII. Could work as a middle ground.
- **Amit's note:** Consensys is on T3's cap table -- they have leverage from that side too.

### T3's Competitive Moat vs Alternatives (IDOS etc.)
- DID/VC issuance -- IDOS can do this (open standards, not hard)
- But T3's power: storage architecture, regulatory vault proposal, architecture that directly fits MetaMask's problem statements, willingness to customize and manage complex flows
- T3 already volunteered to handle MetaMask's KYC decision logic (very complex, 4-5 variable types) -- this is additional lock-in not part of this conversation but strategically valuable long-term

## Action Items

| Who | What | When |
|-----|------|------|
| Amit | Slack huddle with Alex (MetaMask) -- ask clarifying questions, NOT present a proposal | Feb 25 (before evening SGT) |
| Amit | Clarify: Why modular now? Cost issue, ownership issue, vendor lock-in? | Feb 25 |
| Amit | Clarify: What do they mean by "own storage"? Hold PII? Or just want dedicated infra? | Feb 25 |
| Amit | Invite team to huddle if Alex available | Feb 25 |
| Janani | Lorenzo weekly product catch-up -- 10pm SGT Feb 25. MetaMask topic likely to come up | Feb 25 |
| Amit | Try to join Lorenzo call | Feb 25 |
| Malcolm | Double-check MSA re: data controller vs processor status | Post-call |
| Team | NO proposals yet. Questions only. Understand context first, then position solution | Until clarity from Alex |

## Strategic Frame (Janani's insight)
> "My only thing might be to have a proposal which convinces them that this is enough lock-in for us while it feels a little flexible for them."

The goal: a proposal that gives MetaMask comfort (not trapped) while keeping T3 in the critical path (not replaceable).

## Key Quote (Malcolm)
> "The hook for us is to be the source of truth. When we're the source of truth, we're the sun in the universe. Every application and function relies on our identity. Auth is the door towards that."

---

## Upcoming
- **Feb 25 evening:** Lorenzo call (10pm SGT) -- MetaMask will come up
- **Feb 25:** Amit x Alex huddle -- results determine next steps
- **Post-Alex huddle:** Regroup, decide if proposal makes sense or if it's a no-go
