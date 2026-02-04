"""Prompts cho Agent Phỏng vấn Nhân sự.

Mỗi prompt được tách ra một file riêng để dễ quản lý.
File này chỉ làm nhiệm vụ re-export cho các import kiểu:

    from prompt import EXTRACT_CANDIDATE_INFO_PROMPT
"""

from .extract_candidate_info_prompt import EXTRACT_CANDIDATE_INFO_PROMPT
from .generate_questions_prompt import GENERATE_QUESTIONS_PROMPT
from .score_answer_prompt import SCORE_ANSWER_PROMPT
from .final_evaluation_prompt import FINAL_EVALUATION_PROMPT

__all__ = [
    "EXTRACT_CANDIDATE_INFO_PROMPT",
    "GENERATE_QUESTIONS_PROMPT",
    "SCORE_ANSWER_PROMPT",
    "FINAL_EVALUATION_PROMPT",
]
