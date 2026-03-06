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

def para(label, text):
    return {"type":"paragraph","paragraph":{"rich_text":[
        {"text":{"content":label},"annotations":{"bold":True}},
        {"text":{"content":text}}
    ]}}

def divider():
    return {"type":"divider","divider":{}}

def callout(text, emoji="🔵"):
    return {"type":"callout","callout":{"rich_text":[{"text":{"content":text}}],"icon":{"emoji":emoji}}}

children = [
    callout("Created by Content Agent (ANA-168, ANA-169). Reviewed by Janet."),
    h2("Monday Mar 10 -- Colour Hunting Carousel"),
    para("Type: ", "Carousel (5 slides) | Time: 7:30 PM SGT"),
    para("Idea: ", "\"Colour hunting in my kitchen\" -- each slide shows the food inspiration behind each shade."),
    para("Caption: ", "spent the afternoon colour hunting in my kitchen and honestly? this is where the magic happens. these aren't just shades -- they're little love letters to the colours that make us pause and smile. launching saturday. my heart is doing somersaults."),
    para("CTA: ", "Which shade matches your current mood? Tell me in the comments"),
    divider(),
    h2("Tuesday Mar 11 -- Behind the Scenes Reel"),
    para("Type: ", "Reel (30-45 sec) | Time: 12:30 PM SGT"),
    para("Idea: ", "Hands mixing, testing colours on arm, the 'aha!' moments. Process footage."),
    para("CTA: ", "Save this post if you're as obsessed with the process as I am"),
    divider(),
    h2("Wednesday Mar 12 -- Product Flat Lay"),
    para("Type: ", "Static Post | Time: 8:00 PM SGT"),
    para("Idea: ", "Dreamy flat lay with all 5 shades + their food inspiration. Each shade gets a personality line: raspberry coulis (bold but not shouty), strawberry jam (sweet with an edge), hot cocoa (cozy confidence), maraschino cherry (playful pop), tiramisu (sophisticated whisper)."),
    para("CTA: ", "Drop your top 2 must-haves below"),
    divider(),
    h2("Thursday Mar 13 -- GRWM Mood Reel"),
    para("Type: ", "Reel (45-60 sec) | Time: 6:30 PM SGT"),
    para("Idea: ", "Different shades for different moods/times of day. Morning coffee = Hot Cocoa. Lunch date = Strawberry Jam. Creative session = Raspberry Coulis. Evening drinks = Tiramisu. Anytime happiness = Maraschino Cherry."),
    para("CTA: ", "Which vibe are you choosing? Comment your pick!"),
    divider(),
    h2("Friday Mar 14 -- 24-Hour Countdown"),
    para("Type: ", "Carousel (3 slides) | Time: 10:00 AM SGT"),
    para("Idea: ", "Close-up swatches, packaging details, website preview. Urgency without desperation."),
    para("CTA: ", "Set those alarms for tomorrow 9 AM! Link in bio"),
    divider(),
    h2("Saturday Mar 15 -- LAUNCH DAY"),
    para("Type: ", "Reel (60 sec) | Time: 9:00 AM SGT"),
    para("Idea: ", "Dramatic reveal. All shades. Celebration energy. SHE'S HERE. SHE'S LIVE. SHE'S YOURS."),
    para("CTA: ", "Shop now at analemma.shop! Which shade first?"),
    divider(),
    h2("5 Standalone Launch Captions"),
    para("1. ", "plot twist: your lips can now smell like dessert and look like art at the same time. sweet treat lip ganache collection. because regular tinted lip products are cute, but scented ones that actually nourish? that's next level."),
    para("2. ", "me: I'll just do a quick swatch test. also me: *applies all 5 shades on different fingers and stares at them for 20 minutes*. this collection hits different. literally can't pick a favourite and honestly? good. that's what sets are for."),
    para("3. ", "raspberry coulis just entered the chat and said 'I'm THAT girl.' bold but not overwhelming. tinted lip ganache that knows its worth. vegan, scented, ready to be your new signature."),
    para("4. ", "confession: I've been carrying around tiramisu for three days now and every time I reapply, I get a little hit of happiness. that's the thing about scented lip ganache -- it's not just what people see, it's what you experience."),
    para("5. ", "hot cocoa lip ganache on a rainy afternoon = the coziest plot armor possible. some days you need armour. some days you need softness. today? you need both. and maybe a little chocolate scent to complete the vibe."),
]

data = {
    "parent": {"page_id": ANALEMMA_ID},
    "icon": {"emoji": "📅"},
    "properties": {"title": [{"text": {"content": "Launch Week Content Calendar (Mar 10-15)"}}]},
    "children": children,
}

req = urllib.request.Request(
    "https://api.notion.com/v1/pages",
    data=json.dumps(data).encode(),
    headers=headers,
    method="POST",
)
resp = urllib.request.urlopen(req)
result = json.loads(resp.read())
print("Content calendar pushed:", result["id"])
