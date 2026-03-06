#!/usr/bin/env python3
"""
agent_update.py -- Agent self-update helper
Usage:
  python3 agent_update.py start  <notion_page_id> <linear_id> <agent_name> <description>
  python3 agent_update.py done   <notion_page_id> <linear_id> <agent_name> <description> [details]
  python3 agent_update.py block  <notion_page_id> <linear_id> <agent_name> <reason>

Example:
  python3 agent_update.py start "31beab20-0eed-xxxx" "ANA-172" "SEO Agent" "Keyword research for lip ganache"
  python3 agent_update.py done  "31beab20-0eed-xxxx" "ANA-172" "SEO Agent" "Keyword research complete" "Delivered 50 keywords to Notion page XYZ"
"""
import sys, json, urllib.request, urllib.error

BACKOFFICE = "https://analemma-backoffice.vercel.app"

def post(url, data):
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers={"Content-Type": "application/json"}, method="POST")
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP {e.code}: {e.read().decode()[:200]}")
        return None

def patch(url, data):
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers={"Content-Type": "application/json"}, method="PATCH")
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP {e.code}: {e.read().decode()[:200]}")
        return None

def update_ticket(page_id, status):
    result = patch(f"{BACKOFFICE}/api/tickets/{page_id}", {"status": status})
    if result and result.get("ok"):
        print(f"✅ Ticket {page_id} → {status}")
    return result

def log_activity(agent, activity, ticket, details="", activity_type=""):
    data = {"agent": agent, "activity": activity, "ticket": ticket}
    if details: data["details"] = details
    if activity_type: data["type"] = activity_type
    result = post(f"{BACKOFFICE}/api/activity", data)
    if result and result.get("id"):
        print(f"📋 Activity logged")
    return result

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print(__doc__)
        sys.exit(1)

    action = sys.argv[1]
    page_id = sys.argv[2]
    linear_id = sys.argv[3]
    agent = sys.argv[4]
    description = sys.argv[5]
    details = sys.argv[6] if len(sys.argv) > 6 else ""

    if action == "start":
        update_ticket(page_id, "In Progress")
        log_activity(agent, f"Started {linear_id}: {description}", linear_id, details)

    elif action == "done":
        update_ticket(page_id, "Janet Review")
        log_activity(agent, f"Completed {linear_id}: {description}", linear_id, details)

    elif action == "block":
        log_activity(agent, f"Blocked on {linear_id}: {description}", linear_id, details)
        print(f"⚠️  Escalate to Janet via sessions_send")

    else:
        print(f"Unknown action: {action}. Use start, done, or block.")
        sys.exit(1)
