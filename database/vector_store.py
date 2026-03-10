import chromadb
from config.settings import CHROMA_DB_PATH
from models.embedding_model import EmbeddingModel

class VectorStore:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.client = chromadb.Client(
            chromadb.config.Settings(
                persist_directory=CHROMA_DB_PATH
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="memory_store"
        )

    def store_memory(self, text: str):

        embedding = self.embedding_model.embed(text)

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(hash(text))]
        )

    def retrieve_memories(self, query: str, top_k=3):

        embedding = self.embedding_model.embed(query)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return results["documents"][0]
    
    def get_all_memories(self):
        results = self.collection.get()
        return results.get("documents", [])

    def clear_memories(self):
        all_items = self.collection.get()

        if all_items["ids"]:
            self.collection.delete(ids=all_items["ids"])