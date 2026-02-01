"""
Tool 3: Job Retrieval (RAG) — tra cứu vị trí công việc trong dữ liệu đã ingest.
Tìm thông tin JD (Rikkeisoft / jobs.md), có thể kết hợp search tỷ giá + calculator để quy đổi lương sang tiền tệ khác.
"""
import os
import sys
# TODO: @tool
def search_job_positions(query: str, k: int = 5) -> str:
    """
    Tra cứu vị trí công việc trong dữ liệu đã ingest (VD: jobs.md của Rikkeisoft).
    Trả về mô tả công việc, yêu cầu; agent có thể kết hợp với tỷ giá và calculator để quy đổi lương nếu user hỏi.
    
    Args:
        query: Từ khóa vị trí (VD: "Frontend Developer", "Backend Python", "DevOps").
        k: Số chunk trả về (mặc định 5).
    
    Returns:
        Chuỗi đã format: nội dung các Document liên quan (title/source + content).
    """
    # TODO: docs = get_retriever(query, k=k)
    # TODO: Format docs thành chuỗi (VD: "Document 1 (source: ...):\n{content}\n\nDocument 2: ...")
    # TODO: return formatted string
    raise NotImplementedError("TODO: implement search_job_positions using get_retriever")
