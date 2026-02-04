# Node: Chấm câu trả lời (FUNCTIONS.md 2.4)

from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional

from prompt import SCORE_ANSWER_PROMPT


class ScoreItem(BaseModel):
    """Kết quả chấm một câu trả lời (question_id, score, comment). Các trường có thể rỗng."""
    question_id: Optional[str] = Field(default=None, description="Id câu hỏi")
    score: Optional[float] = Field(default=0.0, description="Điểm chấm")
    comment: Optional[str] = Field(default=None, description="Nhận xét")


def score_answer_node(state: dict) -> dict:
    """Input: candidate_answer, questions, current_question_index, scores. Output: append { question_id, score, comment } vào scores; hoặc error nếu lỗi."""
    try:
        candidate_answer = state.get("candidate_answer") or ""
        questions = state.get("questions") or []
        idx = state.get("current_question_index", 0)
        scores = list(state.get("scores") or [])

        # TODO: Gọi LLM (OpenAI) với SCORE_ANSWER_PROMPT + câu hỏi hiện tại (questions[idx]) + candidate_answer, parse JSON -> ScoreItem; append ScoreItem.model_dump() vào scores.
        # TODO: Append câu trả lời (role user) vào messages 
        return {"scores": scores}
    except Exception as e:
        return {"error": True, "error_message": str(e)}
