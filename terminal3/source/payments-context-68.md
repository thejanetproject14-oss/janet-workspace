# **Terminal 3 x Visa TAP**

## **Thesis**

Visa built the armored truck. TAP, built on RFC 9421, proves the agent is legitimate and that the request has not been tampered with.

But the merchant does not know who is inside the truck.

Terminal 3 provides the cargo: verified buyer identity, scoped mandates, user-consented preferences, and a complete governance trail. When integrated as a credential layer inside the TAP handshake, Terminal 3 transforms what is currently a binary trust check into a structured commerce negotiation.

This is **Intelligent Agentic Commerce (IAC)**.

The broader frame is strategic. Visa’s agent strategy today sits primarily as a cost center, focused on risk defense. With the right credential layer, it can evolve into a revenue generator focused on dynamic sales.

That shift preserves Visa’s role as the operating system for the next generation of digital commerce.

---

## **1\. The Gap in Visa’s Stack**

### **What TAP Does**

TAP proves agent legitimacy using RFC 9421 cryptographic signatures.

It delivers three core signals:

* Agent intent, browsing or buying  
* Consumer recognition, a returning customer signal  
* Payment information, a tokenized card

The outcome is binary. Allow or block.

### **What TAP Does Not Do**

TAP does not:

* Identify who the agent represents  
* Express what the agent is authorized to buy, under what rules, or within what constraints  
* Deliver non-payment attributes such as passport status, medical eligibility, or corporate purchasing policy  
* Provide verified buyer attributes required for meaningful personalization  
* Create a durable evidentiary trail to resolve agent-initiated disputes

These omissions are intentional. Visa has made a deliberate architectural decision not to carry identity data, PII, or qualitative authorization on its rails.

That architectural decision is Terminal 3’s permanent positioning.

---

## **2\. From “Don’t Shoot” to “Know Me, Serve Me”**

This unlocks and shifts the value proposition from centering on safety, to the opportunity for add-on sales.

### **Current State Without Terminal 3**

Signal: “I am a valid bot.”

Merchant reaction: Allow connection.

A necessary control. But limited.

### **Future State With Terminal 3**

Signal: “I am a verified corporate officer with a $50,000 budget.”

Merchant reaction: Unlock the B2B catalog and apply a 15% discount.

The interaction shifts from admission control to intelligent negotiation.

### **Three Revenue Plays**

**1\. Dynamic Pricing – The Loyalty Play**

* Scenario: An agent lands on an airline site.  
* Terminal 3 signal: A Visa-attested credential proving “High Net Worth” or “Frequent Flyer.”  
* Result: The merchant waives booking fees or surfaces business class upgrades automatically. The experience adjusts in real time based on verified attributes.

**2\. Gated Inventory – The Compliance Play**

* Scenario: An agent attempts to purchase regulated goods such as pharma or chemicals.  
* Terminal 3 signal: A “Medical Proxy” credential.  
* Result: The restricted catalog unlocks instantly. Manual KYC steps are bypassed because the authorization is already verified.

**3\. Frictionless Checkout – The Conversion Play**

* Scenario: A first-time visit to a luxury retailer.  
* Terminal 3 signal: Verified shipping address plus an “Age \> 21” credential.  
* Result: The merchant skips account creation and age gating and moves directly to payment.

The shift is subtle but material. The agent does not just ask to connect. It arrives pre-qualified.

---

## **3\. Unifying VIC, TAP, and Terminal 3 for Security-Enabled Personalization**

Visa’s VIC data tokens already provide broad cohort-level signals such as “Sports Enthusiast” or “Frequent Traveler.” These are intentionally inferred and generalized. They remain blurry by design to avoid data broker liability.

Terminal 3 introduces a sharper layer: user-consented zero-party data expressed as verifiable credentials. Not inferred preferences, but stated attributes. Cryptographically signed. Selectively disclosed.

Not “likes Nike”

But “Size 10, budget over $200.00, prefers limited editions.”

The merchant benefit is practical. Instead of presenting a generic homepage, the merchant dynamically serves relevant inventory to an agent that arrives with enough verified detail to bypass discovery entirely.

Conversion improves because the agent finds what it needs immediately.

### **The Blurry Problem**

VIC relies on inference. Visa cannot store granular preference data without increasing GDPR exposure.

### **The Sharp Solution**

Terminal 3 allows Visa to mint insight credentials.

Example: “Verified Big Spender.”

