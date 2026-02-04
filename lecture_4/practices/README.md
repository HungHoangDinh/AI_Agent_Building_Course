# Bài tập: Agent Phỏng vấn Nhân sự (AI Interviewer)

## Mục tiêu

Xây dựng một **Agent phỏng vấn** với LangGraph có khả năng:

1. **Trích xuất thông tin ứng viên** từ CV ( đọc CV → thông tin có cấu trúc).
2. **Sinh danh sách câu hỏi** phù hợp với từng ứng viên.
3. **Phỏng vấn nhiều vòng** (Q&A): hỏi từng câu, chờ ứng viên trả lời (Human-in-the-loop).
4. **Chấm điểm từng câu** và lưu kết quả (Memory / State).
5. **Tổng hợp điểm + nhận xét cuối** (Aggregate Score, Final Evaluation).

## Luồng tổng thể (Agent Flow)

```
[START]
   ↓
[Extract candidate's Information]   ← 1 bước: từ cv_text → candidate_info
   ↓
[Generate Interview Questions]
   ↓
[Ask Question Loop]
   ├─ Ask question
   ├─ Wait candidate answer (Human-in-the-loop)
   ├─ Score answer
   └─ Save result (State)
   ↓ (hết câu hỏi)
[Aggregate Score]
   ↓
[Final Evaluation]
   ↓
[END]
```

## Các Node

| Node | Mục đích |
|------|----------|
| **Trích xuất thông tin ứng viên** | Đọc CV (text), trích xuất một lần thành state **thông tin ứng viên** (name, years_experience, skills, position, seniority, main_skills, domain, strengths). |
| **Generate Interview Questions** | Sinh danh sách câu hỏi theo thông tin ứng viên (id, skill, question, max_score). |
| **Ask Question** | Đưa câu hỏi hiện tại ra (messages), sau đó dừng để chờ ứng viên trả lời. |
| **Score Answer** | Chấm câu trả lời (score, comment), append vào scores. |
| **Question Loop Control** | Rẽ nhánh: còn câu hỏi → Ask Question; hết → Aggregate Score. |
| **Aggregate Score** | Tính total_score, max_score, percentage. |
| **Final Evaluation** | Đánh giá cuối: level (Pass/Consider/Reject), summary. |

## State (InterviewState)

- `cv_text` — nội dung CV (input).
- **`candidate_info`** — thông tin ứng viên (trích xuất trong 1 bước): name, years_experience, skills, position, seniority, main_skills, domain, strengths.
- `questions`, `current_question_index`
- `candidate_answer`, `scores`, `messages`
- `total_score`, `final_result`

## Cấu trúc thư mục

```
practices/
├── README.md           # File này
├── FUNCTIONS.md        # Chi tiết các function cần implement (TODO)
├── main.py             # Entry: CLI hoặc Gradio chạy interview
├── agent.py            # LangGraph: State, nodes, graph
├── data/
│   └── sample_cv.txt   # CV mẫu để test
└── prompt/
    ├── __init__.py
    └── prompt.py       # Prompts cho từng node (parse, profile, questions, score, final)
```

## Config

- Dùng config từ `lecture_4`,  `from config import settings` (LLM_API_KEY, LLM_BASE_URL, LLM_CHAT_MODEL).

## Human-in-the-loop — Người học setup ở đâu

Human-in-the-loop (đợi người dùng trả lời rồi mới chạy tiếp) cần setup **2 chỗ**:

1. **`agent.py`** — Khi compile graph:
   - Dùng **`interrupt_after=["ask_question"]`** khi gọi `graph.compile(...)` để graph **dừng sau node ask_question** (trước khi chạy conditional). Khi resume, graph sẽ chạy tiếp conditional với state mới (có `candidate_answer`) và đi sang score_answer.
   - Ví dụ: `graph.compile(checkpointer=memory, interrupt_after=["ask_question"])`.

2. **`main.py`** — Vòng lặp chạy phỏng vấn:
   - **Invoke** graph với `cv_text` (lần đầu) hoặc với state đã có `candidate_answer` (resume).
   - Nếu graph **bị interrupt** (trả về sau ask_question): lấy **state** từ kết quả, lấy câu hỏi từ `state["messages"][-1]["content"]`, **hiển thị** cho người dùng, **nhập** `candidate_answer`, rồi **invoke lại** với `config` cùng `thread_id` và state đã thêm `candidate_answer` (resume).
   - Lặp đến khi không còn interrupt (đã chạy xong final_evaluation), in `final_result`.

Tóm tắt: **agent.py** = bật interrupt sau ask_question; **main.py** = khi bị interrupt thì hiển thị câu hỏi, nhập trả lời, resume với `candidate_answer`.

## Cách làm bài

1. Đọc `FUNCTIONS.md` để biết từng function/node cần implement.
2. Setup Human-in-the-loop như mục trên (agent: interrupt_after; main: vòng invoke → interrupt → nhập answer → resume).
3. Implement theo TODO trong từng file (prompt, agent nodes, main).
4. Chạy `main.py` với CV mẫu trong `data/sample_cv.txt`, trả lời từng câu hỏi, xem kết quả chấm và đánh giá cuối.

## Tham khảo

- **LangGraph**: `lecture_4/main.ipynb` (StateGraph, nodes, conditional_edges, interrupt).
- **State & multi-turn**: Bài toán CSKH hoàn tiền trong notebook (extract, generate_question, loop).
