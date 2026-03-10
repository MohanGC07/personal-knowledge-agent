# agent/memory_extractor.py

class MemoryExtractor:
    def __init__(self):
        # Keywords to detect user memories
        self.keywords = [
            "i like",
            "i love",
            "i work",
            "i study",
            "my favorite",
            "i prefer"
        ]

    def extract(self, text: str):
        """
        Extracts memory from user text and computes importance score.

        Returns:
            dict or None: {
                "memory": str,
                "importance": float  # between 0 and 1
            }
        """
        text_lower = text.lower()
        score = 0

        # Check keyword matches
        for k in self.keywords:
            if k in text_lower:
                score += 1

        if score > 0:
            # Normalize importance: simple formula
            importance = min(1.0, score / len(self.keywords) + len(text) / 200)
            return {
                "memory": text.strip(),
                "importance": round(importance, 2)
            }

        return None