### Danh sách Function / Node cần implement (TODO)

Các mục dưới đây bám sát code scaffold trong thư mục `practices/`. Hãy đọc kỹ TODO trong từng file trước khi viết code.

---

### 1. State (`state.py`)

- File: `state.py`
- Bạn đã có:
  - `InterviewState` (TypedDict)
  - `Message` (TypedDict)
- Đảm bảo các trường trong `InterviewState`:
  - `cv_text`, `candidate_info`, `questions`, `current_question_index`
  - `candidate_answer`, `scores`, `messages`
  - `total_score`, `max_score`, `percentage`
  - `final_result`, `error`, `error_message`
- Mục tiêu: toàn bộ node đều đọc/ghi qua `state: InterviewState`.

---

### 2. Prompts (`prompt/`)

- `prompt/extract_candidate_info_prompt.py`
  - Biến: `EXTRACT_CANDIDATE_INFO_PROMPT`
  - TODO: viết prompt hướng dẫn LLM đọc `{cv_text}` và trả về JSON theo schema `CandidateInfo`.

- `prompt/generate_questions_prompt.py`
  - Biến: `GENERATE_QUESTIONS_PROMPT`
  - TODO: viết prompt sinh 3–5 câu hỏi phỏng vấn (JSON theo `QuestionItem`) dựa trên `candidate_info`.

- `prompt/score_answer_prompt.py`
  - Biến: `SCORE_ANSWER_PROMPT`
  - TODO: viết prompt chấm điểm một câu trả lời, output JSON theo `ScoreItem` (`question_id`, `score`, `comment`).

- `prompt/final_evaluation_prompt.py`
  - Biến: `FINAL_EVALUATION_PROMPT`
  - TODO: prompt đánh giá cuối (Pass / Consider / Reject + summary) dựa trên điểm + `candidate_info`.

Yêu cầu chung cho prompt:

- Hướng dẫn LLM trả về **duy nhất một JSON object** khớp với schema tương ứng.
- Không in thêm text, giải thích, comment ngoài JSON.

---

### 3. Nodes (`nodes/`)

Mỗi node là một file riêng dưới `nodes/`. Hầu hết đã có class Pydantic và TODO mô tả chi tiết; bạn cần hiện thực phần thân.

#### 3.1 `extract_candidate_info_node` — trích xuất thông tin ứng viên

- File: `nodes/extract_candidate_info.py`
- Class: `CandidateInfo`
- Input state:
  - `cv_text`
- Output state:
  - `candidate_info` = `CandidateInfo.model_dump()`
- TODO:
  - Gọi LLM (OpenAI) với `EXTRACT_CANDIDATE_INFO_PROMPT.format(cv_text=...)`.
  - Yêu cầu JSON khớp schema `CandidateInfo`.
  - Parse JSON, tạo `CandidateInfo(...)`, trả về dict update state.

#### 3.2 `generate_interview_questions_node` — sinh câu hỏi phỏng vấn

- File: `nodes/generate_questions.py`
- Class: `QuestionItem`, `InterviewQuestions`
- Input:
  - `candidate_info`
- Output:
  - `questions`: list dict (từ `QuestionItem.model_dump()`).
  - `current_question_index`: 0.
- TODO:
  - Dùng `GENERATE_QUESTIONS_PROMPT` + `candidate_info`.
  - LLM trả về JSON `InterviewQuestions`.
  - Parse, cập nhật state.

#### 3.3 `ask_question_node` — node hỏi & chờ trả lời (Human-in-the-loop)

- File: `nodes/ask_question.py`
- Input:
  - `questions`, `current_question_index`, `messages`, `candidate_answer`.
- Output:
  - Append câu hỏi (role `"assistant"`) hoặc câu trả lời (role `"user"`) vào `messages`
    tùy theo trạng thái.
- Mục đích:
  - Lần 1 (chưa có `candidate_answer`):
    - Lấy câu hỏi hiện tại từ `questions[current_question_index]`.
    - Append vào `messages` với `role="assistant"`.
    - Trả state để graph **interrupt** cho UI hiển thị câu hỏi và chờ người dùng trả lời.
  - Sau khi người dùng trả lời (state đã có `candidate_answer`):
    - Append câu trả lời vào `messages` với `role="user"`.
    - Trả state mới để node `score_answer` sử dụng.
