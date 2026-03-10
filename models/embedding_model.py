from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL

class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed(self, text: str):
        return self.model.encode(text).tolist()