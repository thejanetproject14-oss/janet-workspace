Here are crisp answers you can use. I’m keeping them in the exact “stakeholder Q\&A” style.

---

## **1\) What specifically is idOS doing with MetaMask right now?**

**Answer:** We have **no confirmed integration** between idOS and MetaMask at the moment. From our side, this is currently **competitive check / perceived threat** based on market noise, not a known active MetaMask initiative. We have not seen MetaMask position idOS as a current partner in our working threads.

(If someone challenges this, you can say: “Nothing we’ve been told directly by MetaMask. If they’re exploring, it hasn’t surfaced in our discussions.”)

---

## **2\) What has terminal 3 already shipped or demonstrated to MetaMask?**

**Answer:** We have **not shipped an integration** yet. We are **in architecture discussions** and alignment. We **still owe** the PRD with diagrams, the data-flow diagrams for security review, and the orchestration decision logic.

---

## **3\) What’s MetaMask’s current identity/KYC setup?**

**Answer:** MetaMask **does not do KYC**. Each on-ramp/provider runs **their own KYC** today. MetaMask mainly **routes users into provider flows** (often via widget/URL) and does not maintain centralized KYC state.

---

## **4\) What pain has MetaMask expressed, in their words?**

From the Feb 6 call, their pain is very explicit and practical:

* They need clarity on **“the scope of the KYC token”** and **what we share with providers**, ideally in an industry standard way (OID4VP).  
* They need a concrete answer to **“in our ideal world, what are we sharing with the providers”** and how that maps to KYC levels.  
* They have a major constraint: **they don’t have a backend**, so they need an approach for auth and communication with T3 that works with that reality.  
* They asked for **a system diagram with each API call**, showing **what gets routed where**, as the basis for engineering and security review.  
* Legal and security concerns are blocking: they want an **80/20 pack** before pulling in security because otherwise it becomes piecemeal Q\&A.  
* They want to reduce risk vendor sprawl: security team prefers to audit **one SDK** vs “two or three”.  
* Risk/fraud wishlist: device and behavior signals such as **device ID**, and potentially VPN checks.  
* Operational pain: **edge cases**, step-ups, failures, retries, manual review, and “off-happy-path” flows need a plan.  
* They’re exploring shifting orchestration to **Meld** long-term, but are concerned about **single point of failure** and want fallback strategies.

That’s the real pain: clarity, security-readiness, and operating without a backend.

---

## **5\) What’s terminal 3 tech stack status?**

**Answer (based on what you said):**

* **TEE storage:** live  
* **SD-JWT:** live  
* **KYC:** live  
* **KYA:** not built yet (roadmap)

---

## **6\) Any idOS weaknesses observed?**

**Answer:** No direct evidence. We have not used it hands-on in this thread, so we cannot credibly claim weaknesses. Treat it as **unknown**.

---

# **For the E2E PRD questions**

## **7\) Where is the Transak relationship?**

**Answer:** Not cold. MetaMask has already introduced us to Transak and we are in early integration planning. We need to send a **technical proposal \+ PRD** and then align engineering \+ compliance on the tripartite structure (your internal notes reflect this).

---

## **8\) MetaMask technical constraints and integration patterns?**

**Answer:** Key constraints and patterns (from the call):

* **No backend** today, so webhooks are non-trivial for them.  
* Current provider integrations are typically **widget/URL-based** with a public key, and they use **polling** for order status today.  
* They want a design that can support: token-based auth to T3, order status propagation, and eventually orchestration shifts to Meld.

For Transak specifically, their docs show multiple integration options including SDKs, web, mobile, plus webhooks/websockets and order tracking guidance. ([Transak](https://docs.transak.com/docs/transak-on-ramp?utm_source=chatgpt.com))

---

## **9\) What triggered urgency today?**

**Answer:** MetaMask is trying to start the **security review** and cannot until we provide the **80/20 architecture \+ data-flow pack**. They also have active risk and provider discussions (Transak risk, SDKs), so missing docs slows their internal alignment.

---

## **10\) Who are the stakeholders for these docs?**

**Answer:** Two audiences:

1. **MetaMask:** Product (Lorenzo), plus **Legal** and **Security**, and their EM/engineering team (because they asked for per-API call system diagrams).  
2. **Transak:** Product/engineering counterparts, plus **compliance/legal** for reliance and data-sharing alignment.

---

## **11\) Phase 1 realistic or aspirational?**

**Answer:** If PRD says 8 weeks, treat it as **aspirational unless you lock scope tightly**.

A realistic Phase 1 is:

* One provider (Transak)  
* One platform surface (mobile white-label or a single embedded flow)  
* Minimal KYC tiering (Level 0/1 \+ one step-up)  
* Polling acceptable for MVP if webhooks are hard, with webhooks planned next  
* Security pack delivered early to avoid late surprises

---

## **12\) Transak thresholds: real numbers or guessing $150?**

You mentioned a Transak Notion doc, but I couldn’t fetch that specific Notion page in this environment (it returned a fetch error). What I can confirm from Transak’s public docs is that they maintain **fees/limits** references and partner guidance around payment methods and limits, but thresholds can vary by region and payment method. ([support.transak.com](https://support.transak.com/en/articles/7846060-payment-methods-fees-and-limits?utm_source=chatgpt.com))

So your safe answer is:  
**“$150 is a working assumption we’ve heard in discussion, but we need Transak to confirm the exact threshold logic by region, payment rail, and currency.”**

---

# **Quick, clean way to say this on a call**

If you need a 20-second summary answer set:

* “MetaMask does not do KYC today, providers do. Their pain is: what data we share, how we do it with no backend, and getting security review started. We owe the PRD \+ per-call system diagram \+ data-flow pack \+ orchestration decision logic. Our tech is live for KYC, SD-JWT, and TEE storage. KYA is roadmap. Transak thresholds are region and rail dependent, we’ll validate with Transak.”

---

If you paste the PRD sections you already have (even rough), I can convert it into:

* a one-page “per API call” system diagram outline  
* a decision-tree table  
* a security data-flow checklist

That’s exactly what MetaMask asked for.

