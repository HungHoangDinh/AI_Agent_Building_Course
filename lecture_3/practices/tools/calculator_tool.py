"""
Tool 2: Calculator (LLM-Math) — tính toán chính xác số tiền × tỷ giá.
Tránh lỗi LLM khi tính số lớn (VD: 100.000.000 VND).
Có thể dùng: langchain_community.tools (Calculator) hoặc numexpr.
"""
# TODO: from langchain_core.tools import tool
# TODO: from langchain_community.tools import Calculator (hoặc dùng numexpr trong @tool)


# TODO: @tool
def calculate(expression: str) -> str:
    """
    Tính toán biểu thức toán học (số, +, -, *, /).
    Dùng để nhân/chia số tiền với tỷ giá (VD: 50000 * 25000, 100000000 / 25000).
    
    Args:
        expression: Biểu thức toán (VD: "50000 * 25000").
    
    Returns:
        Kết quả tính toán dạng chuỗi.
    """
    # TODO: Dùng Calculator tool của langchain_community hoặc:
    #       import numexpr; return str(numexpr.evaluate(expression.strip()))
    # TODO: Xử lý ngoại lệ (biểu thức không hợp lệ) và trả về thông báo lỗi rõ ràng
    raise NotImplementedError("TODO: implement calculate (Calculator / LLM-Math)")
