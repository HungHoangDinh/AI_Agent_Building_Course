# Node: Tổng hợp điểm (FUNCTIONS.md 2.6)
# Không gọi LLM, không dùng prompt — chỉ tính total_score, max_score, percentage từ scores và questions.
# Đánh giá bằng LLM (level Pass/Consider/Reject, summary) nằm ở node final_evaluation (FINAL_EVALUATION_PROMPT).


def aggregate_score_node(state: dict) -> dict:
    """Input: scores, questions. Output: total_score, max_score, percentage; hoặc error nếu lỗi."""
    try:
        scores = state.get("scores") or []
        questions = state.get("questions") or []

        # TODO: Tính total_score = tổng score từ scores; max_score = tổng max_score từ questions; percentage = total_score / max_score * 100 nếu max_score > 0.
        total_score = sum((s.get("score") or 0) for s in scores)
        max_score = sum((q.get("max_score") or 0) for q in questions) or 1.0
        percentage = (total_score / max_score * 100) if max_score else 0.0

        return {"total_score": total_score, "max_score": max_score, "percentage": percentage}
    except Exception as e:
        return {"error": True, "error_message": str(e)}
