from scrapers.hackernews import HackerNewsAPIScraper
from app.models import Item, session

scraper = HackerNewsAPIScraper()
items = scraper.fetch_top_items()

for it in items:
    db_item = Item(title=it["title"], url=it["url"], author=it["by"], score=it["score"])
    session.add(db_item)
session.commit()

print(f"Scraped and stored {len(items)} items!")
