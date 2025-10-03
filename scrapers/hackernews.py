# scrapers/hackernews.py
import requests
import time

# safe_get function to handle retries
def safe_get(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return requests.get(url, timeout=5).json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(delay)
    return None  # failed after retries

class HackerNewsAPIScraper:
    def __init__(self):
        self.top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    def fetch_top_items(self, limit=30):
        ids = safe_get(self.top_url)
        if ids is None:
            print("Failed to fetch top stories.")
            ids = []
        else:
            ids = ids[:limit]

        items = []
        for i in ids:
            data = safe_get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json")
            if data is None:
                continue
            items.append({
                "title": data.get("title"),
                "url": data.get("url"),
                "score": data.get("score"),
                "by": data.get("by")
            })
            time.sleep(0.5)  # prevent flooding the API
        return items
