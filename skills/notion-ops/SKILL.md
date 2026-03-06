---
name: notion-ops
description: Manage Sunshine's Notion workspace via API. Use when creating, reading, updating, or searching pages, databases, blocks, or task lists in Notion. Also use for pushing content (strategies, scripts, plans, research) to Notion, logging tasks via the "Task:" protocol, or auditing/restructuring the workspace.
---

# Notion Operations

## Authentication

```bash
TOKEN=$(cat {baseDir}/../../.notion-token)
```

All API calls:
```
Authorization: Bearer $TOKEN
Notion-Version: 2022-06-28
Content-Type: application/json
```

Base URL: `https://api.notion.com/v1`

## Workspace Structure

See `references/workspace-map.md` for full page tree with IDs.

**Top-level pages:**
- ♾️ Analemma: `30beab20-0eed-80a0-80a1-cf6a2ad73acd`
- 3️⃣ Terminal 3: `30beab20-0eed-8056-b8fb-d1cf91255664`
- 🫀 Health: `30beab20-0eed-80f8-ba75-f7bbcf1aaf16`
- 😍 Others: `30beab20-0eed-8088-9865-e17a2be987a9`

**Key pages:**
- ✅ Open Tasks -- Master List: `30beab20-0eed-8188-8965-d32e0f59b930`

## Task Protocol

When Sunshine says "Task:" followed by something, immediately log it to the Open Tasks -- Master List page. Append as a to_do block. No questions, just file it.

```bash
curl -s -X PATCH "$BASE/blocks/30beab20-0eed-8188-8965-d32e0f59b930/children" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"children": [{"object": "block", "type": "to_do", "to_do": {"rich_text": [{"text": {"content": "TASK TEXT HERE"}}], "checked": false}}]}'
```

## Common Operations

### Create a page under a parent
```bash
curl -s -X POST "$BASE/pages" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"parent": {"page_id": "PARENT_ID"}, "properties": {"title": [{"text": {"content": "Page Title"}}]}, "children": [BLOCKS]}'
```

### Read a page
```bash
curl -s "$BASE/pages/PAGE_ID" -H "Authorization: Bearer $TOKEN" -H "Notion-Version: 2022-06-28"
```

### Get page content (blocks)
```bash
curl -s "$BASE/blocks/PAGE_ID/children?page_size=100" -H "Authorization: Bearer $TOKEN" -H "Notion-Version: 2022-06-28"
```

Paginate with `start_cursor` from response if `has_more: true`.

### Append blocks to a page
```bash
curl -s -X PATCH "$BASE/blocks/PAGE_ID/children" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"children": [BLOCKS]}'
```

### Search
```bash
curl -s -X POST "$BASE/search" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"query": "SEARCH_TERM", "page_size": 10}'
```

### Query a database
```bash
curl -s -X POST "$BASE/databases/DB_ID/query" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"page_size": 100}'
```

## Block Types Reference

Common block JSON patterns:

```json
// Heading 2
{"type": "heading_2", "heading_2": {"rich_text": [{"text": {"content": "Title"}}]}}

// Paragraph
{"type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Text"}}]}}

// Bold text
{"type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Bold"}, "annotations": {"bold": true}}]}}

// Bulleted list item
{"type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"text": {"content": "Item"}}]}}

// Numbered list item
{"type": "numbered_list_item", "numbered_list_item": {"rich_text": [{"text": {"content": "Item"}}]}}

// To-do
{"type": "to_do", "to_do": {"rich_text": [{"text": {"content": "Task"}}], "checked": false}}

// Divider
{"type": "divider", "divider": {}}

// Toggle
{"type": "toggle", "toggle": {"rich_text": [{"text": {"content": "Toggle title"}}]}}

// Callout
{"type": "callout", "callout": {"rich_text": [{"text": {"content": "Note"}}], "icon": {"emoji": "💡"}}}
```

## Content Routing

Decide which parent page to create under:
- Analemma content (products, strategy, content, launches) → under Analemma page
- T3 work docs → under Terminal 3 page
- Health plans, meal plans, supplements → under Health page
- Personal, tasks, OKRs → under Others page

## API Limits

- Max 100 blocks per append request. Batch larger content into multiple calls.
- Rich text content max 2000 chars per text object. Split longer text.
- Rate limit: ~3 requests/second. Add brief delays for bulk operations.
- `parent` field is READ-ONLY on updates -- cannot move pages between parents via API.
