#!/usr/bin/env python3
"""Push Regulatory Vault PRD (phased) to Notion."""

import json
import requests
import time

PAGE_ID = "310eab20-0eed-812a-8f76-f4a8d9ca75b3"
TOKEN = "REDACTED_NOTION_TOKEN"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}
URL = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"

def h1(text): return {"type":"heading_1","heading_1":{"rich_text":[{"type":"text","text":{"content":text}}]}}
def h2(text): return {"type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":text}}]}}
def h3(text): return {"type":"heading_3","heading_3":{"rich_text":[{"type":"text","text":{"content":text}}]}}
def p(text): return {"type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":text}}]}}
def pb(text, bold_prefix):
    return {"type":"paragraph","paragraph":{"rich_text":[
        {"type":"text","text":{"content":bold_prefix},"annotations":{"bold":True}},
        {"type":"text","text":{"content":text}}
    ]}}
def bullet(text): return {"type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"type":"text","text":{"content":text}}]}}
def bullet_bold(bold, rest):
    return {"type":"bulleted_list_item","bulleted_list_item":{"rich_text":[
        {"type":"text","text":{"content":bold},"annotations":{"bold":True}},
        {"type":"text","text":{"content":rest}}
    ]}}
def num(text): return {"type":"numbered_list_item","numbered_list_item":{"rich_text":[{"type":"text","text":{"content":text}}]}}
def divider(): return {"type":"divider","divider":{}}
def callout(text, emoji="📋", color="blue_background"):
    return {"type":"callout","callout":{"icon":{"type":"emoji","emoji":emoji},"color":color,"rich_text":[{"type":"text","text":{"content":text}}]}}
def toc(): return {"type":"table_of_contents","table_of_contents":{"color":"default"}}
def toggle(title, children):
    return {"type":"toggle","toggle":{"rich_text":[{"type":"text","text":{"content":title}}],"children":children}}
def quote(text):
    return {"type":"quote","quote":{"rich_text":[{"type":"text","text":{"content":text}}]}}

blocks = []

# ── HEADER ──
blocks += [
    callout("Document Status: 🟠 In Progress | Created: Jan 2026 | Phase 1 Target: MetaMask Launch\nContributors: Janani Gopalakrishnan, Edward Fu, Malcolm Ong\nEngineering: Truong Nguyen, Edward Fu, Phuc Hoang, Quang Tran, Matthew Torres\nDesign: Ruby Wu, Micho Gunawan"),
    toc(),
    divider(),
]

# ── PHASE 1 ──
blocks += [
    h1("Phase 1: Regulatory Vault for MetaMask Launch"),
    p("Phase 1 delivers the minimum viable Regulatory Vault required for the MetaMask/Transak integration. Scope is deliberately narrow: single provider (Transak), two jurisdictions (US + UK), no cross-border reuse, no multi-provider scenarios."),
    divider(),

    h2("1. Core Architecture"),
    h3("Dual-Vault Model"),
    p("Identity is split into two layers to satisfy both user privacy and global compliance:"),
    bullet_bold("SSI Vault: ", "Decentralized, user-controlled storage (IPFS + user private keys). Holds private user data, structured JSON fields, KYC credentials. User chooses when to share. Key feature: Selective Disclosure."),
    bullet_bold("Regulatory Vault: ", "Secure, centralized storage managed by T3 as processor for regulated partners. Holds raw passport images, liveness MP4 videos, Proof of Address PDFs. Exists for enforcement access. Key feature: Immutable Auditability."),
    
    h3("Why the Regulatory Vault Exists"),
    num("Enforcement Requests: Regulators cannot rely on user-owned encrypted SSI vaults. They need guaranteed access to raw evidence."),
    num("Liability & Attestation: T3 is the System of Record for identity verification. The vault holds source-of-truth artifacts justifying KYC Pass status."),
    num("Data Persistence: Financial laws require KYC data held 5-7 years even after relationship ends."),

    h3("Data Handshake Flow (MetaMask)"),
    num("Trigger: User clicks \"Buy\" in MetaMask."),
    num("Collection: T3 collects regulated user data (passport/video)."),
    num("Fork: Raw images/videos → Regulatory Vault (jurisdiction-aware). Extracted data + private user data → SSI Vault."),
    num("Use: User presents VC to Transak to clear the trade. Raw docs stay locked unless regulator asks."),
    divider(),

    h2("2. Phase 1 Scope"),
    callout("Phase 1 = Single provider (Transak via MetaMask), two jurisdictions (US + UK), single-entity storage, no cross-border reuse.", "🎯", "yellow_background"),
    
    h3("What We Build"),
    bullet("Regulatory Vault storage for raw KYC artifacts (passport image, liveness video)"),
    bullet("Email + phone collection (required by MetaMask for downstream providers like Baanx)"),
    bullet("Jurisdiction-aware storage routing: US vault (US users) + UK vault (UK users)"),
    bullet("Jurisdiction determination: Entity registration location → IP address → user-declared residency"),
    bullet("Derived verification record storage (status, timestamps, doc type, provider, VC pointer/hash)"),
    bullet("VC issuance into user SSI vault upon KYC completion"),
    bullet("Immutable audit logs: User ID, Admin ID, Timestamp, Purpose of Access"),
    bullet("RBAC: Transak sees only Transak users, no cross-provider leakage"),
    bullet("AML retention: 5-year minimum retention regardless of user deletion requests"),
    bullet("User deletion workflow: SSI vault data deleted, regulatory vault data retained with \"user-deletion-requested\" flag"),
    bullet("Transak Admin Portal for data retrieval (see section below)"),
    
    h3("Data Classification -- Phase 1"),
    bullet_bold("Stored per user: ", "Email, phone, passport image, liveness video, derived verification record, VC hash/pointer"),
    bullet_bold("Tagged as provider-required: ", "Email + phone (MetaMask/Baanx requirement)"),
    bullet_bold("Retention: ", "US: 5 years (BSA/AML). UK: 5 years (MLR 2017). Both override GDPR erasure rights."),
    bullet_bold("Unverified fields: ", "User-input SSN/address stored and tagged as user_declared=true, verification_level=low for low-tier KYC"),
    divider(),

    h2("3. Scenarios Covered in Phase 1"),
    
    h3("Scenario A: Transak US User Completes KYC"),
    num("User does KYC for Transak (passport + liveness)."),
    num("Vault writes raw artifacts into US Regulatory Vault (IP address check → residency country → must match entity registration)."),
    num("Derived verification record + verified email + user input JSON stored."),
    num("VC issued into user's SSI vault."),
    p("Result: US resident user data sits in US vault."),

    h3("Scenario B: Transak UK User Completes KYC"),
    num("UK user completes KYC for Transak."),
    num("Vault writes raw artifacts into UK Regulatory Vault."),
    num("Same derived verification record pattern, but storage region = UK."),
    num("VC issued into SSI vault."),
    p("Result: UK user data in UK vault. Two Transak partitions, artifacts stored per region."),

    h3("Scenario H: User Requests Data Deletion"),
    num("User requests deletion via SSI vault."),
    num("SSI vault: deletes user-controlled data (VC, pointers, wallet-held items)."),
    num("Regulatory vault: retains all copies under AML retention rules. Marks records as \"user-deletion-requested\"."),
    num("User receives compliant notice: \"We have deleted what we can. Certain data is retained for regulatory obligations.\""),
    p("Result: User rights honored without compromising AML compliance."),
    
    h3("Scenario I: Law Enforcement Request"),
    num("Request received from law enforcement."),
    num("T3 requires formal legal process (court order / MLAT) -- does not disclose on informal request."),
    num("If valid order received, data produced from the correct jurisdiction's vault only."),
    p("Result: Jurisdictional authority preserved, consistent enforcement posture."),

    h3("Scenario J: Low-Tier KYC with Unverified User Input"),
    num("User submits low-tier KYC (SSN + address, not verified)."),
    num("Raw inputs stored and tagged: user_declared=true, verification_level=low."),
    num("If user crosses transaction threshold → full KYC triggered, new verified artifacts collected."),
    num("Old low-tier data retained for audit trail."),
    p("Result: Clear lineage from low-tier to high-tier KYC."),
    divider(),

    h2("4. Transak Admin Portal (Data Retrieval)"),
    callout("Transak has an existing admin portal/dashboard. Phase 1 integrates regulatory vault retrieval into this portal so Transak compliance teams can self-serve.", "🖥️", "green_background"),
    
    h3("Portal Capabilities -- Phase 1"),
    bullet("Tiered access: \"Reviewer\" role sees raw docs (passport, liveness). \"Support\" role sees metadata only (Pass/Fail, timestamps)."),
    bullet("Search by user ID, transaction ID, or date range"),
    bullet("Secure streaming view of raw artifacts -- no local copy creation (data stays in vault region)"),
    bullet("Export capability for audit dataset: key fields (IP, email, phone), passport/ID image, liveness check result"),
    bullet("Case-based evidence pack export for law enforcement requests: artifacts + transaction/IP logs"),
    bullet("All access logged immutably: who accessed what, when, and why"),
    
    h3("Access Governance"),
    bullet_bold("Need-to-know basis: ", "Access scoped by user status (onboarding vs monitoring phases)"),
    bullet_bold("Cross-border viewing: ", "Portal allows remote viewing via secure stream without creating a local copy. Data stays in its jurisdiction."),
    bullet_bold("Audit trail: ", "Every view, export, and search logged with User ID, Admin ID, Timestamp, Purpose"),
    
    h3("Open Question for Transak"),
    quote("Confirm: Does Transak's existing admin portal support plugin/iframe integration, or do we need to build a standalone retrieval interface? If standalone, confirm API-only vs UI requirements."),
    divider(),

    h2("5. Consent & Legal Basis -- Phase 1"),
    bullet_bold("Collection basis: ", "Contractual necessity (KYC required for service) + legal obligation (AML compliance)"),
    bullet_bold("Storage basis: ", "Legal obligation (AML retention 5-7 years)"),
    bullet_bold("No cross-entity reuse in Phase 1: ", "No consent flow needed for sharing between providers"),
    bullet_bold("GDPR response: ", "\"Deleted what we can, retained what must be retained\" -- legally worded response template"),
    bullet_bold("VC metadata: ", "Classified as personal data under GDPR (any data linkable to identifiable person is in-scope)"),
    divider(),
]

# ── OPEN ITEMS AFTER PHASE 1 ──
blocks += [
    h2("6. Open Items After Phase 1"),
    
    h3("Resolved in Phase 1"),
    bullet_bold("Controller/Processor split: ", "T3 = Data Processor. Transak = Data Controller. T3 stores and processes on Transak's instructions. If data is in T3-owned infrastructure, T3 is processor; DPA required between T3 and Transak."),
    bullet_bold("Jurisdiction determination: ", "Entity registration location (primary) → IP address → user-declared residency. For Phase 1: Transak US entity = US vault, Transak UK entity = UK vault."),
    bullet_bold("\"MetaMask as Router\" role: ", "MetaMask holds no PII. If law enforcement contacts MetaMask, legal handoff protocol: MetaMask directs regulator to Transak (controller), who coordinates with T3 (processor) for vault access. MetaMask never touches the vault."),
    
    h3("Open After Phase 1 (Deferred to Phase 2)"),
    bullet_bold("Passport expiry vs retention: ", "If passport expires within 5-year AML window, old artifact remains valid for compliance but useless for re-verification. Need policy: are expired-doc artifacts \"frozen\" or do they trigger a refresh? How does Sumsub handle lost/invalid passports?"),
    bullet_bold("Consent withdrawal without deletion: ", "User says \"stop sharing with Provider B\" but doesn't want data deleted. Phase 1 has no reuse, but Phase 2 needs this flow."),
    bullet_bold("Breach notification protocol: ", "GDPR requires 72-hour notification. Who notifies -- T3 as processor or provider as controller? Need incident response playbook."),
    bullet_bold("VC revocation propagation: ", "If KYC found fraudulent after VC issued, how does revocation propagate to providers who already received claims?"),
    bullet_bold("EU jurisdiction: ", "Phase 1 covers US + UK only. EU (GDPR-specific) storage, SCCs for cross-border transfers, and EU-specific retention rules deferred."),
    bullet_bold("Cross-border reuse: ", "All multi-provider and cross-jurisdiction reuse scenarios deferred."),
    bullet_bold("Travel Rule / VASP integration: ", "Out of scope for Phase 1. Requires travel rule provider integration."),
    bullet_bold("Pricing model: ", "Subscription/annual platform fee vs pay-per-request. Luke's recommendation: bake into service fee, avoid pay-per-access friction."),
    bullet_bold("VC jurisdiction pinning: ", "Raw data is pinned (US/UK). Does the VC metadata also need regional pinning, or can it sit on global IPFS since it contains no raw PII? Likely global is fine, but needs legal sign-off."),
    divider(),
]

# ── PHASE 2 ──
blocks += [
    h1("Phase 2: Multi-Provider Regulatory Vault"),
    p("Phase 2 extends the vault to support multiple providers, cross-border reuse, EU jurisdiction, and full GDPR compliance workflows. Builds on Phase 1 infrastructure."),
    divider(),

    h2("7. Phase 2 Scope"),
    callout("Phase 2 = Multi-provider reuse, EU jurisdiction, cross-border controls, consent management, KYC refresh policies.", "🎯", "purple_background"),

    h3("What We Build"),
    bullet("EU Regulatory Vault (Frankfurt) with GDPR-native storage"),
    bullet("Cross-entity KYC reuse with explicit consent flow"),
    bullet("Provider Copy model: separate stored object per provider, each with independent retention clock, access rules, audit trail"),
    bullet("Consent management: capture, audit, and withdrawal workflows"),
    bullet("KYC refresh/VC freshness policies (risk-tiered: high-risk annual, medium ~5yr, low event-driven)"),
    bullet("Cross-border access controls (claims-only reuse when raw export prohibited)"),
    bullet("Breach notification playbook and incident response protocol"),
    bullet("VC revocation and propagation mechanism"),
    bullet("Passport expiry handling and re-verification triggers"),
    bullet("Pricing engine for cross-border reuse + vault maintenance fees"),
    
    h3("Scenarios Covered in Phase 2"),
    
    h3("Scenario B: Provider B Requests KYC Reuse (Same Jurisdiction)"),
    num("Provider B sends reuse request: user_id, jurisdiction, what it needs (claims vs raw)."),
    num("T3 checks: valid VC exists? Fresh enough?"),
    num("Case 1 (Claims only): User consents → T3 shares VC/derived claims. No raw artifact copy. Reuse event logged."),
    num("Case 2 (Raw artifacts): User consents → Provider Copy created with independent retention, access rules, audit trail."),
    p("Result: Controlled reuse, minimal duplication, full audit trail."),
    
    h3("Scenario C: Same Provider, Cross-Border Expansion"),
    num("User onboarded under Transak US, later uses Transak EU services."),
    num("T3 detects jurisdiction mismatch (IP/currency check)."),
    num("Option A: Claims-only reuse (no raw copy, pointer to original)."),
    num("Option B: Provider Copy duplicated into EU vault, tagged to Transak EU."),
    num("Option C: Re-collect KYC under EU flow if copy not permitted."),
    p("Result: Two entities, jurisdiction-correct storage, no data localization violations."),

    h3("Scenario D: Two Providers, Same Jurisdiction"),
    num("MetaMask user (Transak US) wants to use Provider B (also US)."),
    num("User consents. T3 shares VC + minimal AML fields (name, DOB, nationality)."),
    num("No raw artifact duplication needed."),
    p("Result: No extra storage cost, minimal exposure. Provider B runs AML independently."),

    h3("Scenario E: Provider Requires Raw Artifacts, Jurisdiction Matches"),
    num("Provider B (US) requests raw artifacts for US user."),
    num("Jurisdiction allows. User consents."),
    num("Provider Copy created in US vault with own retention clock + audit trail."),
    p("Result: Two independent objects, same region, each separately compliant."),

    h3("Scenario F: Cross-Border Reuse, Claims Only"),
    num("EU user did KYC for Transak EU. Provider B (US) wants reuse."),
    num("EU raw artifacts cannot be exported to US."),
    num("Claims-only reuse. User consents. VC + derived claims shared."),
    p("Result: Cross-border reuse without violating EU data export constraints."),

    h3("Scenario G: Cross-Border Reuse Prohibited → Re-collection"),
    num("EU user, Provider B (US) insists on raw artifacts."),
    num("T3 enforces: no raw export, no duplication."),
    num("Provider B triggers fresh KYC flow, stores in US vault."),
    p("Result: Clean legal separation. No silent policy violation."),
    divider(),

    h2("8. Phase 2 -- Consent & Legal Framework"),
    bullet_bold("Reuse basis: ", "Explicit consent (safest under GDPR). User sees consent screen: \"Allow Provider B to reuse your KYC result from Transak.\""),
    bullet_bold("Consent audit: ", "Record: consent granted/declined, timestamp, requesting provider, purpose at time of reuse."),
    bullet_bold("Consent withdrawal: ", "User can revoke sharing permission with specific provider. Does not trigger deletion -- just stops future reuse."),
    bullet_bold("Minimum data for AML: ", "Provider compliance teams cannot accept pass/fail only. Must provide name, DOB, nationality for sanctions/PEP screening. Raw artifacts fetched only on escalation/LE request."),
    bullet_bold("VC freshness: ", "Configurable refresh cadence. High risk: annual. Medium: ~5 years. Low: event-driven. May not require re-upload unless ID expired or address changed."),
    divider(),

    h2("9. Phase 2 -- Cross-Border & Jurisdiction Rules"),
    bullet_bold("Jurisdiction determination: ", "License/entity determines rules. User residency determines which entity is used (if provider has multiple licensed entities)."),
    bullet_bold("Residency verification strength: ", "IP capture + VPN detection (weakest) → passport (weak -- multi-passport users) → Proof of Address (gold standard). When POA mandatory vs optional determined by provider policy/thresholds."),
    bullet_bold("Shared vault architecture: ", "\"Shared global system + partitioned access + carve-outs per jurisdiction/client\" is industry standard (per Luke). Physical separation = jurisdiction/client-specific requirement, not universal."),
    bullet_bold("Cross-border admin access: ", "Portal allows remote viewing via secure stream. No local copy unless periodic dumps required by specific regulator."),
    bullet_bold("Replication: ", "Replication requirements are regulator-driven. Acceptable to store encrypted data locally as long as decryptable and producible when seized/requested."),
    divider(),

    h2("10. Pricing Considerations"),
    bullet("Subscription / annual platform fee preferred over pay-per-request (reduces friction, per Luke's advice)"),
    bullet("Cross-border reuse: service fee for vault maintenance + data transfer"),
    bullet("Regulatory vault maintenance fee baked into base pricing"),
    bullet("Per-client, per-jurisdiction pricing model"),
    divider(),

    h2("11. Team"),
    bullet_bold("Product: ", "Janani Gopalakrishnan, Malcolm Ong"),
    bullet_bold("BE Engineering: ", "Truong Nguyen, Edward Fu, Phuc Hoang"),
    bullet_bold("FE Engineering: ", "Quang Tran, Matthew Torres"),
    bullet_bold("Design: ", "Ruby Wu, Micho Gunawan"),
    bullet_bold("Compliance Advisor: ", "Luke"),
]

# Push in batches of 95 (Notion limit is 100)
BATCH = 95
for i in range(0, len(blocks), BATCH):
    batch = blocks[i:i+BATCH]
    resp = requests.patch(URL, headers=HEADERS, json={"children": batch})
    data = resp.json()
    if data.get("object") == "error":
        print(f"ERROR at batch {i//BATCH}: {data.get('message')}")
        break
    else:
        print(f"Batch {i//BATCH}: pushed {len(batch)} blocks OK")
    if i + BATCH < len(blocks):
        time.sleep(0.5)

print(f"\nDone! Total blocks: {len(blocks)}")
print(f"URL: https://notion.so/{PAGE_ID.replace('-','')}")
