# Agent System SOP

## The Flow: Every Piece of Work

```
Sunshine request / Janet initiative
        ↓
   Linear issue created (ANA-XXX)
        ↓
   Janet assigns to sub-agent via sessions_spawn
        ↓
   Agent calls: agent_update.py start → ticket → In Progress
        ↓
   Agent executes work
        ↓
   Agent pushes output to Notion (under Analemma parent page)
        ↓
   Agent calls: agent_update.py done <notion_url> → ticket → Janet Review
        ↓
   Janet reviews output quality
        ↓
   Janet calls: PATCH /api/tickets/:id {"status": "Sunshine Approval", "outputUrl": <url>}
        ↓
   Sunshine reviews on backoffice portal
        ↓
   Ticket → Done. Linear issue → Done.
```

## Mandatory Agent Protocol (NON-NEGOTIABLE)

### On task start:
```bash
python3 /Users/janet/.openclaw/workspace/scripts/agent_update.py start \
  "<notion_ticket_page_id>" \
  "<LINEAR-ID>" \
  "<Agent Name>" \
  "<one-line description of what you're doing>"
```

### On task completion:
```bash
python3 /Users/janet/.openclaw/workspace/scripts/agent_update.py done \
  "<notion_ticket_page_id>" \
  "<LINEAR-ID>" \
  "<Agent Name>" \
  "<one-line summary of what was delivered>" \
  "https://www.notion.so/<output-page-id-no-dashes>" \
  "<optional: additional details for Janet>"
```

### On blocked:
```bash
python3 /Users/janet/.openclaw/workspace/scripts/agent_update.py block \
  "<notion_ticket_page_id>" \
  "<LINEAR-ID>" \
  "<Agent Name>" \
  "<reason for block>"
```
Then: escalate to Janet via sessions_send. Never go to Sunshine directly.

### Notion output URL format:
Every Notion page ID like `31beab20-0eed-8129-943e-fcdabcc91561` becomes:
`https://www.notion.so/31beab200eed8129943efcdabcc91561`
(remove the dashes)

## Review Flow

```
Agent delivers → Janet Review
Janet approves → Sunshine Approval (output URL attached)
Sunshine approves → Done
Janet rejects → back to In Progress with comment
```

**Janet NEVER forwards sub-agent output to Sunshine without reviewing it first.**
**Sunshine only sees "Sunshine Approval" tickets -- everything else is Janet's problem.**

## Finding Your Ticket's Notion Page ID

```bash
python3 /Users/janet/.openclaw/workspace/scripts/find_ticket.py ANA-172
# Returns: Notion ID, task name, current status
```

## Agent Roster

| Agent | HP Name | Model | Role | Linear prefix |
|---|---|---|---|---|
| Janet | Janet | Opus 4.6 | Orchestrator | (none) |
| content-agent | Luna | Sonnet 4 | Content calendars, captions, blog drafts | `[Luna]` |
| research-agent | Neville | Sonnet 4 | Competitor analysis, influencer scouting, trends | `[Neville]` |
| seo-agent | Percy | Sonnet 4 | Keywords, meta copy, blog posts, search | `[Percy]` |
| pr-agent | Gilderoy | Sonnet 4 | Media outreach, influencer comms, pitches | `[Gilderoy]` |
| writer-agent | Sirius | Sonnet 4 | Product copy, brand narrative, captions | `[Sirius]` |
| shopify-agent | Arthur | Sonnet 4 | Store maintenance, product pages, bug fixes | `[Arthur]` |
| devops-agent | McGonagall | Sonnet 4 | Backoffice portal, scripts, infrastructure | `[McGonagall]` |

## Output Routing

All agent outputs go to Notion under the **Analemma parent page** (30beab20-0eed-80a0-80a1-cf6a2ad73acd).

Name pages clearly: `ANA-XXX: [Task Name] -- [Month Year]`
Example: `ANA-172: Keyword Research -- March 2026`

## Model Cost Rules

- **Opus**: Janet only. Strategy, review, judgment.
- **Sonnet**: All sub-agents. Execution work.
- Agents NEVER self-upgrade to a higher model.
- Janet sets the model in the task brief.

## Escalation Rules

- Sub-agents → Janet only (never Sunshine)
- Janet → Sunshine for: brand decisions, pricing, partnerships, external comms, anything that leaves the machine
- All escalations logged in backoffice activity feed

## Backoffice Portal

Live at: https://analemma-backoffice.vercel.app
API docs: see devops-agent SOUL.md

Key APIs:
- `GET /api/tickets` -- all tickets
- `GET /api/activity` -- last 50 activity entries
- `PATCH /api/tickets/:id` -- update status, outputUrl, priority, assignedTo
- `POST /api/activity` -- log agent action or comment
