# ✅ FIXED
# app/embedder.py

from sentence_transformers import SentenceTransformer

class QwenEmbedder:
    def __init__(self, model_name="BAAI/bge-small-en"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        texts = [t for t in texts if t.strip()]  # Skip empty strings
        if not texts:
            return []
        instruction_texts = [f"Represent this sentence for retrieval: {t}" for t in texts]
        embeddings = self.model.encode(instruction_texts, convert_to_numpy=True, normalize_embeddings=True)
        return embeddings.tolist()

def get_embeddings(docs):
    embedder = QwenEmbedder()
    texts = [doc["text"] for doc in docs if doc.get("text") and doc["text"].strip() and "sitemap" not in doc["text"].lower()]
    if not texts:
        return [], []
    embeddings = embedder.embed(texts)
    return texts, embeddings