import requests
from bs4 import BeautifulSoup
import csv

URL = "https://pocket.shonenmagazine.com/ranking/31"
HEADERS = {
"User-Agent": "Mozilla/5.0 (compatible; magapoke-scraper/1.0)"
}

def fetch_titles(url=URL):
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # タイトル要素を上から順に抽出（=ランキング順）
    h3s = soup.select("h3.c-ranking-item__ttl")
    titles = [h.get_text(strip=True) for h in h3s if h.get_text(strip=True)]
    return titles

def main():
    titles = fetch_titles()
    rows = [{"rank": i+1, "title": t} for i, t in enumerate(titles)]
    with open("magapoke_ranking_titles.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["rank","title"])
        w.writeheader()
        w.writerows(rows)
    print(f"saved {len(rows)} rows")

if __name__ == "__main__":
    main()
