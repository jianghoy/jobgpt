from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from typing import List

class StringLoader(BaseLoader):
    """Load text files for LangChain."""

    def __init__(self, s:str):
        """Initialize with string pass in as input."""
        self.s = s

    def load(self) -> List[Document]:
        metadata = {"source": "no source"}
        return [Document(page_content=self.s, metadata=metadata)]