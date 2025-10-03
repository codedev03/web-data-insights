# analytics.py
from collections import Counter
from urllib.parse import urlparse
import re
from datetime import datetime
from app.models import session, Item
import plotly.express as px
import pandas as pd
import webbrowser
import os
# Fetch all items once
items = session.query(Item).all()

# --- Filter by domain ---
domain_filter = "github.com"
domain_filtered_items = [it for it in items if urlparse(it.url).netloc == domain_filter]
print(f"Posts from {domain_filter}: {len(domain_filtered_items)}")

# --- Filter by keyword in title ---
keyword = "ai"
keyword_filtered_items = [it for it in items if keyword.lower() in it.title.lower()]
print(f"Posts containing '{keyword}': {len(keyword_filtered_items)}")

# --- Top domains ---
domains = [urlparse(it.url).netloc for it in items]
top_domains = Counter(domains).most_common(5)
print("Top 5 domains:", top_domains)
top_domains_df = pd.DataFrame(top_domains, columns=['domain', 'count'])
fig_domains = px.bar(top_domains_df, x='domain', y='count', title='Top 5 Domains')
domains_html = fig_domains.to_html(full_html=False, include_plotlyjs='cdn')

# --- Most common words in titles ---
titles = [it.title for it in items]
stopwords = {"the","of","and","in","with","a","i","to","for"}
words = [w for w in re.findall(r'\w+', " ".join(titles).lower()) if w not in stopwords]
top_words = Counter(words).most_common(10)
print("Top 10 meaningful title words:", top_words)
top_words_df = pd.DataFrame(top_words, columns=['word','count'])
fig_words = px.bar(top_words_df, x='word', y='count', title='Top 10 Words in Titles')
words_html = fig_words.to_html(full_html=False, include_plotlyjs=False)

# --- Top scoring posts ---
top_score_items = sorted(items, key=lambda x: x.score or 0, reverse=True)[:5]
print("\nTop scoring posts:")
for item in top_score_items:
    print(f"{item.title} | Score: {item.score}")

top_score_df = pd.DataFrame({
    'title': [item.title[:30] + ("..." if len(item.title) > 30 else "") for item in top_score_items],
    'score': [item.score for item in top_score_items]
})
fig_scores = px.bar(top_score_df, x='title', y='score', title='Top 5 Scoring Posts')
scores_html = fig_scores.to_html(full_html=False, include_plotlyjs=False)

# --- Generate the dashboard HTML ---
with open("dash.html", "w", encoding="utf-8") as f:
    f.write(f"""
    <html>
    <head>
        <title>Hacker News Analytics Dashboard</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h2 {{ color: #333; }}
            .chart {{ margin-bottom: 50px; }}
        </style>
    </head>
    <body>
        <h1>Hacker News Analytics Dashboard</h1>

        <p><strong>Posts from {domain_filter}:</strong> {len(domain_filtered_items)}</p>
        <p><strong>Posts containing '{keyword}':</strong> {len(keyword_filtered_items)}</p>

        <div class="chart">
            <h2>Top Domains</h2>
            {domains_html}
        </div>

        <div class="chart">
            <h2>Top Words in Titles</h2>
            {words_html}
        </div>

        <div class="chart">
            <h2>Top Scoring Posts</h2>
            {scores_html}
        </div>
    </body>
    </html>
    """)

print("Dashboard created: dash.html")
# Assuming dash.html is in the same folder as analytics.py
dashboard_path = os.path.abspath("dash.html")
webbrowser.open(f"file://{dashboard_path}")

print(f"Dashboard opened in browser: {dashboard_path}")