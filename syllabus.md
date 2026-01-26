# LangChain Course 

## Buổi 1: Nền tảng LLM + LangChain căn bản

1. Tổng quan LLM: provider, prompt, context, ứng dụng, hạn chế.
2. LangChain overview: vì sao cần framework; so sánh nhanh với LangGraph.
3. Prompt & PromptTemplate, Structured Output, Output Parser.
4. Chain & Memory: tổ chức logic, ghi nhớ hội thoại.
5. Streamlit and Gradio.

---

## Buổi 2: RAG với dữ liệu cá nhân

1. Kiến trúc RAG; chunking, Embedding, Vector Store, Retriever.
2. Thực hành: ingest tài liệu nội bộ (quy chế công ty), lưu Chroma/FAISS.
3. Xây dựng chatbot RAG: truy xuất theo ngữ nghĩa, kiểm soát trích dẫn nguồn.
4. Nâng cao: xử lý đa tài liệu, lọc theo metadata, hạn chế hallucination.

---

## Buổi 3: Agent & Tool Calling

1. Khái niệm Agent vs Chain; khi nào dùng Agent.
2. Các pattern: ReAct, Plan-and-Execute, Conversational Agent.
3. Thiết kế Tool: mô tả, validation, error handling, retry.
4. Agent Execution Loop và logging.
5. Thực hành: Agent đa tool (web search, calculator, DB/API) với kiểm soát lỗi.

---

## Buổi 4: LangGraph & Project cuối khóa

1. LangGraph cốt lõi: State, StateGraph, Nodes, Edges, Conditional routing.
2. Orchestration nâng cao: checkpoints, persistence, human-in-the-loop, streaming.
3. Thực hành LangGraph: xây workflow nhiều bước có rẽ nhánh và retry.
4. Project cuối khóa: xây agent/workflow hoàn chỉnh (LangGraph + FastAPI + Streamlit/Gradio)