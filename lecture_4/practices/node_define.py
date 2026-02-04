# Định nghĩa tên các node trong graph — dùng GraphNode ở nhiều nơi (agent, nodes, ...).

from enum import Enum


class GraphNode(str, Enum):
    """Tên các node trong graph (LangGraph). Dùng .value khi add_node / add_edge."""
    EXTRACT_CANDIDATE_INFO = "extract_candidate_info"
    GENERATE_QUESTIONS = "generate_questions"
    ASK_QUESTION = "ask_question"
    SCORE_ANSWER = "score_answer"
    NEXT_QUESTION = "next_question"
    AGGREGATE_SCORE = "aggregate_score"
    FINAL_EVALUATION = "final_evaluation"


__all__ = ["GraphNode"]