- TODO:
  - Hiện thực logic hai pha trên theo gợi ý docstring trong file.

#### 3.4 `score_answer_node`

- File: `nodes/score_answer.py`
- Class: `ScoreItem`
- Input:
  - `candidate_answer`, `questions`, `current_question_index`, `scores`.
- Output:
  - Append `{question_id, score, comment}` vào `scores`.
- TODO:
  - Lấy câu hỏi hiện tại.
  - Dùng `SCORE_ANSWER_PROMPT` + nội dung câu hỏi + `candidate_answer`.
  - LLM trả về JSON `ScoreItem`.
  - Parse và append vào `scores`.

#### 3.5 `next_question_node`

- File: `nodes/next_question.py`
- Input:
  - `current_question_index`, `candidate_answer`.
- Output:
  - Tăng `current_question_index`.
  - Reset `candidate_answer`.
- TODO:
  - Implement theo gợi ý trong docstring (hiện đang `NotImplementedError`).

#### 3.6 `aggregate_score_node`

- File: `nodes/aggregate_score.py`
- Input:
  - `scores`, `questions`.
- Output:
  - `total_score`, `max_score`, `percentage`.
- TODO:
  - Tính tổng score, tổng `max_score`, phần trăm điểm.

#### 3.7 `final_evaluation_node`

- File: `nodes/final_evaluation.py`
- Class: `FinalResult`
- Input:
  - `total_score`, `percentage`, `scores`, `candidate_info`.
- Output:
  - `final_result` = `{level, summary}`.
- TODO:
  - Dùng `FINAL_EVALUATION_PROMPT` + các thông tin trên.
  - LLM trả về JSON `FinalResult`.
  - Parse và cập nhật state.

#### 3.8 Routing nodes (`routing_edges.py`)

- File: `nodes/routing_edges.py`
- Các hàm:
  - `route_after_extract_candidate_info`
  - `route_after_generate_questions`
  - `route_after_ask_question`
  - `route_after_score_answer`
  - `route_after_next_question`
  - `route_after_aggregate_score`
- TODO:
  - Dựa vào `state` (`error`, `questions`, `current_question_index`, v.v.) để trả về:
    - `END` hoặc
    - tên node tiếp theo (`GraphNode.XXX.value`).

---

### 4. Graph (agent.py)

- File: `agent.py`
- Hàm: `_build_graph()`
- TODO (docstring đã liệt kê chi tiết):
  - Import:
    - `StateGraph`, `END` từ `langgraph.graph`.
    - `MemorySaver` từ `langgraph.checkpoint.memory`.
    - Các node + routing từ `practices.nodes`.
    - `GraphNode` từ `node_define.py`.
  - Tạo:
    - `graph = StateGraph(InterviewState)`.
  - Thêm node:
    - `GraphNode.EXTRACT_CANDIDATE_INFO.value` → `extract_candidate_info_node`
    - `GraphNode.GENERATE_QUESTIONS.value` → `generate_interview_questions_node`
    - `GraphNode.ASK_QUESTION.value` → `ask_question_node`
    - `GraphNode.SCORE_ANSWER.value` → `score_answer_node`
    - `GraphNode.NEXT_QUESTION.value` → `next_question_node`
    - `GraphNode.AGGREGATE_SCORE.value` → `aggregate_score_node`
    - `GraphNode.FINAL_EVALUATION.value` → `final_evaluation_node`
  - Set entry point:
    - `graph.set_entry_point(GraphNode.EXTRACT_CANDIDATE_INFO.value)`.
  - Thêm các conditional edges với route_*:
    - extract_candidate_info → `route_after_extract_candidate_info`
    - generate_questions → `route_after_generate_questions`
    - ask_question → `route_after_ask_question`
    - score_answer → `route_after_score_answer`
    - next_question → `route_after_next_question`
    - aggregate_score → `route_after_aggregate_score`
  - Khởi tạo checkpointer:
    - `memory = MemorySaver()`.
  - Compile:
    - `graph.compile(checkpointer=memory, interrupt_after=[GraphNode.ASK_QUESTION.value])`.
  - Trả về compiled app.

