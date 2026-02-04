# Node: Sinh câu hỏi phỏng vấn (FUNCTIONS.md 2.2)

from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional

from prompt import GENERATE_QUESTIONS_PROMPT


class QuestionItem(BaseModel):
    """Một câu hỏi phỏng vấn (id, skill, question, max_score). Các trường có thể rỗng nếu LLM không cung cấp."""
    id: Optional[str] = Field(default=None, description="Id câu hỏi")
    skill: Optional[str] = Field(default=None, description="Kỹ năng được hỏi")
    question: Optional[str] = Field(default=None, description="Nội dung câu hỏi")
    max_score: Optional[float] = Field(default=10.0, description="Điểm tối đa cho câu hỏi")


class InterviewQuestions(BaseModel):
    """Danh sách câu hỏi phỏng vấn (3–5 câu)."""
    questions: list[QuestionItem] = Field(default_factory=list, description="Danh sách câu hỏi")


def generate_interview_questions_node(state: dict) -> dict:
    """Input: candidate_info. Output: questions (list dict), current_question_index = 0; hoặc error nếu lỗi."""
    try:
        candidate_info = state.get("candidate_info") or {}
        # TODO: Gọi LLM (OpenAI) với GENERATE_QUESTIONS_PROMPT + candidate_info, parse JSON -> InterviewQuestions; return {"questions": [q.model_dump() for q in data.questions], "current_question_index": 0}
        return {"questions": [], "current_question_index": 0}
    except Exception as e:
        return {"error": True, "error_message": str(e)}
