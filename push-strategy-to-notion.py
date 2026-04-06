#!/usr/bin/env python3
"""Push 25 Orders/Day Strategy + Timetable to Notion pages."""
import json, time, requests, os

TOKEN = open(os.path.expanduser("~/.openclaw/workspace/.notion-token")).read().strip()
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}
BASE = "https://api.notion.com/v1"

STRATEGY_PAGE = "33aeab20-0eed-8192-bfe0-c64d860e2526"
TIMETABLE_PAGE = "33aeab20-0eed-8143-abdc-f7d5e9d5b8dc"

def rt(text, bold=False):
    """Rich text helper."""
    obj = {"text": {"content": text[:2000]}}
    if bold:
        obj["annotations"] = {"bold": True}
    return obj

def h2(text):
    return {"type": "heading_2", "heading_2": {"rich_text": [rt(text)]}}

def h3(text):
    return {"type": "heading_3", "heading_3": {"rich_text": [rt(text)]}}

def p(text, bold=False):
    if len(text) <= 2000:
        return {"type": "paragraph", "paragraph": {"rich_text": [rt(text, bold)]}}
    # Split long text
    chunks = []
    while text:
        chunks.append(rt(text[:2000]))
        text = text[2000:]
    return {"type": "paragraph", "paragraph": {"rich_text": chunks}}

def bullet(text):
    return {"type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [rt(text[:2000])]}}

def todo(text, checked=False):
    return {"type": "to_do", "to_do": {"rich_text": [rt(text[:2000])], "checked": checked}}

def divider():
    return {"type": "divider", "divider": {}}

def callout(text, emoji="💡"):
    return {"type": "callout", "callout": {"rich_text": [rt(text[:2000])], "icon": {"emoji": emoji}}}

def table_row(cells):
    return {"type": "table_row", "table_row": {"cells": [[rt(c)] for c in cells]}}

def append_blocks(page_id, blocks):
    """Append blocks in batches of 100."""
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i+100]
        r = requests.patch(
            f"{BASE}/blocks/{page_id}/children",
            headers=HEADERS,
            json={"children": batch}
        )
        if r.status_code != 200:
            print(f"ERROR batch {i//100}: {r.status_code} {r.text[:200]}")
        else:
            print(f"OK batch {i//100}: {len(batch)} blocks")
        time.sleep(0.5)

# ============================================================
# STRATEGY DOC
# ============================================================
print("=== Pushing Strategy Doc ===")
strategy_blocks = [
    h2("1. The Math: Reverse-Engineering 25 Orders/Day"),
    p("Before building a content plan, we need to know exactly how much traffic, engagement, and conversion each channel must deliver. Analemma's product range (lip ganaches ~SGD 22-35, fragrances ~SGD 55-85, accessories ~SGD 15-25) sits in the sweet spot for both TikTok impulse buys and Instagram aspirational discovery."),
    
    h3("Target Split by Channel"),
    bullet("TikTok Shop: 12-15 orders/day (50-60%) -- Lower friction, in-app checkout, beauty is #1 category"),
    bullet("Instagram → Website: 6-8 orders/day (25-30%) -- Higher AOV, brand-building, repeat buyers"),
    bullet("Direct / Organic / Repeat: 3-5 orders/day (15-20%) -- Email, WhatsApp, returning customers"),
    
    h3("Funnel Math: TikTok Shop (Target: 13 orders/day)"),
    bullet("Video Impressions: 65,000-100,000 daily"),
    bullet("3-Second Views (40-60% hook rate): 26,000-60,000"),
    bullet("Product Click / CTR (1.0-2.0%): 650-2,000"),
    bullet("Product Page View (70% of clicks): 455-1,400"),
    bullet("Add to Cart (8-12%): 36-168"),
    bullet("Purchase (35-50% cart→order): 13 orders"),
    
    h3("Funnel Math: Instagram → Website (Target: 7 orders/day)"),
    bullet("Feed/Reels/Stories Impressions: 25,000-40,000"),
    bullet("Engagement (3-5%): 750-2,000"),
    bullet("Link Click (1.5-3.0%): 375-1,200"),
    bullet("Website Landing (60-70%): 225-840"),
    bullet("Add to Cart (7-8%): 16-67"),
    bullet("Purchase (mobile CVR 1.8-2.5%): 7 orders"),
    p("Key bottleneck: the IG-to-website handoff. Mobile site speed, one-tap checkout (Shop Pay / Apple Pay), and retargeting are critical to prevent 60-80% cart abandonment."),
    
    divider(),
    h2("2. Three-Phase Battle Plan"),
    p("54 days from April 13 to June 5, divided into three phases with distinct objectives."),
    bullet("Phase 1: Foundation (Apr 13-27, 15 days) -- Build infrastructure, seed content, recruit creators. Target: 2-5 orders/day"),
    bullet("Phase 2: Acceleration (Apr 28-May 18, 21 days) -- Scale content, launch TikTok LIVE, run first ads. Target: 8-15 orders/day"),
    bullet("Phase 3: Optimization (May 19-Jun 5, 18 days) -- Double down on winners, retargeting, push to 25/day. Target: 20-25 orders/day"),
    
    divider(),
    h2("Phase 1: Foundation (Apr 13-27)"),
    p("Build the machine before turning it on. No ads, no LIVE yet. Pure setup and content seeding."),
    
    h3("Infrastructure Checklist"),
    todo("Register Analemma on TikTok Shop Singapore Seller Center (seller-sg.tiktok.com)"),
    todo("Upload full product catalog: all lip ganaches (Sweet Treat Collection), Volume I fragrances, accessories"),
    todo("Professional product photos + lifestyle shots optimized for TikTok (vertical 9:16, first 0.5s must hook)"),
    todo("Set up TikTok Shop Affiliate Program: open plan at 10% commission for creators"),
    todo("Instagram Shopping: ensure product tags working on all posts/Reels/Stories, linked to analemma.shop"),
    todo("Website: add Shop Pay / Apple Pay / Google Pay for one-tap mobile checkout"),
    todo("Install Meta Pixel + TikTok Pixel on analemma.shop for retargeting"),
    todo("Set up Klaviyo for abandoned cart email sequence (3-email flow)"),
    todo("Create press kit for creators: product images, brand story one-pager, sample request form"),
    
    h3("TikTok Content Pillars (film 2-3/day)"),
    bullet("GRWM / Get Ready With Me: 15-45s, casual, face-to-camera. 3x/week"),
    bullet("Texture / ASMR: 10-20s, close-up product shots. 2x/week"),
    bullet("Founder Story: 30-60s, personal narrative. 1x/week"),
    bullet("Before/After Lip: 15-30s, split screen. 2x/week"),
    bullet("'What I'd wear' styling: 20-40s, outfit + lip pairing. 2x/week"),
    bullet("Trend Participation: 15-30s, trending audio. 2-3x/week"),
    
    h3("Instagram Content Pillars"),
    bullet("Reels (hero content): 15-60s cinematic product moments -- Discovery, reach, new followers"),
    bullet("Carousel Posts: 5-10 slides, educational or storytelling -- Saves, shares, depth"),
    bullet("Stories: Daily, 5-8 frames -- Engagement, polls, behind-the-scenes, link stickers"),
    bullet("Static Grid Posts: Styled product photography -- Brand aesthetic, trust-building"),
    
    h3("Creator Recruitment (target: 10-15 creators by end of Phase 1)"),
    bullet("Identify 30-50 Singapore-based micro-creators (5K-50K followers) in beauty, lifestyle, GRWM niches"),
    bullet("Check engagement quality: 5-15% like-to-view ratio, real comments (not just emojis)"),
    bullet("DM outreach: lead with genuine compliment, offer free product + 10% affiliate commission"),
    bullet("Priority: creators who already post lip content, fragrance reviews, or 'local brand' content"),
    bullet("Also reach out to 3-5 mid-tier creators (50K-150K) for potential paid collabs in Phase 2"),
]
append_blocks(STRATEGY_PAGE, strategy_blocks)