---

### 5. Main entry (main.py)

- File: `main.py`
- Hàm: `run()`
- TODO (docstring đã ghi rõ):
  - Import:
    - `settings` từ `config`.
    - `_build_graph` từ `practices.agent`.
    - Gradio (`import gradio as gr`).
  - Xây Gradio UI:
    - Upload CV (PDF/TXT).
    - Nếu PDF: dùng loader/LangChain/LangGraph để trích xuất text.
    - Lưu `cv_text` trong một `gr.State`.
  - Sinh `thread_id` cho mỗi session.
  - Lần đầu:
    - Gọi `graph.invoke({"cv_text": cv_text}, config=config)` để bắt đầu phỏng vấn.
  - Khi graph interrupt tại `ASK_QUESTION`:
    - Lấy câu hỏi hiện tại từ state (từ `messages` hoặc từ `questions`/`current_question_index`).
    - Hiển thị trên chat UI.
    - Nhận `candidate_answer` từ người dùng.
    - Gọi lại `graph.invoke({**state, "candidate_answer": answer}, config=config)` để resume.
  - Không cho phép đổi CV khi đang interrupt trong cùng `thread_id`.
  - Khi `final_result` có:
    - Hiển thị `level` + `summary`.

---

### 6. Checklist

- [ ] `prompt/*.py`: Viết nội dung prompt cụ thể cho từng bước.
- [ ] `nodes/extract_candidate_info.py`: gọi LLM, parse về `CandidateInfo`.
- [ ] `nodes/generate_questions.py`: gọi LLM, parse về `InterviewQuestions`.
- [ ] `nodes/ask_question.py`: logic hỏi & chờ trả lời (interrupt).
- [ ] `nodes/score_answer.py`: gọi LLM, parse `ScoreItem`, append `scores`.
- [ ] `nodes/next_question.py`: tăng index, reset `candidate_answer`.
- [ ] `nodes/aggregate_score.py`: tính tổng điểm, phần trăm.
- [ ] `nodes/final_evaluation.py`: gọi LLM, parse `FinalResult`.
- [ ] `nodes/routing_edges.py`: implement các route_* theo mô tả.
- [ ] `agent.py`: build graph, checkpointer, interrupt_after.
- [ ] `main.py`: Gradio app + upload PDF/TXT + interrupt/resume.

Sau khi implement xong, chạy `practices/main.py` để test đầy đủ luồng (bắt đầu có thể dùng `data/sample_cv.txt`).  
Hãy thử cả flow: upload CV → nhận câu hỏi → trả lời từng câu → xem kết quả cuối.

### Danh sách Function / Node cần implement (TODO)

Các mục dưới đây bám sát code scaffold trong thư mục `practices/`. Hãy đọc kỹ TODO trong từng file trước khi viết code.

---

### 1. State (`state.py`)

- File: `state.py`
- Bạn đã có:
  - `InterviewState` (TypedDict)
  - `Message` (TypedDict)
- Đảm bảo các trường trong `InterviewState`:
  - `cv_text`, `candidate_info`, `questions`, `current_question_index`
  - `candidate_answer`, `scores`, `messages`
  - `total_score`, `max_score`, `percentage`
  - `final_result`, `error`, `error_message`
- Mục tiêu: toàn bộ node đều đọc/ghi qua `state: InterviewState`.

---

### 2. Prompts (`prompt/`)

Prompts đã được tách ra thành nhiều file, mỗi file chứa TODO mô tả rõ:

- `prompt/extract_candidate_info_prompt.py`
  - Biến: `EXTRACT_CANDIDATE_INFO_PROMPT`
  - TODO: viết prompt hướng dẫn LLM đọc `{cv_text}` và trả về JSON theo schema `CandidateInfo`.

- `prompt/generate_questions_prompt.py`
  - Biến: `GENERATE_QUESTIONS_PROMPT`
  - TODO: viết prompt sinh 3–5 câu hỏi phỏng vấn (JSON theo `QuestionItem`) dựa trên `candidate_info`.

