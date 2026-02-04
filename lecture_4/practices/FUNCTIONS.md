# Danh sách Function / Node cần implement (TODO)

Các mục dưới đây theo đúng luồng Agent Phỏng vấn Nhân sự. Implement theo TODO trong từng file, tham chiếu `lecture_4/main.ipynb` cho LangGraph.

---

## 1. State

### 1.1 `state.py` — `InterviewState` (TypedDict)

- **Trường**: `cv_text`, **`candidate_info`** (thông tin ứng viên — trích xuất trong 1 bước), `questions`, `current_question_index`, `candidate_answer`, `scores`, `messages`, `total_score`, `final_result` (đều optional trừ khi cần).
- TODO: Khai báo TypedDict với `total=False` cho các key tùy chọn trong **`state.py`**. `agent.py` import `InterviewState` từ `state`.

---

## 2. Nodes

### 2.1 Trích xuất thông tin ứng viên (1 bước)

- **Input (state)**: `cv_text`.
- **Output (state update)**: **`candidate_info`** = thông tin ứng viên gộp trong một state, gồm: `name`, `years_experience`, `skills`, `position`, `seniority`, `main_skills`, `domain`, `strengths`.
- TODO: Rule-based (regex) hoặc LLM extract JSON từ `cv_text` trong một lần (không tách Parse CV + Extract Profile).

### 2.2 Generate Interview Questions Node

- **Input**: `candidate_info`.
- **Output**: `questions` (list dict: id, skill, question, max_score), `current_question_index` = 0.
- TODO: LLM sinh 3–5 câu hỏi phù hợp với thông tin ứng viên.

### 2.3 Ask Question Node

- **Input**: `questions`, `current_question_index`, `messages`.
- **Output**: Append câu hỏi hiện tại vào `messages` (role assistant).
- TODO: Lấy `questions[current_question_index]`, format và append vào `messages`.

### 2.4 Score Answer Node

- **Input**: `candidate_answer`, `questions`, `current_question_index`, `scores`.
- **Output**: Append `{ "question_id", "score", "comment" }` vào `scores`.
- TODO: LLM chấm theo rubric/keyword/reasoning, hoặc rule đơn giản.

### 2.5 Question Loop Control (conditional edge)

- **Logic**: Nếu `current_question_index < len(questions) - 1` → next: tăng index và quay lại Ask Question; ngược lại → Aggregate Score.
- TODO: Hàm routing trả về tên node tiếp theo.

### 2.6 Aggregate Score Node

- **Input**: `scores`, `questions`.
- **Output**: `total_score`, `max_score`, `percentage` (có thể đặt trong state hoặc trong `final_result`).
- TODO: Tính tổng điểm từ `scores`, tổng max từ `questions`.

### 2.7 Final Evaluation Node

- **Input**: `total_score`, `percentage`, `scores`, `candidate_info`.
- **Output**: `final_result` = `{ "level": "Pass | Consider | Reject", "summary": "..." }`.
- TODO: LLM hoặc rule dựa trên percentage và nội dung phỏng vấn.

---

## 3. Graph (agent.py)

- TODO: `StateGraph(InterviewState)`, thêm lần lượt các node trên.
- TODO: Edge: START → extract_candidate_info → generate_questions → ask_question.
- **In-memory lưu trạng thái, xử lý sau :**
  - Compile graph với **checkpointer in-memory** (vd: `MemorySaver`) để lưu state sau mỗi bước.
  - Chạy đến ask_question xong → graph dừng (không dùng interrupt, chỉ dừng tại node đó bằng conditional hoặc bằng cách invoke từng đoạn). Lấy state hiện tại từ checkpointer (thread_id / config), lưu lại (in-memory dict hoặc chính checkpoint).
  - Khi đã có `candidate_answer`: load lại state từ in-memory (hoặc resume với cùng thread_id), cập nhật `candidate_answer` vào state, invoke tiếp từ node score_answer (hoặc resume từ checkpoint) → conditional → aggregate_score → final_evaluation → END.
  - Ưu điểm: không bắt buộc phải “dừng chương trình chờ nhập”; có thể thu thập nhiều câu trả lời rồi xử lý hàng loạt sau.
- TODO: aggregate_score → final_evaluation → END.
- TODO: Compile với checkpointer (vd: `MemorySaver`) để lưu tiến trình.

---

## 4. Prompts (prompt/prompt.py)

- TODO: `EXTRACT_CANDIDATE_INFO_PROMPT` — hướng dẫn LLM trích xuất **thông tin ứng viên** trong một bước từ CV (text): name, years_experience, skills, position, seniority, main_skills, domain, strengths.
- TODO: `GENERATE_QUESTIONS_PROMPT` — sinh câu hỏi phỏng vấn theo candidate_info.
- TODO: `SCORE_ANSWER_PROMPT` — chấm câu trả lời (score, comment).
- TODO: `FINAL_EVALUATION_PROMPT` — level + summary.

---

## 5. Main (main.py)

- TODO: Load graph với checkpointer in-memory (vd: `MemorySaver`).
- Invoke lần đầu với `{"cv_text": "..."}` và config có `thread_id`; chạy đến sau ask_question (graph thiết kế để dừng tại đó, hoặc invoke từng đoạn). Lưu state hiện tại (từ checkpointer hoặc dict in-memory). Sau khi có `candidate_answer` (nhập sau, hoặc batch): load state, gán `candidate_answer`, invoke tiếp (resume với cùng thread_id hoặc truyền state đã load). Lặp cho từng câu hỏi đến khi chạy xong final_evaluation, in `final_result`.

---

## 6. Checklist

- [ ] `state.py`: InterviewState
- [ ] `agent.py`: extract_candidate_info, generate_interview_questions
- [ ] `agent.py`: ask_question, score_answer, aggregate_score, final_evaluation
- [ ] `agent.py`: question_loop_control (conditional), build graph; in-memory state + checkpointer
- [ ] `prompt/prompt.py`: Các prompt cho extract_candidate_info, questions, score, final
- [ ] `main.py`: run interview (invoke, lưu/load state, resume, hiển thị kết quả)

Sau khi implement xong, chạy `main.py` với `data/sample_cv.txt` để test đầy đủ luồng.
