# app/vector_store.py
import chromadb
from chromadb.utils import embedding_functions

class ChromaStore:
    def __init__(self, persist_directory="chromadb_data"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="web_embeddings",
            embedding_function=None  # We're manually passing embeddings
        )

    def add(self, documents, embeddings, metadatas=None):
        if len(documents) != len(embeddings):
            raise ValueError("Documents and embeddings count mismatch")

        ids = [f"doc_{i}" for i in range(len(documents))]
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,  # <-- Already lists, no need to call .tolist()
            metadatas=metadatas or [{} for _ in documents]
        )

    def query(self, query_embedding, top_k=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results
