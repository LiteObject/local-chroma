class Document:
    def __init__(self, id, metadata=None, text_content=None):
        self.id = id
        self.metadata = metadata if metadata else {}
        self.text_content = text_content if text_content else ""

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def update_text_content(self, new_text):
        self.text_content = new_text

    def __str__(self):
        return f"Document(id={self.id}, metadata={self.metadata}, text_content={self.text_content[:50]}...)"