# Phase 1 Day-by-Day
print("--- Phase 1 Day-by-Day ---")
phase1_days = [
    h3("Phase 1: Day-by-Day Plan (Apr 13-27)"),
    callout("Week 1: Setup + First Content (Apr 13-19)", "📅"),
    
    p("Day 1 (Sun Apr 13): Register TikTok Shop SG. Upload 5 hero SKUs. Audit IG (business account, catalog, bio link). Install TikTok+Meta Pixel. Set up Klaviyo abandoned cart flow.", True),
    p("Day 2 (Mon Apr 14): Upload remaining SKUs. Set up affiliate program (10% open plan). Film first 3 TikToks: GRWM, texture ASMR, lip swatch. Post IG Reel teaser. Add Shop Pay/Apple Pay. Test mobile checkout flow."),
    p("Day 3 (Tue Apr 15): Post first TikTok (GRWM). Research and shortlist 30 micro-creators. DM 10 creators. IG Carousel: 'The story behind Analemma'. Photograph missing products (vertical, lifestyle)."),
    p("Day 4 (Wed Apr 16): Post TikTok #2 (texture/ASMR). Continue outreach (10 more DMs). Film 2 more TikToks. IG Stories: founder Q&A. Engage 20 target accounts. Set up UTM tracking."),
    p("Day 5 (Thu Apr 17): Post TikTok #3 (lip before/after). Send product samples to first 3-5 confirmed creators. IG Reel: '3 lip shades for 3 vibes'. Prepare creator press kit."),
    p("Day 6 (Fri Apr 18) ⭐ BATCH FILMING: Film 5-7 TikToks in one session. Post 1. IG static: Sweet Treat Collection flat-lay. Ship creator kits. Order additional inventory if needed."),
    p("Day 7 (Sat Apr 19): Post TikTok #4 (styling). Continue outreach (remaining 10). IG Stories: weekend GRWM. Week 1 review: TikTok analytics, IG insights. Adjust content."),
    
    callout("Week 2: Content Rhythm + Creator Activation (Apr 20-27)", "📅"),
    p("Day 8 (Sun Apr 20): Post TikTok #5 (founder story -- Meenakshi fragrance origin). IG Carousel: 'Why I don't put fragrance notes on packaging'. Review week 1 data."),
    p("Day 9 (Mon Apr 21): Post TikTok #6 (trend). Monitor first affiliate creator content. IG Reel: fragrance reveal -- 'Birthday Cake smells like...' Follow up with silent creators."),
    p("Day 10 (Tue Apr 22) ⭐ BATCH FILMING: Post TikTok #7. Film 5-7 videos. Test fragrance content. IG Stories: 'Day in my life'. Research TikTok LIVE format."),
    p("Day 11 (Wed Apr 23): Post TikTok #8. Duet/stitch creator content. Test 'reply to comment' format. IG static: Yukinohana hero shot. Set up TikTok Shop promotions."),
    p("Day 12 (Thu Apr 24): Post TikTok #9. Film comparison content (Analemma vs drugstore). IG Reel: 'The shade that sells out first'. Prep TikTok ad budget for Phase 2."),
    p("Day 13 (Fri Apr 25) ⭐ BATCH FILMING: Post TikTok #10. Film Phase 2 launch buffer. IG Stories: 'pick your shade' quiz. Finalize TikTok LIVE schedule."),
    p("Day 14 (Sat Apr 26): Post TikTok #11. IG Stories: weekend beauty ritual. Reel: recut best TikTok. Phase 1 retrospective: creators activated, total views, first orders."),
    p("Day 15 (Sun Apr 27): Post TikTok #12. Batch film 5-7 for Phase 2 buffer. Prep LIVE talking points. IG Carousel: 'What Analemma means'. Confirm all systems ready for Phase 2."),
]
append_blocks(STRATEGY_PAGE, phase1_days)

