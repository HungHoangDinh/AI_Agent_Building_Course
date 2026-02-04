"""Agent Phỏng vấn Nhân sự — LangGraph (FUNCTIONS.md mục 3).

TODO tổng quan cho file này:
- Khởi tạo graph LangGraph dùng `InterviewState` làm state chính.
- Thêm các node tương ứng với các bước trong quy trình phỏng vấn:
  extract_candidate_info → generate_questions → ask_question
  → score_answer → next_question / aggregate_score → final_evaluation.
- Cấu hình các routing (conditional edges) sử dụng các hàm route_*
  trong `practices/nodes/routing_edges.py`.
- Thiết lập checkpointer in-memory và human-in-the-loop với interrupt_after.
"""

from state import InterviewState


def _build_graph():
    """Build graph: StateGraph + nodes + edges + conditional + checkpointer. Trả về compiled graph.

    TODO chi tiết cần làm trong hàm này:
    1. Import các class/tool của LangGraph:
       - `from langgraph.graph import StateGraph, END`
       - `from langgraph.checkpoint.memory import MemorySaver`

    2. Khởi tạo StateGraph với state là `InterviewState`:
       - `graph = StateGraph(InterviewState)`

    3. Import các node và routing từ `practices.nodes` và `node_define`:
       - Các node:
         * extract_candidate_info_node
         * generate_interview_questions_node
         * ask_question_node
         * score_answer_node
         * next_question_node
         * aggregate_score_node
         * final_evaluation_node
       - Các hàm routing:
         * route_after_extract_candidate_info
         * route_after_generate_questions
         * route_after_ask_question
         * route_after_score_answer
         * route_after_next_question
         * route_after_aggregate_score
       - Enum tên node:
         * `from practices.node_define import GraphNode`

    4. Thêm các node vào graph bằng `add_node`, dùng tên từ `GraphNode`:
       - Ví dụ:
         `graph.add_node(GraphNode.EXTRACT_CANDIDATE_INFO.value, extract_candidate_info_node)`

    5. Thiết lập entry point:
       - `graph.set_entry_point(GraphNode.EXTRACT_CANDIDATE_INFO.value)`

    6. Cấu hình các conditional edges:
       - Sau extract_candidate_info:
         `graph.add_conditional_edges(
             GraphNode.EXTRACT_CANDIDATE_INFO.value,
             route_after_extract_candidate_info,
             {
                 # mapping giá trị trả về của route_after_extract_candidate_info
                 # sang node name hoặc END phù hợp.
             },
         )`
       - Tương tự cho:
         * generate_questions với route_after_generate_questions
         * ask_question với route_after_ask_question
         * score_answer với route_after_score_answer
         * next_question với route_after_next_question
         * aggregate_score với route_after_aggregate_score

    7. Thêm edge tuyến tính nếu cần (ví dụ nối next_question → wait_for_human_answer
       hoặc các edge phụ trợ khác, theo đúng flow bạn mong muốn).

    8. Khởi tạo checkpointer in-memory và compile graph:
    10. Trả về compiled app để `main.py` có thể import và sử dụng.

    Hãy hiện thực các bước trên theo thiết kế và yêu cầu cụ thể trong bài tập của bạn.
    """

    # TODO: Implement các bước trên để xây dựng graph hoàn chỉnh.
    raise NotImplementedError(
        "_build_graph chưa được cài đặt, hãy triển khai graph LangGraph theo TODO trong docstring."
    )

