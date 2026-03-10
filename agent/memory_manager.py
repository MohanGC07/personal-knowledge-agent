# agent/memory_manager.py

from agent.memory_extractor import MemoryExtractor
from database.vector_store import VectorStore

class MemoryManager:

    def __init__(self):
        self.extractor = MemoryExtractor()
        self.vector_store = VectorStore()

    def process_input(self, user_input: str):
        """
        Process user input, extract memory, and store in vector DB
        """
        extracted = self.extractor.extract(user_input)

        if extracted:
            memory_text = extracted["memory"]
            importance = extracted["importance"]

            # Store memory with metadata
            self.vector_store.store_memory(
                memory_text,
                metadata={"importance": importance}
            )