# Phase 2
print("--- Phase 2 ---")
phase2_blocks = [
    divider(),
    h2("Phase 2: Acceleration (Apr 28 - May 18)"),
    p("The machine is built. Phase 2: more content, first TikTok LIVEs, first paid ads, scaling creator output."),
    
    h3("Phase 2 Key Actions"),
    bullet("Increase TikTok posting to 2-3x/day (own + creator reposts)"),
    bullet("Launch TikTok LIVE sessions: 2-3x/week, 30-60 minutes each"),
    bullet("Start TikTok Shop Ads: SGD 30-50/day on Spark Ads (boost best organic content)"),
    bullet("Start Meta Ads: SGD 20-40/day on Instagram Reels ads driving to analemma.shop"),
    bullet("Scale creator program to 15-20 active affiliates"),
    bullet("Launch first flash sale or bundle promotion on TikTok Shop"),
    bullet("Begin retargeting: website visitors, IG engagers, TikTok video viewers"),
    bullet("Email sequence: welcome flow for new subscribers, post-purchase upsell"),
    
    h3("TikTok LIVE Playbook"),
    bullet("When: Tue/Thu 8-9pm SGT + Sat 2-3pm SGT (peak SG TikTok hours)"),
    bullet("Format: GRWM / swatch party / 'help me pick a shade' interactive"),
    bullet("Duration: 30-60 minutes minimum (algorithm rewards longer sessions)"),
    bullet("Promotions: LIVE-exclusive discount code (e.g., LIVE10 for 10% off)"),
    bullet("Engagement: Call out commenters by name, answer questions, run polls"),
    bullet("Product pins: Pin 2-3 products, rotate every 10-15 minutes"),
    bullet("Goal: 5-15 orders per LIVE session by end of Phase 2"),
    
    h3("Week 3 (Apr 28 - May 4)"),
    p("Day 16 (Mon Apr 28): Post 2 TikToks. Launch Spark Ads on best video (SGD 30/day). Start Meta retargeting (SGD 20/day). IG Reel + Stories."),
    p("Day 17 (Tue Apr 29): Post 2 TikToks. FIRST TikTok LIVE (8pm, 30-45 min) -- casual GRWM, pin 2 products. IG Stories: LIVE teaser + replay."),
    p("Day 18 (Wed Apr 30): Post 2-3 TikToks. Review LIVE metrics. Duet creator content. IG Carousel: '5 ways to wear [shade]'."),
    p("Day 19 (Thu May 1): Post 2 TikToks. Second LIVE (8pm). Swatch party format -- every shade, viewers vote. IG Reel."),
    p("Day 20 (Fri May 2) ⭐ BATCH: Post 2. Film 5-7 for next week. IG Stories: Friday beauty Q&A. Review first week of ads."),
    p("Day 21 (Sat May 3): Post 2. Third LIVE (2pm). Launch flash promo: buy 2 lip ganaches get accessory free. IG Stories: LIVE clips."),
    p("Day 22 (Sun May 4): Post 1-2. IG Carousel: 'Why I named this fragrance Enrosadira.' Week 3 review: target 5-8 orders/day."),
    
    h3("Week 4 (May 5-11)"),
    bullet("Scale Spark Ads to SGD 50/day on top 2-3 creatives"),
    bullet("LIVE schedule: Tue 8pm, Thu 8pm, Sat 2pm (3 LIVEs)"),
    bullet("Try mystery bundle offer during Thursday LIVE"),
    bullet("Launch Meta lookalike audience ad (SGD 30/day) based on purchasers"),
    bullet("Target: 10+ active affiliate creators posting"),
    bullet("End-of-week target: 8-12 orders/day consistently"),
    
    h3("Week 5 (May 12-18)"),
    bullet("Try collab LIVE with a creator (split screen) on Tuesday"),
    bullet("Launch mid-month bundle promo on TikTok Shop"),
    bullet("Kill any ad below 1.5x ROAS. Scale winners by 20-30%"),
    bullet("Active creators target: 15-20"),
    bullet("End-of-week target: 12-15 orders/day consistently"),
    bullet("Sunday: Phase 2 full retrospective. Top 3 content formats, top 5 creators, best ad, optimal LIVE time"),
]
append_blocks(STRATEGY_PAGE, phase2_blocks)

