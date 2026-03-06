#!/usr/bin/env python3
import json, os, urllib.request

TOKEN = open(os.path.expanduser("~/.openclaw/workspace/.notion-token")).read().strip()
BACKOFFICE_ID = "31beab20-0eed-81e0-a888-e004cd1d0f97"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def h2(t): return {"type":"heading_2","heading_2":{"rich_text":[{"text":{"content":t}}]}}
def h3(t): return {"type":"heading_3","heading_3":{"rich_text":[{"text":{"content":t}}]}}
def bold_para(l,t): return {"type":"paragraph","paragraph":{"rich_text":[{"text":{"content":l},"annotations":{"bold":True}},{"text":{"content":t}}]}}
def todo(t): return {"type":"to_do","to_do":{"rich_text":[{"text":{"content":t}}],"checked":False}}
def divider(): return {"type":"divider","divider":{}}
def callout(t,e="🗺️"): return {"type":"callout","callout":{"rich_text":[{"text":{"content":t}}],"icon":{"emoji":e}}}

# Create page with first batch
batch1 = [
    callout("Agent roadmaps: next week (Mar 7-15) + end-of-March goals. Created by Janet."),
    h2("🔵 Content Agent"),
    bold_para("March Goal: ", "18+ posts published. Content calendar running 2 weeks ahead."),
    h3("Week 1: Mar 7-15 (LAUNCH WEEK)"),
    todo("Execute daily launch countdown posts (Mon-Sat)"),
    todo("Daily Stories (BTS, countdown stickers, polls)"),
    todo("Launch day reel -- Mar 15, 9 AM SGT"),
    todo("Draft Week 2 content calendar by Mar 13"),
    h3("Mar 16-31"),
    todo("3 posts/week minimum (Mon/Wed/Fri)"),
    todo("1 Reel per week"),
    todo("First UGC repost"),
    todo("Draft April content calendar by Mar 28"),
    divider(),
    h2("🟢 Research Agent"),
    bold_para("March Goal: ", "Complete competitive landscape. 30 influencer targets. Weekly trend digest."),
    h3("Week 1: Mar 7-15"),
    todo("Competitor analysis -- DONE"),
    todo("Influencer shortlist -- DONE"),
    todo("Research: trending lip formats globally"),
    todo("Research: SG beauty market size 2026"),
    h3("Mar 16-31"),
    todo("Expand influencer pipeline to 30 targets"),
    todo("Competitor pricing benchmark"),
    todo("Weekly trend digest every Monday"),
    todo("Research: Artbox booth strategy"),
    todo("Research: Korea COSMOBEAUTY prep"),
    divider(),
    h2("🔍 SEO Agent"),
    bold_para("March Goal: ", "All pages SEO-optimized. 4 blog posts. Baseline keyword tracking."),
    h3("Week 1: Mar 7-15"),
    todo("Keyword research: lip ganache, vegan lip care SG"),
    todo("Meta titles + descriptions for all product pages"),
    todo("Meta titles + descriptions for all collection pages"),
    todo("Blog post 1: launch announcement"),
]

data = {
    "parent": {"page_id": BACKOFFICE_ID},
    "icon": {"emoji": "🗺️"},
    "properties": {"title": [{"text": {"content": "Agent Roadmaps: March 2026"}}]},
    "children": batch1,
}

req = urllib.request.Request("https://api.notion.com/v1/pages", data=json.dumps(data).encode(), headers=headers, method="POST")
resp = urllib.request.urlopen(req)
result = json.loads(resp.read())
page_id = result["id"]
print("Page created:", page_id)

