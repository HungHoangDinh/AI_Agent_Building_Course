# Tiêu chí bài toán tốt nghiệp & Form nghiệm thu

## Tiêu chí bài toán để được tốt nghiệp

### 1. Khả thi trong 2 tuần
- Hoàn thiện trong 2 tuần, dùng data mẫu công khai, không cần data quá lớn

### 2. BẮT BUỘC sử dụng Agent (không phải Chain đơn giản)
- Agent có reasoning & tool calling: tự quyết định dùng tool nào, có ≥3 tools, xử lý lỗi/retry
- Không chấp nhận: Chain tuyến tính đơn giản

### 3. BẮT BUỘC sử dụng LangGraph cho workflow
- StateGraph ≥4 nodes, có conditional routing (error/retry/threshold), quản lý state giữa nodes

### 4. Tính năng tối thiểu
- Xử lý input (file/text/web/API), thực hiện chức năng chính, tạo output (report/CSV/JSON/PDF), xử lý lỗi cơ bản

### 5. Demo end-to-end có UI
- Có UI để nhập input, xem kết quả, download output
- Sử dụng Streamlit/Gradio/FastAPI + HTML đơn giản/React/Vue/...

## Form nghiệm thu sản phẩm (Microsoft Form)

### Phần 1: Thông tin bài toán
1. **Tên bài toán** (Text, bắt buộc)
2. **Giải quyết vấn đề gì?** (Text dài, bắt buộc)
3. **User/Đối tượng hướng tới** (Text, bắt buộc)

### Phần 2: Demo & Kỹ thuật
4. **Link video demo** (URL, bắt buộc)
5. **Input/Output hệ thống** (Text dài, bắt buộc)
6. **Link web demo** (URL, tùy chọn - nếu có)

### Phần 3: Agent & Tool Calling
7. **Số lượng Agent** (Text, bắt buộc)
8. **Danh sách Tools** (Text dài, bắt buộc)
9. **Tool usage examples** (Text dài, bắt buộc) - Agent dùng tool nào khi nào?

### Phần 4: LangGraph Workflow
10. **Số lượng Nodes** (Number, bắt buộc)
11. **Danh sách Nodes** (Text dài, bắt buộc) - theo thứ tự workflow
12. **Graph flow diagram** (File upload ảnh, bắt buộc) - Xuất ảnh graph từ LangGraph (dùng `graph.get_graph().draw_mermaid()` hoặc export)

### Phần 5: Tính năng đã implement
13. **Checklist tính năng** (Multiple choice checkbox, bắt buộc)

### Phần 6: Đánh giá khóa học
14. **Đánh giá giảng viên** (Rating 1-5 sao, bắt buộc)
15. **Đánh giá nội dung** (Rating 1-5 sao, bắt buộc)
16. **Đề xuất cải thiện** (Text dài, tùy chọn)

---


## Lưu ý khi chấm bài
- Agent: có reasoning, ≥3 tools, tự quyết định dùng tool
- LangGraph: ≥4 nodes, conditional routing, quản lý state
- Demo: có UI, không chỉ notebook
- Error handling: xử lý lỗi cơ bản

