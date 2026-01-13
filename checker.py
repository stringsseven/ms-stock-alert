import requests
from bs4 import BeautifulSoup
import os

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

PRODUCTS = {
    "Cashmere Jumper (XS/S)": {
        "url": "https://www.marksandspencer.com/textured-fringe-wool-cashmere-jumper/p/clp60769872",
        "sizes": ["extra small", "small"]
    },
    "Borg Zip Fleece": {
        "url": "https://www.marksandspencer.com/borg-printed-funnel-neck-zip-up-fleece-jacket/p/clp60723770",
        "sizes": ["6", "8", "10", "12"]
    },
    "Borg Funnel Fleece": {
        "url": "https://www.marksandspencer.com/borg-printed-funnel-neck-fleece-jacket/p/clp60762136",
        "sizes": ["6", "8", "10", "12"]
    },
    "Padded Hood Jacket": {
        "url": "https://www.marksandspencer.com/wool-blend-textured-padded-hood-jacket/p/clp60761866?color=BROWN",
        "sizes": ["6", "8", "10", "12"]
    },
    "Faux Fur Jacket": {
        "url": "https://www.marksandspencer.com/faux-fur-animal-print-collarless-jacket/p/clp60761283",
        "sizes": ["6", "8", "10", "12"]
    },
    "Fair Isle Jumper": {
        "url": "https://www.marksandspencer.com/cable-knit-fair-isle-crew-neck-jumper/p/clp60762457",
        "sizes": ["6", "8", "10", "12"]
    }
}

HEADERS = {"User-Agent": "Mozilla/5.0"}

def send(msg):
    requests.post(WEBHOOK, json={"content": msg})

for name, data in PRODUCTS.items():
    r = requests.get(data["url"], headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")
    page = soup.get_text().lower()

    for size in data["sizes"]:
        if size.lower() in page and "out of stock" not in page:
            send(f"🟢 **{name} — size {size.upper()} may be back in stock!**\n{data['url']}")