# Phase 3
print("--- Phase 3 ---")
phase3_blocks = [
    divider(),
    h2("Phase 3: Optimization + Scale to 25/Day (May 19 - Jun 5)"),
    p("Ruthless optimization. By now you know what works. Double down on winners, cut losers."),
    
    h3("Phase 3 Key Actions"),
    bullet("Scale ad spend to SGD 80-150/day across TikTok + Meta (only proven creatives)"),
    bullet("Increase TikTok LIVE to 4-5x/week"),
    bullet("Launch 'Founder's Collection' bundle or limited-edition Artbox exclusive"),
    bullet("Activate 20-25 affiliate creators (volume play)"),
    bullet("Aggressive retargeting: 7-day site visitors, cart abandoners, LIVE viewers"),
    bullet("Email: blast to full list with exclusive offer, abandoned cart at full capacity"),
    bullet("Optimize product pages: A/B test main images, descriptions, pricing anchors"),
    bullet("WhatsApp broadcast for repeat customers"),
    
    h3("Week 6 (May 19-25)"),
    bullet("Launch retargeting for cart abandoners specifically"),
    bullet("Email blast to subscriber list with exclusive code"),
    bullet("Test midday LIVE (Wed 12-1pm). 4 LIVEs total this week"),
    bullet("Scale ads to SGD 100-120/day total"),
    bullet("End-of-week target: 15-18 orders/day"),
    
    h3("Week 7 (May 26 - Jun 1)"),
    bullet("Launch Founder's Pick limited bundle on TikTok Shop"),
    bullet("Email + WhatsApp broadcast for bundle"),
    bullet("5 LIVE sessions this week"),
    bullet("Scale ads to SGD 120-150/day"),
    bullet("End-of-week target: 18-22 orders/day"),
    
    h3("Week 8: Final Push (Jun 2-5)"),
    bullet("All channels at maximum. 3 TikToks/day + daily LIVE"),
    bullet("Last-chance email for any active promotion"),
    bullet("WhatsApp blast to repeat customers"),
    bullet("Jun 5: Target day -- 25 orders. Full 54-day retrospective"),
    
    divider(),
    h2("3. Budget Estimate"),
    callout("Estimated total: SGD 4,500-8,540 over 54 days. At 25 orders/day × SGD 30-45 AOV = SGD 750-1,125/day revenue (SGD 22,500-33,750/month). ROI-positive by end of Phase 2.", "💰"),
    
    bullet("Phase 1 (15 days): SGD 350-550 -- Creator samples only, no ads"),
    bullet("Phase 2 (21 days): SGD 1,600-2,940 -- Spark Ads SGD 630-1,050 + Meta SGD 420-840 + Samples SGD 200-400 + Paid collabs SGD 300-600"),
    bullet("Phase 3 (18 days): SGD 2,550-5,050 -- Spark Ads SGD 1,080-2,700 + Meta SGD 720-900 + Samples SGD 200-400 + Paid collabs SGD 500-1,000"),
    bullet("Tools (Klaviyo etc.): SGD 150 total"),
    
    divider(),
    h2("4. Weekly KPI Dashboard"),
    p("Track every Sunday. Behind on orders but ahead on views = conversion problem. Behind on views = content volume/distribution problem."),
    
    h3("Phase 1 Targets"),
    bullet("TikTok Daily Impressions: 5K-15K"),
    bullet("TikTok Videos/Day: 1-2"),
    bullet("Active Affiliate Creators: 3-5"),
    bullet("TikTok Shop Orders/Day: 1-3"),
    bullet("IG Reels/Week: 2-3"),
    bullet("Website Orders/Day: 1-2"),
    bullet("Total Orders/Day: 2-5"),
    
    h3("Phase 2 Targets"),
    bullet("TikTok Daily Impressions: 30K-60K"),
    bullet("TikTok Videos/Day: 2-3"),
    bullet("TikTok LIVE/Week: 2-3"),
    bullet("Active Creators: 10-15"),
    bullet("TikTok Shop Orders/Day: 5-8"),
    bullet("IG Reels/Week: 3-4, Link Clicks/Day: 50-100"),
    bullet("Website Orders/Day: 3-5"),
    bullet("Total Orders/Day: 8-15, Blended CAC: <SGD 12, ROAS: >1.5x"),
    
    h3("Phase 3 Targets"),
    bullet("TikTok Daily Impressions: 65K-100K"),
    bullet("TikTok Videos/Day: 3, LIVE/Week: 4-5"),
    bullet("Active Creators: 20-25"),
    bullet("TikTok Shop Orders/Day: 12-15"),
    bullet("IG Reels/Week: 4-5, Link Clicks/Day: 100-200"),
    bullet("Website Orders/Day: 8-10"),
    bullet("Total Orders/Day: 20-25, Blended CAC: <SGD 10, ROAS: >2.0x"),
    
    divider(),
    h2("5. Risk Mitigations"),
    bullet("TikTok Shop registration delayed: Apply Day 1. SG takes 1-3 business days. Drive traffic to analemma.shop meanwhile."),
    bullet("Low TikTok views initially: Normal. Algorithm takes 10-15 videos. Don't stop posting. Test hooks aggressively in Phase 1."),
    bullet("Creators don't convert: Track affiliate GMV weekly. Replace underperformers. Quality > quantity."),
    bullet("Fragrance hard to sell on TikTok: Lead with lip ganaches (visual, demo-friendly). Fragrance as upsell in bundles and LIVEs."),
    bullet("Cart abandonment: 3-email flow over 48 hours. Exit-intent popup with 5-10% discount. One-tap checkout."),
    bullet("Inventory stockout: Monitor daily. Restock when any SKU hits 50% of projected 2-week supply."),
    bullet("Bali trip overlap: Pre-batch 10-15 TikToks. Schedule IG posts. LIVE from Bali = great content angle."),
    
    divider(),
    h2("6. Non-Negotiable Daily Habits"),
    callout("Total daily: 2-3 hours (non-LIVE days), 3-4 hours (LIVE days)", "⚡"),
    todo("Post at least 1 TikTok with product tag (no exceptions, even on bad days)"),
    todo("Post 5-8 IG Story frames (10 minutes)"),
    todo("Respond to every comment and DM within 2 hours"),
    todo("Check TikTok Seller Center + Shopify dashboard"),
    todo("Engage with 10-15 accounts in your niche (genuine comments)"),
]
append_blocks(STRATEGY_PAGE, phase3_blocks)

print("\n=== Strategy doc DONE ===\n")

# ============================================================
# TIMETABLE DOC
# ============================================================
print("=== Pushing Timetable Doc ===")