- `prompt/score_answer_prompt.py`
  - Biến: `SCORE_ANSWER_PROMPT`
  - TODO: viết prompt chấm điểm một câu trả lời, output JSON theo `ScoreItem` (`question_id`, `score`, `comment`).

- `prompt/final_evaluation_prompt.py`
  - Biến: `FINAL_EVALUATION_PROMPT`
  - TODO: prompt đánh giá cuối (Pass / Consider / Reject + summary) dựa trên điểm + `candidate_info`.

Yêu cầu chung cho prompt:

- Hướng dẫn LLM trả về **duy nhất một JSON object** khớp với schema tương ứng.
- Không in thêm text, giải thích, comment ngoài JSON.

---

### 3. Nodes (`nodes/`)

Mỗi node là một file riêng dưới `nodes/`. Hầu hết đã có class Pydantic và TODO mô tả chi tiết; bạn cần hiện thực phần thân.

#### 3.1 `extract_candidate_info_node` — trích xuất thông tin ứng viên

- File: `nodes/extract_candidate_info.py`
- Class: `CandidateInfo`
- Input state:
  - `cv_text`
- Output state:
  - `candidate_info` = `CandidateInfo.model_dump()`
- TODO:
  - Gọi LLM (OpenAI) với `EXTRACT_CANDIDATE_INFO_PROMPT.format(cv_text=...)`.
  - Yêu cầu JSON khớp schema `CandidateInfo`.
  - Parse JSON, tạo `CandidateInfo(...)`, trả về dict update state.

#### 3.2 `generate_interview_questions_node` — sinh câu hỏi phỏng vấn

- File: `nodes/generate_questions.py`
- Class: `QuestionItem`, `InterviewQuestions`
- Input:
  - `candidate_info`
- Output:
  - `questions`: list dict (từ `QuestionItem.model_dump()`).
  - `current_question_index`: 0.
- TODO:
  - Dùng `GENERATE_QUESTIONS_PROMPT` + `candidate_info`.
  - LLM trả về JSON `InterviewQuestions`.
  - Parse, cập nhật state.

#### 3.3 `ask_question_node` — node hỏi & chờ trả lời (Human-in-the-loop)

- File: `nodes/ask_question.py`
- Input:
  - `questions`, `current_question_index`, `messages`, `candidate_answer`.
- Output:
  - Append câu hỏi (role `"assistant"`) hoặc câu trả lời (role `"user"`) vào `messages`
    tùy theo trạng thái.
- Mục đích:
  - Lần 1 (chưa có `candidate_answer`):
    - Lấy câu hỏi hiện tại từ `questions[current_question_index]`.
    - Append vào `messages` với `role="assistant"`.
    - Trả state để graph **interrupt** cho UI hiển thị câu hỏi và chờ người dùng trả lời.
  - Sau khi người dùng trả lời (state đã có `candidate_answer`):
    - Append câu trả lời vào `messages` với `role="user"`.
    - Trả state mới để node `score_answer` sử dụng.
- TODO:
  - Hiện thực logic hai pha trên theo gợi ý docstring trong file.

#### 3.4 `score_answer_node`

- File: `nodes/score_answer.py`
- Class: `ScoreItem`
- Input:
  - `candidate_answer`, `questions`, `current_question_index`, `scores`.
- Output:
  - Append `{question_id, score, comment}` vào `scores`.
- TODO:
  - Lấy câu hỏi hiện tại.
  - Dùng `SCORE_ANSWER_PROMPT` + nội dung câu hỏi + `candidate_answer`.
  - LLM trả về JSON `ScoreItem`.
  - Parse và append vào `scores`.

#### 3.5 `next_question_node`

- File: `nodes/next_question.py`
- Input:
  - `current_question_index`, `candidate_answer`.
- Output:
  - Tăng `current_question_index`.
  - Reset `candidate_answer`.
- TODO:
  - Implement theo gợi ý trong docstring (hiện đang `NotImplementedError`).

