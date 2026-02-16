import os
import shutil
from dotenv import load_dotenv

from langchain_community.document_loaders import (
    DirectoryLoader,
    UnstructuredPDFLoader,
    TextLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if os.path.exists("./chroma_db"):
    shutil.rmtree("./chroma_db")
    print("Old database removed!")

pdf_loader = DirectoryLoader(path="./data",glob="**/*.pdf",loader_cls=UnstructuredPDFLoader)

text_loader = DirectoryLoader(path="./data",glob="**/*.txt",loader_cls=TextLoader)

pdf_docs = pdf_loader.load()
text_docs = text_loader.load()

docs = pdf_docs + text_docs

print(f"Loaded {len(docs)} documents")
#print(docs)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000,chunk_overlap=200)

splitted_docs = text_splitter.split_documents(docs)

print(f"Created {len(splitted_docs)} chunks")
for doc in splitted_docs:
    doc.metadata = {
        "source": doc.metadata.get("source", "unknown")
    }
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
collection_name = "milestone1_collection"

vector_store = Chroma.from_documents(
    documents=splitted_docs,
    embedding=embedding_model,
    persist_directory="./chroma_db",
    collection_name=collection_name
)

print("Milestone 1 Completed Successfully!")
