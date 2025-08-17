#scripts/embed_and_store.py
import json
from app.embedder import QwenEmbedder
from app.vector_store import add_documents

with open("data/chunks.json", "r") as f:
    chunks = json.load(f)

embedder = QwenEmbedder()
vectors = embedder.embed(chunks)

metadata = [{"source": "web"} for _ in chunks]
add_documents(chunks, metadata)

print("All embeddings stored in ChromaDB.")
