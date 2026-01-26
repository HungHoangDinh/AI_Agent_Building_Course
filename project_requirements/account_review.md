
## Tiêu chí bài toán để được tốt nghiệp

### 1. Khả thi trong 2 tuần
- Hoàn thiện được trong 2 tuần
- Không phụ thuộc data quá lớn / private khó lấy
- Có thể dùng công ty công khai để demo 
- Industry reports có thể dùng tài liệu mẫu công khai hoặc tự tạo

### 2. BẮT BUỘC sử dụng Agent (không phải Chain đơn giản)
- **Agent có reasoning & tool calling**:
  - Agent tự quyết định khi nào dùng tool nào
  - Có ít nhất 4 tools: `search_account_info`, `normalize_account_snapshot`, `analyze_business_context`, `fit_scoring` (bắt buộc)
  - Agent tự động retry khi thiếu thông tin, xử lý trường hợp không tìm thấy công ty
- **Không chấp nhận**: Chain tuyến tính đơn giản (search → extract → output)

### 3. BẮT BUỘC sử dụng LangGraph cho workflow
- **StateGraph với ít nhất 5 nodes**:
  - Search/Research node
  - Snapshot/Normalize node
  - Context/Analysis node (RAG)
  - FitScore/Evaluate node
  - Export/Report node
- **Conditional routing logic**:
  - Xử lý lỗi (không tìm thấy công ty → error node)
  - Retry logic (thiếu thông tin → retry search/snapshot)
  - Threshold routing (fit score thấp → flag no-go, không vào recommend node)
- **State management**: Lưu trữ được state giữa các node (raw_data, account_snapshot, industry_context, pain_points, fit_score, recommendations)

### 4. Tính năng tối thiểu bắt buộc
- **Tra cứu thông tin công ty**: Tìm được industry, offerings, size estimate, markets (tối thiểu)
- **Chuẩn hoá Account Snapshot**: JSON với name/industry/model/size/markets/key_offerings/summary
- **RAG với industry context**: Ingest và query được industry reports/solution overview
- **Phân tích pain points**: Đưa ra ít nhất 3 giả thuyết pain points dựa trên ngành/quy mô
- **Chấm điểm fit**: Điểm số 0-100 + lý do chi tiết
- **Xuất report**: Markdown/PDF với ít nhất 5 phần (Overview, Context, Challenges, Fit Assessment, Recommendations)

### 5. Demo end-to-end có UI
- **Không chỉ code snippet / notebook**
- Có giao diện để:
  - Nhập tên công ty/domain
  - Chọn mục tiêu review (first meeting / proposal / qualification)
  - Xem kết quả (Account Snapshot, Fit Score, Pain Points, Recommendations)
  - Download Account Review Report (Markdown/PDF)
- **UI chấp nhận**: Streamlit / Gradio / FastAPI + HTML đơn giản / CLI interactive/...

---

## Form nghiệm thu sản phẩm và đánh giá khóa học

### Thông tin bài toán
- **Tên bài toán**: 
- **Giải quyết vấn đề gì**: 

### Demo & Kỹ thuật
- **Link demo/GitHub**: 
- **Input**: (VD: Tên công ty "Microsoft", mục tiêu "proposal preparation", ngành "Technology")
- **Output**: (VD: Account Review Report PDF với 5 phần: Overview, Context, Challenges, Fit Assessment, Recommendations)
- **Cách chạy demo**: (VD: `streamlit run app.py` hoặc `python main.py --company "Microsoft" --goal "proposal"`)

### Agent & Tool Calling
- **Số lượng Agent**: (VD: 1 Account Review Agent chính)
- **Danh sách Tools**: (liệt kê tất cả tools: search_account_info, normalize_account_snapshot, analyze_business_context, hypothesize_pain_points, fit_scoring, export_report, ...)
- **Tool usage examples**: (Ví dụ: Agent dùng tool nào khi nào? VD: "Khi không tìm thấy công ty → retry search với domain khác")

### LangGraph Workflow
- **Số lượng Nodes**: (VD: 7 nodes)
- **Danh sách Nodes**: (SearchAccount → NormalizeSnapshot → AnalyzeContext → HypothesizePainPoints → ScoreFit → RecommendFocus → ExportReport)
- **State schema**: (Mô tả các field trong state: company_name, raw_data, account_snapshot, industry_context, pain_points, fit_score, recommendations, errors, ...)
- **Routing logic**: 
  - Conditional 1: (VD: Nếu không tìm thấy công ty → error node)
  - Conditional 2: (VD: Nếu fit score < 50 → flag no-go, không vào recommend node)
  - Conditional 3: (VD: Nếu thiếu industry context → retry context node)
- **Graph flow diagram**: (Có thể mô tả text hoặc link ảnh sơ đồ)

### Tính năng đã implement
- [ ] Tra cứu thông tin công ty (web search)
- [ ] Chuẩn hoá Account Snapshot (JSON)
- [ ] RAG với industry reports/solution overview
- [ ] Phân tích business context & signals
- [ ] Hypothesize pain points
- [ ] Chấm điểm fit (0-100 + lý do)
- [ ] Đề xuất focus areas/recommendations
- [ ] Xuất Account Review Report (Markdown/PDF)
- [ ] Xử lý lỗi (không tìm thấy công ty, thiếu dữ liệu)
- [ ] UI để nhập công ty và xem kết quả
- [ ] (Tùy chọn) Go/No-Go Decision Agent
- [ ] (Tùy chọn) Competitive Landscape Analysis
- [ ] (Tùy chọn) Risk & Compliance Signals

