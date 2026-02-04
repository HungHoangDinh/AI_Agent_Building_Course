# Node: Đánh giá cuối (FUNCTIONS.md 2.7) — gọi LLM với FINAL_EVALUATION_PROMPT

from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional

from prompt import FINAL_EVALUATION_PROMPT


class FinalResult(BaseModel):
    """Kết quả đánh giá cuối cho ứng viên.

    - level: Pass | Consider | Reject
    - summary: 1–2 câu nhận xét ngắn gọn (ví dụ: lý do pass/reject, điểm mạnh/yếu chính).
    """
    level: Optional[str] = Field(default=None, description="Pass | Consider | Reject")
    summary: Optional[str] = Field(
        default=None,
        description="Một câu nhận xét/ngắn gọn về ứng viên (cho HR/manager đọc nhanh).",
    )


def final_evaluation_node(state: dict) -> dict:
    """Input: total_score, percentage, scores, candidate_info.

    Output:
        final_result = { level, summary } — trong đó:
        - level   = Pass | Consider | Reject
        - summary = 1–2 câu đánh giá ngắn gọn về ứng viên (dựa trên điểm và CV).
    Hoặc trả về { error, error_message } nếu lỗi.
    """
    try:
        total_score = state.get("total_score", 0)
        percentage = state.get("percentage", 0.0)
        scores = state.get("scores") or []
        candidate_info = state.get("candidate_info") or {}

        # TODO gợi ý triển khai:
        # - Khởi tạo OpenAI client theo config của bạn.
        # - Tạo prompt từ FINAL_EVALUATION_PROMPT, truyền vào:
        #     + total_score, max_score (nếu có), percentage
        #     + toàn bộ danh sách scores (score/comment từng câu)
        #     + candidate_info (seniority, main_skills, domain, strengths, ...)
        # - Yêu cầu LLM trả về JSON khớp schema FinalResult (level, summary).
        # - Parse JSON:
        #       result = FinalResult(**json_data)
        #       return {"final_result": result.model_dump()}

        raise NotImplementedError(
            "final_evaluation_node chưa được cài đặt, hãy tự triển khai logic gọi LLM để đánh giá cuối."
        )
    except Exception as e:
        return {"error": True, "error_message": str(e)}
