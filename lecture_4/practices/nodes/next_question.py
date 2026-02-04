# Node: Tăng index chuyển sang câu hỏi tiếp theo (sau score_answer, trước khi quay lại ask_question)


def next_question_node(state: dict) -> dict:
    """Tăng current_question_index; xóa candidate_answer để sẵn sàng nhận câu trả lời cho câu hỏi tiếp theo.

    TODO gợi ý triển khai:
    - Đọc chỉ số hiện tại từ state["current_question_index"] (mặc định 0 nếu chưa có).
    - Tăng chỉ số này lên 1 để chuyển sang câu hỏi kế tiếp.
    - Đặt lại state["candidate_answer"] về None hoặc "" để vòng hỏi tiếp theo sẵn sàng nhận câu trả lời mới.
    - Trả về dict chứa các key cần cập nhật (vd: {"current_question_index": ..., "candidate_answer": None}).
    """
    try:
        # TODO: implement logic tăng current_question_index và reset candidate_answer.
        raise NotImplementedError(
            "next_question_node chưa được cài đặt, hãy tự triển khai logic tăng index câu hỏi."
        )
    except Exception as e:
        return {"error": True, "error_message": str(e)}
