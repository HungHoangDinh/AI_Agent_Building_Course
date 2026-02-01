"""
Retriever: tra cứu document từ vector store theo query.
Dùng bởi tool job_retrieval_tool để tra cứu vị trí công việc trong dữ liệu đã ingest.
Tham khảo: lecture_2/src/retriever.py
"""
from typing import List

# TODO: Import Document từ langchain_core.documents
# TODO: Import create_or_get_vector_store từ src.embeddings


def get_retriever(query: str, k: int = 5, persist_directory: str = None) -> List["Document"]:
    """
    Tra cứu k document liên quan nhất với query trong vector store.
    
    Args:
        query: Câu hỏi hoặc từ khóa (VD: "Frontend Developer", "Backend Python").
        k: Số document trả về (mặc định 5).
        persist_directory: Thư mục vector store (phải trùng với ingest; VD: practices/vector_store).
    
    Returns:
        Danh sách Document (LangChain) liên quan đến query.
    """
    # TODO Tạo hàm search từ vector store.
    raise NotImplementedError("TODO: implement get_retriever")
