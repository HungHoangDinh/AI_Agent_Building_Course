"""Prompt đánh giá cuối cùng Pass | Consider | Reject (FUNCTIONS.md mục 4).

TODO trong file này:
- Thiết kế prompt để LLM đưa ra **kết luận cuối** cho ứng viên dựa trên:
    * total_score, max_score, percentage (kết quả tổng hợp điểm).
    * Danh sách scores (score + comment cho từng câu hỏi).
    * candidate_info (seniority, main_skills, domain, strengths, ...).
- Quy định rõ format output: một JSON object khớp với schema `FinalResult`:
    * level: "Pass" | "Consider" | "Reject"
    * summary: 1–2 câu nhận xét ngắn gọn (lý do, điểm mạnh/yếu chính).
- Hướng dẫn LLM:
    * Không bịa thêm thông tin ngoài dữ liệu cung cấp.
    * Chỉ trả về **JSON duy nhất**, không kèm giải thích.
    * Dùng mức đánh giá hợp lý với percentage và nhận xét chi tiết.
"""

FINAL_EVALUATION_PROMPT = """
TODO: Viết prompt yêu cầu LLM đánh giá cuối (level + summary) dựa trên điểm số và candidate_info, output JSON theo schema FinalResult.
"""
