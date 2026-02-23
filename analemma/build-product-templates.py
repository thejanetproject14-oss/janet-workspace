#!/usr/bin/env python3
"""
Build product-type-specific Shopify templates for Analemma.
Creates: accessories, perfume, hair-oil, handbag templates.
Also fixes the default template and updates lip-ganache product assignments.
"""
import json
import subprocess
import os
import copy
import time

TOKEN = open('/Users/janet/.openclaw/workspace/.shopify-token').read().strip()
SHOP = "5xtqdr-za.myshopify.com"
API = f"https://{SHOP}/admin/api/2024-10"
THEME_ID = 181546287389

def api_get(path):
    r = subprocess.run(
        ["curl", "-s", "-H", f"X-Shopify-Access-Token: {TOKEN}", f"{API}/{path}"],
        capture_output=True, text=True
    )
    return json.loads(r.stdout)

def api_put(path, data):
    r = subprocess.run(
        ["curl", "-s", "-X", "PUT", "-H", f"X-Shopify-Access-Token: {TOKEN}",
         "-H", "Content-Type: application/json", f"{API}/{path}", "-d", json.dumps(data)],
        capture_output=True, text=True
    )
    return json.loads(r.stdout)

def put_theme_asset(key, value):
    """Upload a theme asset."""
    data = {"asset": {"key": key, "value": value}}
    r = subprocess.run(
        ["curl", "-s", "-X", "PUT", "-H", f"X-Shopify-Access-Token: {TOKEN}",
         "-H", "Content-Type: application/json",
         f"{API}/themes/{THEME_ID}/assets.json", "-d", json.dumps(data)],
        capture_output=True, text=True
    )
    return json.loads(r.stdout)

# Load default template as base
with open('/Users/janet/.openclaw/workspace/analemma/theme-product-default.json') as f:
    base_template = json.loads(f.read())

def make_template(collapsible_tabs, base=None):
    """Create a template by replacing collapsible tabs in the main section."""
    tmpl = copy.deepcopy(base or base_template)
    main = tmpl['sections']['main']
    
    # Remove all existing collapsible tabs and FAQ blocks from blocks
    old_tab_keys = [k for k, v in main['blocks'].items() 
                    if v.get('type') == 'collapsible_tab' or k.startswith('product-details')]
    for k in old_tab_keys:
        del main['blocks'][k]
    
    # Remove from block_order too
    main['block_order'] = [k for k in main['block_order'] if k not in old_tab_keys]
    
    # Add new collapsible tabs
    new_tab_keys = []
    for i, tab in enumerate(collapsible_tabs):
        key = f"tab_{tab['id']}"
        main['blocks'][key] = {
            "type": "collapsible_tab",
            "settings": {
                "icon": tab.get('icon', 'none'),
                "heading": tab['heading'],
                "content": tab['content'],
                "page": "",
                "custom_liquid": "",
                "keep_open": tab.get('keep_open', False)
            }
        }
        new_tab_keys.append(key)
    
    # Insert tabs before buy_buttons in block_order
    buy_idx = main['block_order'].index('buy_buttons') if 'buy_buttons' in main['block_order'] else len(main['block_order'])
    for i, key in enumerate(new_tab_keys):
        main['block_order'].insert(buy_idx + i, key)
    
    return tmpl

# ============================================================
# SHIPPING TAB (shared across all templates)
# ============================================================
SHIPPING_TAB = {
    "id": "shipping",
    "icon": "plane",
    "heading": "Shipping",
    "content": "<p>- Only ships within Singapore<br/>- Ships within 3-5 business days<br/>- FREE delivery for orders over $80</p>",
    "keep_open": False
}

# ============================================================
# 1. ACCESSORIES TEMPLATE (bag charms, enamel pins, pouches, brush set, lip balm charms)
# ============================================================
accessories_tabs = [
    {
        "id": "details",
        "heading": "Details",
        "content": "<p>Handcrafted with care. Each piece is unique and may have slight variations -- that's the beauty of handmade work.</p><p>100% vegan materials. Cruelty-free. Always.</p>"
    },
    {
        "id": "materials",
        "heading": "Materials & Care",
        "content": "<p><strong>Bag Charms:</strong> Glass beads, metal clip attachment. Wipe gently with a soft cloth. Avoid submerging in water.</p><p><strong>Enamel Pins:</strong> Hard enamel with butterfly clutch backing. Store flat to avoid scratching.</p><p><strong>Makeup Pouches:</strong> Cross-woven vegan material with zip closure. Spot clean with a damp cloth.</p><p><strong>Brush Set:</strong> 100% synthetic vegan bristles. Wash gently with mild soap, reshape, and air dry flat.</p>"
    },
    SHIPPING_TAB
]

# ============================================================
# 2. PERFUME TEMPLATE
# ============================================================
perfume_tabs = [
    {
        "id": "about",
        "heading": "About This Fragrance",
        "content": "<p>Each Analemma fragrance is crafted as an eau de parfum -- a higher concentration for richer, longer-lasting scent. Available in 15ml (travel) and 100ml (full vanity bottle).</p><p>100% vegan. Cruelty-free. No animal-derived ingredients at any stage.</p>"
    },
    {
        "id": "how_to_wear",
        "heading": "How to Wear",
        "content": "<p>Apply to pulse points: wrists, behind ears, base of throat, inner elbows. For longer-lasting scent, layer on moisturised skin. Avoid rubbing wrists together -- it breaks down the top notes.</p><p>For a subtle scent cloud, spray into the air and walk through it.</p>"
    },
    {
        "id": "storage",
        "heading": "Storage",
        "content": "<p>Keep in a cool, dry place away from direct sunlight. Avoid storing in the bathroom where heat and humidity can alter the fragrance. A bedroom drawer or vanity shelf is ideal.</p>"
    },
    SHIPPING_TAB
]

