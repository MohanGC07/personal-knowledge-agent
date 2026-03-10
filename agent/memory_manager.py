from agent.memory_extractor import MemoryExtractor
from database.vector_store import VectorStore

class MemoryManager:

    def __init__(self):

        self.extractor = MemoryExtractor()
        self.vector_store = VectorStore()

    def process_input(self, user_input: str):

        memory = self.extractor.extract(user_input)

        if memory:
            self.vector_store.store_memory(memory)