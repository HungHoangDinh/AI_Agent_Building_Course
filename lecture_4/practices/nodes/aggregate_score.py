# Node: Tổng hợp điểm (FUNCTIONS.md 2.6)
# Không gọi LLM, không dùng prompt — chỉ tính total_score, max_score, percentage từ scores và questions.
# Đánh giá bằng LLM (level Pass/Consider/Reject, summary) nằm ở node final_evaluation (FINAL_EVALUATION_PROMPT).


def aggregate_score_node(state: dict) -> dict:
    """Input: scores, questions. Output: total_score, max_score, percentage; hoặc error nếu lỗi."""
    try:
        scores = state.get("scores") or []
        questions = state.get("questions") or []

        # TODO:
        # - Tính:
        #     + total_score = tổng các trường score trong list scores.
        #     + max_score   = tổng các trường max_score trong list questions.
        #     + percentage  = total_score / max_score * 100 (nếu max_score > 0, ngược lại có thể để 0).
        # - Xử lý an toàn khi thiếu trường hoặc giá trị None.
        # - Trả về dict: {"total_score": total_score, "max_score": max_score, "percentage": percentage}.

        raise NotImplementedError(
            "aggregate_score_node chưa được cài đặt, hãy tự triển khai logic tổng hợp điểm."
        )
    except Exception as e:
        return {"error": True, "error_message": str(e)}
