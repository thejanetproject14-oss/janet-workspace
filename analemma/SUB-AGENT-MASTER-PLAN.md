# Sub-Agent Master Plan -- Janet's Team 🏗️

## The Org

**Janet (Chief of Staff / PM)** -- orchestrates everything, direct line to Sunshine, delegates to specialists, maintains context across all workstreams.

---

### Division 1: Operations & Daily Life
| Agent | Role | Trigger / Cadence | Model |
|---|---|---|---|
| **Ops** | Scheduling, Sita management, daily logistics, calendar, grocery ordering | Daily tasks, ad-hoc requests | Sonnet |
| **Health** | Meal plans, supplement tracking, fitness plans, recipe generation | Weekly meal plans, ad-hoc health questions | Sonnet |

### Division 2: Analemma
| Agent | Role | Trigger / Cadence | Model |
|---|---|---|---|
| **Writer** | Product copy, About page, FAQs, emails, launch comms | On-demand from Janet | Sonnet |
| **Content** | IG/TikTok content calendar, caption drafts, hashtag strategy, posting schedule | Weekly calendar generation, daily caption drafts | Sonnet |
| **Shopify** | Website build, product pages, checkout testing, bug fixes, SEO on-site | Active during build phase, then maintenance | Sonnet |
| **SEO** | Search optimization, keyword research, organic growth strategy | Weekly analysis, monthly reports | Sonnet |
| **Sales** | D2C strategy, retail expansion, customer-facing growth, pricing, promotions | Monthly strategy, ad-hoc analysis | Sonnet |
| **PR** | Magazine outreach, partnership pitches, press releases, brand reputation | Bi-weekly pitches, event-driven | Sonnet |
| **Analemma Research** | Market intel, competitor analysis, influencer scouting, trend tracking | Weekly research briefs, ad-hoc deep dives | Sonnet |

### Division 3: terminal 3
| Agent | Role | Trigger / Cadence | Model |
|---|---|---|---|
| **T3 Research** | Protocol landscape, standards tracking, competitive intelligence | On-demand, pre-meeting briefs | Sonnet |
| **T3 Writer** | PRDs, proposals, decks for Visa/Mastercard/Transak | On-demand from Janet or Sunshine | Opus (complex docs) |

### Division 4: Creative
| Agent | Role | Trigger / Cadence | Model |
|---|---|---|---|
| **Music** | Suno.ai prompts, backing track generation for 1-min covers | On-demand when Sunshine records | Sonnet |

---

## Phase 1: Launch This Week (Feb 18-19) 🚀

These 4 agents are critical for the Mar 8 lip ganache launch:

### 1. Writer Agent
**Why now:** Website copy, product descriptions, About page, launch emails all needed before Mar 8.
**First tasks:**
- Write 5 lip ganache product descriptions (dessert-themed, sensory, luxurious)
- Draft Analemma About page copy
- Draft FAQ page
- Write Shipping & Returns policy
**Context needed:** Brand voice guide, product details (ingredients, pricing, sizing), Sunshine's vision for how the brand should sound.
**Communication with Janet:** Janet sends task briefs, Writer returns drafts. Janet reviews and either approves or sends back with notes.

### 2. Shopify Agent
**Why now:** Website must be live before Mar 8. This is THE bottleneck.
**First tasks:**
- Theme selection and configuration
- Site structure (navigation, collections, homepage)
- Product page setup (once photos are ready from Tuesday shoot)
- Checkout flow, payments, shipping configuration
- Domain connection
**Context needed:** Shopify admin access (from Sunshine), brand assets (logo, colors, fonts), product photos, pricing, shipping details.
**Communication with Janet:** Janet coordinates between Shopify agent and Writer (copy goes into pages). Sunshine reviews via browser relay.

### 3. Health Agent
**Why now:** Meal plans, grocery lists, and recipe generation should be automated weekly.
**First tasks:**
- Generate Week 2 meal plan (anti-inflammatory, vegetarian, no eggs/mushrooms)
- Create grocery list split by FairPrice vs Saastha
- Build supplement tracking template
- Generate seed cycling recipe ideas (how to incorporate seeds into meals)
**Context needed:** Health profile from USER.md, dietary restrictions, grocery budget ($100/week), current supplements.
**Communication with Janet:** Health agent generates plans on schedule (Sunday for the week ahead). Janet reviews and sends to Sunshine.

### 4. Ops Agent
**Why now:** Daily logistics, Sita management, and calendar ops need a dedicated handler.
**First tasks:**
- Morning task list generation
- Sita daily cleaning task lists (in Nepali)
- Calendar event creation (once Janet email is set up)
- Grocery ordering assistance
**Context needed:** Sunshine's schedule, Sita's schedule, cleaning standards (reference photos), calendar access.
**Communication with Janet:** Ops runs on schedule (morning tasks). Janet escalates only when Sunshine's input is needed.

