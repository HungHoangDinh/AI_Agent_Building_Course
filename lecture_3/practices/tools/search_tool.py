"""
Tool 1: Search (DuckDuckGo) — tìm tỷ giá mới nhất từ Internet.
Dùng để trả lời: "1 USD bằng bao nhiêu VND hôm nay?", "Tỷ giá Vietcombank hôm nay".
Tham khảo: lecture_3/main.ipynb (DuckDuckGoSearchRun / DuckDuckGoSearchResults).
"""
# TODO: from langchain_core.tools import tool
# TODO: from langchain_community.tools import DuckDuckGoSearchRun (hoặc DuckDuckGoSearchResults)


# TODO: @tool
def search_internet(query: str) -> str:
    """
    Tìm kiếm thông tin trên Internet (tỷ giá, tin tức...).
    Dùng để lấy tỷ giá mới nhất: VD "1 USD to VND today", "tỷ giá Vietcombank hôm nay".
    
    Args:
        query: Câu hỏi hoặc từ khóa tìm kiếm.
    
    Returns:
        Chuỗi kết quả tìm kiếm cho agent đọc.
    """
    # TODO: Search Bằng DuckDuckGoSearchRun
    raise NotImplementedError("TODO: implement search_internet with DuckDuckGo")
