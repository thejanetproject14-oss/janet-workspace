#!/usr/bin/env python3
import json, re, time, urllib.request

TOKEN = open('/Users/janet/.openclaw/workspace/.shopify-token').read().strip()
BASE = 'https://5xtqdr-za.myshopify.com/admin/api/2024-10'

TAROT_PAGE_IDS = [
    155518533917,  # Ace Of Cups
    155518566685,  # Nine of Pentacles
    155518632221,  # Page of Cups
    155518599453,  # Queen of Wands
    155518468381,  # The Empress
    155518435613,  # The Star
    155518501149,  # The Sun
    155518730525,  # The Tower
    155518697757,  # The World
    155518664989,  # Three of Wands
]

NEW_BOTTOM = """<p><strong>🍒 Try our Tinted Lip Ganache</strong><br>Peptide-powered, hyaluronic acid-infused lip colour in 5 dessert-inspired shades.<br>• <a href="https://analemma.shop/products/strawberry-jam-tinted-lip-ganache">Strawberry Jam</a> • <a href="https://analemma.shop/products/raspberry-coulis-tinted-lip-ganache">Raspberry Coulis</a> • <a href="https://analemma.shop/products/hot-cocoa-tinted-lip-ganache">Hot Cocoa</a> • <a href="https://analemma.shop/products/maraschino-cherry-tinted-lip-ganache">Maraschino Cherry</a> • <a href="https://analemma.shop/products/tiramisu-tinted-lip-ganache">Tiramisu</a></p>
<p><strong>✨ Metallic Purse Charms</strong><br>Tarnish-free, clip-on lip ganache charms for your bag.<br><a href="https://analemma.shop/products/metallic-lip-balm-charm">Shop Metallic Charms</a></p>
<p><strong>Find us at Artbox Singapore</strong><br>Booth 185, Singapore Expo Hall 3<br>April 3--5 &amp; April 10--12, 12pm--11pm</p>
<p><strong>Shop online:</strong> <a href="https://analemma.shop">analemma.shop</a></p>
<p><a href="https://instagram.com/analemma.shop">Follow us on Instagram</a> · <a href="https://tiktok.com/@analemma.shop">Follow us on TikTok</a></p>"""

def api_get(path):
    req = urllib.request.Request(f'{BASE}{path}', headers={
        'X-Shopify-Access-Token': TOKEN,
        'Content-Type': 'application/json'
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def api_put(path, data):
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(f'{BASE}{path}', data=body, method='PUT', headers={
        'X-Shopify-Access-Token': TOKEN,
        'Content-Type': 'application/json'
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

for pid in TAROT_PAGE_IDS:
    try:
        page_data = api_get(f'/pages/{pid}.json')
        page = page_data['page']
        title = page['title']
        body = page['body_html']
        
        # Remove old "Available in person" section
        cleaned = re.sub(
            r'<p[^>]*>\s*<strong[^>]*>Available in person</strong>.*$',
            '', body, flags=re.DOTALL
        ).rstrip()
        
        new_body = cleaned + '\n' + NEW_BOTTOM
        
        result = api_put(f'/pages/{pid}.json', {
            'page': {'id': pid, 'body_html': new_body}
        })
        
        print(f'✅ {title}')
    except Exception as e:
        print(f'❌ Page {pid}: {e}')
    
    time.sleep(0.6)

print('\nDone! All 10 tarot pages updated.')
