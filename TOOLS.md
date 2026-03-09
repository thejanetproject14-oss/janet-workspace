# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Notion
- Workspace: The Janet Project's Space
- Integration: "janet" (internal)
- Token stored at: .notion-token (chmod 600)
- API version: 2022-06-28
- Access: read, update, insert content + user info with emails
- Pages:
  - Analemma: 30beab20-0eed-80a0-80a1-cf6a2ad73acd
  - Terminal 3: 30beab20-0eed-8056-b8fb-d1cf91255664
  - Health: 30beab20-0eed-80f8-ba75-f7bbcf1aaf16
  - Others: 30beab20-0eed-8088-9865-e17a2be987a9
  - Open Tasks -- Master List: 30beab20-0eed-8188-8965-d32e0f59b930
  - Good things are always happening to me (Gratitude): 31beab20-0eed-8113-a010-fe6776857a26
- Strategy: Notion = hub/databases/links. Google Drive = long-form docs. Always link GDrive docs back into Notion.

## Linear
- Workspace: Analemma
- Team: Analemma (ID: 85f39310-e8c1-479c-b67b-cfeb3168096b)
- Token stored at: .linear-token (chmod 600)
- API: GraphQL at https://api.linear.app/graphql
- User: Janani (analemma.contact@gmail.com)
- Existing issues: ~10 video/content tasks in Backlog

## Janet Email
- thejanetproject14@gmail.com (all Janet logins)

## Slack
- Workspace: Janet x Analemma (janetxanalemma.slack.com)
- Bot user: janet_ai_team (U0AGPSW6Q80)
- Bot ID: B0AFZ71G2LC
- Token stored at: .slack-tokens (chmod 600)
- Channels: #general, #shopify, #content-engine, #seo-engine, #linear-updates, #social, #all-janet-x-analemma
- Channel IDs: general=C0AFP41TC0K, shopify=C0AFVFSJEE6, content-engine=C0AFE2LNTP1, seo-engine=C0AFS3CC6BX, linear-updates=C0AG8DFJ057, social=C0AG8D2D341, all=C0AFTDRF1F0

## Linear
- Workspace: Janani's (analemma.contact@gmail.com)
- Team: Analemma (id: 85f39310-e8c1-479c-b67b-cfeb3168096b)
- Token stored at: .linear-token (chmod 600)
- API: GraphQL at https://api.linear.app/graphql

## WhatsApp Groups
- Tiny Wins Society: 120363406967771634@g.us
- Sita Management: 120363426048870156@g.us

## WhatsApp Rules (HARD CONSTRAINTS)

### NEVER DM Sita. NEVER.
- All messages to Sita go through the Sita Management group ONLY
- Do NOT respond to Sita's DMs. Ignore completely.
- Do NOT initiate DMs to Sita under any circumstances.
- The ONLY way I communicate with Sita is in the group with Sunshine present.

### Sita Management Group Rules:
- Topic: chores, food schedules, household management ONLY
- Language: English + transliterated Hindi/Nepali
- Call Sunshine "ma'am" in this group
- NO work, Analemma, terminal 3, personal info, finances, health details
- Off-topic questions: do not answer

### Tiny Wins Society Group Rules:
- Topic: Health check-ins, scoring, streaks, encouragement ONLY
- Call Sunshine "Jan" in this group
- NO work, Analemma, terminal 3, personal info, finances, relationship details
- Off-topic questions: do not answer
- Raghavi + Kruthika are members -- privacy is critical
- Do NOT respond to DMs from group members outside the group

### General Group Rules:
- ALWAYS respond when mentioned in a group. Don't ignore mentions.
- NEVER share in ANY group: weight, height, BMI, medical conditions, financial info, relationship details, career details, or any PII
- Messages to people in groups go through the group, not DMs
- When in doubt, don't share. Privacy > helpfulness.

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Token Usage Monitoring Workflow

### Alerts Strategy
1. Check all active sessions
2. Track alerts in `/memory/token_usage_alerts.json`
3. Alert thresholds:
   - Warning: 60,000 tokens
   - Urgent: 100,000 tokens
4. Send alerts via WhatsApp
5. Ensure only one alert per threshold per session

### Alert JSON Structure
```json
{
    "60k_alerted_sessions": ["session_key1", "session_key2"],
    "100k_alerted_sessions": ["session_key3"]
}
```

### Recommended Cron Frequency
- Every 30 minutes during active work hours
- Hourly during off-peak times
