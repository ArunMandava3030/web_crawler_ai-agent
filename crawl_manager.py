# ✅ FIXED VERSION
# app/crawl_manager.py

import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai import CacheMode
from bs4 import BeautifulSoup

def extract_meaningful_text(raw_text):
    if not raw_text:
        return ""
    soup = BeautifulSoup(raw_text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

async def crawl_single_page(url: str):
    browser_cfg = BrowserConfig(headless=True, verbose=False)
    run_cfg = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result = await crawler.arun(url=url, config=run_cfg)

    content = result.markdown.raw_markdown if result.markdown and result.markdown.raw_markdown else result.text
    if content:
        clean_text = extract_meaningful_text(content)
        return [{"text": clean_text, "url": url}] if clean_text.strip() else []
    return []

async def crawl_sitemap(url: str):
    browser_cfg = BrowserConfig(headless=True)
    run_cfg = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        try:
            results = await crawler.arun_many(urls=[url], config=run_cfg)
        except Exception as e:
            print(f"[ERROR] Exception while crawling sitemap: {e}")
            return []

    pages = []
    for res in results:
        content = res.markdown.raw_markdown if res.markdown and res.markdown.raw_markdown else res.text
        if content:
            clean_text = extract_meaningful_text(content)
            if clean_text.strip():
                pages.append({"text": clean_text, "url": res.url})
    return pages

async def crawl_recursive(url: str, depth: int = 2):
    return await crawl_sitemap(url)

def smart_crawl(url: str, mode: str = "recursive"):
    try:
        if mode == "single":
            return asyncio.run(crawl_single_page(url))
        elif mode == "sitemap":
            return asyncio.run(crawl_sitemap(url))
        else:
            docs = asyncio.run(crawl_recursive(url))
            if not docs:
                print("[WARN] Recursive crawl failed. Trying single page instead.")
                return asyncio.run(crawl_single_page(url))
            return docs
    except Exception as e:
        print(f"[ERROR] Crawling failed: {e}")
        return []