#### 3.6 `aggregate_score_node`

- File: `nodes/aggregate_score.py`
- Input:
  - `scores`, `questions`.
- Output:
  - `total_score`, `max_score`, `percentage`.
- TODO:
  - Tính tổng score, tổng `max_score`, phần trăm điểm.

#### 3.7 `final_evaluation_node`

- File: `nodes/final_evaluation.py`
- Class: `FinalResult`
- Input:
  - `total_score`, `percentage`, `scores`, `candidate_info`.
- Output:
  - `final_result` = `{level, summary}`.
- TODO:
  - Dùng `FINAL_EVALUATION_PROMPT` + các thông tin trên.
  - LLM trả về JSON `FinalResult`.
  - Parse và cập nhật state.

#### 3.8 Routing nodes (`routing_edges.py`)

- File: `nodes/routing_edges.py`
- Các hàm:
  - `route_after_extract_candidate_info`
  - `route_after_generate_questions`
  - `route_after_wait_for_human_answer` (routing sau `ask_question`)
  - `route_after_score_answer`
  - `route_after_next_question`
  - `route_after_aggregate_score`
- TODO:
  - Dựa vào `state` (`error`, `questions`, `current_question_index`, v.v.) để trả về:
    - `END` hoặc
    - tên node tiếp theo (`GraphNode.XXX.value`).

---

### 4. Graph (agent.py)

- File: `agent.py`
- Hàm: `_build_graph()`
- TODO (docstring đã liệt kê chi tiết):
  - Import:
    - `StateGraph`, `END` từ `langgraph.graph`.
    - `MemorySaver` từ `langgraph.checkpoint.memory`.
    - Các node + routing từ `practices.nodes`.
    - `GraphNode` từ `node_define.py`.
  - Tạo:
    - `graph = StateGraph(InterviewState)`.
  - Thêm node:
    - `GraphNode.EXTRACT_CANDIDATE_INFO.value` → `extract_candidate_info_node`
    - `GraphNode.GENERATE_QUESTIONS.value` → `generate_interview_questions_node`
    - `GraphNode.ASK_QUESTION.value` → `ask_question_node`
    - `GraphNode.SCORE_ANSWER.value` → `score_answer_node`
    - `GraphNode.NEXT_QUESTION.value` → `next_question_node`
    - `GraphNode.AGGREGATE_SCORE.value` → `aggregate_score_node`
    - `GraphNode.FINAL_EVALUATION.value` → `final_evaluation_node`
  - Set entry point:
    - `graph.set_entry_point(GraphNode.EXTRACT_CANDIDATE_INFO.value)`.
  - Thêm các conditional edges với route_*:
    - extract_candidate_info → `route_after_extract_candidate_info`
    - generate_questions → `route_after_generate_questions`
    - ask_question → `route_after_wait_for_human_answer`
    - score_answer → `route_after_score_answer`
    - next_question → `route_after_next_question`
    - aggregate_score → `route_after_aggregate_score`
  - Khởi tạo checkpointer:
    - `memory = MemorySaver()`.
  - Compile:
    - `graph.compile(checkpointer=memory, interrupt_after=[GraphNode.ASK_QUESTION.value])`.
  - Trả về compiled app.

---

### 5. Main entry (main.py)

- File: `main.py`
- Hàm: `run()`
- TODO (docstring đã ghi rõ):
  - Import:
    - `settings` từ `config`.
    - `_build_graph` từ `practices.agent`.
    - Gradio (`import gradio as gr`).
  - Xây Gradio UI:
    - Upload CV (PDF/TXT).
    - Nếu PDF: dùng loader/LangChain/LangGraph để trích xuất text.
    - Lưu `cv_text` trong một `gr.State`.
  - Sinh `thread_id` cho mỗi session.
  - Lần đầu:
    - Gọi `graph.invoke({"cv_text": cv_text}, config=config)` để bắt đầu phỏng vấn.
  - Khi graph interrupt tại `ASK_QUESTION`:
    - Lấy câu hỏi hiện tại từ state (từ `messages` hoặc từ `questions`/`current_question_index`).
    - Hiển thị trên chat UI.
    - Nhận `candidate_answer` từ người dùng.
    - Gọi lại `graph.invoke({**state, "candidate_answer": answer}, config=config)` để resume.
  - Không cho phép đổi CV khi đang interrupt trong cùng `thread_id`.
  - Khi `final_result` có:
    - Hiển thị `level` + `summary`.

