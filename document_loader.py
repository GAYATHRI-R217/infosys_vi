from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    UnstructuredPDFLoader
)

DATA_DIR = "data"

def load_all_documents():
    """Load all supported files from data folder"""

    pdf_loader = DirectoryLoader(
        DATA_DIR,
        glob="**/*.pdf",
        loader_cls=UnstructuredPDFLoader
    )

    text_loader = DirectoryLoader(
        DATA_DIR,
        glob="**/*.txt",
        loader_cls=TextLoader
    )

    docs = pdf_loader.load() + text_loader.load()
    return docs