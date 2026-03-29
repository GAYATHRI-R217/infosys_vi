import os
import shutil
from dotenv import load_dotenv

from loaders.document_loader import load_all_documents

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

DATA_DIR = "data"
DB_DIR = "chroma_db"

def cleanup():
    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)
        print("Old DB removed")


def clean_metadata(docs):
    for d in docs:
        d.metadata = {k: str(v) for k, v in d.metadata.items()}
    return docs
def split_docs(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")
    return chunks
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
def store_vectors(chunks, embeddings):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR,
        collection_name="doc_collection"
    )

    vectordb.persist()
    print("Vectors stored successfully")
if __name__ == "__main__":

    cleanup()

    docs = load_all_documents()
    print(f"Loaded {len(docs)} documents")

    if len(docs) == 0:
        print("No documents found inside data folder")
        exit()

    docs = clean_metadata(docs)
    chunks = split_docs(docs)

    embeddings = get_embeddings()
    store_vectors(chunks, embeddings)

    print("INGESTION COMPLETE")