---

### 6. Checklist

- [ ] `prompt/*.py`: Viết nội dung prompt cụ thể cho từng bước.
- [ ] `nodes/extract_candidate_info.py`: gọi LLM, parse về `CandidateInfo`.
- [ ] `nodes/generate_questions.py`: gọi LLM, parse về `InterviewQuestions`.
- [ ] `nodes/ask_question.py`: logic hỏi & chờ trả lời (interrupt).
- [ ] `nodes/score_answer.py`: gọi LLM, parse `ScoreItem`, append `scores`.
- [ ] `nodes/next_question.py`: tăng index, reset `candidate_answer`.
- [ ] `nodes/aggregate_score.py`: tính tổng điểm, phần trăm.
- [ ] `nodes/final_evaluation.py`: gọi LLM, parse `FinalResult`.
- [ ] `nodes/routing_edges.py`: implement các route_* theo mô tả.
- [ ] `agent.py`: build graph, checkpointer, interrupt_after.
- [ ] `main.py`: Gradio app + upload PDF/TXT + interrupt/resume.

Sau khi implement xong, chạy `practices/main.py` để test đầy đủ luồng (bắt đầu có thể dùng `data/sample_cv.txt`).  
Hãy thử cả flow: upload CV → nhận câu hỏi → trả lời từng câu → xem kết quả cuối.

### Danh sách Function / Node cần implement (TODO)

Các mục dưới đây bám sát code scaffold trong thư mục `practices/`. Hãy đọc kỹ TODO trong từng file trước khi viết code.

---

### 1. State (`state.py`)

- File: `state.py`
- Bạn đã có `InterviewState` (TypedDict) và `Message`.
- Đảm bảo các trường:
  - `cv_text`, `candidate_info`, `questions`, `current_question_index`,
  - `candidate_answer`, `scores`, `messages`,
  - `total_score`, `max_score`, `percentage`,
  - `final_result`, `error`, `error_message`.
- Mục tiêu: toàn bộ node đều đọc/ghi qua `state: InterviewState`.

---

### 2. Prompts (`prompt/`)

Prompts đã được tách ra thành nhiều file, mỗi file chứa TODO mô tả rất rõ:

- `prompt/extract_candidate_info_prompt.py`
  - Biến: `EXTRACT_CANDIDATE_INFO_PROMPT`
  - TODO: viết prompt hướng dẫn LLM đọc `{cv_text}` và trả về JSON theo schema `CandidateInfo`.

- `prompt/generate_questions_prompt.py`
  - Biến: `GENERATE_QUESTIONS_PROMPT`
  - TODO: viết prompt sinh 3–5 câu hỏi phỏng vấn (JSON theo `QuestionItem`) dựa trên `candidate_info`.

- `prompt/score_answer_prompt.py`
  - Biến: `SCORE_ANSWER_PROMPT`
  - TODO: viết prompt chấm điểm một câu trả lời, output JSON theo `ScoreItem` (question_id, score, comment).

- `prompt/final_evaluation_prompt.py`
  - Biến: `FINAL_EVALUATION_PROMPT`
  - TODO: prompt đánh giá cuối (Pass / Consider / Reject + summary) dựa trên điểm + `candidate_info`.

Yêu cầu chung:

- Tất cả prompt nên yêu cầu **LLM trả về duy nhất một JSON object** khớp với schema tương ứng.
- Không in thêm text, giải thích, comment ngoài JSON.

---

### 3. Nodes (`nodes/`)

Mỗi node là một file riêng dưới `nodes/`. Hầu hết đã có class Pydantic và TODO mô tả chi tiết, bạn cần hiện thực phần thân.

#### 3.1 `extract_candidate_info_node` — trích xuất thông tin ứng viên

