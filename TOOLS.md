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

## Linear
- Workspace: Janani's (analemma.contact@gmail.com)
- Team: Analemma (id: 85f39310-e8c1-479c-b67b-cfeb3168096b)
- Token stored at: .linear-token (chmod 600)
- API: GraphQL at https://api.linear.app/graphql

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
