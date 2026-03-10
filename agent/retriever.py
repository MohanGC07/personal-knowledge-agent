from database.vector_store import VectorStore
from config.settings import TOP_K_RESULTS

class MemoryRetriever:

    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(self, query: str):

        memories = self.vector_store.retrieve_memories(
            query,
            TOP_K_RESULTS
        )

        return "\n".join(memories)