## Meeting Agenda: MasterCard \<\> T3 

Objective: To position MasterCard as the first-mover orchestrator of the AI Agent economy through Terminal 3’s decentralized identity and credentialing infrastructure.

### **1\. The Strategic "Why": Why MasterCard, Why Now?**

* State of the Industry: The Inevitability of A2X (Agent-to-Everything)  
  * The shift from human-initiated commerce to autonomous agent transactions is already underway.  
  * Existing protocols (like Google’s UCP) are emerging but fragmented; the industry is searching for a unifying trust layer.  
  * The Industry is Moving with or without us: Agentic commerce (AI bots buying things) isn't a "maybe" anymore, it’s the inevitable next step in ecommerce. Right now, the standards are still emerging. Everyone is trying to get pie from the huge opportunity.   
  * If payment rails treat an AI agent as just another "tokenized transaction." , this is a fatal mistake. A token historically helps confirm that the the *money* is there for the payment to go through; it does NOT confirm the *intent* was valid \- which is what we need when agentic commerce emerges  
* The Shift:   
  * Agents are gaining Digital Personhood. Because they make autonomous decisions (negotiating prices, choosing vendors), they require an identity framework similar to humans. If you only verify the *token* and not the *agent’s identity*, you are essentially giving a blank check to a black box..  
  * The Risk : Without a verified identity tied to the agent’s specific decision-path, MasterCard faces a dispute explosion. Current chargeback rules ($50 limits, Regulation E/Z) were built for "lost cards," not "misbehaving software."  
  * If a merchant fulfills an order placed by an AI agent that "exceeded its authority," the resulting legal battle between the merchant, the bank, and the AI developer will be catastrophic with more high value transactions.   
  * There’s a great piece by Mastercard themselves (from early 2026\) titled ["Trusting AI to Buy: Agentic Commerce that's Secure, Transparent.](https://www.mastercard.com/global/en/news-and-trends/stories/2026/agentic-commerce-standards.html)" It basically admits that the "Standard Card-Not-Present" (CNP) rules we’ve used for 20 years aren't going to cut it anymore.  
* The Risk of Inaction  
  * An article from SAP stated that by 2030, the U.S. retail market alone is projected to see up to $1 trillion in "orchestrated revenue" (purchases handled by agents). Globally, that number jumps to between $3 trillion and $5 trillion.  
  * So much about agentic commerce is about appetite for capturing opportunity today.   
  * Right now, merchants are terrified to let agents check-out because they can't verify the agent's mandate. If MasterCard doesn't set the standard and lead the comprehensive solution including the trust handshakes, other tech giants like OpenAI (via their Agentic Commerce Protocol) or Stripe or Visa will.  
* The Cost: If another tech giant sets the standard, they control the data, the identity, and the fees. MasterCard gets relegated to being a processing pipe that just processes the smaller percentage of the value chain.  
* The Leader’s Reward: Capturing Market Share  
  * By defining the Industry Standard (not just a MasterCard-siloed standard), MasterCard creates a moat where merchants *want* to use the MasterCard stack to interact with agents.  
  * Opportunity to gain massive reputation and revenue by becoming the "plumbing" for the next decade of commerce.

### **2\. The Core Proposal: Terminal 3’s Agentic Trust Layer**

* T3 Technical Foundation: Trinity & TEE (Trusted Execution Environments)  
  * A Trusted Execution Environment (TEE) is a "Black Box" built directly into the computer chip (CPU).  
  * Aspects not required for agent to know, stay within the TEE.   
  * The agent never actually "sees" your credit card or passport. T3’s Trinity architecture holds those secrets inside the TEE. The TEE communicates directly with MasterCard’s rails to authorize the payment without the AI agent ever touching the raw data.  
  * TEEs provide the "Immutable Audit Trail." If a transaction is disputed, the TEE provides a signed log of exactly what the agent was thinking.  
  * Additionally, TEEs allow for "Micro-Delegations." A user can give an agent $50 for "Groceries only" and the TEE   will physically block the agent from spending it on "Electronics."

The Terminal 3 Network (T3N) is a decentralized Agentic Trust Layer designed to address critical challenges in AI agent identity, permission and delegation, data privacy, and auditability. T3N architecture comprises three main networks: **Secure Computation (TEEs) Network**, **Storage Network**, and **Blockchain Network.**

* **TEE** \- **“**Confidential Computation” \- All computations are performed inside the secure computational enclaves within processors that deliver enhanced security beyond conventional operating systems. TEEs maintain data **confidentiality** and **integrity**. This ensures that even if the broader system is compromised, the most critical information remains safe.  
  * Aspects not required for agents to know, stay within the TEE.  
  * The agent never actually "sees" your credit card or passport.  Those secrets only are securely loaded to TEE during computation. The TEE communicates directly with MasterCard’s rails to authorize the payment without the AI agent ever touching the raw data.  
  * TEEs allow any programmable business logic such as "Micro-Delegations." A user can give an agent $50 for "Groceries only" and the TEE will block the agent from spending it on "Electronics."  
* **Blockchain** \- “Global Access Governance and Immutable Audit Trail”  
  * If a transaction is disputed, all related events—such as user intent, authorization, and agent actions—are immutably recorded on the blockchain.  
* **Storage \- The T3N Storage Network securely stores credentials and private data encrypted with quantum-proof encryption in a decentralized storage network by default.**

## **The Solution** 

At time of Agentic ID registration

1. ***The Agent ID registration***  
   The Cryptographic Handshake: When a user first grants an agent payment access, T3N issues a Customer Agent ID. This is not a static login, but a verifiable, reusable credential that represents the agent's type and risk tier.

At time of Payment, 

### ***b. The Authentication Check (Identity & Intent)*** 

### *Occurs at Initiation: "Who is this, and do they have the right to be here?"*

* Identity Binding: Before the payment is even considered, the T3N verifies the Customer Agent ID. This is a cryptographic link that proves this specific agent belongs to a specific, KYC-verified MasterCard customer.  
* The "Anti-Hallucination" Gate: At this stage, the T3N checks the Agent's Mandate. It ensures the agent isn't just "hallucinating" a purchase, but is acting on a valid, human-signed instruction.

### ***c. The Authorization Check (Limits & Scope)*** 

### *Occurs at Transaction: "Does this specific action fit the pre-approved rules?"*

* Dynamic Limit Verification: While traditional cards have a flat credit limit, T3N allows for Contextual Limits. Inside the T3N, the system checks: *"Does this agent have the authority to spend $200 at a Pharmacy?"* vs. *"Does it have authority for $200 at a Casino?"*.  
* Zero-Exposure Authorization: The T3N holds the user’s sensitive "spending rules" in an encrypted storage network. It checks the transaction against these rules without ever revealing the user's private data or full balance to the AI agent or the merchant.  
* Cryptographic "Green Light": Once the limits are cleared, the T3N issues a high-integrity authorization signal to MasterCard. Because this happened in a TEE, MasterCard can be 100% certain that the limits were checked in an environment that even a rogue AI cannot bypass.

### **3\. Why T3?**

* Set the Global Standard Together: Partnering with Terminal 3 empowers MasterCard to define the industry standard for agent trust, rather than inheriting a framework shaped by competitors, Big Tech, or fragmented regional schemes.  
*  Move in Months, Not Years: Building a specialized, secure identity layer from scratch is a multi-year undertaking; T3 allows MasterCard to launch quickly, establish immediate authority, and shape the market while others are still in the development phase.  
*  A Regulatory Shield by Design: T3’s T3N architecture delivers cryptographic trust signals to your rails without exposing sensitive agent or user data, preserving MasterCard's full authorization power while eliminating the liability of a centralized data "honeypot".  
* Architected for Machine Intent: Legacy systems are built for human intent; T3’s two-part,  \-secured model (Identity \+ Limits) provides the mathematical proof of authorization needed to virtually eliminate agent-driven disputes and fraud.  
* Architected for autonomous interaction: Traditional systems assume human-in-the-loop control and manual consent. In contrast, T3N’s decentralized design (e.g., leveraging distributed ledgers, DID, and verifiable credentials) establishes verifiable trust that reduces disputes and fraud while enabling autonomous agent interactions.  
* Users own their own  PII : By design, the burden of managing and securing users’ and Agents’ PII stays entirely with the decentralized network. Because we use TEEs to process identity, MasterCard never has to ingest, store, or protect the sensitive raw data of the human behind the bot. We provide you with the Attestation (the proof) but T3N keeps the Liability (the data), ensuring your regulatory profile remains clean as you scale.

### **4\. Strategic Value for the MasterCard Ecosystem**

*Goal: Show how this benefits their primary customers \- the issuing banks and merchants.*

* Empowering the Issuing Banks  
  * *Team Insight:* While big banks are tech-heavy, smaller banks and Neo-banks struggle with compliance and audits for AI.  
  * MasterCard can offer T3-powered identity as a Value-Add Service to these banks, strengthening the MasterCard "Scheme" and increasing the number of active user profiles.  
* Incentivizing the Merchants  
  * Merchants cannot verify agent credentials on their own without high friction.  
  * By using the MasterCard stack powered by T3, merchants get a "Turnkey" solution to safely accept agent payments, instantly boosting their own "Agent-Readiness."

### **5\. Path Forward**

* Defining the Pilot: High-utility credentialing trial.  
* Metrics for Success: Transitioning from "growth and genetic statistics" to transaction volume and bank adoption rates.  
* Next Steps: Mapping the technical integration of T3 into the current payment flow 

## On the day : Topic & Responsibility

- Payments \- Janani   
- TEE(T3N) / Trinity \- Jack   
- Pitch / converting overall Business Opportunity / Value \- Malcolm   
- Standards in the market \- Elton  
- Questions on the company deck / Next steps \- Lauren

