# State cho Agent Phỏng vấn Nhân sự (FUNCTIONS.md mục 1)

"""
Các trường trong InterviewState và tác dụng:

- cv_text: Nội dung CV (text) — input ban đầu từ main; dùng cho node trích xuất thông tin ứng viên.
- candidate_info: Thông tin ứng viên trích xuất trong 1 bước (name, years_experience, skills, position, seniority, main_skills, domain, strengths) — output của extract_candidate_info; dùng cho generate_questions và final_evaluation.
- questions: Danh sách câu hỏi phỏng vấn (list dict: id, skill, question, max_score) — output của generate_questions; dùng cho ask_question, score_answer, aggregate_score.
- current_question_index: Chỉ số câu hỏi hiện tại — tăng sau mỗi lần score_answer; dùng cho ask_question, score_answer, routing question_loop_control.
- candidate_answer: Câu trả lời của ứng viên cho câu hỏi hiện tại — nhập từ main (human); dùng cho score_answer và routing route_after_ask.
- scores: Danh sách kết quả chấm từng câu (question_id, score, comment) — append bởi score_answer; dùng cho aggregate_score và final_evaluation.
- messages: Danh sách tin nhắn (list message) — mỗi câu hỏi có một câu trả lời tương ứng: append câu hỏi (role assistant) bởi ask_question, append câu trả lời (role user) khi có candidate_answer; dùng để hiển thị / log toàn bộ Q&A.
- total_score, max_score, percentage: Tổng điểm, điểm tối đa, phần trăm — output của aggregate_score; dùng cho final_evaluation.
- final_result: Kết quả đánh giá cuối — dict có dạng {\"level\": \"Pass|Consider|Reject\", \"summary\": \"1 câu nhận xét ngắn gọn về ứng viên\"}, được tạo bởi node final_evaluation; dùng để in cho HR/nguời phỏng vấn.
- error: Có lỗi hay không (bool) — True khi node báo lỗi; main kiểm tra và xử lý (hiển thị error_message / retry).
- error_message: Thông báo lỗi (string) — nội dung lỗi khi error=True; dùng để hiển thị / log.
"""

from typing import TypedDict, Optional
class Message(TypedDict):
    role: str
    content: str
class InterviewState(TypedDict, total=False):
    cv_text: Optional[str]
    candidate_info: Optional[dict]
    questions: Optional[list]
    current_question_index: Optional[int]
    candidate_answer: Optional[str]
    scores: Optional[list]
    messages: list[Message]
    total_score: Optional[float]
    max_score: Optional[float]
    percentage: Optional[float]
    final_result: Optional[dict]
    error: Optional[bool]  # handle lỗi: True khi node báo lỗi; main kiểm tra và xử lý
    error_message: Optional[str]  # nội dung lỗi khi error=True


__all__ = ["InterviewState", "Message"]
