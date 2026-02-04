"""
Node: ask_question — bước hỏi & chờ người dùng trả lời (Human-in-the-loop)

Mục đích:
- Đóng vai trò node "ask_question" đơn giản:
  1) Lấy câu hỏi hiện tại từ `state["questions"][state["current_question_index"]]`.
  2) Append câu hỏi đó vào `state["messages"]` với `role="assistant"`.
  3) Graph **interrupts** tại đây để UI/ứng dụng hiển thị câu hỏi và chờ user trả lời.
  4) Sau khi user trả lời, ứng dụng gán câu trả lời vào `state["candidate_answer"]`.
  5) Node (khi được gọi lại với state đã có `candidate_answer`) sẽ append câu trả lời
     vào `state["messages"]` với `role="user"`, rồi trả state ra cho các node tiếp theo
     (vd: `score_answer`).

Ghi chú:
- Node này **không tự gọi LLM, không trực tiếp đọc input**; việc hiển thị câu hỏi
  và nhận câu trả lời thuộc về `main.py` / UI (vd: Gradio).
"""


def ask_question_node(state: dict) -> dict:
    """Node hỏi & chờ người dùng trả lời (giống ask_question đơn giản).

    TODO gợi ý triển khai:
    - Lấy câu hỏi hiện tại từ `questions[current_question_index]`.
    - Khởi tạo hoặc lấy list `messages` từ state.
    - Nếu CHƯA có `candidate_answer`:
        + Append câu hỏi (role="assistant") vào `messages`.
        + Trả về state cập nhật `messages` và để graph interrupt (UI sẽ lo phần hiển thị).
    - Nếu ĐÃ có `candidate_answer`:
        + Append câu trả lời (role="user") vào `messages`.
        + Trả về state mới (đã có `messages` đầy đủ) để node `score_answer` sử dụng.
    - Node này không gọi LLM, không đọc input trực tiếp; toàn bộ I/O là qua state + interrupt.
    """
    try:
        # TODO: implement ask_question_node theo mô tả ở docstring trên.
        raise NotImplementedError(
            "ask_question_node chưa được cài đặt, hãy tự triển khai logic human-in-the-loop."
        )
    except Exception as e:
        return {"error": True, "error_message": str(e)}

