from typing import List, Optional

from langchain_chroma import Chroma
from langchain_core.documents import Document
from openai import OpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import settings


# =========================
# OpenAI Embedding Function
# =========================

client = OpenAI(api_key=settings.LLM_API_KEY, base_url=settings.LLM_BASE_URL)

# =========================
# Initialize Embeddings
# =========================

embeddings = GoogleGenerativeAIEmbeddings(
    api_key=settings.LLM_API_KEY,
    model=settings.LLM_EMBEDDING_MODEL
)


# =========================
# Vector Store
# =========================

def create_or_get_vector_store(
    collection_name: str = "documents",
    persist_directory: str = "vector_store",
    delete_existing: bool = False,
):
    if delete_existing:
        Chroma(
            persist_directory=persist_directory,
            collection_name=collection_name,
            embedding_function=embeddings,
        ).delete_collection(collection_name)

    return Chroma(
        persist_directory=persist_directory,
        collection_name=collection_name,
        embedding_function=embeddings,
    )


# =========================
# Ingest Documents
# =========================

def ingest_documents(
    collection_name: str = "documents",
    persist_directory: str = "vector_store",
    documents: Optional[List[Document]] = None,
):
    if not documents:
        raise ValueError("documents must not be None or empty")

    vector_store = create_or_get_vector_store(
        collection_name=collection_name,
        persist_directory=persist_directory,
    )

    vector_store.add_documents(documents)
    return vector_store
