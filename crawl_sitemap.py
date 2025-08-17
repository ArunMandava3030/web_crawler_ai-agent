# scripts/crawl_sitemap.py

import asyncio
from app.crawl_manager import crawl_sitemap
import json

url = input("Enter sitemap URL: ")
markdown_pages = asyncio.run(crawl_sitemap(url))

with open("data/chunks.json", "w") as f:
    json.dump(markdown_pages, f)

print("Done crawling sitemap.")
