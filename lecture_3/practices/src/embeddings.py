"""
Embedding function và vector store (Chroma) cho RAG.
Ingest documents vào vector store để tool retrieval tra cứu.
Tham khảo: lecture_2/src/embeddings.py
"""
from typing import List, Optional

# TODO: Import Chroma từ langchain_chroma
# TODO: Import Document từ langchain_core.documents
# TODO: Import config/settings


# =========================
# OpenAI Embedding Function
# =========================

client = OpenAI(api_key=settings.LLM_API_KEY, base_url=settings.LLM_BASE_URL)


class OpenAIEmbeddingFunction:
    def __init__(self, model: str = "text-embedding-3-large"):
        self.model = model

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        response = client.embeddings.create(
            model=self.model,
            input=texts,
        )
        return [item.embedding for item in response.data]

    def embed_query(self, text: str) -> List[float]:
        response = client.embeddings.create(
            model=self.model,
            input=text,
        )
        return response.data[0].embedding

# =========================
# Vector Store
# =========================

def create_or_get_vector_store(
    collection_name: str = "jobs",
    persist_directory: str = "vector_store",
    delete_existing: bool = False,
):
    """
    Tạo hoặc lấy Chroma vector store.
    
    Args:
        collection_name: Tên collection trong Chroma.
        persist_directory: Thư mục lưu vector store (VD: practices/vector_store).
        delete_existing: Nếu True thì xóa collection cũ rồi tạo mới.
    
    Returns:
        Chroma vector store instance.
    """
    # TODO: Nếu delete_existing: tạo Chroma rồi delete_collection(collection_name)
    # TODO: Return Chroma(persist_directory, collection_name, embedding_function=embeddings)
    raise NotImplementedError("TODO: implement create_or_get_vector_store")


# =========================
# Ingest Documents
# =========================

def ingest_documents(
    collection_name: str = "jobs",
    persist_directory: str = "vector_store",
    documents: Optional[List["Document"]] = None,
):
    """
    Ingest danh sách Document vào vector store.
    
    Args:
        collection_name: Tên collection.
        persist_directory: Thư mục lưu vector store.
        documents: Danh sách Document đã load và split.
    
    Returns:
        Vector store đã add documents.
    """
    # TODO
    raise NotImplementedError("TODO: implement ingest_documents")
