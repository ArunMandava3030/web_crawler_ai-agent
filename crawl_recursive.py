# scripts/crawl_recursive.py

import asyncio
from app.crawl_manager import crawl_recursive
import json

url = input("Enter root URL: ")
depth = int(input("Enter crawl depth: "))
markdown_pages = asyncio.run(crawl_recursive(url, depth=depth))

with open("data/chunks.json", "w") as f:
    json.dump(markdown_pages, f)

print("Done recursive crawling.")
