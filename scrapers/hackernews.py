import requests

class HackerNewsAPIScraper:
    def __init__(self):
        self.top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    def fetch_top_items(self, limit=30):
        ids = requests.get(self.top_url).json()[:limit]
        items = []
        for i in ids:
            data = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json").json()
            items.append({
                "title": data.get("title"),
                "url": data.get("url"),
                "score": data.get("score"),
                "by": data.get("by")
            })
        return items

if __name__ == "__main__":
    scraper = HackerNewsAPIScraper()
    items = scraper.fetch_top_items()
    for it in items:
        print(it["title"], "|", it["url"])
