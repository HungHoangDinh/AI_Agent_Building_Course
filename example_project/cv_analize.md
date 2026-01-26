# Bài thực hành: Hệ thống AI Agent lọc & phân tích CV

## Mục tiêu tổng quát
- Đọc & phân tích CV (PDF/DOCX)
- Trích xuất thông tin có cấu trúc (Excel/CSV)
- Chấm điểm, nhóm, so sánh ứng viên theo JD
- Tư duy AI Agent + orchestration bằng LangGraph

## Tổng quan hệ thống
- **Input**: CV (PDF/DOCX), JD (text)
- **Output**: Excel/CSV tổng hợp, bảng xếp hạng/so sánh, CV format chuẩn, báo cáo (Markdown/PDF)

---

## Buổi 1 – Đọc & trích xuất CV (LangChain)
- Dùng loader `PyPDFLoader` / `Docx2txtLoader` để đọc CV và chuẩn hóa text
- PromptTemplate + Pydantic Output Parser để trích xuất JSON (name/email/phone/skills/years/education)
- Xuất CSV/Excel (mỗi CV = 1 dòng) bằng `pandas`

## Buổi 2 – RAG: phân tích CV theo JD
- Ingest JD: chunk → embedding → vector store
- Hỏi–đáp CV theo JD (kỹ năng khớp, kinh nghiệm phù hợp) dựa trên ngữ cảnh truy xuất
- Gắn metadata (nguồn CV/vị trí/năm KN) + chấm điểm sơ bộ (0–10 kỹ năng, 0–10 kinh nghiệm + nhận xét)

## Buổi 3 – Agent & Tool Calling: lọc, nhóm, so sánh
- Xây tools: `read_cv`, `extract_candidate_info`, `score_candidate`, `compare_candidates`
- Agent chạy batch: đọc nhiều CV, skip lỗi/thiếu thông tin, chấm điểm theo JD, chọn top N
- Xuất bảng so sánh và xếp hạng

## Buổi 4 – LangGraph: workflow hoàn chỉnh + formatter
- StateGraph nodes: Load → Extract → Score → Group → Compare → Export (kèm errors)
- Conditional routing: lỗi → error node; thiếu info → retry; dưới threshold → loại
- Thêm CV Formatter Agent: chuẩn hóa template, Việt↔Anh, text→Markdown/PDF (không bịa thêm thông tin)

---
