#!/usr/bin/env python3
"""
find_ticket.py -- Look up a Notion page ID by Linear ID
Usage: python3 find_ticket.py ANA-172
Returns: notion_page_id (for use with agent_update.py)
"""
import sys, json, os, urllib.request

TOKEN = open(os.path.expanduser("~/.openclaw/workspace/.notion-token")).read().strip()
BOARD_ID = "31beab20-0eed-8121-8f5c-d70671e58b1a"

def find_ticket(linear_id):
    req = urllib.request.Request(
        f"https://api.notion.com/v1/databases/{BOARD_ID}/query",
        data=json.dumps({"page_size": 100}).encode(),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
        method="POST"
    )
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    
    for page in data.get("results", []):
        lid = page["properties"].get("Linear ID", {}).get("rich_text", [{}])
        if lid and lid[0].get("text", {}).get("content", "") == linear_id:
            task = page["properties"].get("Task", {}).get("title", [{}])[0].get("text", {}).get("content", "")
            status = page["properties"].get("Status", {}).get("select", {}).get("name", "")
            print(f"Found: {linear_id}")
            print(f"  Notion ID: {page['id']}")
            print(f"  Task: {task[:60]}")
            print(f"  Status: {status}")
            return page["id"]
    
    print(f"❌ No ticket found with Linear ID: {linear_id}")
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    find_ticket(sys.argv[1])
