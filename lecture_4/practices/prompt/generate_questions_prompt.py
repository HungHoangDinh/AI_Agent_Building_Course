"""Prompt sinh câu hỏi phỏng vấn từ candidate_info (FUNCTIONS.md mục 4).

TODO trong file này:
- Thiết kế prompt để LLM sinh ra 3–5 câu hỏi phỏng vấn kỹ thuật/phù hợp
  dựa trên thông tin ứng viên `candidate_info` (skills, main_skills, domain, seniority...).
- Quy định rõ format output: một JSON object chứa danh sách câu hỏi khớp với
  schema `InterviewQuestions`/`QuestionItem` trong node `generate_questions`:
    * id: string
    * skill: string
    * question: string
    * max_score: number
- Hướng dẫn LLM không trả thêm text ngoài JSON (không giải thích, không comment).
- Có thể thêm ví dụ minh họa nếu muốn, nhưng vẫn đảm bảo cuối cùng chỉ trả về JSON.
"""

GENERATE_QUESTIONS_PROMPT = """
TODO: Viết prompt yêu cầu LLM sinh 3–5 câu hỏi phỏng vấn (JSON, theo schema QuestionItem) dựa trên candidate_info.
"""
