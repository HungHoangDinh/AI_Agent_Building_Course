# Node: Đánh giá cuối (FUNCTIONS.md 2.7) — gọi LLM với FINAL_EVALUATION_PROMPT

from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional

from prompt import FINAL_EVALUATION_PROMPT


class FinalResult(BaseModel):
    """Kết quả đánh giá cuối (level: Pass | Consider | Reject, summary). Các trường có thể rỗng."""
    level: Optional[str] = Field(default=None, description="Pass | Consider | Reject")
    summary: Optional[str] = Field(default=None, description="Tóm tắt đánh giá")


def final_evaluation_node(state: dict) -> dict:
    """Input: total_score, percentage, scores, candidate_info. Output: final_result = { level, summary }; hoặc error nếu lỗi."""
    try:
        total_score = state.get("total_score", 0)
        percentage = state.get("percentage", 0.0)
        scores = state.get("scores") or []
        candidate_info = state.get("candidate_info") or {}

        # TODO: Gọi LLM (OpenAI) với FINAL_EVALUATION_PROMPT + total_score, percentage, scores, candidate_info; parse JSON -> FinalResult; return {"final_result": result.model_dump()}.
        return {"final_result": {"level": "", "summary": ""}}
    except Exception as e:
        return {"error": True, "error_message": str(e)}