timetable_blocks = [
    h2("Part 1: Master Task Breakdown"),
    p("Every activity decomposed into atomic subtasks. Times are for a solo founder with phone, laptop, and products."),
    
    h3("A. TikTok Content Creation"),
    p("Each TikTok requires four steps. Batching (filming 5 in one session) is 3x more efficient. Total per video: 45 min single, 26 min batched. Batch day (5 videos): 90 min shooting + edit 1/day over the week."),
    bullet("A1 Idea and Hook (5 min / 3 min batched): Write hook line, decide format, pick product, note trending audio"),
    bullet("A2 Setup and Shoot (20 min / 8 min batched): Ring light or natural light, position phone, film 2-3 takes"),
    bullet("A3 Edit (15 min / 10 min batched): Trim clips in CapCut, text overlays, sync audio, add captions"),
    bullet("A4 Post and Tag (5 min): Write caption, hashtags, tag TikTok Shop product, choose cover frame, post/schedule"),
    
    h3("B. Instagram Content Creation"),
    p("Daily IG minimum: Stories (10 min) + 1 repurposed Reel (10 min) = 20 min. Carousel days add 30-45 min."),
    bullet("B1 Reel (repurposed TikTok) -- 10 min: Re-export without watermark, adjust caption, product tags"),
    bullet("B2 Reel (IG-original) -- 40-50 min: Concept + shoot + edit + post (more polished than TikTok)"),
    bullet("B3 Carousel Post -- 30-45 min: Write 5-10 slides in Canva, export, caption, product tags"),
    bullet("B4 Static Post -- 10-15 min: Select/edit photo, write caption, product tag"),
    bullet("B5 Stories (5-8 frames) -- 10-15 min: Quick phone photos/videos, text/polls/stickers"),
    
    h3("C. Creator and Influencer Pipeline"),
    bullet("C1 Research creators -- 30 min per 10: Search TikTok/IG by hashtag, check profiles, note engagement"),
    bullet("C2 Vet creators -- 3 min per creator: Check last 10 videos for like-to-view ratio (want 5-15%)"),
    bullet("C3 Write outreach DM -- 5 min per creator: Personalize template with specific compliment"),
    bullet("C4 Send DMs -- 2 min per creator"),
    bullet("C5 Pack sample kit -- 10 min per kit: Select products, print thank-you card, branded packaging"),
    bullet("C6 Ship or deliver -- 10 min per batch of 3-5: Label, book courier"),
    bullet("C7 Follow up -- 3 min per creator: Gentle nudge + content ideas"),
    bullet("C8 Track performance -- 10 min per weekly review: TikTok Shop Affiliate dashboard GMV, clicks, orders"),
    
    h3("D. TikTok Shop Setup (One-Time)"),
    bullet("D1 Register seller account -- 30 min: seller-sg.tiktok.com, ACRA upload, verify identity"),
    bullet("D2 Upload product catalog -- 15 min per SKU: name, description, price, images (min 3), category, weight"),
    bullet("D3 Set up affiliate program -- 15 min: Seller Center > Affiliate > Open Plan, 10% commission"),
    bullet("D4 Set up promotions -- 20 min: Discount codes, bundle deals, flash sale config"),
    bullet("D5 Product photography -- 60-90 min: Missing photos in 9:16 vertical, lifestyle context"),
    
    h3("E. Website and Tech Setup (One-Time)"),
    bullet("E1 Install TikTok Pixel -- 20 min: Shopify > TikTok channel > connect > enable > test"),
    bullet("E2 Install Meta Pixel -- 20 min: Shopify > FB and IG channel > connect > verify"),
    bullet("E3 Add express checkout -- 15 min: Enable Shop Pay, Apple Pay, Google Pay"),
    bullet("E4 Test mobile checkout flow -- 15 min: Place test order, time the flow, fix friction"),
    bullet("E5 Set up Klaviyo -- 60-90 min: Install, connect Shopify, build 3-email abandoned cart + welcome"),
    bullet("E6 UTM tracking setup -- 30 min: Create UTM links for TikTok bio, IG bio, Stories. Tracking spreadsheet"),
    
    h3("F. Paid Advertising"),
    bullet("F1 Set up TikTok Ads account -- 20 min: Connect to Seller Center, add payment, set budget cap"),
    bullet("F2 Create Spark Ad -- 15 min per ad: Select best TikTok, boost, set targeting (SG, F 18-40, beauty)"),
    bullet("F3 Set up Meta ad account -- 15 min: Business Suite, connect IG + pixel, add payment"),
    bullet("F4 Create IG Reels ad -- 15 min per ad: Select Reel, set objective, target, budget"),
    bullet("F5 Create retargeting campaign -- 20 min: Custom audience (7-day visitors, cart abandoners), urgency ad"),
    bullet("F6 Daily ad review -- 10 min: CTR, CPC, ROAS. Pause below 1.5x ROAS after 3 days. Scale winners 20-30%"),
    
    h3("G. TikTok LIVE Sessions"),
    p("Total per LIVE: 75-110 min. Done as separate evening block on LIVE days."),
    bullet("G1 Prep talking points -- 10 min: 5-7 bullets, products to feature, promo code"),
    bullet("G2 Set up space -- 10 min: Ring light, mount, products laid out, tidy background, test audio"),
    bullet("G3 Go LIVE -- 30-60 min: Pin products, engage comments, demo, call out usernames, mention promo"),
    bullet("G4 Post-LIVE review -- 10 min: Screenshot metrics (peak viewers, engagement, orders), save replay"),
    bullet("G5 Clip and repost -- 15-20 min: Export 2-3 best moments, edit into standalone TikToks/Reels"),
    
    h3("H. Daily Engagement and Community"),
    p("Total daily: 20-30 min. Non-negotiable. Can be split across pockets of the day."),
    bullet("H1 Reply to TikTok comments -- 5-10 min: Every comment. Prioritize questions + purchase-intent"),
    bullet("H2 Reply to IG comments and DMs -- 5-10 min"),
    bullet("H3 Proactive engagement -- 10 min: Visit 10-15 niche accounts, leave genuine comments"),
    bullet("H4 Repost UGC -- 5 min when applicable: Repost to Stories, thank via DM"),
    
    h3("I. Analytics and Review"),
    bullet("I1 Daily quick check -- 5 min: TikTok Seller Center + Shopify: orders, revenue, top product"),
    bullet("I2 Weekly deep review -- 30-45 min: All data, 3 learnings + 3 actions"),
]
append_blocks(TIMETABLE_PAGE, timetable_blocks)

