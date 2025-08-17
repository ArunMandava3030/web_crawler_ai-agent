#scripts/run_pipeline.py
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.crawl_manager import smart_crawl
from app.embedder import get_embeddings
from app.vector_store import ChromaStore

def main(url):
    print(f"\n🔍 Crawling: {url}")
    
    # Step 1: Crawl the website
    docs = smart_crawl(url)
    print(f"✅ Extracted {len(docs)} documents")

    # Step 2: Convert to embeddings
    documents, embeddings = get_embeddings(docs)
    print(f"🧠 Generated {len(embeddings)} embeddings")

    # Step 3: Store in ChromaDB
    metadatas = [{"source": url} for _ in documents]

    store = ChromaStore()
    store.add(documents, embeddings, metadatas)
    print(f"📦 Stored embeddings in ChromaDB")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/run_pipeline.py <URL>")
        sys.exit(1)

    input_url = sys.argv[1]
    main(input_url)