# Batch 2: SEO cont + PR + Writer
batch2 = [
    h3("SEO: Mar 16-31"),
    todo("Blog: 'Best vegan lip products Singapore 2026'"),
    todo("Blog: 'Lip ganache vs lip gloss vs lip oil'"),
    todo("Blog: 'Why scented beauty products make you more present'"),
    todo("Internal linking audit"),
    todo("Baseline keyword tracking setup"),
    todo("Submit sitemap to Google Search Console"),
    divider(),
    h2("📣 PR Agent"),
    bold_para("March Goal: ", "30 PR boxes sent. 10 influencer outreach emails. 3 media pitches."),
    h3("Week 1: Mar 7-15"),
    todo("Draft influencer outreach email template"),
    todo("Draft gifting brief (PR box contents + guidelines)"),
    todo("3 personalized emails for Phase 1 influencers"),
    todo("Media pitch for SG publications (Her World, Nylon SG, Zula)"),
    h3("Mar 16-31"),
    todo("Send all 30 PR boxes"),
    todo("Send 10 influencer outreach emails"),
    todo("Send 3 media pitches"),
    todo("Follow-up sequence (5 days after initial)"),
    todo("Track responses in Notion"),
    todo("Draft Artbox press announcement"),
    divider(),
    h2("✍️ Writer Agent"),
    bold_para("March Goal: ", "All product descriptions finalized. Brand story locked. Email templates ready."),
    h3("Week 1: Mar 7-15"),
    todo("Polish all 5 lip ganache descriptions on Shopify"),
    todo("Write launch email"),
    todo("Write 'About Analemma' page copy"),
    todo("Write PR box insert card copy"),
    h3("Mar 16-31"),
    todo("Product descriptions for all accessories"),
    todo("Sunday Rituals Hair Oil description"),
    todo("Welcome email sequence (3 emails)"),
    todo("Artbox event copy (booth signage, flyer, social)"),
    todo("'Thank you for your order' email copy"),
]

req2 = urllib.request.Request(
    f"https://api.notion.com/v1/blocks/{page_id}/children",
    data=json.dumps({"children": batch2}).encode(),
    headers=headers, method="PATCH"
)
urllib.request.urlopen(req2)
print("Batch 2 appended")

# Batch 3: Shopify + Janet
batch3 = [
    divider(),
    h2("🛒 Shopify Agent"),
    bold_para("March Goal: ", "Store launch-ready. All products live. Checkout optimized. Post-launch bugs squashed."),
    h3("Week 1: Mar 7-15"),
    todo("Audit all product pages (images, descriptions, pricing, variants)"),
    todo("Test checkout flow end-to-end"),
    todo("Verify all collections populated and navigable"),
    todo("Fix header white space issue"),
    todo("Verify HitPay payment integration"),
    h3("Mar 16-31"),
    todo("Apply SEO meta from SEO Agent to all pages"),
    todo("Post-launch bug sweep (mobile, tablet, desktop)"),
    todo("Set up branded order notification emails"),
    todo("Add blog posts to Shopify blog"),
    todo("Weekly analytics: traffic, conversion, bounce rate"),
    divider(),
    h2("🟣 Janet (Orchestrator)"),
    bold_para("March Goal: ", "Smooth launch. All agents delivering. Sunshine's ops cognitive load near zero."),
    h3("Week 1: Mar 7-15"),
    todo("Review all agent outputs before they reach Sunshine"),
    todo("Coordinate cross-agent deps (SEO→Shopify, Writer→PR, Research→PR)"),
    todo("Daily launch countdown check-in"),
    todo("Store 100% ready by Mar 14"),
    h3("Mar 16-31"),
    todo("Weekly agent performance review"),
    todo("Triage tasks to correct agent"),
    todo("Maintain backoffice + ticket board"),
    todo("Artbox coordination plan"),
    todo("Korea trip research coordination"),
]

req3 = urllib.request.Request(
    f"https://api.notion.com/v1/blocks/{page_id}/children",
    data=json.dumps({"children": batch3}).encode(),
    headers=headers, method="PATCH"
)
urllib.request.urlopen(req3)
print("Batch 3 appended")
print("All roadmaps pushed!")
