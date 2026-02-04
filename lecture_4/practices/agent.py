# Agent Phỏng vấn Nhân sự — LangGraph (FUNCTIONS.md mục 3)
# Graph + Checkpointer in-memory. State định nghĩa tại state.py.

"""
TODO:
- Import StateGraph, END từ langgraph.graph; MemorySaver từ langgraph.checkpoint.memory.
- Import các node từ nodes và routing (route_after_extract_candidate_info, route_after_generate_questions, route_after_ask, question_loop_control, route_after_aggregate_score).
- Tạo StateGraph(InterviewState), thêm từng node. START → extract_candidate_info. Human-in-the-loop: sau ask_question đợi trả lời → END; resume với candidate_answer → score_answer.
- set_entry_point("extract_candidate_info"). add_conditional_edges("extract_candidate_info", route_after_extract_candidate_info, {...}); add_conditional_edges("generate_questions", route_after_generate_questions, {...}); add_conditional_edges("ask_question", route_after_ask, {END, "score_answer": "score_answer"}); add_conditional_edges("score_answer", question_loop_control, {END, "next_question": "next_question", "aggregate_score": "aggregate_score"}); next_question → ask_question; add_conditional_edges("aggregate_score", route_after_aggregate_score, {END, "final_evaluation": "final_evaluation"}); final_evaluation → END.
- Compile với checkpointer=MemorySaver() và **interrupt_after=["ask_question"]** (Human-in-the-loop: graph dừng sau ask_question, main nhập candidate_answer rồi resume); export graph để main.py dùng.
"""

from state import InterviewState


def _build_graph():
    """Build graph: StateGraph + nodes + edges + conditional + checkpointer. Trả về compiled graph."""
    # TODO: implement theo mục TODO đầu file
    return None
