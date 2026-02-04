from langgraph.graph import END
from practices.node_define import GraphNode
from practices.state import InterviewState

def route_after_extract_candidate_info(state: InterviewState):
    """Routing sau extract_candidate_info.

    TODO:
    - Nếu có lỗi trong state (ví dụ node extract_candidate_info trả về error)
      thì trả về END để dừng graph.
    - Nếu không có lỗi thì chuyển sang node generate_questions
      (GraphNode.GENERATE_QUESTIONS.value).
    - Cài đặt logic routing cụ thể tùy theo InterviewState của bạn.
    """
    # TODO: implement logic routing sau extract_candidate_info theo mô tả trên.
    raise NotImplementedError("route_after_extract_candidate_info chưa được cài đặt.")


def route_after_generate_questions(state: InterviewState):
    """Routing sau generate_questions.

    TODO:
    - Nếu có lỗi trong state (ví dụ node generate_questions trả về error)
      thì trả về END để dừng graph.
    - Nếu không có lỗi thì chuyển sang node ask_question
      (GraphNode.ASK_QUESTION.value).
    - Cài đặt logic routing cụ thể tùy theo InterviewState của bạn.
    """
    # TODO: implement logic routing sau generate_questions theo mô tả trên.
    raise NotImplementedError("route_after_generate_questions chưa được cài đặt.")


def route_after_ask_question(state: InterviewState):
    """Routing sau ask_question.

    TODO:
    - Nếu có lỗi trong state (ví dụ node ask_question báo lỗi)
      thì trả về END để dừng graph.
    - Nếu không có lỗi thì chuyển sang node score_answer
      (GraphNode.SCORE_ANSWER.value).
    - Có thể bổ sung thêm logic tuỳ nhu cầu (ví dụ: bỏ qua câu hỏi, hủy phỏng vấn...).
    """
    # TODO: implement logic routing sau ask_question theo mô tả trên.
    raise NotImplementedError("route_after_ask_question chưa được cài đặt.")


def route_after_score_answer(state: InterviewState):
    """Routing sau score_answer.

    TODO:
    - Nếu có lỗi trong state (ví dụ node score_answer báo lỗi) thì trả về END.
    - Nếu không có lỗi:
        * Nếu còn câu hỏi tiếp theo → trả về GraphNode.NEXT_QUESTION.value.
        * Nếu đã hết câu hỏi       → trả về GraphNode.AGGREGATE_SCORE.value.
    - Dựa vào:
        * state["questions"]: danh sách câu hỏi.
        * state["current_question_index"]: index câu hỏi hiện tại.
    """
    # TODO: implement logic routing sau score_answer theo mô tả trên.
    raise NotImplementedError("route_after_score_answer chưa được cài đặt.")



def route_after_next_question(state: InterviewState):
    """Routing sau next_question.

    TODO:
    - Nếu có lỗi trong state → trả về END để dừng graph.
    - Nếu không có lỗi      → chuyển sang node ask_question
      (GraphNode.ASK_QUESTION.value) để hỏi câu tiếp theo.
    - Có thể mở rộng thêm logic nếu muốn (ví dụ: dừng khi đã đạt ngưỡng điểm nào đó).
    """
    # TODO: implement logic routing sau next_question theo mô tả trên.
    raise NotImplementedError("route_after_next_question chưa được cài đặt.")

def route_after_aggregate_score(state: InterviewState):
    """Routing sau aggregate_score.

    TODO:
    - Nếu có lỗi trong state → trả về END để dừng graph.
    - Nếu không có lỗi      → chuyển sang node final_evaluation
      (GraphNode.FINAL_EVALUATION.value) để LLM đánh giá tổng thể.
    - Có thể mở rộng thêm điều kiện (ví dụ: bỏ qua final_evaluation nếu percentage quá thấp).
    """
    # TODO: implement logic routing sau aggregate_score theo mô tả trên.
    raise NotImplementedError("route_after_aggregate_score chưa được cài đặt.")

