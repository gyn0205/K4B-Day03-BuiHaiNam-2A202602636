# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên: Bùi Hải Nam** 
> **Mã Sinh Viên / Mã Học viên: 2A202602636**  
> **Chủ đề Lựa chọn: Trợ lý Dịch vụ Khách hàng VinBus**

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | **4 / 5** | Agent cần phân tích nhu cầu của khách hàng, xác định điểm đi và điểm đến, tra cứu tuyến xe phù hợp, kiểm tra thời gian hoạt động hoặc giá vé, sau đó mới thực hiện đăng ký vé tháng nếu khách hàng yêu cầu. |
| **2. Tool Interaction** | **4 / 5** | Hệ thống cần kết nối với các Tool thông qua MCP Server để tra cứu lộ trình, thời gian chạy, giá vé và thực hiện đăng ký vé tháng. Đây là dữ liệu động, không nên chỉ trả lời từ System Prompt. |
| **3. Dynamic Decision** | **5 / 5** | Quyết định tiếp theo phụ thuộc vào kết quả tra cứu trước đó. Nếu có tuyến phù hợp, Agent có thể tiếp tục tư vấn hoặc đăng ký vé; nếu không có tuyến, Agent phải đề xuất phương án khác và không thực hiện đăng ký. |
| **4. Long Horizon Goal** | **3 / 5** | Agent cần duy trì mục tiêu phục vụ khách hàng qua nhiều bước hoặc nhiều lượt hội thoại, từ xác định nhu cầu, tìm tuyến phù hợp, xác nhận thông tin đến hoàn tất đăng ký vé tháng. |
| **TỔNG ĐIỂM AGENTIC FIT** | **16 / 20** | Bài toán có điểm Agentic Fit cao vì kết hợp suy luận nhiều bước, sử dụng Tool, ra quyết định dựa trên dữ liệu quan sát và hoàn thành mục tiêu dịch vụ khách hàng. |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[ {
    "step": 1,
    "query": "toi muon di chuyen tu thanh pho phu ly den san bay tan son nhat",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "route_lookup",
    "arguments": {
      "origin": "Thành phố Phủ Lý",
      "destination": "Sân bay Tân Sơn Nhất"
    },
    "observation": {
      "status": "NO_ROUTE",
      "message": "Không tìm thấy tuyến VinBus phù hợp từ 'Thành phố Phủ Lý' đến 'Sân bay Tân Sơn Nhất'."
    },
    "latency_ms": 2589.02
  },
  {
    "step": 2,
    "query": "toi muon di chuyen tu thanh pho phu ly den san bay tan son nhat",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Dạ, hiện tại mạng lưới xe bus điện VinBus chưa có tuyến xe hỗ trợ di chuyển trực tiếp từ **Thành phố Phủ Lý (Hà Nam)** đến **Sân bay Tân Sơn Nhất (TP. Hồ Chí Minh)**.\n\nVì Thành phố Phủ Lý thuộc miền Bắc và Sân bay Tân Sơn Nhất thuộc miền Nam, quý khách vui lòng tham khảo các phương tiện di chuyển đường dài như:\n1. **Máy bay:** Di chuyển từ Phủ Lý lên Sân bay Quốc tế Nội Bài (Hà Nội), sau đó bay vào Sân bay Tân Sơn Nhất (TP.HCM).\n2. **Tàu hỏa:** Đón tàu Bắc - Nam từ ga Phủ Lý vào ga Sài Gòn, sau đó di chuyển bằng taxi/xe bus đến sân bay Tân Sơn Nhất.\n3. **Xe khách / Xe limousine:** Đi xe khách đường dài hoặc xe limousine từ Phủ Lý vào TP.HCM.\n\nNếu quý khách cần tra cứu các tuyến xe VinBus tại khu vực Hà Nội, TP. Hồ Chí Minh hoặc Phú Quốc, em rất sẵn lòng hỗ trợ ạ!",
    "latency_ms": 4129.53
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 5 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
