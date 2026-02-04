# Entry: chạy Agent Phỏng vấn Nhân sự (FUNCTIONS.md mục 5, README)
# Cấu hình: từ lecture_4 — from config import settings (LLM_API_KEY, LLM_BASE_URL, LLM_CHAT_MODEL)

import os
import sys

# Thêm thư mục lecture_4 để import config
_lecture4 = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
if _lecture4 not in sys.path:
    sys.path.insert(0, _lecture4)

# TODO: from config import settings
# TODO: Load graph (có interrupt_after=["ask_question"] — xem README mục Human-in-the-loop).
# TODO: config = {"configurable": {"thread_id": "..."}}; invoke lần đầu với {"cv_text": "..."}.
# TODO: Nếu graph interrupt (sau ask_question): lấy state, hiển thị câu hỏi (messages[-1]["content"]), nhập candidate_answer, invoke lại với state đã có candidate_answer (resume cùng config).
# TODO: Lặp đến khi không còn interrupt; in final_result.


def load_cv(path: str) -> str:
    """Đọc nội dung file CV (text)."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run():
    # TODO: graph = ... ; config = {"configurable": {"thread_id": "interview-1"}}
    # TODO: state = graph.invoke({"cv_text": load_cv("data/sample_cv.txt")}, config=config)
    # TODO: Sau ask_question: in câu hỏi từ state, nhập candidate_answer, state = graph.invoke({**state, "candidate_answer": ...}, config=config)
    # TODO: Lặp đến khi có final_result, in kết quả.
    print("TODO: Implement run() theo FUNCTIONS.md mục 5.")


if __name__ == "__main__":
    run()
