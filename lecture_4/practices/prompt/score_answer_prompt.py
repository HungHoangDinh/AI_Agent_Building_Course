"""Prompt chấm điểm câu trả lời cho từng câu hỏi (FUNCTIONS.md mục 4).

TODO trong file này:
- Thiết kế prompt để LLM **chấm điểm và nhận xét** cho một câu trả lời của ứng viên
  dựa trên:
    * Nội dung câu hỏi (question)
    * Thông tin kỹ năng / tiêu chí (skill, max_score)
    * Câu trả lời của ứng viên (candidate_answer)
- Quy định rõ format output: một JSON object khớp với schema `ScoreItem`
  trong node `score_answer`:
    * question_id: string
    * score: number
    * comment: string
- Hướng dẫn LLM:
    * Không bịa thêm thông tin ngoài những gì ứng viên trả lời.
    * Chỉ trả về **JSON duy nhất**, không giải thích hoặc text ngoài JSON.
    * Điểm `score` phải nằm trong khoảng [0, max_score].
"""

SCORE_ANSWER_PROMPT = """
TODO: Viết prompt yêu cầu LLM chấm điểm (score) và nhận xét (comment) cho một câu trả lời, trả về JSON theo schema ScoreItem.
"""
