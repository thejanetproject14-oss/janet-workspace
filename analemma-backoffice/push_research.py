#!/usr/bin/env python3
import json, os, urllib.request

TOKEN = open(os.path.expanduser("~/.openclaw/workspace/.notion-token")).read().strip()
ANALEMMA_ID = "30beab20-0eed-80a0-80a1-cf6a2ad73acd"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def h2(text):
    return {"type":"heading_2","heading_2":{"rich_text":[{"text":{"content":text}}]}}

def h3(text):
    return {"type":"heading_3","heading_3":{"rich_text":[{"text":{"content":text}}]}}

def para(text):
    return {"type":"paragraph","paragraph":{"rich_text":[{"text":{"content":text}}]}}

def bullet(text):
    return {"type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"text":{"content":text}}]}}

def divider():
    return {"type":"divider","divider":{}}

def callout(text, emoji="🟢"):
    return {"type":"callout","callout":{"rich_text":[{"text":{"content":text}}],"icon":{"emoji":emoji}}}

# Page 1: Competitor Analysis
comp_children = [
    callout("Created by Research Agent (ANA-170). Reviewed by Janet."),
    h2("Philippines"),
    h3("Colourette Cosmetics -- 333K followers"),
    bullet("Multi-use lip & cheek products, $5-11 USD. Strong community, Filipino skin tone focus."),
    h3("Sunnies Face -- 400K+ followers"),
    bullet("FluffMattes, Lip Treats. $7-11 USD. 'Effortless beauty', cruelty-free, minimalist aesthetic."),
    h3("BLK Cosmetics -- 250K+ followers"),
    bullet("Soft Matte Mousse, PillowMattes. $6-12 USD. Urban/edgy, inclusive shades."),
    h3("Happy Skin -- 150K+ followers"),
    bullet("Tinted lip balms, multi-functional. $7-13 USD. 'Made for morenas' pioneer."),
    divider(),
    h2("Indonesia"),
    h3("Dear Me Beauty -- 800K+ followers"),
    bullet("Lip coats, matte lip creams. $3-6 USD. Collaboration strategy, affordable luxury."),
    h3("Wardah -- 2.8M+ followers"),
    bullet("Matte lip creams, lip tints. $2.40-5 USD. Halal-certified, K-beauty influenced."),
    divider(),
    h2("Malaysia"),
    h3("Velvet Vanity -- 80K followers"),
    bullet("Liquid lipsticks, Peptide Glo Lip Oil (bestseller). $5.50-12 USD. Lip care + color hybrid."),
    h3("Zhuco (North Borneo) -- 40K followers"),
    bullet("Liquid lipsticks, rainbow highlighters. $4.40-10 USD. Regional cultural identity differentiator."),
    divider(),
    h2("Thailand"),
    h3("Cathy Doll -- 200K followers"),
    bullet("Bear Lip Moist, Jelly Lip Tints. $4.50-8 USD. Cute/kawaii aesthetic, innovative textures."),
    h3("Nongchat Cosmetics -- 120K followers"),
    bullet("Lip gloss, traditional Thai beauty. $3.40-7 USD. Heritage beauty story."),
    divider(),
    h2("Global Brands in SEA"),
    bullet("Glossier ($14-22): 'Skin first' positioning, community-driven."),
    bullet("Rare Beauty ($16-20): Purpose-driven, mental health advocacy."),
    bullet("Fenty Beauty ($19-25): Radical inclusivity, innovation."),
    divider(),
    h2("Key Takeaways for Analemma"),
    bullet("Multi-functionality is key -- lip products that double as cheek colors win."),
    bullet("Price sweet spot: $5-12 USD for indie brands."),
    bullet("Cultural relevance beats global generic."),
    bullet("Innovative textures (jelly, mousse, ganache) create differentiation."),
    bullet("Nobody occupies the Ayurveda x K-beauty intersection. Category is open."),
    bullet("Community building > traditional advertising at this stage."),
]

data = {
    "parent": {"page_id": ANALEMMA_ID},
    "icon": {"emoji": "🔍"},
    "properties": {"title": [{"text": {"content": "Competitor Analysis: Indie Lip Brands in SEA"}}]},
    "children": comp_children,
}

req = urllib.request.Request("https://api.notion.com/v1/pages", data=json.dumps(data).encode(), headers=headers, method="POST")
resp = urllib.request.urlopen(req)
result = json.loads(resp.read())
print("Competitor analysis pushed:", result["id"])

# Page 2: Influencer Shortlist
inf_children = [
    callout("Created by Research Agent (ANA-171). Reviewed by Janet."),
    h2("Phase 1: Core Beauty (Launch Week)"),
    h3("@beautybudget.sg -- 50K followers"),
    bullet("Drugstore beauty reviews. 7% engagement. Budget-conscious audience = perfect for accessible pricing."),
    h3("@leannelow -- 57.5K followers"),
    bullet("Fashion, travel, beauty. Singapore-based. Professional content quality."),
    h3("@graceful.living -- 48K followers"),
    bullet("Minimalist living, sustainable products. 6.2% engagement. Values ingredient transparency."),
    divider(),
    h2("Phase 2: Lifestyle Expansion (Month 1)"),
    h3("@minimalist.mind -- 39K followers"),
    bullet("Intentional living. 6.5% engagement. 'Art of noticing' messaging alignment."),
    h3("@singaporeuncovered -- 44K followers"),
    bullet("Hidden gems, local experiences. 7.1% engagement. Singapore pride = local brand story."),
    h3("@homewithharmony -- 41K followers"),
    bullet("Interior design, aesthetic content. 6.3% engagement. Values beautiful packaging."),
    divider(),
    h2("Phase 3: Community Building (Month 2-3)"),
    h3("@plantparent.sg -- 37K followers"),
    bullet("Urban gardening, sustainable living. 7.3% engagement. Natural/botanical ingredients story."),
    h3("@theurbanparent.sg -- 52K followers"),
    bullet("Millennial parenting. 5.8% engagement. Key beauty consumer demographic."),
    h3("@weekendwarrior.sg -- 46K followers"),
    bullet("Weekend getaways, lifestyle. 6.8% engagement. Travel-ready beauty."),
    h3("@expat.diaries.sg -- 35K followers"),
    bullet("Expatriate lifestyle. 5.9% engagement. International audience."),
    divider(),
    h2("Seeding Strategy"),
    bullet("Budget: ~$200-2,000 per post depending on follower count."),
    bullet("SG micro-influencers average 5-7% engagement -- significantly higher than macro."),
    bullet("Focus on authentic long-term partnerships, not one-off posts."),
    bullet("Send 30 PR boxes total. Phase 1 influencers get boxes in launch week."),
]

data2 = {
    "parent": {"page_id": ANALEMMA_ID},
    "icon": {"emoji": "🎯"},
    "properties": {"title": [{"text": {"content": "Influencer Shortlist: SG Beauty Micro-Influencers"}}]},
    "children": inf_children,
}

req2 = urllib.request.Request("https://api.notion.com/v1/pages", data=json.dumps(data2).encode(), headers=headers, method="POST")
resp2 = urllib.request.urlopen(req2)
result2 = json.loads(resp2.read())
print("Influencer shortlist pushed:", result2["id"])
