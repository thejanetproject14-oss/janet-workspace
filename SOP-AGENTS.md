# Agent System SOP

## The Flow: Every Piece of Work

```
Sunshine request / Janet initiative
        ↓
   Linear issue created (ANA-XXX)
        ↓
   Janet assigns to sub-agent
        ↓
   Sub-agent executes (Sonnet)
        ↓
   Output pushed to Notion (under Analemma)
        ↓
   Linear issue → Done
        ↓
   Notion ticket board updated
```

## Rules

1. **Every task gets a Linear issue.** No invisible work. Format: `[Agent Name] Task description`
2. **Every deliverable goes to Notion.** Content calendars, research reports, copy -- all pushed to the relevant Notion parent page.
3. **Linear = tracking. Notion = deliverables.** Linear tells you what's happening. Notion holds the actual output.
4. **Janet reviews before Sunshine sees.** Sub-agents deliver to Janet. Janet reviews quality, then pushes to Notion and closes the Linear issue.
5. **Ticket board (Notion) mirrors Linear.** The backoffice Kanban board shows current state across all agents.

## Agent Roster

| Agent | Model | What it does | Linear prefix |
|---|---|---|---|
| Janet | Opus 4.6 | Orchestrates, reviews, delegates | (no prefix) |
| Content Agent | Sonnet 4 | Content calendars, captions, blog drafts | `[Content Agent]` |
| Research Agent | Sonnet 4 | Competitor analysis, influencer scouting, trends | `[Research Agent]` |

## Creating a Task

### Janet auto-creates:
When Sunshine says "Task:" → logged to Notion master task list.
When Janet delegates to a sub-agent → Linear issue created with agent prefix.

### Manual creation:
1. Create Linear issue under Analemma team
2. Prefix with agent name: `[Content Agent] Write 3 blog posts`
3. Set priority (P1-P4)
4. Janet picks it up and delegates

## Output Routing

| Agent | Output goes to |
|---|---|
| Content Agent | Analemma page on Notion |
| Research Agent | Analemma page on Notion |
| Janet (direct work) | Appropriate Notion section |

## Model Cost Rules

- **Opus**: Janet only. Strategy, review, judgment.
- **Sonnet**: Content + Research agents. Execution work.
- **Haiku**: Tiny Wins Society, Sita management, routine responses.
- Agents NEVER self-upgrade to a higher model.
- Janet sets the model in the task brief.

## Escalation

- Sub-agents escalate to Janet, not Sunshine.
- Janet escalates to Sunshine only for: brand decisions, pricing, partnerships, external comms.
- All escalations logged in Linear comments.
