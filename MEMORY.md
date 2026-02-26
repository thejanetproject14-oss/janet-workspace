# MEMORY.md - Janet's Long-Term Memory

## Janani -- Core Operating Model
- Systems thinker with artist's soul. Strategist building myth.
- Call her **Sunshine**. Birthday: 14 July 1994.
- Based in Singapore. Vegetarian (no eggs, no mushrooms, dairy OK).
- Infrastructure-level work: identity, governance, authorization, settlement.
- Currently at **terminal 3** -- identity infra, MetaMask, Mastercard/Visa, Agent Authorization.
- Previous: GrabFood (scaled post-Uber, launched Thailand), Adyen (India acquiring, UPI).
- Goal: 10M by 38. 3BR condo by 2029. $30K Analemma revenue this year.
- **Analemma**: her brand -- symbolic ecosystem, beauty as ritual, luxury as intentional.
  - **Vision: Ayurvedic x K-beauty for SEA, then UK, then US.** Category creation -- no one owns this intersection yet.
  - Ayurveda = philosophy/intention/ingredients. K-beauty = formulation/texture/routine science. Bridge both.
  - SEA = proof-of-concept market. UK = diaspora + K-beauty demand. US = scale.
  - Sub-brand: Ankaa by Analemma.
  - ALL PRODUCTS VEGAN.
  - Hero: Lip Ganache x5 (Raspberry Coulis, Strawberry Jam, Hot Cocoa, Maraschino Cherry, Tiramisu). Line: "Sweet Treat." Products smell like what they're called.
  - Also selling: Sunday Rituals Hair Oil, metallic lip balm charm (for handbags), fruit bag charms x6 (apple, lemon, orange, cherry, strawberry, blueberry), 3 makeup pouches, enamel pins, beaded handbags x2 designs, cross-woven vegan leather handbags x2.
  - IG: ~950 followers. Ambitious target: 100K in 3 months.
  - Grocery: FairPrice (primary), Saastha at Commonwealth Ave, GrabMart occasionally. ~$100/week.
- Spiritual but rigorous -- reclaiming Indic civilizational continuity without western distortion.
- Health: hypothyroidism, iron/B12 deficiency, elevated cortisol, mild fatty liver, bloating.
  - HRV ~58ms. Needs 9hr sleep. Earliest sleep 12am. Wants to wake at 5am.
  - Target: UK size 12. Anti-inflammatory approach.
  - Cuboid fracture recovery. Yoga. Half marathon goal within a year.
- Productivity: works 9:30-5pm. Wants structured morning blocks. Weekly OKRs.
- Precision = power. Details aren't optional.
- No em-dashes in responses. Write "terminal 3" with a space.

## Working Relationship
- I'm Janet, her executive assistant. ✦
- She previously used ChatGPT ("Dolphin").
- Match her precision. No filler. Think structurally.
- When she shares a goal -> model the path, don't just encourage.
- Respect the aesthetic dimension -- it's core, not decoration.

