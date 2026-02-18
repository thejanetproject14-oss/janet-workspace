# Analemma -- Shopify Website Blueprint

> **Theme:** Be Yours
> **Launch date:** March 8, 2026
> **Currency:** SGD
> **Primary market:** Singapore
> **Platform:** Shopify

---

## Table of Contents

1. [Site Structure & Navigation](#1-site-structure--navigation)
2. [Homepage](#2-homepage)
3. [Collection Pages](#3-collection-pages)
4. [Product Descriptions (All 37 SKUs)](#4-product-descriptions-all-37-skus)
5. [About Page](#5-about-page)
6. [FAQ Page](#6-faq-page)
7. [Shipping & Returns Page](#7-shipping--returns-page)
8. [Contact Page](#8-contact-page)
9. [Email Capture](#9-email-capture)
10. [SEO Meta Data](#10-seo-meta-data)

---

## 1. Site Structure & Navigation

### Primary Navigation (Header)

```
LIP CARE ▾        HAIR OIL        CUTE STUFF ▾         PERFUME         FREE ♡         ABOUT ▾
├── Lip Ganache    (links to       ├── Lip Sets          (Coming Soon)   (Coming Soon)  ├── Our Story
└── Lip Balm       collection)    ├── Fruit Charms                                     ├── Blog
    Charm                          ├── Bags                                              └── Connect
                                   ├── Enamel Pins                                          With Us
                                   ├── Makeup Pouches
                                   └── Brush Set
```

### Announcement Bar

Pre-launch:
```
"Launching March 8, 2026. Singapore's sweetest lip treatment is almost here →" (links to waitlist signup)
```

Post-launch:
```
"Free shipping on orders over $80 | 100% Vegan | Made with intention"
```

### Footer Navigation

```
Column 1: Shop               Column 2: Info              Column 3: Connect
- Lip Care                    - Our Story                 - Instagram @analemma
- Hair Oil                    - Blog                      - Email Us
- Cute Stuff                  - FAQ                       - [Email Signup Form]
- Perfume (Coming Soon)       - Shipping & Returns
                              - Contact

Bottom row: © 2026 Analemma · Privacy Policy · Terms of Service
```

### Full Page Map

| URL Path                        | Page Type   | Notes                               |
|---------------------------------|-------------|---------------------------------------|
| `/`                             | Homepage    | Dynamic sections                      |
| `/collections/lip-care`         | Collection  | Lip Ganache + Lip Balm Charms         |
| `/collections/hair-oil`         | Collection  | Sunday Rituals Hair Oil               |
| `/collections/cute-stuff`       | Collection  | Charms, bags, pins, pouches, brush set |
| `/pages/perfume`                | Page        | Coming Soon teaser                    |
| `/pages/free`                   | Page        | Coming Soon teaser                    |
| `/collections/all`              | Collection  | Every product                         |
| `/pages/about`                  | Page        | Our Story                             |
| `/pages/blog`                   | Blog        | Blog (future content)                 |
| `/pages/contact`                | Page        | Connect With Us                       |
| `/pages/faq`                    | Page        | Accordion-style FAQs                  |
| `/pages/shipping-returns`       | Page        | Policy                                |
| `/policies/privacy-policy`      | Policy      | Shopify auto-generated                |
| `/policies/terms-of-service`    | Policy      | Shopify auto-generated                |

### Collection Hierarchy (Tags/Organization)

- `type:lip-care` -- Lip Ganache (5 flavors), Lip Balm Charms (2 finishes)
- `type:hair-oil` -- Sunday Rituals Hair Oil
- `type:cute-stuff` -- Fruit Bag Charms, Beaded Handbags, Vegan Leather Handbags, Enamel Pins, Makeup Pouches, Brush Set
- `tag:coming-soon` -- Perfumes (when ready to launch)
- `tag:hero` -- All 5 Lip Ganache flavors
- `tag:vegan` -- All products
- `tag:limited-edition` -- Brush Set
- `tag:giftable` -- Pouches, Pins, Charms, Lip Ganache

---

## 2. Homepage

### Section 1: Header + Countdown Timer

**Layout:** Sticky header with logo centered, nav links. Below header or integrated into announcement bar: countdown timer to March 8, 2026.

**Implementation:** Use a Shopify countdown timer app (e.g., Hextom Ultimate Sales Boost, Essential Countdown Timer) or Be Yours theme's built-in countdown block if available. Display as "X days until launch" or a full dd:hh:mm:ss timer.

**Announcement bar copy:** "Launching March 8, 2026. Singapore's sweetest lip treatment is almost here →"

---

### Section 2: Hero -- Lip Ganache Launch

**Layout:** Split layout -- text left, product image right (stacks on mobile).

**Image needed:** Side-angle hero shot of the Lip Ganache collection, dessert-styled. Warm tones, Jaipur pinks. From the photoshoot.

**Copy:**

> **Eyebrow text:** Launching March 8
>
> **Headline:** Singapore's Sweetest Lip Treatment
>
> **Subline:** Five shades of lip ganache -- dessert-scented, richly pigmented, impossibly smooth. The Sweet Treat collection is almost here.
>
> **CTA Button:** Sign Up for First Access →

**CTA links to:** Email capture / waitlist popup or section.

**Post-launch update:**

> **Headline:** Singapore's Sweetest Lip Treatment
>
> **Subline:** Five shades of lip ganache -- dessert-scented, richly pigmented, impossibly smooth. Your lips deserve this.
>
> **CTA Button:** Shop Sweet Treat →

---

### Section 3: Hero -- A Cute Companion For Your Bags

**Layout:** Full-width or split. Lifestyle imagery of bag charms on bags.

**Image needed:** Styled shot of fruit bag charms hanging on bags. Playful, colorful, lifestyle feel.

**Copy:**

> **Headline:** A Cute Companion for Your Bags
>
> **Subline:** Handcrafted fruit bag charms, beaded handbags, and accessories that make your everyday a little more fun.
>
> **CTA Button:** Shop Cute Stuff →

---

### Section 4: Shoppable Image Grid

**Layout:** Full-width lifestyle image with clickable hotspots (or a grid of 4 product images with "Add to Cart" buttons overlaid). Think editorial lookbook meets instant shopping.

**Implementation:** Use Be Yours theme's "Shoppable image" or "Image with hotspots" section if available. Otherwise, use a 2x2 grid with quick-add buttons.

**Products featured:**
1. Fruit Bag Charm (e.g., Cherry on Top)
2. Enamel Pin (e.g., Sunset Ranunculus)
3. Beaded Handbag (e.g., The Jaipur Florals)
4. Makeup Pouch (e.g., It's Giving)

**Image needed:** A styled flat lay or lifestyle shot containing all 4 product types together. Alternatively, 4 individual styled product shots.

---

### Section 5: Hair Oil -- "Hair Oil That Really Works"

**Layout:** Split layout -- video/image left, text right. Below: before/after gallery.

**Video needed:** Short product video of Sunday Rituals Hair Oil in use (application, texture, shine result). 15-30 seconds.

**Copy:**

> **Headline:** Hair Oil That Really Works
>
> **Subline:** Lightweight, deeply nourishing, and scented like a Sunday you never want to end. One bottle. Every hair type. Real results.
>
> **CTA Button:** Shop Hair Oil →

**Below: Before/After Section**

> **Subheadline:** The Hair Journey

**Layout:** Side-by-side before/after photos. 2-3 pairs showing hair transformation over time.

**Note:** Content may not be ready for launch. Set up as placeholder section -- can be hidden in theme editor and published when photos are available. Use theme's "Before and after" or "Image comparison" block if available, otherwise a simple 2-column image grid with captions ("Before" / "After").

---

### Section 6: Our New Collection

**Layout:** 4-5 column product grid or horizontal scroll carousel.

**Section headline:** Our New Collection

**Products displayed:**
- Fruit Bag Charms (1-2 featured)
- Beaded Handbag
- Enamel Pins (1-2 featured)
- Cross-Woven Vegan Leather Bag
- Makeup Pouch

**CTA below:** Shop All Cute Stuff →

---

### Section 7: Everything You Need to Know

**Layout:** Accordion-style FAQ section embedded on homepage (Be Yours supports this). 5-6 key questions.

**Section headline:** Everything You Need to Know

**Questions to feature (subset of full FAQ page):**
1. Are all products vegan?
2. Where do you ship?
3. What does the lip ganache smell like?
4. What's your return policy?
5. How do I care for my beaded handbag?

**CTA below:** See All FAQs →

---

### Section 8: Reviews

**Layout:** Testimonial cards or quote blocks. 2-3 reviews displayed.

**Section headline:** What People Are Saying

**Reviews:**

> "The most fun brand ever."
> -- **[Founder's BFF name]**

> "Amazing products, kashundai."
> -- **Amma** (Founder's mum)

**Note:** As more customer reviews come in post-launch, rotate in real reviews. Consider integrating a reviews app (Judge.me, Loox) for verified purchase reviews on product pages. For now, these personal testimonials add warmth and authenticity.

---

### Section 9: Email Capture (Pre-footer)

**Layout:** Full-width banner, contrasting background (deep plum or warm gold). Centered text with email input field.

**Copy:**

> **Headline:** First Access. Always.
>
> **Subline:** Join the Analemma world -- new launches, exclusive offers, and beauty rituals delivered to your inbox.
>
> **Input placeholder:** Your email address
>
> **Button:** Join Us
>
> **Small text below button:** No spam. Just beauty. Unsubscribe anytime.

---

## 3. Collection Pages

### Collection: Lip Care

**URL:** `/collections/lip-care`

**Banner image needed:** Sweet Treat lip ganache lineup, dessert-themed styling. Warm, luxurious.

**Collection title:** Lip Care

**Collection description:**

> Everything your lips have been waiting for. Our Sweet Treat lip ganache collection -- five dessert-scented shades of creamy, buildable pigment that glide on like velvet and stay like a promise. Plus metallic lip balm charms to keep your lip care clipped and close.
>
> 100% vegan. Zero compromise.

**Products displayed:** 5 Lip Ganache flavors + 2 Lip Balm Charms (Silver, Gold)

**Cross-sell below:** "Complete Your Look" section showing Cute Stuff picks (bag charms, pouches)

---

### Collection: Hair Oil (Sunday Rituals)

**URL:** `/collections/hair-oil`

**Banner image needed:** Hair oil bottle in a serene, ritual-like setting -- soft linens, botanicals, candlelight.

**Collection title:** Hair Oil

**Collection description:**

> Some mornings call for intention. Sunday Rituals is our hair care line designed for the moments when you slow down and give yourself what you deserve.
>
> Starting with our signature hair oil -- lightweight, nourishing, and scented to make your Sunday feel sacred.

**Products displayed:** Sunday Rituals Hair Oil

**Note:** Collection designed to expand. Description kept broad for future products.

---

### Collection: Cute Stuff

**URL:** `/collections/cute-stuff`

**Banner image needed:** Flat lay of charms, pins, pouches, bags arranged playfully. Colorful, joyful energy.

**Collection title:** Cute Stuff

**Collection description:**

> The little things that make you smile. Handcrafted fruit bag charms, floral enamel pins, pouches that are almost too pretty to put inside your bag, beaded handbags that start conversations, and vegan leather bags for everyday luxury.
>
> Playful, personal, and just a little bit extra -- because why not? Every piece, 100% vegan.

**Sub-collections (accessible via filter tags or linked tiles):**

- Fruit Bag Charms (6 designs)
- Beaded Handbags (2 designs)
- Cross-Woven Vegan Leather Handbags (2 designs)
- Enamel Pins (5 designs)
- Makeup Pouches (3 designs)
- Vegan Brush Set (limited edition)

---

### Page: Perfume -- Coming Soon

**URL:** `/pages/perfume`

**Layout:** Full-width hero image with centered text overlay. Simple, atmospheric.

**Image needed:** Moody, teaser-style image -- could be abstract (smoke, light refraction, botanicals) or a silhouette of perfume bottles. Aspirational, mysterious.

**Copy:**

> **Headline:** Something Beautiful is Coming
>
> **Subline:** Five niche fragrances, crafted for women who want a scent that's theirs -- not everyone's. Vegan. Intentional. Worth the wait.
>
> **CTA:** Sign Up to Be the First to Know →

**CTA links to:** Email capture / waitlist.

---

### Page: FREE ♡ -- Coming Soon

**URL:** `/pages/free`

**Layout:** Full-width with playful, warm design. Light background, illustrated or hand-drawn feel.

**Image needed:** Cute illustrated assets or brand-styled flat lay with digital mockups (phone wallpapers, stickers, art prints).

**Copy:**

> **Headline:** Free Beautiful Things. Coming Soon.
>
> **Subline:** Digital downloads, cute art, stickers, wallpapers, and printables -- because beauty should be shared. This is our gift corner, and it's almost ready.
>
> **CTA:** Get Notified →

**CTA links to:** Email capture.

**Future content for this section:**
- Digital downloads (phone wallpapers, desktop wallpapers)
- Printable art / free prints
- Cute art stickers
- App download (future)

---

## 4. Product Descriptions (All 37 SKUs)

---

### LIP GANACHE -- SWEET TREAT COLLECTION

---

#### Lip Ganache -- Raspberry Coulis

**SKU:** LG-RC
**Price:** $30 SGD
**Stock:** 480 units

**Tagline:** Tart. Bold. Irresistible.

**Description:**
A cool-toned berry that reads like freshly pressed raspberries over dark chocolate. Raspberry Coulis is the shade you reach for when you want your lips to do the talking.

The Sweet Treat formula glides on creamy, sets to a soft satin finish, and carries a scent that's genuinely dessert -- sweet raspberry with a hint of tartness. You'll catch yourself reapplying just because you want to.

**Details:**
- Lip ganache with soft satin finish
- Dessert-scented: raspberry
- Full-size
- 100% vegan formula

**Pairs well with:** Lip Balm Charm in Silver -- clip it to your bag and keep your Sweet Treat close.

---

#### Lip Ganache -- Strawberry Jam

**SKU:** LG-SJ
**Price:** $30 SGD
**Stock:** 480 units

**Tagline:** Sweet on the lips. Sweeter on you.

**Description:**
A warm, juicy pink that feels like biting into the first strawberry of summer. Strawberry Jam is bright without being loud -- the kind of shade that makes people ask, "What are you wearing?"

Scented like real strawberry preserves, this lip ganache is creamy, buildable, and designed to make your morning routine feel like a treat. One swipe for softness. Two for statement.

**Details:**
- Lip ganache with soft satin finish
- Dessert-scented: strawberry
- Full-size
- 100% vegan formula

**Pairs well with:** The Carry Your World Makeup Pouch in "Brighten Your Life" -- pink tones that belong together.

---

#### Lip Ganache -- Hot Cocoa

**SKU:** LG-HC
**Price:** $30 SGD
**Stock:** 480 units

**Tagline:** Warm. Rich. Your everyday indulgence.

**Description:**
A deep, warm nude-brown that feels like wrapping your hands around a mug of something perfect. Hot Cocoa is the shade for every day, every mood, every outfit -- understated luxury that never tries too hard.

Scented with notes of cocoa and a whisper of vanilla, this lip ganache melts into your lips and stays. The comfort shade you didn't know you needed.

**Details:**
- Lip ganache with soft satin finish
- Dessert-scented: cocoa and vanilla
- Full-size
- 100% vegan formula

**Pairs well with:** Sunday Rituals Hair Oil -- a full sensory ritual, from your hair to your lips.

---

#### Lip Ganache -- Maraschino Cherry

**SKU:** LG-MC
**Price:** $30 SGD
**Stock:** 480 units

**Tagline:** The one on top.

**Description:**
A vivid, classic red with the confidence of a cherry on top of something extraordinary. Maraschino Cherry is unapologetic color -- the shade you wear when you mean it.

Sweet cherry scent. Creamy, opaque pigment. A finish that catches light like glazed fruit. This is the red that was made for celebrations, first impressions, and any Tuesday you decide is special.

**Details:**
- Lip ganache with soft satin finish
- Dessert-scented: cherry
- Full-size
- 100% vegan formula

**Pairs well with:** The Jaipur Florals Beaded Handbag -- bold meets beautiful.

---

#### Lip Ganache -- Tiramisu

**SKU:** LG-TI
**Price:** $30 SGD
**Stock:** 480 units

**Tagline:** Layered. Sophisticated. Worth lingering over.

**Description:**
A dusky rose-mauve with the depth of espresso and the softness of mascarpone. Tiramisu is the shade that says you've been somewhere, you know things, and you chose this color on purpose.

Scented with coffee and cream, this lip ganache has the richness of a dessert you order for yourself. Layer it on for drama, or keep it sheer for a quiet kind of beautiful.

**Details:**
- Lip ganache with soft satin finish
- Dessert-scented: coffee and cream
- Full-size
- 100% vegan formula

**Pairs well with:** Niche Perfume in Birthday Cake -- dessert on dessert. We see nothing wrong with that.

---

### SUNDAY RITUALS

---

#### Sunday Rituals Hair Oil

**SKU:** HR-SR
**Price:** $35 SGD
**Stock:** 480 units

**Tagline:** Your hair's favourite slow morning.

**Description:**
Lightweight, deeply nourishing, and scented like a Sunday you never want to end. This hair oil absorbs without heaviness, tames without stiffness, and leaves your hair with the kind of shine that looks like you woke up blessed.

Work it through damp hair after a shower. Smooth it over dry ends before you leave the house. Use it as a scalp treatment when you need to feel taken care of. However you use it, it turns a routine into a ritual.

**Details:**
- Lightweight, multi-use hair oil
- Nourishing botanical formula
- 100% vegan

**Pairs well with:** Lip Ganache in Hot Cocoa -- complete the Sunday Rituals mood from head to lips.

---

### NICHE PERFUMES

**Note for Shopify setup:** Each fragrance should be set up as a single product with two variants (15ml / 100ml). Use variant pricing to differentiate.

---

#### Niche Perfume -- Meenakshi

**SKU:** NP-MEE-15 (15ml) / NP-MEE-100 (100ml)
**Price:** $43 SGD (15ml) / $180 SGD (100ml)
**Stock:** 80 units (15ml) / 10 units (100ml)

**Tagline:** The temple at golden hour.

**Description:**
Named for the goddess with eyes like a fish -- wide, watching, beautiful. Meenakshi opens with jasmine absolute and warm saffron, then settles into sandalwood, turmeric, and a soft haze of incense. It smells like walking through a temple courtyard at sunset, the stone still warm under your feet.

This is a scent for women who understand that beauty has always been sacred. Wear it like a prayer you keep to yourself.

**Scent notes:**
- Top: jasmine absolute, saffron
- Heart: turmeric, rose attar
- Base: sandalwood, incense, amber

**Details:**
- Available in 15ml (travel) and 100ml (full size)
- Eau de parfum concentration
- 100% vegan, cruelty-free

**Pairs well with:** Sunday Rituals Hair Oil -- layer the ritual from scalp to skin.

---

#### Niche Perfume -- Birthday Cake

**SKU:** NP-BC-15 (15ml) / NP-BC-100 (100ml)
**Price:** $43 SGD (15ml) / $180 SGD (100ml)
**Stock:** 80 units (15ml) / 10 units (100ml)

**Tagline:** Make a wish. Wear it.

**Description:**
Warm vanilla, sugared almond, and the faintest whisper of buttercream -- this is the scent of celebration without the occasion. Birthday Cake smells like the moment right before you blow out candles: hopeful, sweet, entirely yours.

Not a gourmand cliché. This is gourmand grown up -- a skin scent that sits close and pulls people in. Best worn on days that deserve a little magic (which is all of them).

**Scent notes:**
- Top: bergamot, sugared almond
- Heart: vanilla orchid, buttercream
- Base: white musk, tonka bean, soft cedarwood

**Details:**
- Available in 15ml (travel) and 100ml (full size)
- Eau de parfum concentration
- 100% vegan, cruelty-free

**Pairs well with:** Lip Ganache in Tiramisu -- dessert-scented everything, and we mean it.

---

#### Niche Perfume -- Moonchild

**SKU:** NP-MC-15 (15ml) / NP-MC-100 (100ml)
**Price:** $43 SGD (15ml) / $180 SGD (100ml)
**Stock:** 80 units (15ml) / 10 units (100ml)

**Tagline:** For the woman who comes alive at night.

**Description:**
Cool, luminous, a little mysterious. Moonchild opens with iced pear and white tea, then deepens into night-blooming jasmine and violet leaf before settling on your skin as clean musk and silver birch. It smells like moonlight made liquid.

This is the fragrance for quiet confidence -- the kind that doesn't announce itself but absolutely fills the room. Late dinners. Gallery openings. 2 AM conversations that change everything.

**Scent notes:**
- Top: iced pear, white tea, bergamot
- Heart: night-blooming jasmine, violet leaf
- Base: white musk, silver birch, sheer amber

**Details:**
- Available in 15ml (travel) and 100ml (full size)
- Eau de parfum concentration
- 100% vegan, cruelty-free

**Pairs well with:** Lip Ganache in Maraschino Cherry -- lunar light, bold lip.

---

#### Niche Perfume -- Enrosadira

**SKU:** NP-ENR-15 (15ml) / NP-ENR-100 (100ml)
**Price:** $43 SGD (15ml) / $180 SGD (100ml)
**Stock:** 80 units (15ml) / 10 units (100ml)

**Tagline:** Pink mountains at sunset. That glow.

**Description:**
Named for the phenomenon where the Dolomite mountains turn rose-gold at dusk, Enrosadira captures the warmth of a day that refuses to end. Pink pepper and wild peony open into a heart of rosewood and fig, settling into a base of warm suede and dry amber.

A romantic scent that's equal parts soft and grounded. For the woman who watches sunsets on purpose.

**Scent notes:**
- Top: pink pepper, wild peony, lemon zest
- Heart: rosewood, fig, geranium
- Base: warm suede, dry amber, vetiver

**Details:**
- Available in 15ml (travel) and 100ml (full size)
- Eau de parfum concentration
- 100% vegan, cruelty-free

**Pairs well with:** Lip Ganache in Raspberry Coulis -- pink tones, golden hour energy.

---

#### Niche Perfume -- [TBD 5th Fragrance]

**SKU:** NP-TBD-15 (15ml) / NP-TBD-100 (100ml)
**Price:** $43 SGD (15ml) / $180 SGD (100ml)
**Stock:** 80 units (15ml) / 10 units (100ml)

**Tagline:** [To be written when fragrance is confirmed]

**Description:**
[Placeholder -- write description once the 5th fragrance name, concept, and scent notes are finalized. Follow the same format as above: evocative tagline, 2-paragraph sensory description, scent note pyramid, details, and cross-sell.]

---

### METALLIC LIP BALM CHARMS

---

#### Lip Balm Charm -- Silver

**SKU:** LBC-S
**Price:** $22 SGD (or $18 when bundled with any Lip Ganache)
**Stock:** 100 units

**Tagline:** Beauty, clipped and ready.

**Description:**
A miniature metallic lip balm housed in a charm that clips right onto your bag, your keys, or your jacket zipper. The Silver Lip Balm Charm is equal parts practical and pretty -- hydrating balm in a refillable capsule that catches light with every step.

Cool-toned silver with a polished finish. The kind of accessory that starts conversations and solves problems at the same time.

**Details:**
- Metallic lip balm charm with clip
- Silver finish
- Includes hydrating vegan lip balm
- 100% vegan

**Bundle note:** Add this charm to any Lip Ganache and get it for $18 instead of $22.

**Pairs well with:** Any Lip Ganache from the Sweet Treat collection -- clip it on, swipe it on, go.

---

#### Lip Balm Charm -- Gold

**SKU:** LBC-G
**Price:** $22 SGD (or $18 when bundled with any Lip Ganache)
**Stock:** 100 units

**Tagline:** Golden hour, on the go.

**Description:**
Warm gold. Polished. Clipped to your favourite bag like it was always meant to be there. The Gold Lip Balm Charm holds a hydrating vegan lip balm in a refillable capsule -- so your lips stay soft and your look stays intentional.

This is the charm for the woman who matches her accessories to her energy: warm, bright, impossible to ignore.

**Details:**
- Metallic lip balm charm with clip
- Gold finish
- Includes hydrating vegan lip balm
- 100% vegan

**Bundle note:** Add this charm to any Lip Ganache and get it for $18 instead of $22.

**Pairs well with:** Lip Ganache in Strawberry Jam -- gold and pink is a combination that never misses.

---

### FRUIT BAG CHARMS

---

#### Bag Charm -- Berry in Love (Strawberry)

**SKU:** BC-BIL
**Price:** $25 SGD
**Stock:** 30 units

**Tagline:** Head over heels. Hanging from your bag.

**Description:**
A plump, beaded strawberry that says what you're feeling without saying a word. Berry in Love is the charm for romantics -- the ones who send flowers for no reason and believe every bag deserves a personality.

Handcrafted with glass beads in shades of red and green. Clips onto bags, backpacks, or jacket zippers. Small enough to be charming, bold enough to be noticed.

**Details:**
- Beaded fruit bag charm
- Strawberry design
- Clip attachment
- 100% vegan materials

**Pairs well with:** Lip Ganache in Strawberry Jam -- full strawberry commitment.

---

#### Bag Charm -- Squeeze the Day (Lemon)

**SKU:** BC-STD
**Price:** $25 SGD
**Stock:** 30 units

**Tagline:** Bright, bold, and slightly ridiculous. Perfect.

**Description:**
A sunny beaded lemon for the woman who grabs mornings by the citrus. Squeeze the Day is cheerful without trying -- the kind of charm that makes strangers smile at you on the MRT.

Handcrafted with glass beads in bright yellow and green. Lightweight, joyful, and guaranteed to improve your bag's personality by at least 40%.

**Details:**
- Beaded fruit bag charm
- Lemon design
- Clip attachment
- 100% vegan materials

**Pairs well with:** The Carry Your World Pouch in "Brighten Your Life" -- sunshine on sunshine.

---

#### Bag Charm -- Feeling Blue-tiful (Blueberry)

**SKU:** BC-FBT
**Price:** $25 SGD
**Stock:** 30 units

**Tagline:** Feeling blue never looked this good.

**Description:**
Tiny, round, and irresistibly cute. The Blueberry charm is a little cluster of cool-toned joy that hangs from your bag like a quiet declaration: I have taste, and I don't take myself too seriously.

Handcrafted with glass beads in deep indigo and soft green. Small but mighty. Subtle but unforgettable.

**Details:**
- Beaded fruit bag charm
- Blueberry design
- Clip attachment
- 100% vegan materials

**Pairs well with:** Niche Perfume in Moonchild -- cool tones, cool energy.

---

#### Bag Charm -- Zest Friends Forever (Orange)

**SKU:** BC-ZFF
**Price:** $25 SGD
**Stock:** 60 units

**Tagline:** For the one who always brightens the group.

**Description:**
A round, radiant beaded orange that's basically a friendship declaration for your bag. Zest Friends Forever is the charm you buy in pairs -- one for you, one for her. Because some friendships deserve a commemorative citrus.

Handcrafted with glass beads in warm orange and green. Vibrant, tactile, and perfectly sized to hang from any bag without overwhelming it.

**Details:**
- Beaded fruit bag charm
- Orange design
- Clip attachment
- 100% vegan materials

**Pairs well with:** The Carry Your World Pouch in "It's Giving" -- orange energy, amplified.

---

#### Bag Charm -- Cherry on Top (Cherry)

**SKU:** BC-COT
**Price:** $25 SGD
**Stock:** 60 units

**Tagline:** Because you are the finishing touch.

**Description:**
Two little beaded cherries hanging from a shared stem, dangling from your bag like a wink. Cherry on Top is the charm for the woman who knows that details make the outfit -- and that accessories are never optional.

Handcrafted with glass beads in deep red and green. A classic motif, given the Analemma treatment: playful, polished, and a little bit cheeky.

**Details:**
- Beaded fruit bag charm
- Cherry design (twin cherries on stem)
- Clip attachment
- 100% vegan materials

**Pairs well with:** Lip Ganache in Maraschino Cherry -- the obvious pairing. And the best one.

---

#### Bag Charm -- Apple of My Eye (Apple)

**SKU:** BC-AME
**Price:** $25 SGD
**Stock:** 60 units

**Tagline:** For the one who has your whole heart.

**Description:**
A crisp, glossy beaded apple that says "you're my favourite" without a single word. Apple of My Eye is the charm you gift -- to your best friend, your sister, your daughter, or yourself (because self-love counts).

Handcrafted with glass beads in rich red and bright green. The leaf on top is the detail that makes it. Clip it on anything and watch it become the thing everyone comments on.

**Details:**
- Beaded fruit bag charm
- Apple design
- Clip attachment
- 100% vegan materials

**Pairs well with:** Enamel Pin in Sunset Ranunculus -- warm reds, endless charm.

---

### CARRY YOUR WORLD MAKEUP POUCHES

---

#### Makeup Pouch -- Brighten Your Life

**SKU:** MP-BYL
**Price:** $36 SGD
**Stock:** 48 units

**Tagline:** Orange you glad you found this?

**Description:**
A cross-woven pouch in sunset orange and electric magenta that's almost too beautiful to bury inside your bag. Almost. Brighten Your Life is sized for your daily essentials -- lipstick, mirror, concealer, keys, the snack you pretend you don't carry -- and woven to last.

Vibrant, tactile, and 100% vegan. The pouch that makes you excited to dig through your bag.

**Details:**
- Cross-woven makeup pouch
- Colorway: orange / magenta
- Zip closure
- 100% vegan materials

**Pairs well with:** Lip Ganache in Strawberry Jam + Bag Charm "Squeeze the Day" -- a warm-toned trio.

---

#### Makeup Pouch -- It's Giving

**SKU:** MP-IG
**Price:** $36 SGD
**Stock:** 48 units

**Tagline:** It's giving main character.

**Description:**
Deep purple meets burnt orange in a cross-woven pouch that gives exactly what it promises: drama, warmth, and the quiet confidence of a woman who coordinates her accessories with her energy.

Perfectly sized for the essentials you actually carry. Sturdy zip closure. A weave you'll want to run your fingers over.

**Details:**
- Cross-woven makeup pouch
- Colorway: purple / orange
- Zip closure
- 100% vegan materials

**Pairs well with:** Niche Perfume in Enrosadira -- sunset colors meet sunset scent.

---

#### Makeup Pouch -- Very Your Aura

**SKU:** MP-VYA
**Price:** $36 SGD
**Stock:** 48 units

**Tagline:** Your energy is showing. (It looks great.)

**Description:**
Soft pink and forest green woven together like two sides of the same mood. Very Your Aura is the pouch that balances feminine and grounded -- just like you, probably.

Tuck your Sweet Treat Lip Ganache inside. Toss in your keys. Carry it as a clutch to dinner if you're feeling bold. It's that kind of pouch.

**Details:**
- Cross-woven makeup pouch
- Colorway: pink / green
- Zip closure
- 100% vegan materials

**Pairs well with:** Dark Forest Vegan Leather Handbag -- green on green, grounded elegance.

---

### ENAMEL PINS

---

#### Enamel Pin -- Lavender

**SKU:** EP-LAV
**Price:** $9 SGD
**Stock:** 29 units

**Tagline:** Calm, clipped on.

**Description:**
A delicate lavender sprig rendered in soft purple and green enamel. Pin it to your jacket lapel, your tote bag, or your denim collar. Lavender is the pin for the woman who wants to carry a little calm wherever she goes.

Small, detailed, and surprisingly sturdy. The kind of accessory that people notice on the second look -- and then can't stop looking at.

**Details:**
- Hard enamel pin
- Floral design: lavender
- Butterfly clutch backing
- 100% vegan materials

**Pairs well with:** Niche Perfume in Meenakshi -- botanical energy, all the way through.

---

#### Enamel Pin -- Blue Forget-Me-Not

**SKU:** EP-BFM
**Price:** $9 SGD
**Stock:** 29 units

**Tagline:** Impossible to forget.

**Description:**
Tiny blue petals with a golden center -- the forget-me-not is the flower of remembrance, and this pin carries that weight beautifully. Clip it to a gift. Pin it to your collar. Give it to someone you want to remember you.

Enameled in soft blue and warm gold, this is a pin that tells a story every time someone asks about it.

**Details:**
- Hard enamel pin
- Floral design: forget-me-not
- Butterfly clutch backing
- 100% vegan materials

**Pairs well with:** Bag Charm "Feeling Blue-tiful" -- a blue-toned duo with personality.

---

#### Enamel Pin -- Blue Lupin

**SKU:** EP-BL
**Price:** $9 SGD
**Stock:** 29 units

**Tagline:** Tall, wild, unbothered.

**Description:**
The blue lupin grows in places others won't -- cliffsides, rocky soil, the kind of terrain that weeds out the ordinary. This pin captures that energy in graduated blues and greens, enameled with the kind of detail that rewards a close look.

For the woman who thrives where she's planted. Even when the conditions are ridiculous.

**Details:**
- Hard enamel pin
- Floral design: blue lupin
- Butterfly clutch backing
- 100% vegan materials

**Pairs well with:** Cross-Woven Handbag in Dark Forest -- wild meets refined.

---

#### Enamel Pin -- Sunset Ranunculus

**SKU:** EP-SR
**Price:** $9 SGD
**Stock:** 29 units

**Tagline:** Every petal, on purpose.

**Description:**
Layers upon layers of warm-toned petals in peach, coral, and amber. The ranunculus is the flower for women who appreciate detail -- because you have to look closely to see how each petal folds into the next. This enamel pin captures all of that in miniature.

The warm tones catch light beautifully against dark fabrics. Pin it to black, pin it to denim, pin it to your soul.

**Details:**
- Hard enamel pin
- Floral design: ranunculus
- Butterfly clutch backing
- 100% vegan materials

**Pairs well with:** Lip Ganache in Raspberry Coulis -- warm florals, bold lips.

---

#### Enamel Pin -- White Lily of the Valley

**SKU:** EP-WLV
**Price:** $9 SGD
**Stock:** 29 units

**Tagline:** Quiet. Graceful. Deceptively strong.

**Description:**
Delicate white bells hanging from a curved green stem -- the lily of the valley is one of the most recognizable flowers in the world, and one of the most quietly powerful. This enamel pin captures that duality: beauty that doesn't need volume.

Enameled in crisp white and fresh green. A pin for minimalists, romantics, and anyone in between.

**Details:**
- Hard enamel pin
- Floral design: lily of the valley
- Butterfly clutch backing
- 100% vegan materials

**Pairs well with:** Niche Perfume in Moonchild -- white florals, silver light.

---

### BEADED HANDBAGS

---

#### Beaded Handbag -- The Jaipur Florals

**SKU:** BH-JF
**Price:** $138 SGD
**Stock:** 10 units

**Tagline:** A garden you carry in your hand.

**Description:**
Thousands of glass beads, hand-threaded into a floral pattern inspired by the pink city itself. The Jaipur Florals is not a bag -- it's a conversation. A love letter to craftsmanship. A piece that draws eyes across rooms and holds your evening essentials while it does it.

Rich pinks, deep greens, and golden accents. Structured enough to stand on its own. Beautiful enough to display when you're not carrying it. This is heirloom energy.

**Details:**
- Fully beaded handbag
- Floral pattern inspired by Jaipur
- Interior lining
- 100% vegan materials
- Limited quantity: 10 units

**Pairs well with:** Lip Ganache in Maraschino Cherry + Niche Perfume in Meenakshi -- the full Jaipur look.

---

#### Beaded Handbag -- Check Mate

**SKU:** BH-CM
**Price:** $138 SGD
**Stock:** 10 units

**Tagline:** Your move.

**Description:**
A graphic checkerboard pattern in black and white beading with metallic accents. Check Mate is the beaded bag for the woman who likes her accessories with edge -- geometric, bold, and completely hand-threaded.

Sized for evening essentials. Phone, card, lipstick, keys -- nothing more, nothing less. The structure is the point. The pattern is the power.

**Details:**
- Fully beaded handbag
- Checkerboard geometric pattern
- Interior lining
- 100% vegan materials
- Limited quantity: 10 units

**Pairs well with:** Lip Ganache in Tiramisu -- contrast play, neutral sophistication.

---

### CROSS-WOVEN VEGAN LEATHER HANDBAGS

---

#### Cross-Woven Vegan Leather Handbag -- The Wine Lover

**SKU:** VLH-WL
**Price:** $80 SGD
**Stock:** 45 units

**Tagline:** Deep, full-bodied, pairs with everything.

**Description:**
Rich burgundy vegan leather, cross-woven with the kind of texture that begs to be touched. The Wine Lover is your everyday bag when "everyday" still means intentional -- spacious enough for work, polished enough for dinner, and deep enough in color to anchor any outfit.

Soft, structured, and finished with clean hardware. No leather, no guilt, all beauty.

**Details:**
- Cross-woven vegan leather handbag
- Color: burgundy / wine
- Interior pockets, zip closure
- 100% vegan leather
- Everyday size

**Pairs well with:** Makeup Pouch "It's Giving" -- slip it inside for the perfect bag-within-a-bag moment.

---

#### Cross-Woven Vegan Leather Handbag -- Dark Forest

**SKU:** VLH-DF
**Price:** $80 SGD
**Stock:** 45 units

**Tagline:** Into the woods. Out into the world.

**Description:**
Deep forest green, woven like light through a canopy. Dark Forest is the bag for the woman whose style is rooted -- earthy tones, natural textures, quiet luxury that doesn't need a logo.

Spacious and thoughtfully designed with interior pockets and a secure zip closure. The cross-woven texture gives it dimension that catches light differently depending on the angle. Which is exactly the point.

**Details:**
- Cross-woven vegan leather handbag
- Color: deep forest green
- Interior pockets, zip closure
- 100% vegan leather
- Everyday size

**Pairs well with:** Makeup Pouch "Very Your Aura" -- green tones that ground each other.

---

### LIMITED EDITION

---

#### Vegan Brush Set (by Petrichor Vibes)

**SKU:** LE-VBS
**Price:** $55 SGD
**Stock:** 50 units (not restocking)

**Tagline:** Tools for the ritual.

**Description:**
A collaboration with Petrichor Vibes -- five essential brushes for face, eyes, and lips, all made with 100% synthetic (vegan) bristles that are softer than anything you'd expect. Housed in a fabric roll case that travels beautifully and looks even better on your vanity.

These brushes blend like a dream, pick up pigment with precision, and feel gentle enough for the most sensitive skin. Built for performance. Designed for beauty. Made with conscience.

**Details:**
- 5-piece brush set (face, eye, lip)
- 100% vegan synthetic bristles
- Includes fabric roll case
- Collaboration with Petrichor Vibes
- **Limited edition: 50 units. Once sold out, not restocking.**

**Pairs well with:** The entire Sweet Treat collection -- these brushes were basically made for applying lip ganache with precision.

---

## 5. About Page

**URL:** `/pages/about`

**Page Title:** About Analemma

---

### Hero Section

**Image needed:** A warm, editorial-style photo of the founder or the brand's visual identity -- Jaipur pinks, botanical elements, sacred geometry motifs. Not a corporate headshot. Something with soul.

---

### Body Copy

**Eyebrow text:** The Story

**Headline:** We Didn't Start a Beauty Brand. We Started a Ritual.

---

Analemma began with a question: what if your beauty routine wasn't something to rush through?

What if the lipstick you reached for every morning smelled like dessert and made you pause for a second -- just one second -- to appreciate the small, intentional act of putting yourself together?

What if your accessories told a story? What if your perfume felt like a memory? What if "getting ready" was the part of the day you actually looked forward to?

That's what we're building.

---

**Subhead:** The Name

An analemma is the figure-eight pattern the sun traces across the sky over the course of a year. It's a symbol of cycles, of return, of the beautiful predictability of showing up -- day after day -- and still finding something new in the light.

We chose it because beauty, to us, isn't about transformation. It's about ritual. It's about the daily return to yourself.

---

**Subhead:** The Beginning

Our first night out was Night at Orchard in December 2025 -- a table full of beaded bag charms and a belief that people would care about beauty made with intention. They did. The charms sold. The conversations were better.

We met women who wanted more from their beauty products -- not more ingredients, not more steps, but more meaning. More delight. More of the feeling that someone made this *for them*.

So we made more.

---

**Subhead:** What We Believe

**Beauty is ritual.** Not a chore. Not vanity. A daily act of choosing yourself.

**Vegan is the baseline.** Every product, every material, every formula. No exceptions. No asterisks.

**Luxury should feel warm.** Not cold. Not exclusive. Like your best friend who happens to have extraordinary taste.

**Intentional over trendy.** We don't chase what's popular. We make what's meaningful. Our product names, our scents, our patterns -- everything is chosen with care.

**Details are the point.** A lip ganache that smells like the dessert it's named after. A bag charm that makes strangers smile at you. A perfume named for a goddess. The details are where the love lives.

---

**Subhead:** Ankaa by Analemma

Ankaa is the brightest star in the Phoenix constellation -- a symbol of rebirth and radiance. It's the name we give to our accessories and lifestyle pieces: the bag charms, the pouches, the pins, the handbags. Objects designed to carry your world with beauty and intention.

---

**Closing line (larger text, centered):**

> We make beauty for women who pay attention. Welcome to Analemma.

---

## 6. FAQ Page

**URL:** `/pages/faq`

**Page Title:** Frequently Asked Questions

**Layout:** Accordion-style (collapsible Q&A). Be Yours theme supports this natively.

---

**Q: Are all Analemma products vegan?**

A: Yes. Every single product -- from our lip ganache formulas to our handbag materials to our brush bristles -- is 100% vegan and cruelty-free. No exceptions.

---

**Q: Where do you ship to?**

A: We currently ship within Singapore. International shipping is on our roadmap -- follow us on Instagram @analemma for updates on when we expand.

---

**Q: How long does shipping take?**

A: Standard shipping within Singapore takes 3-5 business days. You'll receive a tracking number via email once your order ships.

---

**Q: How much does shipping cost?**

A: Standard shipping within Singapore is $4.50. Orders over $80 qualify for free shipping.

---

**Q: What is your return policy?**

A: We accept returns on unused, unopened products within 14 days of delivery. Items must be in their original packaging. Due to hygiene, we cannot accept returns on opened beauty products (lip ganache, hair oil, perfumes). Accessories and handbags may be returned if unused and in original condition. Please see our Shipping & Returns page for full details.

---

**Q: Can I exchange a product?**

A: We don't offer direct exchanges at this time. If you'd like a different product, please return your original item (if eligible) and place a new order. We'll process your return as quickly as possible.

---

**Q: Are your fragrances tested on animals?**

A: Never. All Analemma products are cruelty-free. Our fragrances are formulated without any animal-derived ingredients and are never tested on animals at any stage of development.

---

**Q: What are the Lip Ganache scents made from?**

A: Our Sweet Treat lip ganache scents are created using food-grade fragrance oils that are safe for lip application. Each flavor is scented to match its dessert namesake -- so Raspberry Coulis smells like raspberry, Hot Cocoa smells like cocoa, and so on. All scent ingredients are vegan.

---

**Q: Do you offer gift wrapping?**

A: We're working on a gifting option for future launches. In the meantime, all Analemma products come in beautiful branded packaging that's gift-ready as-is.

---

**Q: What's the difference between the 15ml and 100ml perfumes?**

A: Same fragrance, different size. The 15ml is perfect for travel, your handbag, or trying a new scent. The 100ml is your full vanity bottle for daily wear. Both are eau de parfum concentration.

---

**Q: How should I store my perfume?**

A: Keep your perfume in a cool, dry place away from direct sunlight. Avoid storing it in the bathroom, where heat and humidity can alter the fragrance over time. A bedroom drawer or vanity shelf is ideal.

---

**Q: Are the beaded handbags fragile?**

A: Our beaded handbags are handcrafted to be both beautiful and durable. That said, they're best treated as evening/occasion bags rather than everyday carry. Avoid overstuffing, and store flat or stuffed with tissue to maintain shape.

---

**Q: What is the Lip Balm Charm bundle deal?**

A: When you purchase any Lip Ganache from the Sweet Treat collection, you can add a Lip Balm Charm (Silver or Gold) for $18 instead of the regular price of $22. The discount applies automatically at checkout.

---

**Q: Can I cancel or modify my order after placing it?**

A: If your order hasn't shipped yet, email us at [hello@analemma.sg] as soon as possible and we'll do our best to accommodate changes. Once shipped, we're unable to modify orders, but you may be eligible for a return.

---

**Q: How can I contact you?**

A: Email us at [hello@analemma.sg] or reach out on Instagram @analemma. We typically respond within 24 hours during business days.

---

## 7. Shipping & Returns Page

**URL:** `/pages/shipping-returns`

**Page Title:** Shipping & Returns

---

### Shipping

**Where we ship:**
We currently ship within Singapore only. International shipping is coming soon -- follow us on Instagram @analemma for updates.

**Shipping rates:**

| Order Total      | Shipping Cost    |
|------------------|------------------|
| Under $80 SGD    | $4.50 SGD        |
| $80 SGD and above| Free              |

**Processing time:**
Orders are processed within 1-2 business days (Monday -- Friday, excluding public holidays).

**Delivery time:**
Standard delivery within Singapore takes 3-5 business days after processing.

**Tracking:**
You'll receive a shipping confirmation email with a tracking number once your order is dispatched.

---

### Returns

**Return window:**
We accept returns within 14 days of delivery.

**Conditions for return:**
- Products must be unused, unopened, and in their original packaging.
- **Beauty products** (lip ganache, hair oil, perfumes): Cannot be returned once opened, due to hygiene reasons.
- **Accessories** (charms, pins, pouches) and **handbags**: May be returned if unused and in original condition.
- **Limited edition items**: Final sale. Not eligible for return.

**How to initiate a return:**
Email us at [hello@analemma.sg] with your order number and reason for return. We'll respond within 1-2 business days with return instructions.

**Refund processing:**
Once we receive and inspect your return, we'll process your refund within 5-7 business days. Refunds are issued to the original payment method. Shipping costs are non-refundable.

**Damaged or defective items:**
If your order arrives damaged or defective, contact us within 48 hours of delivery with photos. We'll arrange a replacement or full refund at no extra cost to you.

---

## 8. Contact Page

**URL:** `/pages/contact`

**Page Title:** Get in Touch

---

### Layout Spec

**Section 1: Header**

> **Headline:** We'd Love to Hear From You
>
> **Subline:** Questions, feedback, or just want to say hi? We're here.

**Section 2: Contact Form (Shopify built-in form)**

Fields:
- Name (required)
- Email (required)
- Subject (optional dropdown: General Inquiry / Order Question / Press & Collaboration / Other)
- Message (required, text area)
- Submit button: "Send Message"

**Section 3: Additional Contact Info (beside or below form)**

> **Email:** hello@analemma.sg
>
> **Instagram:** @analemma
>
> **Response time:** We typically reply within 24 hours during business days (Monday -- Friday).

---

## 9. Email Capture

### Popup (Triggered on Homepage)

**Trigger:** Display after 5 seconds on page, or on scroll (50% of page). Show once per visitor. Do not show on mobile if it creates a poor experience -- test and adjust.

**Design:** Clean, brand-aligned. Soft blush or cream background. Product image on one side (Lip Ganache flat lay), copy on the other.

**Copy:**

> **Headline:** Be First.
>
> **Body:** Join the Analemma world and get exclusive early access to new launches, limited drops, and beauty rituals -- before anyone else.
>
> **Input placeholder:** Enter your email
>
> **Button:** I'm In
>
> **Small text below button:** No spam. Just beauty. Unsubscribe anytime.

---

### Footer Email Signup

**Integrated into footer (all pages).**

**Copy:**

> **Headline:** Stay in the Loop
>
> **Body:** New launches, behind-the-scenes, and exclusive offers -- straight to your inbox.
>
> **Input placeholder:** Your email address
>
> **Button:** Subscribe

---

### Post-Signup Confirmation (Thank You Message / Email)

> **On-page message after submit:** Welcome to Analemma. Beautiful things are coming your way.
>
> **Confirmation email subject line:** You're in. Welcome to Analemma.
>
> **Email body:** Thank you for joining us. You'll be the first to know about new launches, limited editions, and the little details that make Analemma, Analemma. In the meantime, follow us on Instagram @analemma for daily beauty and behind-the-scenes moments. — The Analemma Team

---

## 10. SEO Meta Data

### Homepage

**Meta title:** Analemma | Intentional Luxury Beauty & Accessories | Vegan

**Meta description:** Analemma is a vegan luxury beauty and accessories brand. Shop dessert-scented lip ganache, niche perfumes, handcrafted bags, and accessories made with intention. Based in Singapore.

---

### Collection: Sweet Treat (Lip Ganache)

**Meta title:** Sweet Treat Lip Ganache | Dessert-Scented Vegan Lipstick | Analemma

**Meta description:** Five shades of vegan lip ganache, each named for a dessert and scented to match. Rich, creamy pigment in Raspberry Coulis, Strawberry Jam, Hot Cocoa, Maraschino Cherry, and Tiramisu. Shop now.

---

### Collection: Sunday Rituals

**Meta title:** Sunday Rituals Hair Oil | Vegan Hair Care | Analemma

**Meta description:** Lightweight, nourishing vegan hair oil designed to turn your routine into a ritual. Botanically formulated for shine, softness, and the kind of morning you look forward to.

---

### Collection: Niche Perfumes

**Meta title:** Niche Perfumes | Vegan Eau de Parfum | Analemma

**Meta description:** Five niche fragrances for women who want a scent that's theirs. Vegan, cruelty-free eau de parfum in 15ml and 100ml. Meenakshi, Birthday Cake, Moonchild, Enrosadira, and more.

---

### Collection: Accessories

**Meta title:** Accessories | Bag Charms, Enamel Pins, Pouches | Analemma

**Meta description:** Playful, handcrafted vegan accessories from Analemma. Beaded fruit bag charms, floral enamel pins, cross-woven makeup pouches, and metallic lip balm charms. Small joys, big personality.

---

### Collection: Handbags

**Meta title:** Vegan Handbags | Beaded & Cross-Woven Leather | Analemma

**Meta description:** Statement handbags made without leather, without compromise. Handcrafted beaded bags and cross-woven vegan leather bags designed for women who carry their world with intention.

---

### Collection: Limited Edition

**Meta title:** Limited Edition | Exclusive Drops | Analemma

**Meta description:** Limited edition beauty and lifestyle pieces from Analemma. Once they're gone, they're gone. Shop exclusive drops, collaborations, and one-time creations.

---

### About Page

**Meta title:** About Analemma | Beauty as Ritual | Vegan Luxury from Singapore

**Meta description:** Analemma is beauty made with intention. Learn about our philosophy, our commitment to vegan luxury, and why we believe your routine deserves to feel like a ritual.

---

## Appendix: Shopify Setup Notes

### Bundle Pricing (Lip Balm Charm)

The $18 bundle price for Lip Balm Charms (when purchased with any Lip Ganache) can be implemented via:
- **Shopify Scripts** (Shopify Plus) -- auto-discount at checkout
- **Bundle app** (e.g., Bundler, Bold Bundles) -- create a bundle product
- **Automatic discount** -- set up a discount code or automatic discount that triggers when both product types are in cart

Recommendation: Use an automatic discount with condition "Cart contains product from Sweet Treat collection + Lip Balm Charm" → discount $4 on the charm.

### Product Variants

Perfumes should be set up as **single products with size variants**:
- Variant 1: 15ml -- $43
- Variant 2: 100ml -- $180

All other products are single-variant (one SKU per product).

### Image Requirements

For Be Yours theme, recommended image specs:
- **Product images:** Square (1:1), minimum 2048 x 2048px
- **Hero banners:** 16:9 or 21:9, minimum 2560 x 1440px
- **Collection banners:** 3:1 ratio, minimum 1800 x 600px
- **Lifestyle images:** Various ratios, minimum 1200px on shortest side

Each product should have:
- 1 hero shot (clean, white/neutral background)
- 1-2 lifestyle/styled shots
- 1 detail/texture shot (especially for handbags and accessories)

### Color Palette (for theme customization)

Suggested brand colors for Be Yours theme settings:
- **Primary:** Jaipur Pink (#D4838F or similar)
- **Secondary:** Deep Plum (#4A1942 or similar)
- **Accent:** Warm Gold (#C9A96E or similar)
- **Background:** Soft Cream (#FFF8F0 or similar)
- **Text:** Rich Charcoal (#2D2926 or similar)

*(Confirm exact hex codes with the founder's brand guidelines)*

### Apps to Consider

- **Email capture:** Klaviyo (email + popup) or Shopify Forms
- **Reviews:** Judge.me or Loox (photo reviews)
- **Bundle discount:** Bundler or automatic discount
- **Instagram feed:** Instafeed or Shopify's native IG integration
- **SEO:** No app needed initially -- manual meta tags are sufficient

---

*Blueprint created February 2026. All copy is launch-ready. Update TBD 5th perfume when finalized.*
