# scripts/crawl_single.py

import asyncio
from app.crawl_manager import crawl_single_page
import json

url = input("Enter URL to crawl: ")
markdown = asyncio.run(crawl_single_page(url))

with open("data/chunks.json", "w") as f:
    json.dump([markdown], f)

print("Done crawling single page.")