* Visa issues the badge based on internal insights.  
* The agent holds the badge, removing Visa’s custody of the attribute.  
* The agent presents the badge to the merchant via TAP.

The outcome is important. Visa monetizes its data insights as insight badges without becoming a data broker.

The asset stays on balance sheet. The liability does not.

---

## **4\. Visa-Attested Credentials as a New Revenue Stream**

Visa sits on one of the world’s strongest transaction datasets. Today, that data remains centralized and largely defensive in use.

Terminal 3 enables Visa to mint attested attributes derived from that data. Not raw transaction histories, but verified claims.

Examples:

* Verified Premium Traveler  
* Verified High-Value B2B Buyer

These credentials are issued to the user’s agent, held in the user’s identity wallet, and presented to merchants at the user’s discretion through the TAP handshake.

| Why Visa Wants This | Why It Requires T3 \* |
| :---- | :---- |
| Monetize data without selling it. Merchants pay to verify credentials. | Needs a decentralized identity container using DID and VC standards, and selective disclosure capabilities |
| Reduce GDPR and CCPA liability. The user holds and controls the credential. | Needs TEE-based issuance and privacy-preserving verification infrastructure. |
| Expand Value-Added Services. “Verified Buyer” badges become a premium product line. | Needs the trust architecture (threshold encryption, ZK proofs, audit trail) to make credentials tamper-proof. |

\* A centralized database model cannot provide these properties.

For FY2025, approximately 50% of Visa’s revenue came from value-added services. Cross-border and other revenue streams are trending down. Directionally, this aligns with where growth must come from.

---

## **5\. One-Way Authentication Becomes Bi-Directional Mandate Negotiation**

Today, authentication is one-directional. The agent proves legitimacy (TAP/4291).

Terminal 3 introduces a pre-transaction compatibility layer.

Merchants publish structured requirements, for example: “Verified Corporate ID required for B2B catalog access.”

The agent evaluates its mandate against those requirements before initiating the TAP request. Only compatible transactions proceed to handshake.

Mismatches are caught before a cart is created, a compute is consumed, or a dispute is triggered.

The value is that we replace failed checkouts with intelligent filtering. Less friction. Less waste. Lower dispute exposure.

---

## **6\. The Chargeback Shield**

Agent-initiated commerce introduces a new dispute category. The transaction may be technically authorized through a valid token. The user may still claim the agent exceeded intent.

With Terminal 3’s mandate and audit layer embedded in the TAP handshake, each transaction carries:

* The user’s signed mandate  
* The agent’s decision logic  
* Evaluated policy constraints  
* The transaction outcome

All logged immutably.

Example:

In a dispute, Visa queries the T3 audit trail. “The mandate authorized economy flights under $800.00 on Star Alliance. The agent selected this flight because it was the only option meeting all constraints. Chargeback denied.”

Dispute resolution shifts from ambiguity to evidence.

---

## **7\. How This Scales**

This is a distribution question as much as a technical one.

Visa integrates Terminal 3 credential verification into Visa Acceptance Cloud. Merchants enable “Verified Agent Commerce.” Visa calls the Terminal 3 API in the background.

The same integration model applies to Stripe, Adyen, Shopify, Cloudflare, and Akamai. All already process TAP verification at the edge. Terminal 3 provides an SDK for embedded credential verification. Merchant effort remains close to zero.

Merchants do not build new systems. They consume a standardized signal defined jointly by Visa and Terminal 3\.

**Technical Execution: The Smart Header**

We do not ask Visa to redesign merchant APIs. We ride on top of the existing standard.

1. **Header**

    The agent includes a custom header (X-Agent-Auth) containing the Terminal 3 verifiable credential.

2. **Signature**

    The agent signs the header using RFC 9421\. The signature binds header, body, and credential together.

3. **Verification**

   The merchant verifies the RFC 9421 signature, Visa’s responsibility, and then reads the Terminal 3 credential.

The HTTP body remains untouched. The merchant API schema remains untouched.

The merchant verifies that the agent is authorized to spend $500.00 without accessing raw bank balances or PII. Low friction integration. High structural leverage.

---

## **Recommended Next Steps**

1. Convene a technical working session with Visa’s TAP and VIC engineering teams to walk through the sidecar header architecture and credential flow.

2. Develop a joint pilot with two to three merchants in high-value verticals such as travel, luxury, or regulated goods. Measure conversion lift, dispute reduction, and checkout friction.

3. Explore Visa-attested credentials as a co-developed product aligned with Visa’s Value-Added Services roadmap.

