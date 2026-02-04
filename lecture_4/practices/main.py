"""Entry: chạy Agent Phỏng vấn Nhân sự (FUNCTIONS.md mục 5, README).

Yêu cầu mở rộng:
- Dùng Gradio để tạo giao diện chat với người dùng.
- Cho phép người dùng upload file CV (PDF), xử lý PDF → text trước khi gọi agent.
- Mỗi phiên phỏng vấn dùng một `thread_id` riêng để có thể resume bằng LangGraph.
- Mỗi lần chạy phải xử lý xem graph có interrupt không để lần sau resume.
"""

import os
import sys

# Thêm thư mục lecture_4 để import config
_lecture4 = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
if _lecture4 not in sys.path:
    sys.path.insert(0, _lecture4)


def load_cv(path: str) -> str:
    """Đọc nội dung file CV (text hoặc đã được trích xuất từ PDF)."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run():
    """Khởi chạy ứng dụng Gradio cho Agent phỏng vấn nhân sự.

    TODO chi tiết:
    1. Import cấu hình và agent:
       - `from config import settings`
       - Import `_build_graph` từ `practices.agent` và build graph:
         `graph = _build_graph()`

    2. Thiết kế pipeline xử lý CV:
       - Dùng Gradio (`gr.File` / `gr.UploadButton`) cho phép user upload file:
           * Nếu PDF:
               + Dùng LangGraph/LangChain hoặc loader đọc PDF để trích xuất text.
               + Có thể tạo một graph nhỏ chuyên xử lý PDF → text (nếu muốn),
                 sau đó lấy output text để truyền sang agent phỏng vấn.
           * Nếu TXT:
               + Đọc file và dùng trực tiếp.
       - Lưu text CV vào state đầu vào cho agent: `{"cv_text": cv_text}`.

    3. Quản lý thread_id cho từng phiên:
       - Mỗi phiên phỏng vấn sinh một `thread_id` duy nhất (vd: UUID, session_id).
       - Khi gọi graph, luôn truyền:
           `config = {"configurable": {"thread_id": thread_id}}`.

    4. Vòng lặp gọi graph với interrupt/resume:
       - Lần đầu:
           * `state = graph.invoke({"cv_text": cv_text}, config=config)`
       - Sau mỗi lần invoke:
           * Kiểm tra xem graph có đang interrupt (theo API LangGraph mà bạn dùng).
           * Nếu đang interrupt ở bước hỏi/đợi trả lời:
               + Lấy câu hỏi hiện tại từ state (ví dụ:
                 `state["messages"][-1]["content"]` hoặc từ `questions`/`current_question_index`).
               + Hiển thị câu hỏi trên giao diện chat Gradio.
               + Chờ người dùng nhập `candidate_answer`.
               + Gọi lại graph với Comsume và resume
           * Lặp lại cho đến khi:
               + Có `state.get("final_result")`, hoặc
               + Graph kết thúc mà không còn interrupt.

    5. Tích hợp với Gradio:
       - Dùng `gr.Blocks` / `gr.ChatInterface`:
           * Component upload CV.
           * Vùng hiển thị hội thoại hỏi–đáp.
           * `gr.State` để lưu `thread_id` và `state` hiện tại cho mỗi session.
       - Callback xử lý:
           * Nếu chưa có CV → yêu cầu upload trước.
           * Nếu đã có CV và chưa có state → khởi chạy graph lần đầu.
           * Nếu đã có state và graph đang ở trạng thái interrupt:
               - **Không cho phép đổi / upload CV mới trong cùng thread_id** (để tránh làm
                 lệch context so với state hiện tại).
               - Chỉ nhận thêm `candidate_answer` và gọi resume graph.
           * Nếu muốn dùng CV khác → tạo thread_id mới (reset session) rồi upload lại.

    6. Xử lý lỗi:
       - Nếu `state.get("error")` là True, hiển thị `error_message` và cho phép user thử lại hoặc reset.

    7. Khi `final_result` có trong state:
       - Hiển thị level + summary cho HR/người dùng.
       - (Tùy chọn) hiển thị thêm tổng điểm, phần trăm, danh sách scores.

    Hãy hiện thực các bước trên theo đúng API LangGraph và Gradio bạn chọn.
    """

    # TODO: Implement hàm run() theo checklist ở docstring.
    raise NotImplementedError(
        "run() chưa được cài đặt, hãy xây Gradio app + logic interrupt/resume theo TODO."
    )


if __name__ == "__main__":
    run()