# ============================================================
# 3. HAIR OIL TEMPLATE
# ============================================================
hair_oil_tabs = [
    {
        "id": "whats_inside",
        "heading": "What's Inside",
        "content": "<p>A lightweight, multi-use botanical hair oil formulated to nourish without heaviness. Absorbs quickly, tames frizz, and leaves hair with natural, healthy shine.</p><p>100% vegan. No silicones. No parabens.</p>"
    },
    {
        "id": "how_to_use",
        "heading": "How to Use",
        "content": "<p><strong>Post-wash:</strong> Work a few drops through damp hair from mid-lengths to ends. Let air dry or blow dry as usual.</p><p><strong>Daily styling:</strong> Smooth a small amount over dry ends to tame flyaways and add shine.</p><p><strong>Scalp treatment:</strong> Massage into scalp before bed. Wash out in the morning for deep nourishment.</p>"
    },
    {
        "id": "details",
        "heading": "Details",
        "content": "<p>- Lightweight botanical formula<br/>- Suitable for all hair types<br/>- 100% vegan<br/>- Cruelty-free</p>"
    },
    SHIPPING_TAB
]

# ============================================================
# 4. HANDBAG TEMPLATE (beaded + vegan leather)
# ============================================================
handbag_tabs = [
    {
        "id": "details",
        "heading": "Details",
        "content": "<p><strong>Beaded Handbags:</strong> Fully hand-threaded glass bead construction with interior lining. Sized for evening essentials -- phone, card, lipstick, keys.</p><p><strong>Cross-Woven Vegan Leather:</strong> Everyday-sized bag with interior pockets, secure zip closure, and a textured weave that catches light beautifully. 100% vegan leather.</p>"
    },
    {
        "id": "care",
        "heading": "Care",
        "content": "<p><strong>Beaded bags:</strong> Best treated as evening/occasion bags. Avoid overstuffing. Store flat or stuffed with tissue paper to maintain shape. Wipe gently with a soft, dry cloth.</p><p><strong>Vegan leather bags:</strong> Wipe with a damp cloth. Avoid prolonged exposure to direct sunlight. Store stuffed with tissue to keep shape.</p>"
    },
    {
        "id": "materials",
        "heading": "Materials",
        "content": "<p>All Analemma handbags are made with 100% vegan materials. No animal leather, no animal-derived components, no exceptions.</p>"
    },
    SHIPPING_TAB
]

# ============================================================
# 5. FIX DEFAULT TEMPLATE (fallback for anything not assigned)
# ============================================================
default_tabs = [
    {
        "id": "details",
        "heading": "Details",
        "content": "<p>100% vegan. Cruelty-free. Made with intention.</p>"
    },
    SHIPPING_TAB
]

# Build all templates
templates = {
    "accessories": make_template(accessories_tabs),
    "perfume": make_template(perfume_tabs),
    "hair-oil": make_template(hair_oil_tabs),
    "handbag": make_template(handbag_tabs),
}

# Also fix the default template
fixed_default = make_template(default_tabs)

# ============================================================
# UPLOAD TEMPLATES TO THEME
# ============================================================
print("Uploading templates to Shopify theme...")

# Upload new templates
for name, tmpl in templates.items():
    key = f"templates/product.{name}.json"
    result = put_theme_asset(key, json.dumps(tmpl, indent=2))
    if 'asset' in result:
        print(f"  ✅ {key} uploaded")
    else:
        print(f"  ❌ {key} FAILED: {json.dumps(result)[:200]}")
    time.sleep(0.6)

# Fix default template
result = put_theme_asset("templates/product.json", json.dumps(fixed_default, indent=2))
if 'asset' in result:
    print(f"  ✅ templates/product.json (default) updated")
else:
    print(f"  ❌ templates/product.json FAILED: {json.dumps(result)[:200]}")

time.sleep(1)

# ============================================================
# ASSIGN PRODUCTS TO TEMPLATES
# ============================================================
print("\nAssigning products to templates...")

products_data = api_get("products.json?limit=250&fields=id,title,product_type,template_suffix")
products = products_data.get('products', [])

# Define template assignments based on product type / title
assignments = {}
for p in products:
    pid = p['id']
    title = p['title']
    ptype = p.get('product_type', '')
    current = p.get('template_suffix') or ''
    
    if 'Lip Ganache' in title and current != 'lip-ganache':
        assignments[pid] = ('lip-ganache', title)
    elif ptype == 'Perfume':
        assignments[pid] = ('perfume', title)
    elif ptype == 'Hair Oil':
        assignments[pid] = ('hair-oil', title)
    elif ptype in ('Handbag',) or 'Handbag' in title or title in ('The Jaipur Florals', 'Check Mate', 'Dark Forest', 'The Wine Lover'):
        assignments[pid] = ('handbag', title)
    elif ptype in ('Bag Charm', 'Pin', 'Pouch', 'Accessory', 'Tools') or \
         'Enamel Pin' in title or 'Carry Your World' in title or \
         'Brush Set' in title or 'Charm' in title or \
         title in ('Apple of My Eye', 'Berry in Love', 'Cherry on Top', 'Feeling Blue-tiful', 
                    'Squeeze the Day', 'Zest Friends Forever'):
        assignments[pid] = ('accessories', title)

for pid, (template, title) in assignments.items():
    result = api_put(f"products/{pid}.json", {"product": {"id": pid, "template_suffix": template}})
    product = result.get('product', {})
    if product.get('template_suffix') == template:
        print(f"  ✅ {title} -> {template}")
    else:
        print(f"  ❌ {title} -> {template} FAILED")
    time.sleep(0.6)

print("\nDone! All templates created and products assigned.")
