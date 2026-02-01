"""
Load and split markdown documents for RAG ingest.
Tham khảo: lecture_2/src/loader.py (PyPDFLoader + RecursiveCharacterTextSplitter).
"""
from typing import List

# TODO: Import Document từ langchain_core.documents
# TODO: Import loader phù hợp cho markdown (UnstructuredMarkdownLoader hoặc đọc file + tạo Document)
# TODO: Import RecursiveCharacterTextSplitter từ langchain_text_splitters


def load_and_split(path: str) -> List["Document"]:
    """
    Load file markdown từ path, split thành các chunk.
    
    Args:
        path: Đường dẫn file markdown (VD: data/jobs.md).
    
    Returns:
        Danh sách Document (LangChain) có metadata source (đường dẫn file).
    """
    # TODO: Load file markdown từ path
    # TODO: Split bằng RecursiveCharacterTextSplitter
    # TODO: Đảm bảo mỗi Document có metadata["source"] = path
    raise NotImplementedError("TODO: implement load_and_split for markdown")
