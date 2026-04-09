from langchain_huggingface import HuggingFaceEmbeddings
import os

# Disable SSL verification for HuggingFace if needed (corporate proxy)
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["HF_HUB_DISABLE_SSL"] = "true"

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={
            "trust_remote_code": True,
            "local_files_only": True
        }
    )