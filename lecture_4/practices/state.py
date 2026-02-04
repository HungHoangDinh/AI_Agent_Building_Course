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
- final_result: Kết quả đánh giá cuối (level: Pass | Consider | Reject, summary) — output của final_evaluation; dùng để in kết quả.
- error: Có lỗi hay không (bool) — True khi node báo lỗi; main kiểm tra và xử lý (hiển thị error_message / retry).
- error_message: Thông báo lỗi (string) — nội dung lỗi khi error=True; dùng để hiển thị / log.
"""

from typing import TypedDict
class Message(TypedDict):
    role: str
    content: str
# TODO: Khai báo InterviewState (TypedDict, total=False) với các key trên.
class InterviewState(TypedDict, total=False):
    cv_text: str
    candidate_info: dict
    questions: list
    current_question_index: int
    candidate_answer: str
    scores: list
    messages: list[Message]
    total_score: float
    max_score: float
    percentage: float
    final_result: dict
    error: bool  # handle lỗi: True khi node báo lỗi; main kiểm tra và xử lý
    error_message: str  # nội dung lỗi khi error=True


__all__ = ["InterviewState", "Message"]
