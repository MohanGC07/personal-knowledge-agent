class MemoryExtractor:

    def __init__(self):

        self.keywords = [
            "i like",
            "i love",
            "i work",
            "i study",
            "my favorite",
            "i prefer"
        ]

    def extract(self, text: str):

        text_lower = text.lower()

        for k in self.keywords:
            if k in text_lower:
                return text

        return None