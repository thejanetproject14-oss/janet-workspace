# terminal 3 Knowledge Base Architecture

## How Context Is Organized

```
terminal3/
├── MISSION-CONTROL.md          ← Hub: current status, priorities, who's doing what
├── STATE-OF-PLAY.md            ← Living summary: what's true RIGHT NOW (Janet maintains)
│
├── briefs/                     ← Pre-compiled agent briefs (injected into sub-agent prompts)
│   ├── arjuna-brief.md         ← What Arjuna needs to know (payments, Visa, Mastercard)
│   ├── yudhishthira-brief.md   ← What Yudhishthira needs to know (KYC, identity, MetaMask)
│   ├── vidura-brief.md         ← What Vidura needs to know (company knowledge, competitive)
│   └── sahadeva-brief.md       ← What Sahadeva needs to know (stablecoins, CBDC, Hedera)
│
├── source/                     ← Raw context (transcripts, dumps, reference docs)
│   ├── metamask-master-prd-raw.md
│   ├── qa-context-feb20.md
│   ├── kyb-osn-reference.md
│   └── [future raw context goes here]
│
├── prds/                       ← Finished deliverables
│   ├── competitive-analysis-idos-vs-t3-v2.md
│   ├── metamask-t3-transak-e2e-prd.md
│   ├── metamask-t3-transak-architecture-pack.md
│   └── metamask-terminal3-value-proposition.md
│
├── agents/                     ← Agent definitions and profiles
│   └── AGENTS.md
│
└── handover/                   ← Handover docs between Local/Cloud Janet
    └── cloudjanethandover-terminal3-2026-02-20.md
```

## How It Works

### Layer 1: STATE-OF-PLAY.md (The Brain)
- **What:** A living document that Janet maintains with the CURRENT state of everything
- **Updated:** Every time Sunshine shares new context or decisions change
- **Contains:** Key facts, decisions made, open questions, what's true right now
- **Used by:** Janet reads this every session to get up to speed instantly
- **Size:** Kept lean -- distilled facts only, no raw transcripts

### Layer 2: Agent Briefs (The Briefing Packets)
- **What:** Pre-compiled context packets, one per sub-agent
- **Updated:** By Janet after each major context update
- **Contains:** Only what THAT agent needs for THEIR domain
- **Used by:** Injected into sub-agent prompts when they're deployed
- **Size:** ~2-4 pages each, focused and actionable

### Layer 3: Source Files (The Archive)
- **What:** Raw transcripts, dumps, reference docs, meeting notes
- **Updated:** Whenever Sunshine shares new context
- **Contains:** Everything, unprocessed
- **Used by:** Janet reads these to update Layer 1 and Layer 2. Sub-agents only read these if they need deep detail.
- **Size:** Unlimited -- this is the raw archive

## The Flow

1. **Sunshine shares new context** → saved to `source/`
2. **Janet processes it** → updates `STATE-OF-PLAY.md` with key facts
3. **Janet updates relevant agent briefs** → agents get fresh context next time they're deployed
4. **Sub-agent is deployed** → reads their brief + STATE-OF-PLAY + relevant source files if needed
5. **Sub-agent delivers** → output goes to `prds/` or relevant folder

## Why This Works
- **Janet (Opus) doesn't carry everything** -- reads STATE-OF-PLAY for instant context
- **Sub-agents get focused briefs** -- no wasted tokens on irrelevant context
- **Raw context is preserved** -- nothing lost, always available for deep dives
- **Scales infinitely** -- just add more source files and update the briefs
