#!/usr/bin/env python3
import json, os, urllib.request, urllib.error
from datetime import datetime

TOKEN = open(os.path.expanduser("~/.openclaw/workspace/.notion-token")).read().strip()
BOARD_ID = "31beab20-0eed-8121-8f5c-d70671e58b1a"
LOG_ID = "31beab20-0eed-81c1-9b46-ec4172020b6d"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def create_ticket(task, assigned_to, priority, linear_id, ticket_type, due_date=None, notes=""):
    props = {
        "Task": {"title": [{"text": {"content": task}}]},
        "Assigned To": {"select": {"name": assigned_to}},
        "Priority": {"select": {"name": priority}},
        "Status": {"select": {"name": "To Do"}},
        "Type": {"select": {"name": ticket_type}},
        "Linear ID": {"rich_text": [{"text": {"content": linear_id}}]},
        "Notes": {"rich_text": [{"text": {"content": notes}}]},
    }
    if due_date:
        props["Due Date"] = {"date": {"start": due_date}}
    
    data = {
        "parent": {"database_id": BOARD_ID},
        "properties": props,
    }
    req = urllib.request.Request("https://api.notion.com/v1/pages", data=json.dumps(data).encode(), headers=headers, method="POST")
    try:
        resp = urllib.request.urlopen(req)
        result = json.loads(resp.read())
        print(f"✅ {linear_id}: {task[:60]}")
        return result["id"]
    except urllib.error.HTTPError as e:
        print(f"❌ {linear_id}: {e.read().decode()[:200]}")
        return None

def log_activity(agent, action, ticket_id="", details=""):
    data = {
        "parent": {"database_id": LOG_ID},
        "properties": {
            "Activity": {"title": [{"text": {"content": f"[{agent}] {action}"}}]},
            "Agent": {"select": {"name": agent}},
            "Ticket": {"rich_text": [{"text": {"content": ticket_id}}]},
            "Details": {"rich_text": [{"text": {"content": details}}]},
            "Timestamp": {"date": {"start": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")}},
        }
    }
    req = urllib.request.Request("https://api.notion.com/v1/pages", data=json.dumps(data).encode(), headers=headers, method="POST")
    try:
        urllib.request.urlopen(req)
        print(f"  📋 Activity logged for {agent}")
    except urllib.error.HTTPError as e:
        print(f"  ⚠️ Log failed: {e.read().decode()[:100]}")

# Week 1 tickets
tickets = [
    # SEO
    ("Keyword research: lip ganache, tinted lip care, vegan lip products SG", "SEO Agent", "Urgent", "ANA-172", "SEO", "2026-03-10", "Deliver: top 50 keywords with volume + difficulty. Focus on long-tail for new brand."),
    ("Meta titles + descriptions for all product + collection pages", "SEO Agent", "Urgent", "ANA-173", "SEO", "2026-03-13", "Max 60 chars title, 155 chars description. Must include target keyword naturally."),
    ("Blog post: Launch announcement (SEO-optimized)", "SEO Agent", "High", "ANA-174", "Content", "2026-03-14", "800-1200 words. Warm tone. CTA to shop. Link to all 5 lip ganache variants."),
    
    # PR
    ("Draft influencer outreach email template + gifting brief", "PR Agent", "Urgent", "ANA-175", "PR", "2026-03-10", "Template must feel personal, not mass blast. Brief: what's in box, what we ask for, no requirements."),
    ("3 personalized outreach emails for Phase 1 influencers", "PR Agent", "High", "ANA-176", "PR", "2026-03-12", "Use Research Agent's shortlist. Reference something specific about each creator. Under 150 words each."),
    ("Media pitch for SG publications (Her World, Nylon SG, Zula)", "PR Agent", "High", "ANA-177", "PR", "2026-03-13", "Lead with founder story + category creation angle. Not just 'new product launch'."),
    
    # Writer
    ("Polish all 5 lip ganache product descriptions on Shopify", "Writer Agent", "Urgent", "ANA-178", "Copy", "2026-03-12", "Sensory language. Dessert metaphors. Tinted lip ganache -- never lip balm. 100-150 words each."),
    ("Write launch email + About Analemma page copy", "Writer Agent", "Urgent", "ANA-179", "Copy", "2026-03-13", "Launch email: punchy, exciting, link to all shades. About page: brand story, founder, ethos."),
    ("Write PR box insert card copy", "Writer Agent", "High", "ANA-180", "Copy", "2026-03-12", "Small card. 50-80 words max. Warm, personal, like a note from a friend. Not corporate."),
    
    # Shopify
    ("Pre-launch audit: all product pages, checkout, collections", "Shopify Agent", "Urgent", "ANA-181", "Tech", "2026-03-12", "Check: images, descriptions, pricing, variants, mobile responsiveness, checkout flow end-to-end."),
    ("Fix header white space + verify HitPay payment integration", "Shopify Agent", "High", "ANA-182", "Tech", "2026-03-13", "Header logo_position: top-center causing white space. HitPay: test a real transaction if possible."),
    
    # Research
    ("Expand influencer pipeline: SG micro-influencers Phase 2 + MY/ID targets", "Research Agent", "Medium", "ANA-183", "Research", "2026-03-14", "Extend shortlist to 30 total. Add Malaysia + Indonesia creators. Format same as Phase 1 shortlist."),
    ("Research: trending lip product formats globally Q1 2026", "Research Agent", "Medium", "ANA-184", "Research", "2026-03-14", "Lip oils, tinted serums, lip stains -- what's gaining traction? TikTok + Sephora data preferred."),
    
    # Content
    ("Launch countdown content: Mar 10-14 daily posts", "Content Agent", "Urgent", "ANA-185", "Content", "2026-03-10", "5 posts: carousel (shades reveal), reel (texture/scent), static (quote), reel (GRWM), carousel (ingredients). Include captions."),
    ("Launch day content: Mar 15 reel + stories", "Content Agent", "Urgent", "ANA-186", "Content", "2026-03-14", "Hero launch reel. All 5 shades. 30-45 seconds. Stories: countdown, link sticker, swipe-ups. Have copy ready by Mar 14 EOD."),
]

print("Creating tickets...\n")
ticket_ids = []
for t in tickets:
    tid = create_ticket(*t)
    if tid:
        ticket_ids.append((t[0], t[1], t[3], tid))

print(f"\nCreated {len(ticket_ids)} tickets.")

# Log activity for each agent
print("\nLogging activity...")
agents_briefed = set()
for name, agent, linear_id, tid in ticket_ids:
    if agent not in agents_briefed:
        log_activity("Janet", f"Briefed {agent} -- Week 1 tasks assigned", linear_id, f"Tickets assigned and visible on backoffice. Agent to begin immediately.")
        agents_briefed.add(agent)

print("\nDone! Backoffice will reflect all tickets on next refresh.")
