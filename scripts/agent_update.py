#!/usr/bin/env python3
"""
agent_update.py -- Agent self-update helper
SOP: Every agent MUST call this at task start and task completion.

Usage:
  python3 agent_update.py start  <notion_page_id> <linear_id> <agent_name> "<description>"
  python3 agent_update.py done   <notion_page_id> <linear_id> <agent_name> "<description>" "<notion_output_url>" ["<details>"]
  python3 agent_update.py block  <notion_page_id> <linear_id> <agent_name> "<reason>"

Examples:
  python3 agent_update.py start "31beab20-xxxx" "ANA-172" "Percy" "Starting keyword research"

  python3 agent_update.py done "31beab20-xxxx" "ANA-172" "Percy" "Keyword research complete" \
    "https://www.notion.so/ANA-172-Keyword-Research-31beab20xxxx" \
    "Delivered 55 keywords across 4 categories"

  python3 agent_update.py block "31beab20-xxxx" "ANA-172" "Percy" "Cannot access Shopify API"

Output URL format: https://www.notion.so/<page-title>-<page-id-no-dashes>
"""
import sys, json, urllib.request, urllib.error

BACKOFFICE = "https://analemma-backoffice.vercel.app"

def notion_url(page_id: str) -> str:
    """Convert a Notion page ID to its URL."""
    clean = page_id.replace("-", "")
    return f"https://www.notion.so/{clean}"

def post(url, data):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"❌ POST {url} HTTP {e.code}: {e.read().decode()[:200]}")
        return None

def patch(url, data):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"}, method="PATCH"
    )
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"❌ PATCH {url} HTTP {e.code}: {e.read().decode()[:200]}")
        return None

def update_ticket(page_id, status, output_url=None):
    body = {"status": status}
    if output_url:
        body["outputUrl"] = output_url
    result = patch(f"{BACKOFFICE}/api/tickets/{page_id}", body)
    if result and result.get("ok"):
        print(f"✅ Ticket → {status}" + (f" | output linked" if output_url else ""))
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
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(1)

    action      = sys.argv[1]
    page_id     = sys.argv[2]
    linear_id   = sys.argv[3]
    agent       = sys.argv[4]
    description = sys.argv[5] if len(sys.argv) > 5 else ""

    if action == "start":
        update_ticket(page_id, "In Progress")
        log_activity(agent, f"Started {linear_id}: {description}", linear_id, "", "System")

    elif action == "done":
        if len(sys.argv) < 7:
            print("❌ 'done' requires a Notion output URL as argument 6")
            print("   Usage: agent_update.py done <page_id> <linear_id> <agent> <description> <notion_url> [details]")
            sys.exit(1)
        output_url = sys.argv[6]
        details    = sys.argv[7] if len(sys.argv) > 7 else ""
        update_ticket(page_id, "Janet Review", output_url)
        log_activity(
            agent,
            f"Completed {linear_id}: {description}",
            linear_id,
            f"Output: {output_url}" + (f"\n{details}" if details else ""),
            "System"
        )
        print(f"🔗 Output URL attached: {output_url}")
        print(f"⏳ Ticket moved to Janet Review -- awaiting Janet's check before Sunshine sees it")

    elif action == "block":
        log_activity(agent, f"Blocked on {linear_id}: {description}", linear_id, "", "System")
        print(f"⚠️  Escalate to Janet via sessions_send")

    else:
        print(f"Unknown action: {action}. Use start, done, or block.")
        sys.exit(1)