---

## Phase 2: Layer In (Week of Feb 23+)
- **Content** -- once photoshoot photos are ready and website structure is set
- **SEO** -- once website has content to optimize
- **Analemma Research** -- once we need influencer deep dives beyond the initial list

## Phase 3: Scale (March+)
- **Sales** -- post-launch, once we have data on what's moving
- **PR** -- post-launch, once we have professional photos and a live site to pitch
- **T3 Research + T3 Writer** -- as terminal 3 work demands (first task: Agent Pay PRD Thursday)
- **Music** -- when Sunshine is ready to record covers

---

## Communication Protocol 📡

### How Janet talks to sub-agents:
1. **Task assignment:** Janet sends a structured brief with clear deliverables, context, and deadline
2. **Review cycle:** Sub-agent returns work -> Janet reviews -> approve / revise / reject
3. **Escalation:** Only surface to Sunshine when decision is needed or work is ready for final approval
4. **Context sharing:** Janet maintains a shared context doc per agent so they don't lose thread between sessions

### How sub-agents talk to each other:
They don't. All communication flows through Janet. This prevents:
- Context leaks between workstreams
- Conflicting instructions
- Token waste from agents chatting with each other

### How Sunshine interacts:
- **Direct to Janet** (Telegram) -- strategy, decisions, approvals, brain dumps
- **Never directly to sub-agents** -- Janet translates and delegates
- **Exception:** Shopify agent during browser relay sessions (Sunshine + Janet + Shopify working together on screen)

---

## Agent Setup Checklist (Wednesday) ✅

For each Phase 1 agent, we need to:
- [ ] Define the agent's system prompt / personality
- [ ] Set the model (Sonnet default, Opus for T3 Writer)
- [ ] Create the agent's workspace context file (what it needs to know)
- [ ] Test with a sample task
- [ ] Set up any scheduled triggers (Health: weekly, Ops: daily)

### What Sunshine needs to provide Wednesday:
- [ ] Shopify admin access (invite or credentials)
- [ ] Brand assets (logo, brand colors, fonts)
- [ ] Product pricing for all lip ganache flavors
- [ ] Shipping details (SG only? International? Rates?)
- [ ] Analemma brand voice notes (how should the brand sound?)
- [ ] Sita's schedule and cleaning reference photos
- [ ] Notion + Linear access
- [ ] OpenAI API key

---

## Cost Model 💰

| Component | Model | Est. cost/day |
|---|---|---|
| Janet (main) | Opus | ~$5-8 (heavy days), ~$2-3 (light) |
| Morning check-in | Sonnet (isolated) | ~$0.10 |
| Sunday review | Sonnet (isolated) | ~$0.15 |
| Sub-agent task (per run) | Sonnet | ~$0.10-0.50 |
| Weekly sub-agent ops (4 agents, ~3 tasks each) | Sonnet | ~$2-4/week |

**Estimated weekly cost:** $20-40 depending on intensity
**Current budget context:** $50 OpenRouter top-up, need to monitor burn rate

### Cost Controls:
- **HARD BUDGET: $300/month MAX (~$10/day)**
- First 2 days cost $180 -- setup cost, not recurring. Must come down dramatically.
- Sub-agents on Sonnet (5x cheaper than Opus)
- Morning check-ins + routine reminders → Haiku (pennies)
- Janet on Sonnet for routine days, Opus only for strategy/PRD/complex work
- Batch similar tasks to reduce session overhead
- Monitor daily spend -- alert Sunshine if trending over budget
- Track weekly via Sunday review

---

## Success Metrics 📊

**Week 1 (Feb 18-22):**
- [ ] 4 Phase 1 agents operational
- [ ] Lip ganache product descriptions written
- [ ] Shopify site structure built
- [ ] Week 2 meal plan generated
- [ ] Sita daily management running

**By Mar 8 (Launch):**
- [ ] Website live with all products, photos, copy
- [ ] Content calendar executing (posts going out)
- [ ] Influencer outreach started
- [ ] Health system running on autopilot
- [ ] All 7 cron reminders firing consistently

**By end of March:**
- [ ] Phase 2 agents operational (Content, SEO, Research)
- [ ] First sales coming through Shopify
- [ ] PR pitches sent to 5+ magazines/blogs
- [ ] Sunshine's daily ops load reduced by 50%+

---

*This is the operating system. Janet runs the team. Sunshine runs the vision. The agents do the work.* ✦
