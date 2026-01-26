
## Tiêu chí bài toán để được tốt nghiệp

### 1. Khả thi trong 2 tuần
- Hoàn thiện được trong 2 tuần
- Không phụ thuộc data quá lớn / private khó lấy
- Có thể dùng CV mẫu công khai để demo

### 2. BẮT BUỘC sử dụng Agent (không phải Chain đơn giản)
- **Agent có reasoning & tool calling**:
  - Agent tự quyết định khi nào dùng tool nào
  - Có ít nhất 3 tools: `read_cv`, `extract_info`, `score_candidate` (bắt buộc)
  - Agent xử lý được batch nhiều CV, tự skip lỗi
- **Không chấp nhận**: Chain tuyến tính đơn giản (load → extract → output)

### 3. BẮT BUỘC sử dụng LangGraph cho workflow
- **StateGraph với ít nhất 4 nodes**:
  - Load/Ingest node
  - Extract/Process node  
  - Score/Analyze node
  - Export/Output node
- **Conditional routing logic**:
  - Xử lý lỗi (CV không đọc được → error node)
  - Retry logic (thiếu thông tin → retry extract)
  - Threshold routing (điểm < ngưỡng → loại bỏ)
- **State management**: Lưu trữ được state giữa các node (parsed_cvs, scores, errors)

### 4. Tính năng tối thiểu bắt buộc
- **Đọc CV**: Hỗ trợ ít nhất PDF hoặc DOCX
- **Trích xuất thông tin**: Name, email, phone, skills, years_experience (tối thiểu)
- **Chấm điểm theo JD**: Điểm số 0-100 + lý do
- **Xuất kết quả**: CSV/Excel với ít nhất 5 ứng viên
- **Xử lý lỗi**: Không crash khi CV lỗi format

### 5. Demo end-to-end có UI
- **Không chỉ code snippet / notebook**
- Có giao diện để:
  - Upload CV (nhiều file)
  - Nhập/upload JD
  - Xem kết quả (bảng xếp hạng, điểm số)
  - Download CSV/Excel
- **UI chấp nhận**: Streamlit / Gradio / FastAPI + HTML đơn giản / CLI interactive

---

## Form nghiệm thu sản phẩm và đánh giá khóa học

### Thông tin bài toán
- **Tên bài toán**: 
- **Giải quyết vấn đề gì**: 

### Demo & Kỹ thuật
- **Link demo/GitHub**: 
- **Input**: (VD: 5 CV files PDF/DOCX + 1 JD text)
- **Output**: (VD: CSV với 5 ứng viên đã xếp hạng + điểm số)
- **Cách chạy demo**: (VD: `streamlit run app.py` hoặc `python main.py --cv_dir ./cvs --jd job.txt`)

### Agent & Tool Calling
- **Số lượng Agent**: (VD: 1 Agent chính + 1 Formatter Agent)
- **Danh sách Tools**: (liệt kê tất cả tools: read_cv, extract_info, score_candidate, compare_candidates, export_csv, ...)
- **Tool usage examples**: (Ví dụ: Agent dùng tool nào khi nào? VD: "Khi CV lỗi → dùng error_handler tool")

### LangGraph Workflow
- **Số lượng Nodes**: (VD: 6 nodes)
- **Danh sách Nodes**: (LoadCV → ExtractInfo → ScoreCandidate → GroupCandidates → CompareTop → ExportCSV)
- **State schema**: (Mô tả các field trong state: cv_files, parsed_cvs, scores, errors, ...)
- **Routing logic**: 
  - Conditional 1: (VD: Nếu extract lỗi → retry node)
  - Conditional 2: (VD: Nếu điểm < 50 → loại bỏ, không vào compare node)
  - Conditional 3: (VD: Nếu không có JD → bỏ qua score node)
- **Graph flow diagram**: (Có thể mô tả text hoặc link ảnh sơ đồ)

### Tính năng đã implement
- [ ] Đọc CV PDF/DOCX
- [ ] Trích xuất thông tin có cấu trúc (JSON)
- [ ] Chấm điểm theo JD
- [ ] So sánh ứng viên
- [ ] Xuất CSV/Excel
- [ ] Xử lý lỗi (CV lỗi format)
- [ ] UI để upload và xem kết quả
- [ ] (Tùy chọn) CV Formatter
- [ ] (Tùy chọn) Nhóm ứng viên
- [ ] (Tùy chọn) Deduplication


