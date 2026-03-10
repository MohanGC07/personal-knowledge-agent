# models/embedding_model.py

from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL

class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed(self, texts):
        """
        Embed single text or list of texts.
        Returns list of embeddings.
        """
        if isinstance(texts, str):
            # Single string -> return embedding as list
            return self.model.encode(texts).tolist()
        elif isinstance(texts, list):
            # List of strings -> return list of embeddings
            return [emb.tolist() for emb in self.model.encode(texts)]
        else:
            raise ValueError("Input must be a string or list of strings")