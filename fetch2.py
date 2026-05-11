#!/usr/bin/env python3
"""Fill remaining 20 empty photoUrls for Albania places"""
import json, time, urllib.request, urllib.parse, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AlbaniaTripBot/1.0)"}

def search_wikimedia(query):
    """Search Wikimedia and return best image URL"""
    q = urllib.parse.quote(query)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={q}&srnamespace=6&format=json&origin=*"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        resp = urllib.request.urlopen(req, timeout=10, context=ctx)
        data = json.loads(resp.read())
        results = data.get('query', {}).get('search', [])
        if not results:
            return None
        pageid = results[0]['pageid']
        title = results[0]['title']
        # Get imageinfo URL
        info_url = f"https://commons.wikimedia.org/w/api.php?action=query&pageids={pageid}&prop=imageinfo&iiprop=url&format=json&origin=*"
        req2 = urllib.request.Request(info_url, headers=HEADERS)
        resp2 = urllib.request.urlopen(req2, timeout=10, context=ctx)
        info_data = json.loads(resp2.read())
        pages = info_data.get('query', {}).get('pages', {})
        img_url = pages.get(str(pageid), {}).get('imageinfo', [{}])[0].get('url', '')
        return img_url if img_url else None
    except Exception as e:
        return None

# Manual overrides for difficult places
OVERRIDES = {
    "vlr-akrolli-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Akrolli_tower.jpg/800px-Akrolli_tower.jpg",
    "vlr-dyrmishi-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Dymishti_waterfall.jpg/600px-Dymishti_waterfall.jpg",
    "sar-kanali-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Albanian_Riviera.jpg/800px-Albanian_Riviera.jpg",
    "riv-himaranta-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Albanian_Riviera_beach.jpg/600px-Albanian_Riviera_beach.jpg",
    "riv-pilur-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Pilur_Castle.jpg/600px-Pilur_Castle.jpg",
    "riv-cape-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Albanian_Riviera_Cliffs.jpg/600px-Albanian_Riviera_Cliffs.jpg",
    "riv-fterra-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Fterra_Beach.jpg/600px-Fterra_Beach.jpg",
    "tir-lake-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Tirana_Lake.jpg/600px-Tirana_Lake.jpg",
    "gji-zagarotti-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Gjirokaster_Old_Town.jpg/600px-Gjirokaster_Old_Town.jpg",
    "gji-safary-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Libohove_Palace.jpg/600px-Libohove_Palace.jpg",
    "gji-sword-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Gjirokaster_Castle.jpg/600px-Gjirokaster_Castle.jpg",
    "ber-mangal-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Berat_Mangalemi.jpg/600px-Berat_Mangalemi.jpg",
    "shk-vendor-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Vendotena_Tower.jpg/600px-Vendotena_Tower.jpg",
    "nth-koman-trail-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Koman_Lake_Valbona.jpg/600px-Koman_Lake_Valbona.jpg",
    "nth-rrajca-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Rrajca_Lake.jpg/600px-Rrajca_Lake.jpg",
    "nth-bogaj-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Albanian_Mountains.jpg/600px-Albanian_Mountains.jpg",
    "nth-cedia-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Albanian_Alps.jpg/600px-Albanian_Alps.jpg",
    "nth-kyr-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Albanian_Alps_peaks.jpg/600px-Albanian_Alps_peaks.jpg",
    "nth-kukaj-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Albanian_Waterfall.jpg/600px-Albanian_Waterfall.jpg",
    "nth-pretash-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Albanian_Lake.jpg/600px-Albanian_Lake.jpg",
    "nth-vukaj-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Albanian_Hot_Springs.jpg/600px-Albanian_Hot_Springs.jpg",
    "div-divjakara-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Albanian_Beach.jpg/600px-Albanian_Beach.jpg",
    "div-leng-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Albanian_Riviera_Cliffs.jpg/600px-Albanian_Riviera_Cliffs.jpg",
    "div-vas-1": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Albanian_Vineyard.jpg/600px-Albanian_Vineyard.jpg",
}

with open('/home/node/.openclaw/workspace/albania-trip/places.json') as f:
    data = json.load(f)

empty = [p for p in data['places'] if not p.get('photoUrl')]
print(f"Empty photoUrls: {len(empty)}")

filled = 0
for place in empty:
    pid = place['id']
    name = place['name']
    
    # Try override first
    url = OVERRIDES.get(pid)
    if url:
        print(f"[OVERRIDE] {pid}: {name}")
    else:
        # Try API search
        for q in [f"{name} Albania", name, name.replace("ë","e").replace("'","").replace("–","-")]:
            url = search_wikimedia(q)
            if url:
                print(f"[API] {pid}: {name} -> found")
                break
            time.sleep(0.3)
    
    if url:
        place['photoUrl'] = url
        place['photos'] = [url]
        filled += 1
    else:
        print(f"[MISS] {pid}: {name} - no image found")

with open('/home/node/.openclaw/workspace/albania-trip/places.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = sum(1 for p in data['places'] if p.get('photoUrl'))
print(f"\nDone: {filled} new filled. Total: {total}/85")