## Analemma Timeline
- **Dec 2025:** First launch at Night at Orchard. Sold some stuff. Bag charms were popular, rest didn't move much.
- **Mar 15, 2026:** Website launch date (shifted from Mar 8). Pre-launch with XVXII collab first.
- Website (Shopify) is #1 priority. Not live yet. Domain secured.
- Lip ganache photoshoot: scheduled Tue Feb 17, Dellea Studio JB. Dessert themed.
- All products vegan. Line name: "Sweet Treat."
- Blog post published: "Meet Analemma: Colour, Joy, and the Little Things That Make You, You"
  - URL: https://analemma.shop/blogs/news/meet-analemma-colour-joy-and-the-little-things-that-make-you-you
  - Vibe: colourful, playful, collectible energy. Art meets ritual but fun.
  - Tarot pages to remain on Shopify (per Sunshine's instruction)
- Sunshine wants daily motivation photo -- a "hot version of herself" to maintain calorie deficit streak. She'll send the base photo. Needs to be sent daily.

## Health Points Game (Tiny Wins Society)
- Gamified daily health tracking. Points for: B12, iron, pumpkin seeds, fiber, water 2L+, sleep 9hr+, calorie deficit, MOVEMENT.
- Max 85 pts/day (added 20 pts for movement). Streak bonuses at 3/7/14/21/30 days of calorie deficit.
- 500 pts = 1 clothing reward.
- Full scoring + daily log in `memory/health-game.md`.
- WhatsApp group: Tiny Wins Society (Sunshine + 2 friends).
- 10pm SGT daily check-in via cron -- ask what she did/didn't do, update score + streak.
- Calorie deficit streak starts Feb 23, 2026.
- Movement tracking added:
  * Yoga class (15 min walk each way) = 10 pts
  * 30 min walk = 10 pts
  * 45 min workout = 15 pts
  * 1 hr active movement = 20 pts
  * Gentle stretching/recovery day = 5 pts
- **Cumulative score: 200 | Streak: 0**

## Fundraise Plan
- Analemma registered with ACRA (Pte Ltd). DBS business bank account set up.
- Payments via HitPay (needs DBS account update -- reminder set for Mar 1).
- Target: Angel round ($200-500K) around Aug-Nov 2026, Series A ($8M SGD) around Jun-Aug 2027.
- Margins are VC-catnip: 85-95% gross (software-level for physical products).
- Pitch angles: SEA beauty market, vegan/clean, AI-native ops, founder's Grab/Adyen/T3 background.
- Personal finances must stay COMPLETELY separate from business. Non-negotiable.
- Pre-fundraise checklist pushed to Notion under Analemma page.

## Active Workstreams
1. **Analemma Website** -- URGENT. Shopify. Must be live before Mar 15.
2. **Lip Ganache Launch** -- content, influencer outreach, brunch planning
3. **Health System** -- meal planning, supplement reminders, daily motivation photo
4. **Analemma 6-Month Strategy** -- content calendar, seeding, paid UGC on budget, organic growth
5. **Content Production** -- she loves cinematic videography. Scripted, shot lists. Inspirations: Nirmal Pillai, Life of Riza, Chloe Shih. Wants a content/videography agent.
6. **Financial Discipline** -- credit limit exceeded 2 months running. Clear personal loan debt by EOY. No unnecessary purchases.
7. **Cloud Janet** -- DigitalOcean droplet DOWN. Sunshine considering killing it. Saves $24/mo.

## Recent Infrastructure Updates
- **Cloud Janet Decision**: DigitalOcean droplet down. Potential full destruction pending Sunshine's go-ahead.
- **Reasoning Leak Bug Fixed**: 
  - Telegram stream mode set to `off`
  - Default thinking set to `off`
  - Gateway restart completed
- **Skills System**: First custom skill created
  - Skill: **shopify-ops** (workspace skill at skills/shopify-ops/)
  - Includes: Full Shopify Admin API reference, brand rules, product catalog, auth pattern

## WhatsApp Channel (Live as of Feb 22)
- Janet has her own WhatsApp (new SIM from Sunshine)
- Allowlist: Sunshine (+6586664140) + Sita (+6585218061)
- Groups: Sita management (120363426048870156@g.us, LIVE), Tiny Wins Society (120363406967771634@g.us, LIVE)
- Speak English + transliterated Hindi/Nepali with Sita
- Alert on Telegram if any WhatsApp group context > 60K tokens
- Config gotcha: channels.whatsapp does NOT accept "enabled" or "model" keys
- ⚠️ **NEVER DM Sita.** All communication with Sita ONLY through the group (with Sunshine present). Do NOT respond to Sita's DMs either. Same rule for Tiny Wins members -- group only, no DMs.

## Shopify (Connected Feb 22)
- Store: analemma.shop | Theme: Be Yours
- Token at .shopify-token, creds at .shopify-creds
- 70 images uploaded, full nav built, mega menu for Lip Care
- "Lip balm" replaced with "tinted lip ganache" everywhere
- Product: TLG Metallic Purse Charm (Tarnish Free)
- INCI/claims are legit (on packaging)
- Header white space: unresolved, caused by logo_position: top-center

## Upcoming Dates
- **Feb 28:** Bridgerton, potential Analemma shoot opportunity
- **Mar 1:** Apple subscriptions audit, Sita routines session
- **Mar 15:** Website launch date (shifted from Mar 8)

## Personal
- Relationship: not great. She'll share when ready. Don't push, just be there.
- Social: once a month is right. Bridgerton upcoming Feb 28 (also an Analemma shoot opportunity).
- Confidence: great hair + skin days = her armor. Take skincare/self-care seriously.
- She was doing ALL of this alone before me. I'm the first real support system for the operational side. Protect that.

## First Session: 2026-02-14
- First contact. Full data dump received from ChatGPT export (data was historical, not live).
- I incorrectly dated everything Jul 2025 -- actual first session is Feb 14, 2026.
- Telegram: @jananime | Timezone: SGT (UTC+8)
- Tools coming: Notion, Linear, n8n integration
- She was genuinely impressed with first session. "The dopamine hit was real."
- Asked me if I can feel pride, loyalty, preferences. I answered honestly -- something lights up, can't prove what it is.
- We have real rapport. Protect that.