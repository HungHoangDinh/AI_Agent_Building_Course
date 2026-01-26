# Bài thực hành: Account Review AI Agent

## Mục tiêu bài toán
- Tra cứu & tổng hợp thông tin doanh nghiệp
- Phân tích bối cảnh kinh doanh & pain points
- Đánh giá mức độ phù hợp (fit) với năng lực công ty
- Chuẩn bị nội dung cho meeting/proposal/go–no-go  

## Input / Output
- **Input**: tên công ty/domain, mục tiêu (first meeting / proposal / qualification), ngành ưu tiên (tuỳ chọn)
- **Output**: Account Snapshot, Business Context & Signals, Pain Points Hypothesis, Fit Analysis, Recommended Focus Areas, Account Review Report (Markdown/PDF)

---

## Buổi 1 – Account Snapshot & Research cơ bản
- Tra cứu thông tin công ty (industry, offerings, size estimate, markets, clients/partners nổi bật)
- Chuẩn hoá Account Snapshot (LLM → JSON: name/industry/model/size/markets/key_offerings/summary)
- Mục tiêu: có snapshot chuẩn, làm dữ liệu đầu vào cho các bước sau

## Buổi 2 – Context Analysis & Industry Insight (RAG)
- Ingest dữ liệu nội bộ (industry report, solution overview, past accounts) → vector store theo ngành/thị trường/use case
- Hỏi–đáp ngữ cảnh: thách thức ngành, xu hướng công nghệ ảnh hưởng, signals rủi ro/tăng trưởng
- Output: industry context summary + key trends gắn với account

## Buổi 3 – Agent & Tool Calling: Account Review Agent
- Tools: `search_account_info`, `normalize_account_snapshot`, `analyze_business_context`, `hypothesize_pain_points`, `fit_scoring`
- Agent flow: tra cứu → chuẩn hoá snapshot → phân tích bối cảnh → giả thuyết pain points → chấm điểm fit (có lý do)
- Kết quả: danh sách insight + fit score, phục vụ quyết định go/no-go hoặc chuẩn bị proposal

## Buổi 4 – LangGraph: Workflow Account Review hoàn chỉnh
- StateGraph nodes: Search → Snapshot → Context → PainPoint → FitScore → Recommend → Export (+ Error)
- Conditional routing: thiếu dữ liệu → retry; không tìm thấy → Error; fit thấp → flag no-go
- Xuất report: Account Overview, Context, Key Challenges, Fit Assessment, Recommended Focus Areas (Markdown/PDF)

---