# Phase 1 Week 1 Day-by-Day with time blocks
print("--- Timetable Phase 1 ---")
phase1_tt = [
    divider(),
    h2("Part 2: Day-by-Day 2-Hour Timetable"),
    p("Each day fits within 120 minutes unless marked as a LIVE day (+60-75 min evening). Batch filming days marked with ⭐."),
    
    callout("PHASE 1, WEEK 1: Setup + First Content (Apr 13-19)", "📅"),
    
    h3("Day 1 -- Sunday, April 13: TikTok Shop registration + website tech"),
    bullet("0-30 min: D1 -- TikTok Shop registration (seller-sg.tiktok.com, ACRA upload)"),
    bullet("30-50 min: E1 -- Install TikTok Pixel (Shopify > TikTok channel > test)"),
    bullet("50-65 min: E2 -- Install Meta Pixel (Shopify > FB and IG > verify)"),
    bullet("65-80 min: E3 -- Add express checkout (Shop Pay, Apple Pay, Google Pay)"),
    bullet("80-95 min: E4 -- Test mobile checkout (place test order, time flow, fix friction)"),
    bullet("95-120 min: Audit IG profile (business account, catalog linked, bio link, photo)"),
    
    h3("Day 2 -- Monday, April 14: Product catalog + first content"),
    bullet("0-60 min: D2 -- Upload first 5 hero SKUs to TikTok Shop (12 min/SKU)"),
    bullet("60-65 min: D3 -- Set up affiliate program (10%, invitation note)"),
    bullet("65-70 min: A1 -- Plan GRWM TikTok. Hook: 'The lip colour strangers compliment you on'"),
    bullet("70-90 min: A2 -- Shoot TikTok #1 (ring light, 2-3 takes applying lip ganache)"),
    bullet("90-100 min: B5 -- IG Stories (5 frames: BTS of setup, poll, TikTok Shop teaser)"),
    bullet("100-120 min: H1+H2+H3 -- Engagement (reply comments/DMs, comment on 10 niche accounts)"),
    
    h3("Day 3 -- Tuesday, April 15: Post first TikTok + start creator research"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #1 (CapCut, text overlay, captions, product tag)"),
    bullet("15-45 min: C1 -- Creator research batch 1 (search #sgbeauty #tiktokmakeupsg, shortlist 10)"),
    bullet("45-65 min: C2+C3+C4 -- Vet and DM first 5 creators"),
    bullet("65-95 min: B3 -- IG Carousel (Story behind Analemma in Canva)"),
    bullet("95-105 min: B5 -- IG Stories (share TikTok + carousel teaser)"),
    bullet("105-120 min: H1+H2+H3 -- Engagement"),
    
    h3("Day 4 -- Wednesday, April 16: TikTok #2 + more outreach"),
    bullet("0-5 min: A1 -- Plan texture/ASMR video (slow-mo ganache swipe)"),
    bullet("5-25 min: A2 -- Shoot TikTok #2 (close-up angles, good lighting)"),
    bullet("25-40 min: A3+A4 -- Edit and post TikTok #2 (ASMR audio, product tag)"),
    bullet("40-60 min: C2+C3+C4 -- Vet next 5 creators + send DMs"),
    bullet("60-85 min: D2 -- Upload remaining SKUs (5 more at 5 min each)"),
    bullet("85-95 min: B5 -- IG Stories (Founder Q&A, BTS)"),
    bullet("95-120 min: H1+H2+H3 + I1 + E6 (Engagement + analytics + UTM setup)"),
    
    h3("Day 5 -- Thursday, April 17: TikTok #3 + pack creator samples"),
    bullet("0-5 min: A1 -- Plan before/after lip video (bare → one-swipe payoff)"),
    bullet("5-25 min: A2 -- Shoot TikTok #3 (split-screen or transition)"),
    bullet("25-40 min: A3+A4 -- Edit and post (transition, product tag)"),
    bullet("40-70 min: C5 -- Pack 3-5 creator sample kits (products, thank-you card, packaging)"),
    bullet("70-80 min: B1 -- IG Reel (repurpose TikTok #1 or #2)"),
    bullet("80-95 min: B5 -- IG Stories (share Reel, tease creator packages going out)"),
    bullet("95-120 min: H1+H2+H3 -- Engagement (check creator DM responses)"),
    
    h3("Day 6 -- Friday, April 18 ⭐ BATCH FILMING DAY"),
    bullet("0-10 min: A1 x5 -- Plan batch (write hooks for 5 videos, lay out products + outfits)"),
    bullet("10-80 min: A2 x5 batched -- Batch shoot 5 TikToks (change outfits, different products/angles)"),
    bullet("80-90 min: A3+A4 -- Edit and post TikTok #4 (best from batch)"),
    bullet("90-100 min: C6 -- Ship creator kits (label, book Grab Express or Ninja Van)"),
    bullet("100-110 min: B5 -- IG Stories (BTS of batch filming, flat-lay of creator packages)"),
    bullet("110-120 min: H1+H2+H3 -- Engagement"),
    p("✅ You now have 4 pre-filmed TikToks banked for next week. Edit 1 per day."),
    
    h3("Day 7 -- Saturday, April 19: Buffer post + week 1 review"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #5 (styling/outfit pairing from batch)"),
    bullet("15-40 min: D2 -- Upload final SKUs (fragrances + remaining accessories)"),
    bullet("40-60 min: C2+C3+C4 -- Creator outreach batch 3 (vet + DM final 10)"),
    bullet("60-70 min: B5 -- IG Stories (weekend GRWM, casual lifestyle)"),
    bullet("70-85 min: H1+H2+H3 -- Engagement (extra on weekend)"),
    bullet("85-120 min: I2 -- Week 1 Review (TikTok analytics, IG insights, hooks that worked, creator pipeline, 3 learnings)"),
]
append_blocks(TIMETABLE_PAGE, phase1_tt)

# Week 2
print("--- Timetable Week 2 ---")
week2_tt = [
    callout("PHASE 1, WEEK 2: Content Rhythm + Creator Activation (Apr 20-27)", "📅"),
    
    h3("Day 8 -- Sunday, April 20: Founder story + Klaviyo"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #6 (founder story: Meenakshi fragrance origin)"),
    bullet("15-70 min: E5 -- Set up Klaviyo email flows (install, connect Shopify, 3-email abandoned cart + welcome)"),
    bullet("70-80 min: B5 -- IG Stories (BTS of brand origin, share TikTok)"),
    bullet("80-95 min: H1+H2+H3 -- Engagement (engage all comments from week 1 TikToks)"),
    bullet("95-120 min: C7 -- Creator follow-ups (DM creators who received samples but haven't posted)"),
    
    h3("Day 9 -- Monday, April 21: Trend + ad account setup"),
    bullet("0-10 min: Research trending sounds (TikTok Discover/Creative Center)"),
    bullet("10-25 min: A3+A4 -- Edit and post TikTok #7 (trend video)"),
    bullet("25-40 min: Monitor creator content (check if affiliates posted, engage)"),
    bullet("40-70 min: B2 -- IG Reel (original): Fragrance reveal -- 'Birthday Cake smells like...'"),
    bullet("70-80 min: B5 -- IG Stories (repost creator content with credit, Reel teaser)"),
    bullet("80-95 min: H1+H2+H3+H4 -- Replies + engage + repost UGC"),
    bullet("95-120 min: F1+F3 -- Set up TikTok Ads Manager + Meta Ads Manager (payment methods)"),
    
    h3("Day 10 -- Tuesday, April 22 ⭐ BATCH FILMING DAY"),
    bullet("0-5 min: A4 -- Post TikTok #8 (from buffer)"),
    bullet("5-60 min: A1 x5 + A2 x5 batched -- Batch film 5 new TikToks (include fragrance storytelling)"),
    bullet("60-75 min: Research TikTok LIVE (watch 3-4 SG beauty LIVEs, note format)"),
    bullet("75-90 min: B5 -- IG Stories (day in my life featuring products naturally)"),
    bullet("90-105 min: H1+H2+H3 -- Engagement"),
    bullet("105-120 min: D4 -- TikTok Shop promo (set up 10% new-customer discount)"),
    
    h3("Day 11 -- Wednesday, April 23: Creator press kit + IG hero"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #9"),
    bullet("15-40 min: Create creator press kit (brand one-pager in Canva, images folder, sample form, affiliate instructions)"),
    bullet("40-55 min: B4 -- IG static (Yukinohana hero shot with storytelling caption, product tags)"),
    bullet("55-65 min: B5 -- IG Stories (share post, poll: 'what's your go-to lip colour mood?')"),
    bullet("65-90 min: C7 + C1 -- Follow up 5 creators + research 5 mid-tier (50K-150K) for Phase 2"),
    bullet("90-105 min: H1+H2+H3 -- Engagement"),
    bullet("105-120 min: I1 -- Analytics (orders, top TikTok, IG link clicks, note which hooks work)"),
    
    h3("Day 12 -- Thursday, April 24: Comparison content + ad prep"),
    bullet("0-5 min: A4 -- Post TikTok #10 (from buffer)"),
    bullet("5-25 min: A1+A2 -- Film comparison TikTok (Analemma vs drugstore, texture/longevity side-by-side)"),
    bullet("25-40 min: A3 -- Edit comparison video (split screen, text callouts)"),
    bullet("40-55 min: ID best ad creatives (rank all TikToks by views + engagement, top 3 = Spark Ad candidates)"),
    bullet("55-75 min: B1 + B5 -- IG Reel (repurpose best TikTok) + Stories (pick-your-shade quiz)"),
    bullet("75-90 min: H1+H2+H3 -- Engagement"),
    bullet("90-105 min: G1 -- Plan LIVE format (write first LIVE talking points, pick 3 products, plan GRWM)"),
    bullet("105-120 min: Prep ad drafts (draft Spark Ad settings ready for Day 16)"),
    
    h3("Day 13 -- Friday, April 25 ⭐ BATCH FILMING DAY"),
    bullet("0-10 min: A1 x5 -- Plan batch (hooks for Phase 2 launch week buffer, more polished/sales-oriented)"),
    bullet("10-75 min: A2 x5 batched -- Film (1 GRWM, 1 all-shades swatch, 1 reply-to-comment, 1 trend, 1 fragrance)"),
    bullet("75-90 min: A3+A4 -- Edit and post TikTok #11"),
    bullet("90-100 min: B5 -- IG Stories (BTS of batch day + customer reviews)"),
    bullet("100-120 min: H1+H2+H3 + affiliate dashboard check + follow up silent creators"),
    
    h3("Day 14 -- Saturday, April 26: Weekend + Phase 2 prep"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #12 (casual weekend vibes from batch)"),
    bullet("15-45 min: B3 -- IG Carousel ('Why I don't put fragrance notes on packaging' in Canva)"),
    bullet("45-60 min: B5 -- IG Stories (weekend beauty ritual, lifestyle)"),
    bullet("60-75 min: H1+H2+H3 -- Weekend round (people more active on weekends)"),
    bullet("75-120 min: I2 -- Phase 1 Retrospective (views, orders, creator status, best formats, finalize Phase 2 ad strategy/LIVE schedule/budget)"),
    
    h3("Day 15 -- Sunday, April 27: Final Phase 1 day + system check"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok from buffer"),
    bullet("15-40 min: LIVE practice run (record mock LIVE 10 min, watch back, note pacing/energy)"),
    bullet("40-65 min: B3 + B5 -- IG Carousel ('What Analemma means') + Stories (Phase 2 hype teaser)"),
    bullet("65-80 min: System check (all pixels firing? checkout smooth? inventory? SKUs live? affiliate active?)"),
    bullet("80-95 min: H1+H2+H3 -- Engagement"),
    bullet("95-120 min: Content calendar (map Phase 2 week 3: which videos when, LIVE days, Reels schedule)"),
]
append_blocks(TIMETABLE_PAGE, week2_tt)

# Phase 2+3 Templates and Weekly Cadence
print("--- Timetable Phase 2+3 ---")
phase23_tt = [
    divider(),
    callout("PHASE 2, WEEK 3: Ads Launch + First LIVEs (Apr 28 - May 4). LIVE days add 60-75 min evening block.", "🔥"),
    
    h3("Day 16 -- Monday, April 28: Launch ads"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #14 (sales-oriented hook from buffer)"),
    bullet("15-30 min: F2 -- Launch Spark Ad #1 (best TikTok, SG F 18-40 beauty, SGD 30/day)"),
    bullet("30-50 min: F5 -- Launch Meta retargeting (custom audience IG engagers 30 days, SGD 20/day)"),
    bullet("50-60 min: A1+A2 -- Film quick TikTok (reply-to-comment or trending sound)"),
    bullet("60-75 min: B1 + B5 -- IG Reel + Stories"),
    bullet("75-90 min: H1+H2+H3 -- Engagement"),
    bullet("90-105 min: C7+C8 -- Creator management (affiliate dashboard, follow up, content ideas)"),
    bullet("105-120 min: I1 -- Analytics (ads approved? pixels firing? first metrics?)"),
    
    h3("Day 17 -- Tuesday, April 29: FIRST LIVE 🔴"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #15"),
    bullet("15-25 min: A4 -- Post TikTok #16 (two posts today)"),
    bullet("25-40 min: B5 -- IG Stories LIVE teaser (countdown, products preview, follow reminder)"),
    bullet("40-55 min: G1+G2 -- LIVE prep (5 talking points, lay out 3 products, test audio)"),
    bullet("55-75 min: H1+H2+H3 -- Engagement before LIVE"),
    bullet("75-85 min: F6 -- Ad check (Spark + Meta CTR after 24 hours)"),
    bullet("EVENING 8-9pm: G3 -- LIVE (30-45 min GRWM, pin 2 products, engage comments, code LIVE10)"),
    bullet("POST-LIVE: G4+G5 -- Screenshot metrics, save replay, clip 1-2 best moments"),
    
    h3("Days 18-22 continue same pattern (see strategy doc for details)"),
    
    divider(),
    h2("Repeating Templates (Weeks 4-8)"),
    
    h3("Template A: Standard Day (non-LIVE, non-batch)"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok #1 from buffer"),
    bullet("15-25 min: A4 -- Post TikTok #2 (pre-edited, 2 posts/day minimum)"),
    bullet("25-40 min: B1 or B4 -- IG content (repurpose TikTok as Reel or post static, rotate)"),
    bullet("40-55 min: B5 -- IG Stories (5-8 frames: product moments, polls, BTS, creator reposts)"),
    bullet("55-70 min: H1+H2+H3 -- Reply all comments/DMs + engage 10 accounts"),
    bullet("70-85 min: C7+C8 or F6 -- Alternate: check creators OR review ads"),
    bullet("85-100 min: Variable (batch prep / new outreach / promo setup / planning)"),
    bullet("100-120 min: I1 + content plan tomorrow + inventory check"),
    
    h3("Template B: LIVE Day"),
    bullet("0-15 min: A3+A4 -- Edit and post TikTok"),
    bullet("15-25 min: A4 -- Post TikTok #2"),
    bullet("25-40 min: B5 -- IG Stories LIVE teaser (countdown + what you'll show)"),
    bullet("40-55 min: G1+G2 -- LIVE prep (talking points, product layout, test setup)"),
    bullet("55-70 min: H1+H2+H3 -- Engagement"),
    bullet("70-85 min: F6 or C7+C8 -- Review ads or creators"),
    bullet("85-100 min: B1 or B3 -- IG Reel or carousel"),
    bullet("100-120 min: I1 + tomorrow prep"),
    bullet("EVENING: G3+G4+G5 -- LIVE 45-60 min + metrics + clip 1-2 highlights (60-75 min total)"),
    
    h3("Template C: Batch Filming Day (Fridays)"),
    bullet("0-10 min: A1 x5 -- Plan (write 5 hooks, lay out products and outfits)"),
    bullet("10-70 min: A2 x5 -- Batch shoot 5 TikToks (change outfits between, different angles)"),
    bullet("70-85 min: A3+A4 -- Edit and post 1 TikTok (or LIVE clip)"),
    bullet("85-100 min: B5 -- IG Stories (BTS of batch filming day)"),
    bullet("100-110 min: F6 -- Weekly ad performance review"),
    bullet("110-120 min: H1+H2+H3 -- Engagement"),
    
    divider(),
    h2("Phase 3 Daily Template (adds 1 extra quick-film TikTok)"),
    bullet("0-15 min: A3+A4 -- Post TikTok #1 from buffer"),
    bullet("15-25 min: A4 -- Post TikTok #2 (pre-edited)"),
    bullet("25-35 min: A1+A2 -- Quick-film TikTok #3 (1-take reply/trend/duet, don't over-edit)"),
    bullet("35-50 min: B1 + B5 -- IG Reel (repurpose) + Stories"),
    bullet("50-65 min: H1+H2+H3 -- Engagement"),
    bullet("65-80 min: F6 -- Ad management (review, scale winners, kill losers, new retargeting)"),
    bullet("80-95 min: C7+C8 -- Creator management (affiliate GMV, follow ups, onboard new)"),
    bullet("95-120 min: Strategic work (email campaign / WhatsApp blast / promo setup / inventory / planning)"),
    
    divider(),
    h2("Quick Reference: Daily Time Budget"),
    callout("Core daily commitment: 2 hours. LIVE days add 60-75 min evening. Batch Fridays shift to mostly filming. Everything fits 120 min with the templates.", "⏰"),
]
append_blocks(TIMETABLE_PAGE, phase23_tt)

print("\n=== Timetable doc DONE ===")
print(f"\nStrategy: https://www.notion.so/33aeab200eed8192bfe0c64d860e2526")
print(f"Timetable: https://www.notion.so/33aeab200eed8143abdcf7d5e9d5b8dc")
