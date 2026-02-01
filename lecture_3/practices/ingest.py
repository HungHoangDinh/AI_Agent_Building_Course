"""
Script ingest dữ liệu markdown (jobs.md) vào vector store.
Chạy file này trước khi dùng tool Job Retrieval trong agent.
Tham khảo: lecture_2/ingest.py
"""
import os

# TODO: Import load_and_split từ src.loader
# TODO: Import ingest_documents từ src.embeddings


def ingest_documents_from_markdown(
    path: str,
    ingest_directory: str = "vector_store",
    collection_name: str = "jobs",
) -> None:
    """
    Load file markdown từ path, split, embed và ingest vào vector store.
    
    Args:
        path: Đường dẫn file markdown (VD: data/jobs.md).
        ingest_directory: Thư mục lưu vector store (có thể nằm trong practices/).
        collection_name: Tên collection trong Chroma.
    """
    # TODO:
    raise NotImplementedError("TODO: implement ingest_documents_from_markdown")


if __name__ == "__main__":
    # Đường dẫn tương đối từ thư mục practices/
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "jobs.md")
    vector_dir = os.path.join(base_dir, "vector_store")
    
    # TODO: Gọi ingest_documents_from_markdown
    pass  # TODO: uncomment sau khi implement
