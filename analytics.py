# analytics.py
from collections import Counter
from urllib.parse import urlparse
import re
from app.models import session, Item

# Top domains
domains = [urlparse(it.url).netloc for it in session.query(Item).all()]
top_domains = Counter(domains).most_common(5)
print("Top 5 domains:", top_domains)

# Most common words in titles
titles = [it.title for it in session.query(Item).all()]
stopwords = {"the","of","and","in","with","a","i","to","for"}
words = [w for w in re.findall(r'\w+', " ".join(titles).lower()) if w not in stopwords]
top_words = Counter(words).most_common(10)
print("Top 10 meaningful title words:", top_words)
