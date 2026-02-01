# Bài tập: Trợ lý Chuyển đổi Ngoại tệ & Tra cứu Lương Real-time

## Mục tiêu

Xây dựng một **Agent** có khả năng:

1. **Cập nhật tỷ giá mới nhất từ Internet** (không dùng dữ liệu cũ trong bộ nhớ AI).
2. **Xử lý các con số lớn của VND chính xác** (dùng tool Calculator, tránh lỗi tính toán của LLM).
3. **Hỗ trợ đa loại tiền tệ** (USD, EUR, JPY, KRW...) sang VND và ngược lại.
4. **Tra cứu vị trí công việc tại Rikkeisoft**, tìm lương cơ bản và quy đổi sang các đồng tiền khác.

## Các công cụ (Tools) cần thiết

| Tool | Mục đích |
|------|----------|
| **Tool 1: Search (DuckDuckGo)** | Tìm tỷ giá: "1 USD bằng bao nhiêu VND hôm nay?", "Tỷ giá Vietcombank hôm nay". |
| **Tool 2: Calculator (LLM-Math)** | Nhân/chia số tiền với tỷ giá; đảm bảo chính xác với số lớn (VD: 100.000.000 VND). |
| **Tool 3: Job Retrieval (RAG)** | Tra cứu vị trí công việc trong dữ liệu đã ingest (jobs.md), trả về thông tin JD/lương (nếu có) và có thể kết hợp quy đổi tiền tệ. |

## Memory

- Agent có **memory** dạng bài tập: lưu lịch sử hội thoại hoặc context ngắn để tham chiếu khi cần (VD: tỷ giá vừa tra, vị trí vừa hỏi).

## Retrieval / Ingest (RAG)

- **Ingest**: Load dữ liệu `data/jobs.md` → split → embed → lưu vào vector store (Chroma), tương tự `lecture_2` (loader → embeddings → ingest).
- **Retrieval**: Tool tra cứu job dùng retriever để tìm các chunk liên quan đến vị trí công việc (Frontend, Backend, DevOps...) trong vector store.

## Cấu trúc thư mục

```
practices/
├── README.md                 # File này
├── FUNCTIONS.md              # Liệt kê chi tiết các function cần implement (TODO)
├── config.py                 # (optional) Hoặc dùng config từ lecture_3
├── ingest.py                 # Script ingest data vào vector store (RAG)
├── main.py                   # Entry: Gradio/CLI chạy agent
├── agent.py                  # Tạo agent với tools + memory
├── data/
│   └── jobs.md               # Dữ liệu JD (đã có)
├── src/                      # RAG pipeline (loader, embeddings, retriever)
│   ├── __init__.py
│   ├── loader.py             # Load & split markdown
│   ├── embeddings.py         # Embedding + vector store + ingest_documents
│   └── retriever.py          # get_retriever(query)
├── tools/
│   ├── __init__.py
│   ├── search_tool.py        # DuckDuckGo search
│   ├── calculator_tool.py    # Calculator / LLM-Math
│   └── job_retrieval_tool.py # Tra cứu job qua RAG
└── prompt/
    ├── __init__.py
    └── prompt.py             # System prompt cho agent
```

## Tham khảo

- **RAG pipeline**: `lecture_2/src` (loader, embeddings, retriever), `lecture_2/ingest.py`, `lecture_2/main.py`.
- **Tools**: `lecture_3/main.ipynb` (DuckDuckGo search).

## Config

- Có thể dùng `config` từ `lecture_3` (parent): thêm `lecture_3` vào `sys.path` rồi `from config import settings` (LLM_API_KEY, LLM_BASE_URL, LLM_CHAT_MODEL, LLM_EMBEDDING_MODEL).
- Vector store mặc định nằm trong `practices/vector_store`; khi gọi `get_retriever` cần truyền cùng `persist_directory` đã dùng khi ingest.

## Cách làm bài

1. Đọc `FUNCTIONS.md` để biết từng function cần implement.
2. Implement theo TODO trong từng file (loader, embeddings, retriever, ingest, tools, agent, main).
3. Chạy `ingest.py` để ingest `data/jobs.md` vào vector store trước khi dùng tool Job Retrieval.
4. Chạy `main.py` (hoặc Gradio) để test agent với các câu hỏi mẫu: tỷ giá, quy đổi tiền, tra cứu lương/vị trí Rikkeisoft.
