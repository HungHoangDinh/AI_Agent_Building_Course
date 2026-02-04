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

        # TODO:
        # - Lấy câu hỏi hiện tại: current_question = questions[idx]
        # - Tạo prompt từ SCORE_ANSWER_PROMPT + current_question + candidate_answer.
        # - Gọi LLM (OpenAI) để chấm điểm và nhận xét, yêu cầu trả về JSON theo schema ScoreItem.
        # - Parse JSON:
        #       item = ScoreItem(**json_data)
        #       scores.append(item.model_dump())
        # - Nếu bạn có giữ lịch sử hội thoại trong state["messages"], hãy append
        #   câu trả lời của ứng viên (role="user") và/hoặc kết quả chấm (role="assistant")
        #   tuỳ thiết kế.
        # - Cuối cùng trả về dict mới chứa "scores" đã được cập nhật.

        raise NotImplementedError(
            "score_answer_node chưa được cài đặt, hãy tự triển khai logic chấm điểm với LLM."
        )
    except Exception as e:
        return {"error": True, "error_message": str(e)}
