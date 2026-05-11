#!/usr/bin/env python3
"""
Fetch photos from Wikimedia Commons for Albania trip places.
Uses Wikimedia Search API + ImageInfo API.
Note: validate_url is skipped because upload.wikimedia.org returns 403 from this
NAS network environment — but URLs are valid for end-user browsers.
"""
import json
import time
import urllib.request
import urllib.parse


def _api_request(url):
    """Make Wikimedia API request with proper User-Agent."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "AlbaniaTripBot/1.0 (Kigochen NAS; contact@example.com)",
        "Accept": "application/json"
    })
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def search_wikimedia(query):
    """Search Wikimedia Commons for images. Returns (pageid, title) or None."""
    url = (f"https://commons.wikimedia.org/w/api.php?action=query&list=search"
           f"&srsearch={urllib.parse.quote(query)}+Albania&srnamespace=6"
           f"&format=json&origin=*")
    try:
        data = _api_request(url)
        results = data.get("query", {}).get("search", [])
        if results:
            return results[0]["pageid"], results[0]["title"]
    except Exception as e:
        print(f"  Search failed for '{query}': {e}")
    return None, None


def get_image_url(pageid):
    """Get thumbnail URL (800px) for a Wikimedia pageid. Returns URL or None."""
    url = (f"https://commons.wikimedia.org/w/api.php?action=query&pageids={pageid}"
           f"&prop=imageinfo&iiprop=url|thumburl&iiurlwidth=800&format=json&origin=*")
    try:
        data = _api_request(url)
        pages = data.get("query", {}).get("pages", {})
        page = pages.get(str(pageid), {})
        imageinfo = page.get("imageinfo", [])
        if imageinfo:
            # Prefer thumburl (smaller, faster), fallback to full url
            return imageinfo[0].get("thumburl") or imageinfo[0].get("url")
    except Exception as e:
        print(f"  ImageInfo failed for pageid {pageid}: {e}")
    return None


def main():
    with open("places.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    places = data["places"]
    total = len(places)
    filled = 0
    failed = []

    for i, place in enumerate(places):
        if place.get("photoUrl"):
            print(f"[{i+1}/{total}] SKIP {place['name']} — already has photoUrl")
            continue

        name = place["name"]
        print(f"[{i+1}/{total}] FETCH {name}...")

        pageid, title = search_wikimedia(name)
        if not pageid:
            print(f"  -> No search result for '{name}', skipping")
            failed.append((i+1, name, "no search result"))
            time.sleep(0.5)
            continue

        image_url = get_image_url(pageid)
        if not image_url:
            print(f"  -> No image URL for pageid {pageid}, skipping")
            failed.append((i+1, name, f"no image for pageid {pageid}"))
            time.sleep(0.5)
            continue

        place["photoUrl"] = image_url
        place["photos"] = [image_url]
        filled += 1
        print(f"  -> SUCCESS [{title}]: {image_url}")
        time.sleep(0.5)

    with open("places.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n=== DONE: {filled}/{total} places filled ===")
    if failed:
        print(f"Failed ({len(failed)}):")
        for idx, name, reason in failed:
            print(f"  [{idx}] {name}: {reason}")


if __name__ == "__main__":
    main()
