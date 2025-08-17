#app/rag_agent.py

from app.embedder import QwenEmbedder
from app.vector_store import ChromaStore

embedder = QwenEmbedder()
store = ChromaStore()

def answer_query(query: str):
    query_vec = embedder.embed([query])[0]
    results = store.query(query_vec)  # pass the embedding directly
    docs = results['documents'][0]
    return "\n\n".join(docs)