- File: `nodes/extract_candidate_info.py`
- Class: `CandidateInfo`
- Input state:
  - `cv_text`
- Output state:
  - `candidate_info` = `CandidateInfo.model_dump()`
- TODO:
  - Gọi LLM (OpenAI) với `EXTRACT_CANDIDATE_INFO_PROMPT.format(cv_text=...)`.
  - Yêu cầu JSON khớp schema `CandidateInfo`.
  - Parse JSON, tạo `CandidateInfo(...)`, trả về dict update state.

#### 3.2 `generate_interview_questions_node` — sinh câu hỏi phỏng vấn

- File: `nodes/generate_questions.py`
- Class: `QuestionItem`, `InterviewQuestions`
- Input:
  - `candidate_info`
- Output:
  - `questions`: list dict (từ `QuestionItem.model_dump()`).
  - `current_question_index`: 0.
- TODO:
  - Dùng `GENERATE_QUESTIONS_PROMPT` + `candidate_info`.
  - LLM trả về JSON `InterviewQuestions`.
  - Parse, cập nhật state.

#### 3.3 `wait_for_human_answer_node` — mốc interrupt

- File: `nodes/wait_for_human_answer.py`
- Mục đích:
  - Không gọi LLM, không đọc input.
  - Chỉ là điểm dừng (interrupt) để UI/`main.py`:
    - Lấy câu hỏi hiện tại.
    - Hiển thị cho người dùng.
    - Nhận câu trả lời và gán vào `candidate_answer` rồi resume.
- TODO:
  - Implement nhẹ (hoặc chỉ raise `NotImplementedError`) theo gợi ý trong docstring, tùy bạn thiết kế interrupt.

#### 3.4 `ask_question_node`

- File: `nodes/ask_question.py`
- Input:
  - `questions`, `current_question_index`, `messages`.
- Output:
  - Append câu hỏi hiện tại (role `"assistant"`) vào `messages`.
- TODO:
  - Lấy `questions[idx]`, format thành câu text, append vào `messages`.
  - Trả về dict cập nhật `messages`.

#### 3.5 `score_answer_node`

- File: `nodes/score_answer.py`
- Class: `ScoreItem`
- Input:
  - `candidate_answer`, `questions`, `current_question_index`, `scores`.
- Output:
  - Append `{question_id, score, comment}` vào `scores`.
- TODO:
  - Lấy câu hỏi hiện tại.
  - Dùng `SCORE_ANSWER_PROMPT` + question + `candidate_answer`.
  - LLM trả về JSON `ScoreItem`.
  - Parse và append vào `scores`.

#### 3.6 `next_question_node`

- File: `nodes/next_question.py`
- Input:
  - `current_question_index`, `candidate_answer`.
- Output:
  - Tăng `current_question_index`.
  - Reset `candidate_answer`.
- TODO:
  - Implement theo gợi ý trong docstring (hiện đang `NotImplementedError`).

#### 3.7 `aggregate_score_node`

- File: `nodes/aggregate_score.py`
- Input:
  - `scores`, `questions`.
- Output:
  - `total_score`, `max_score`, `percentage`.
- TODO:
  - Tính tổng score, tổng max_score, phần trăm.

#### 3.8 `final_evaluation_node`

- File: `nodes/final_evaluation.py`
- Class: `FinalResult`
- Input:
  - `total_score`, `percentage`, `scores`, `candidate_info`.
- Output:
  - `final_result` = `{level, summary}`.
- TODO:
  - Dùng `FINAL_EVALUATION_PROMPT` + các thông tin trên.
  - LLM trả về JSON `FinalResult`.
  - Parse và cập nhật state.

#### 3.9 Routing nodes (`routing_edges.py`)

- File: `nodes/routing_edges.py`
- Các hàm:
  - `route_after_extract_candidate_info`
  - `route_after_generate_questions`
  - `route_after_wait_for_human_answer`
  - `route_after_score_answer`
  - `route_after_next_question`
  - `route_after_aggregate_score`
- Hầu hết đã được chuyển về dạng TODO + `NotImplementedError`. Bạn cần:
  - Dựa vào `state` (`error`, `questions`, `current_question_index`, v.v.) để trả về:
    - `END` hoặc
    - tên node tiếp theo (`GraphNode.XXX.value`).

