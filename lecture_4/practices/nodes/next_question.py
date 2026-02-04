# Node: Tăng index chuyển sang câu hỏi tiếp theo (sau score_answer, trước khi quay lại ask_question)


def next_question_node(state: dict) -> dict:
    """Tăng current_question_index; xóa candidate_answer để sẵn sàng nhận câu trả lời cho câu hỏi tiếp theo."""
    try:
        idx = state.get("current_question_index", 0)
        return {
            "current_question_index": idx + 1,
            "candidate_answer": None,  # xóa để ask_question → END, main nhập câu trả lời mới
        }
    except Exception as e:
        return {"error": True, "error_message": str(e)}
