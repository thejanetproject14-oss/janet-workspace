---
name: shopify-ops
description: Manage the Analemma Shopify store via Admin API. Use when creating/updating products, collections, pages, metafields, navigation, inventory, or any Shopify admin task. Also use for bulk operations, theme settings, and store audits.
---

# Shopify Operations -- Analemma

## Store Details
- **Shop:** 5xtqdr-za.myshopify.com
- **Public domain:** analemma.shop
- **Theme:** Be Yours
- **Currency:** SGD
- **Token path:** `{baseDir}/../../.shopify-token`
- **API version:** 2024-10

## Authentication

Read the token from the token path. All API calls use:

```
X-Shopify-Access-Token: <token>
Content-Type: application/json
```

Base URL: `https://5xtqdr-za.myshopify.com/admin/api/2024-10`

## Common Operations

### Products

**List products:**
```bash
curl -s -H "X-Shopify-Access-Token: $TOKEN" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/products.json?limit=250"
```

**Create product:**
```bash
curl -s -X POST -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/products.json" \
  -d '{"product": {"title": "...", "body_html": "...", "vendor": "Analemma", "product_type": "...", "tags": "...", "variants": [...]}}'
```

**Update product:**
```bash
curl -s -X PUT -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/products/$PRODUCT_ID.json" \
  -d '{"product": {"id": $PRODUCT_ID, ...}}'
```

### Collections

**Create custom collection:**
```bash
curl -s -X POST -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/custom_collections.json" \
  -d '{"custom_collection": {"title": "...", "body_html": "...", "sort_order": "manual"}}'
```

**Add product to collection (collect):**
```bash
curl -s -X POST -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/collects.json" \
  -d '{"collect": {"product_id": $PRODUCT_ID, "collection_id": $COLLECTION_ID}}'
```

### Pages

**Create page:**
```bash
curl -s -X POST -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/pages.json" \
  -d '{"page": {"title": "...", "body_html": "...", "published": true}}'
```

### Inventory

**Get inventory levels:**
```bash
curl -s -H "X-Shopify-Access-Token: $TOKEN" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/inventory_levels.json?inventory_item_ids=$IDS"
```

### Smart Collections (automated)

```bash
curl -s -X POST -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/smart_collections.json" \
  -d '{"smart_collection": {"title": "...", "rules": [{"column": "tag", "relation": "equals", "condition": "..."}]}}'
```

### GraphQL (for bulk operations)

```bash
curl -s -X POST -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://5xtqdr-za.myshopify.com/admin/api/2024-10/graphql.json" \
  -d '{"query": "..."}'
```

## Product Reference

Full catalog with SKUs, pricing, and stock levels: see `{baseDir}/references/product-catalog.md`

## Brand Rules (ALWAYS FOLLOW)

- **ALL products are vegan.** Always tag "vegan" and mention in descriptions.
- Say "tinted lip ganache" -- NEVER "lip balm" or "lipstick."
- Brand: Analemma. Sub-brand: Ankaa by Analemma. Lip line: Sweet Treat.
- Currency: SGD. All prices in SGD.
- Vendor field: always "Analemma"
- No em-dashes in copy. Use -- instead.
- Tone: fun, colourful, art-forward. The art of noticing. Playful, warm, joyful. NOT ritual/luxury/sacred/pâtisserie-luxury.
- Include sensory descriptors: "Smells like / Feels like / Looks like" where appropriate.
- Tags should include: product type, collection, vegan, cruelty-free, flavor/scent name.

## Bulk Workflow

For operations touching many products (price updates, tag changes, inventory sync):
1. Fetch all products first
2. Build the update payload programmatically
3. Execute updates in a loop with rate-limit awareness (2 calls/sec for REST, 50 points/sec for GraphQL)
4. Log results and report summary

## Rate Limits
- REST: 2 requests/second (bucket of 40, refills 2/sec)
- GraphQL: 50 cost points/second (bucket of 1000)
- Always add small delays between bulk calls
