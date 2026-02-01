# Danh sách Function cần implement (TODO)

Các function dưới đây được liệt kê theo thứ tự phụ thuộc. Implement theo TODO trong từng file, có thể tham chiếu `lecture_2` cho RAG và `lecture_3/main.ipynb` cho tools.

---

## 1. RAG pipeline (ingest & retrieval)

### 1.1 `src/loader.py`

- **`load_and_split(path: str) -> List[Document]`**
  - TODO: Load file markdown từ `path` (VD: `data/jobs.md`).
  - TODO: Dùng loader phù hợp (UnstructuredMarkdownLoader hoặc đọc file + tạo Document).
  - TODO: Split bằng RecursiveCharacterTextSplitter (chunk_size, chunk_overlap phù hợp).
  - Trả về danh sách Document (LangChain) có metadata `source` (đường dẫn file).

### 1.2 `src/embeddings.py`

- **Embedding function**
  - TODO: Khởi tạo embedding (OpenAI hoặc tương thích với `config` của lecture_3), tham chiếu `lecture_2/src/embeddings.py`.

- **`create_or_get_vector_store(collection_name, persist_directory, delete_existing=False)`**
  - TODO: Tạo hoặc lấy Chroma vector store với embedding function.
  - TODO: Nếu `delete_existing` thì xóa collection cũ rồi tạo mới.

- **`ingest_documents(collection_name, persist_directory, documents)`**
  - TODO: Lấy vector store, add_documents(documents). Raise ValueError nếu documents rỗng.

### 1.3 `src/retriever.py`

- **`get_retriever(query: str, k: int = 5) -> List[Document]`**
  - TODO: Lấy vector store (create_or_get_vector_store), gọi similarity_search(query, k).
  - Trả về danh sách Document liên quan đến `query`.

### 1.4 `ingest.py`

- **`ingest_documents_from_markdown(path: str, ingest_directory: str = "vector_store")`**
  - TODO: Gọi `load_and_split(path)` từ `src.loader`.
  - TODO: Gọi `ingest_documents(documents=..., persist_directory=ingest_directory)` từ `src.embeddings`.
  - TODO: In log số chunk đã ingest.
- **`if __name__ == "__main__"`**: Gọi ingest với `data/jobs.md` và thư mục vector_store (có thể nằm trong `practices/`).

---

## 2. Tools

### 2.1 `tools/search_tool.py`

- **`search_internet(query: str) -> str`** (hoặc dùng `@tool` của LangChain)
  - TODO: Dùng DuckDuckGoSearchRun (langchain_community.tools) để search.
  - Mô tả tool: dùng để tìm tỷ giá mới nhất (VD: "1 USD to VND today", "tỷ giá Vietcombank hôm nay").
  - Trả về chuỗi kết quả tìm kiếm cho agent đọc.

### 2.2 `tools/calculator_tool.py`

- **`calculate(expression: str) -> str`** (hoặc dùng tool Calculator / LLM-Math của LangChain)
  - TODO: Dùng tool Calculator (langchain_community.tools) hoặc LLMMathChain / numexpr để tính biểu thức toán.
  - Mô tả tool: tính toán chính xác phép nhân/chia số tiền với tỷ giá (VD: 50000 * 25000).
  - Trả về kết quả dạng chuỗi.

### 2.3 `tools/job_retrieval_tool.py`

- **`search_job_positions(query: str, k: int = 5) -> str`** (hoặc `@tool`)
  - TODO: Gọi `get_retriever(query, k)` từ `src.retriever`.
  - TODO: Format danh sách Document thành chuỗi (title + content + source) để agent đọc.
  - Mô tả tool: tra cứu vị trí công việc tại Rikkeisoft (hoặc trong dữ liệu đã ingest); dữ liệu có thể chứa JD, yêu cầu, không nhất thiết có lương — agent có thể kết hợp với search tỷ giá và calculator để ước tính/quy đổi nếu user hỏi lương theo tiền tệ khác.

---

## 3. Agent & Memory

### 3.1 `prompt/prompt.py`

- **`CURRENCY_JOB_AGENT_SYSTEM_PROMPT`** (chuỗi)
  - TODO: Viết system prompt cho agent:
    - Nhiệm vụ: trả lời câu hỏi về tỷ giá, quy đổi ngoại tệ (USD, EUR, JPY, KRW... ↔ VND), tra cứu vị trí công việc và lương (nếu có) trong dữ liệu Rikkeisoft.
    - Quy tắc: luôn dùng tool Search để lấy tỷ giá mới nhất (không đoán); luôn dùng Calculator cho phép tính tiền tệ; dùng Job Retrieval khi user hỏi về job/vị trí/lương.
    - Hướng dẫn ngắn về khi nào dùng từng tool.

### 3.2 `agent.py`

- **`create_tools()`** (hoặc tương đương)
  - TODO: Tạo list tools: search_internet, calculate, search_job_positions (đã wrap bằng @tool hoặc LangChain Tool).

- **`create_memory()`**
  - TODO: Tạo memory cho agent (dạng bài tập): có thể là ChatMessageHistory (window buffer) hoặc ConversationBufferWindowMemory để lưu vài turn gần nhất.

- **`create_agent(llm, tools, memory, prompt)`**
  - TODO: Tạo agent (ReAct hoặc create_react_agent) với llm, tools, system prompt; bind memory vào agent/chain.
  - Trả về object agent/chain có thể invoke.

### 3.3 `main.py`

- **`run_agent(user_message: str, history: list) -> tuple`** (hoặc tương đương)
  - TODO: Load agent (create_agent), invoke với user_message và history/memory; trả về (output_string, updated_history).

- **Gradio (hoặc CLI)**
  - TODO: Giao diện đơn giản: ô nhập câu hỏi, nút gửi, hiển thị lịch sử chat; có thể thêm nút "Clear" để xóa memory/history.
  - Gợi ý câu hỏi mẫu: "1 USD bằng bao nhiêu VND?", "Tra cứu vị trí Frontend Developer tại Rikkeisoft", "Quy đổi 50 triệu VND sang USD theo tỷ giá hôm nay".

---

## 4. Thiết kế Retrieval / Ingest (RAG)

- **Ingest**: Giống `lecture_2`: một script `ingest.py` gọi loader (markdown) → split → embed → ingest_documents vào Chroma. Người dùng chạy một lần (hoặc khi cập nhật `jobs.md`).
- **Retrieval**: Tool `search_job_positions` gọi `get_retriever(query)` → similarity_search trên vector store đã ingest → format kết quả cho agent. Không cần RAG chain phức tạp trong bước này; agent tự quyết định dùng kết quả retrieval kết hợp với search tỷ giá và calculator.

---

## 5. Checklist

- [ ] `src/loader.py`: load_and_split cho markdown
- [ ] `src/embeddings.py`: embedding, create_or_get_vector_store, ingest_documents
- [ ] `src/retriever.py`: get_retriever
- [ ] `ingest.py`: ingest_documents_from_markdown, __main__
- [ ] `tools/search_tool.py`: search_internet (DuckDuckGo)
- [ ] `tools/calculator_tool.py`: calculate (Calculator/LLM-Math)
- [ ] `tools/job_retrieval_tool.py`: search_job_positions (RAG)
- [ ] `prompt/prompt.py`: CURRENCY_JOB_AGENT_SYSTEM_PROMPT
- [ ] `agent.py`: create_tools, create_memory, create_agent
- [ ] `main.py`: run_agent, Gradio/CLI

Sau khi implement xong, chạy ingest rồi chạy main để test đầy đủ luồng.