---

### 4. Graph (agent.py)

- File: `agent.py`
- Hàm: `_build_graph()`
- TODO (docstring đã liệt kê rất chi tiết):
  - Import:
    - `StateGraph`, `END` từ `langgraph.graph`.
    - `MemorySaver` từ `langgraph.checkpoint.memory`.
    - Các node và routing từ `practices.nodes`.
    - `GraphNode` từ `node_define.py`.
  - Tạo `graph = StateGraph(InterviewState)`.
  - Thêm node:
    - `GraphNode.EXTRACT_CANDIDATE_INFO.value` → `extract_candidate_info_node`, ...
  - Set entry point:
    - `graph.set_entry_point(GraphNode.EXTRACT_CANDIDATE_INFO.value)`.
  - Thêm các conditional edges với route_*:
    - extract_candidate_info → route_after_extract_candidate_info → ...
    - generate_questions → route_after_generate_questions → ...
    - wait_for_human_answer → route_after_wait_for_human_answer → ...
    - score_answer → route_after_score_answer → ...
    - next_question → route_after_next_question → ...
    - aggregate_score → route_after_aggregate_score → final_evaluation / END.
  - Khởi tạo checkpointer:
    - `memory = MemorySaver()`.
  - Compile:
    - `graph.compile(checkpointer=memory, interrupt_after=[GraphNode.WAIT_FOR_HUMAN_ANSWER.value])`.
  - Trả về compiled app.

---

### 5. Main entry (main.py)

- File: `main.py`
- Hàm: `run()`
- TODO (docstring đã ghi rõ):
  - Import:
    - `settings` từ `config`.
    - `_build_graph` từ `practices.agent`.
    - Gradio (`import gradio as gr`).
  - Xây Gradio UI:
    - Upload CV (PDF/TXT).
    - Nếu PDF: dùng loader/LangChain/LangGraph để trích xuất text.
    - Lưu `cv_text` trong một `gr.State`.
  - Sinh `thread_id` cho mỗi session.
  - Lần đầu:
    - Gọi `graph.invoke({"cv_text": cv_text}, config=config)` để bắt đầu phỏng vấn.
  - Khi graph interrupt:
    - Lấy câu hỏi hiện tại từ state.
    - Hiển thị trên chat UI.
    - Nhận `candidate_answer` từ người dùng.
    - Gọi lại `graph.invoke({**state, "candidate_answer": answer}, config=config)` để resume.
  - Không cho phép đổi CV khi đang interrupt trong cùng `thread_id`.
  - Khi `final_result` có:
    - Hiển thị level + summary.

---

### 6. Checklist

- [ ] `prompt/*.py`: Viết nội dung prompt cụ thể cho từng bước.
- [ ] `nodes/extract_candidate_info.py`: gọi LLM, parse về `CandidateInfo`.
- [ ] `nodes/generate_questions.py`: gọi LLM, parse về `InterviewQuestions`.
- [ ] `nodes/ask_question.py`: append câu hỏi vào `messages`.
- [ ] `nodes/wait_for_human_answer.py`: thiết kế interrupt node.
- [ ] `nodes/score_answer.py`: gọi LLM, parse `ScoreItem`, append `scores`.
- [ ] `nodes/next_question.py`: tăng index, reset `candidate_answer`.
- [ ] `nodes/aggregate_score.py`: tính tổng điểm, phần trăm.
- [ ] `nodes/final_evaluation.py`: gọi LLM, parse `FinalResult`.
- [ ] `nodes/routing_edges.py`: implement các route_* theo mô tả.
- [ ] `agent.py`: build graph, checkpointer, interrupt_after.
- [ ] `main.py`: Gradio app + upload PDF/TXT + interrupt/resume.

Sau khi implement xong, chạy `practices/main.py` để test đầy đủ luồng (bắt đầu có thể dùng `data/sample_cv.txt`).  
Hãy thử cả flow: upload CV → nhận câu hỏi → trả lời từng câu → xem kết quả cuối.
