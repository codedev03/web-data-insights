# Web Data Insights – Hacker News Scraper & Analytics
## Dashboard

You can view the interactive dashboard output here: [Dashboard PDF](docs/dash.pdf)
## Overview

This project collects, stores, and analyzes top stories from [Hacker News](https://news.ycombinator.com/) using Python. It demonstrates **data collection, database management, and basic data analysis** without requiring a web dashboard.

The project includes:

- **Scraping top posts** via Hacker News API
- **Storing posts** in a SQLite database
- **Analyzing trends** such as top domains and most common keywords

---

## Features

1. **Data Collection**  
   - Fetches top 30 Hacker News posts using the Hacker News API.
   - Collects `title`, `url`, `author`, and `score`.

2. **Database Storage**  
   - Uses SQLAlchemy to store posts in a SQLite database (`items` table).
   - Makes future querying and analysis simple and scalable.

3. **Data Analysis**  
   - Finds **top domains** from URLs.
   - Finds **top meaningful words** in post titles, ignoring common stopwords.
   - Optional: Can analyze top-scoring posts or create time-based insights.

---

## Folder Structure
web-data-insights/
├─ app/
│ ├─ init.py
│ ├─ models.py
├─ scrapers/
│ ├─ init.py
│ ├─ hackernews.py
├─ scrape_and_store.py
├─ analytics.py
├─ create_tables.py
├─ requirements.txt
├─ .gitignore
├─ README.md
## Installation
1. **Clone the repository**

git clone https://github.com/yourusername/web-data-insights.git
cd web-data-insights
2.**Create a virtual environment**
python -m venv virt
virt\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
Usage
1.Create the database tables
python create_tables.py
2.Scrape Hacker News and store items
python scrape_and_store.py
Example output:
Scraped and stored 30 items!
3.Run analytics
python analytics.py
Example output:
Top 5 domains: [('github.com', 6), ('entropicthoughts.com', 2), ...]
Top 10 meaningful title words: [('ai', 3), ('go', 2), ('curl', 2), ...]
