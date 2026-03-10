# database/vector_store.py

import os
import chromadb
from config.settings import CHROMA_DB_PATH
from models.embedding_model import EmbeddingModel

class VectorStore:

    def __init__(self):
        self.embedding_model = EmbeddingModel()

        # Ensure the directory exists
        os.makedirs(CHROMA_DB_PATH, exist_ok=True)

        self.client = chromadb.Client(
            chromadb.config.Settings(
                persist_directory=CHROMA_DB_PATH
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="memory_store",
            metadata={"description": "Stores user memories with importance scores"}
        )

    def store_memory(self, text: str, metadata: dict = None):
        """
        Store a memory with optional metadata (like importance)
        """
        embedding = self.embedding_model.embed(text)

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(hash(text))],
            metadatas=[metadata or {}]
        )

    def retrieve_memories(self, query: str, top_k: int = 3):
        """
        Retrieve top_k memories relevant to the query
        """
        embedding = self.embedding_model.embed(query)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        # return the list of documents
        return results.get("documents", [[]])[0]

    def get_all_memories(self):
        """
        Fetch all stored memories
        """
        results = self.collection.get()
        return results.get("documents", [])

    def clear_memories(self):
        """
        Delete all memories from collection
        """
        all_items = self.collection.get()
        if all_items.get("ids"):
            self.collection.delete(ids=all_items["ids"])