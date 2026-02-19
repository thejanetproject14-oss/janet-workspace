#!/bin/bash
TOKEN=$(cat /root/.openclaw/workspace/.notion-token)
PAGE_ID="30beab20-0eed-81c6-9b7d-c31ed08f0bca"

append_blocks() {
  local json="$1"
  local response=$(curl -s -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Notion-Version: 2022-06-28" \
    -H "Content-Type: application/json" \
    -d "$json")
  local has_error=$(echo "$response" | jq -r '.object // empty')
  if [ "$has_error" = "error" ]; then
    echo "ERROR: $(echo "$response" | jq -r '.message')"
    return 1
  fi
  echo "OK - appended blocks"
  return 0
}

# Helper: build a day heading (toggle heading with to_do items inside)
# We'll use heading_2 for dates and to_do blocks underneath

echo "=== PHASE 1: TEASE & WORLD-BUILD ==="

# Phase 1 header
append_blocks '{
  "children": [
    {
      "object": "block",
      "type": "heading_1",
      "heading_1": {
        "rich_text": [{"text": {"content": "🔮 PHASE 1: TEASE & WORLD-BUILD (Feb 19-23)"}}],
        "color": "purple_background"
      }
    }
  ]
}'

sleep 0.5

########################################
# DAY 18 - Feb 19 (Wed)
########################################
append_blocks '{
  "children": [
    {
      "object": "block",
      "type": "heading_2",
      "heading_2": {
        "rich_text": [{"text": {"content": "📅 Feb 19 (Wed) — Day 18 — TEASE"}, "annotations": {"color": "purple"}}]
      }
    },
    {
      "object": "block",
      "type": "callout",
      "callout": {
        "icon": {"emoji": "⚠️"},
        "rich_text": [{"text": {"content": "JB photos NOT yet arrived. Use existing assets or mystery/teaser shots only. Effort: 🟢 Low (15 min)"}}],
        "color": "yellow_background"
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📝 PLAN"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Select moodiest, most editorial close-up from any existing assets for mystery feed post"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Write caption: \"something sweet is coming...\" (tease, no product name visible)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Prep 2 story frames: black screen \"we have a secret\" + photo with 03.08.26 overlay"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📸 SHOOT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "No new shooting needed — use existing moody close-up assets"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "✂️ EDIT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Light edit on selected photo in Lightroom mobile — heavy shadow, tight crop"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Create story overlay graphic with 03.08.26 in clean serif font"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📤 POST"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Feed Post "}, "annotations": {"bold": true}},
          {"text": {"content": "(12 PM SGT): Mystery shot. Caption: \"something sweet is coming...march 8. mark it.\" | Hashtags: Set B + Set C + brand tags | Pillar: 🍰 Dessert Aesthetic"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Stories ×2: "}, "annotations": {"bold": true}},
          {"text": {"content": "(1) Black screen + white text \"we have a secret\" (2) Photo + \"03.08.26\" + countdown sticker to Mar 8"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "Reel: "}, "annotations": {"bold": true}},
          {"text": {"content": "None"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "TikTok: "}, "annotations": {"bold": true}},
          {"text": {"content": "None"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "divider",
      "divider": {}
    }
  ]
}'

sleep 0.5

########################################
# DAY 17 - Feb 20 (Thu)
########################################
append_blocks '{
  "children": [
    {
      "object": "block",
      "type": "heading_2",
      "heading_2": {
        "rich_text": [{"text": {"content": "📅 Feb 20 (Thu) — Day 17 — TEASE"}, "annotations": {"color": "purple"}}]
      }
    },
    {
      "object": "block",
      "type": "callout",
      "callout": {
        "icon": {"emoji": "📸"},
        "rich_text": [{"text": {"content": "🎉 JB PHOTOSHOOT PHOTOS ARRIVE TODAY! No feed post — stories only. Effort: 🟢 Low (15 min)"}}],
        "color": "green_background"
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📝 PLAN"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Review JB photoshoot photos as they arrive — start selecting hero shots for each flavor"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Pull BTS video clip (3-5 sec) from phone camera roll — studio setup, lights, props, no product"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Plan poll sticker: \"guess what we are launching\" — skincare / something for your lips"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📸 SHOOT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "No new shooting — use BTS clips from phone camera roll"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "✂️ EDIT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Trim BTS video clip to 3-5 seconds, add text overlay: \"the day we brought it to life\""}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📤 POST"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Feed Post: "}, "annotations": {"bold": true}},
          {"text": {"content": "None (save feed for tomorrow)"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Stories ×3: "}, "annotations": {"bold": true}},
          {"text": {"content": "(1) BTS video clip — studio setup, text: \"the day we brought it to life\" (2) BTS still of set with dessert props, text: \"every detail matters\" (3) Poll: \"guess what we're launching 👀\""}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "Reel: "}, "annotations": {"bold": true}},
          {"text": {"content": "None | TikTok: None"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "divider",
      "divider": {}
    }
  ]
}'

sleep 0.5

########################################
# DAY 16 - Feb 21 (Fri)
########################################
append_blocks '{
  "children": [
    {
      "object": "block",
      "type": "heading_2",
      "heading_2": {
        "rich_text": [{"text": {"content": "📅 Feb 21 (Fri) — Day 16 — TEASE"}, "annotations": {"color": "purple"}}]
      }
    },
    {
      "object": "block",
      "type": "callout",
      "callout": {
        "icon": {"emoji": "🟡"},
        "rich_text": [{"text": {"content": "Effort: 🟡 Medium (30 min). Texture/sensory tease. Also Analemma Episode 3 edit day (5hr block). Pillar: 🍰 Dessert Aesthetic"}}],
        "color": "yellow_background"
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📝 PLAN"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Select extreme macro/close-up of Lip Ganache texture from JB photos — swatch on skin, product surface, creamy texture"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Write caption: \"ganache. not a gloss. not a matte. not a balm...\" — name reveal: lip ganache"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Prep question sticker: \"what does lip ganache make you think of?\""}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📸 SHOOT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Optional: film quick hand swatch video at home Friday evening (good lighting, slow-mo if possible)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "✂️ EDIT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Edit selected texture/swatch macro photo — make it abstract and intriguing"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Edit founder journey teaser Reel for Sat (15-20 sec, use existing footage per growth strategy)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📤 POST"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Feed Post "}, "annotations": {"bold": true}},
          {"text": {"content": "(12 PM SGT): Texture/swatch macro close-up. Caption reveals \"lip ganache\" name. | Hashtags: Set A + Set E + brand tags | Pillar: 🍰 Dessert Aesthetic"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Stories ×2: "}, "annotations": {"bold": true}},
          {"text": {"content": "(1) Swatch video, text: \"the texture though 🤤\" (2) Question sticker: \"what does lip ganache make you think of?\""}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "Reel: "}, "annotations": {"bold": true}},
          {"text": {"content": "None | TikTok: None"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "divider",
      "divider": {}
    }
  ]
}'

sleep 0.5

########################################
# DAY 15 - Feb 22 (Sat) - HIGH EFFORT
########################################
append_blocks '{
  "children": [
    {
      "object": "block",
      "type": "heading_2",
      "heading_2": {
        "rich_text": [{"text": {"content": "📅 Feb 22 (Sat) — Day 15 — TEASE 🔴 HIGH EFFORT"}, "annotations": {"color": "red"}}]
      }
    },
    {
      "object": "block",
      "type": "callout",
      "callout": {
        "icon": {"emoji": "🔴"},
        "rich_text": [{"text": {"content": "Effort: 🔴 High (1.5-2 hrs). Scent story carousel + inspo montage reel + stories. Saturday content day. Pillar: 🍰 Dessert Aesthetic"}}],
        "color": "red_background"
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📝 PLAN"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Plan 3-slide carousel: (1) dessert ingredient flat-lay (2) close-up of one ingredient (3) text card: \"5 flavors. all real. all vegan. 03.08.26\""}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Write caption: scent story — \"we didn't do flavored. we did scented...five dessert-inspired scents\""}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Plan reel: \"Things that inspired our new launch\" — 5-7 clips, 1-2 sec each, dessert montage"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Plan stories: boomerang smelling product, ingredient close-up, quiz sticker with flavor guesses"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📸 SHOOT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "SHOOT dessert ingredient flat-lay at home (raspberries, cocoa powder, coffee beans, cherries, strawberry jam) — Saturday morning, good window light"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Film 5-7 short clips for reel: pour chocolate sauce (overhead), slice strawberry, stir coffee, pick up cherry, quick product swatch"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Film smelling product reaction for stories (genuine smile/surprise)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "✂️ EDIT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Edit carousel slides — flat-lay photos + Canva text card (30 sec)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Cut reel: 15-20 sec montage, sultry jazz or \"dessert ASMR\" trending sound, end card with Analemma logo + date"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📤 POST"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Feed Carousel "}, "annotations": {"bold": true}},
          {"text": {"content": "(10 AM SGT): Scent story — 3 slides. Caption: \"we didn't do flavored. we did scented...\" | Hashtags: Set B + Set A + brand tags"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Reel "}, "annotations": {"bold": true}},
          {"text": {"content": "(7:30 PM SGT): \"Things that inspired our new launch\" — dessert inspo montage, 15-20 sec"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "TikTok: "}, "annotations": {"bold": true}},
          {"text": {"content": "Cross-post reel (8 PM SGT) — save without IG watermark first"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Stories ×3: "}, "annotations": {"bold": true}},
          {"text": {"content": "(1) Boomerang smelling product, text: \"this is real\" (2) Ingredient close-up: \"can you guess the five flavors?\" (3) Quiz sticker with 1 real + 3 fake flavors"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "callout",
      "callout": {
        "icon": {"emoji": "📌"},
        "rich_text": [{"text": {"content": "After posting: spend 30 min selecting + editing photoshoot photos for Mon-Fri next week. Export 5-6 selects to phone."}}],
        "color": "blue_background"
      }
    },
    {
      "object": "block",
      "type": "divider",
      "divider": {}
    }
  ]
}'

sleep 0.5

########################################
# DAY 14 - Feb 23 (Sun) - MAJOR BATCH DAY
########################################
append_blocks '{
  "children": [
    {
      "object": "block",
      "type": "heading_2",
      "heading_2": {
        "rich_text": [{"text": {"content": "📅 Feb 23 (Sun) — Day 14 — TEASE 📦 BATCH PREP DAY"}, "annotations": {"color": "blue"}}]
      }
    },
    {
      "object": "block",
      "type": "callout",
      "callout": {
        "icon": {"emoji": "📦"},
        "rich_text": [{"text": {"content": "🔵 MAJOR BATCH SESSION: After posting, spend 2-3 hours prepping Mon-Fri (Feb 24-28) content. Edit 5 hero product photos, write all 5 reveal captions, create countdown graphics, schedule posts, film swatch videos. Effort: 🟡 Medium (30-45 min posting + 2-3 hrs batch)"}}],
        "color": "blue_background"
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📝 PLAN"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Select warm, personal founder portrait from photoshoot or phone selfie from shoot day"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Write caption: \"a note from me...\" — founder vulnerability, why Analemma exists, Sweet Treat is \"that gasp\""}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📸 SHOOT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Film casual talking-head story (Sunday morning, no/minimal makeup — authenticity): thank followers, tease the week ahead"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "✂️ EDIT"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Edit founder portrait (light touch)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📤 POST"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Feed Post "}, "annotations": {"bold": true}},
          {"text": {"content": "(10 AM SGT): Founder portrait + personal note. \"13 days.\" | Hashtags: Set D + Set C + brand tags | Pillar: 👩\u200d💼 Founder Journey"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "IG Stories ×2: "}, "annotations": {"bold": true}},
          {"text": {"content": "(1) Casual talking-head: \"thank you for following along, launch is in 2 weeks\" (2) Repost feed to stories with \"read the caption 🤍\""}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [
          {"text": {"content": "Reel: "}, "annotations": {"bold": true}},
          {"text": {"content": "None | TikTok: None"}}
        ],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "heading_3",
      "heading_3": {
        "rich_text": [{"text": {"content": "📦 BATCH PREP CHECKLIST (2-3 hrs afternoon)"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Edit + finalize 5 hero product photos (one per flavor: Raspberry Coulis, Strawberry Jam, Hot Cocoa, Maraschino Cherry, Tiramisu)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Write all 5 flavor reveal captions (Mon-Fri Feb 24-28)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Create countdown graphics in Canva (\"13 days\" through \"8 days\")"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Prep lip swatch comparison photo (Raspberry vs Strawberry Jam on arm)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Film needed swatch videos for the week"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Schedule Mon-Fri feed posts via Later/Planoly/Meta Business Suite"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"text": {"content": "Design \"Introducing Sweet Treat\" name reveal carousel for Tue Feb 24 (per growth strategy)"}}],
        "checked": false
      }
    },
    {
      "object": "block",
      "type": "divider",
      "divider": {}
    }
  ]
}'

echo "=== Phase 1 complete ==="
