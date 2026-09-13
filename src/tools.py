"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
Chủ đề: Trợ lý Dịch vụ Khách hàng VinBus (Tra cứu lộ trình tuyến xe bus điện & Đăng ký vé tháng).
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1 (Tương đương công cụ mẫu "tra cứu"): Tra cứu lộ trình tuyến xe bus điện VinBus
    {
        "name": "route_lookup",
        "description": "Tra cứu tuyến xe bus điện VinBus phù hợp giữa điểm đi và điểm đến, kèm giờ hoạt động và giá vé.",
        "parameters": {
            "type": "object",
            "properties": {
                "origin": {
                    "type": "string",
                    "description": "Điểm đón/xuất phát của khách hàng (ví dụ: 'Vinhomes Central Park')"
                },
                "destination": {
                    "type": "string",
                    "description": "Điểm đến của khách hàng (ví dụ: 'Bến xe Miền Đông mới')"
                },
                "departure_time": {
                    "type": "string",
                    "description": "Thời gian dự kiến khởi hành (ví dụ: '07:30 15/09/2026'), có thể bỏ trống nếu khách chưa nêu rõ"
                }
            },
            "required": ["origin", "destination"]
        }
    },

    # --------------------------------------------------------------------------
    # TODO 1.2 (ĐÃ HOÀN THIỆN): TOOL SCHEMA CHO CHỦ ĐỀ VINBUS - 'monthly_pass_registration'
    # 🎯 YÊU CẦU THIẾT KẾ SCHEMA (JSON SCHEMA STANDARD):
    # 1. Tool dùng để đăng ký vé tháng cho một tuyến xe bus điện VinBus cụ thể.
    # 2. Thiết kế các tham số (properties) để LLM trích xuất:
    #    - route_code (string): Mã tuyến xe cần đăng ký (ví dụ: 'E01')
    #    - start_date (string): Ngày bắt đầu sử dụng vé tháng (ví dụ: '20/09/2026')
    #    - passenger_name (string): Tên hành khách đăng ký (không bắt buộc)
    # 3. Khai báo danh sách các trường bắt buộc (required).
    # --------------------------------------------------------------------------
    {
        "name": "monthly_pass_registration",
        "description": "Đăng ký vé tháng VinBus cho một tuyến xe bus điện cụ thể.",
        "parameters": {
            "type": "object",
            "properties": {
                "route_code": {
                    "type": "string",
                    "description": "Mã tuyến xe VinBus cần đăng ký vé tháng (ví dụ: 'E01')"
                },
                "start_date": {
                    "type": "string",
                    "description": "Ngày bắt đầu sử dụng vé tháng (ví dụ: '20/09/2026')"
                },
                "passenger_name": {
                    "type": "string",
                    "description": "Tên hành khách đăng ký vé tháng (không bắt buộc)"
                }
            },
            "required": ["route_code", "start_date"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_VINBUS_ROUTES = {
    "E01": {
        "origin": "Vinhomes Central Park",
        "destination": "Bến xe Miền Đông mới",
        "operating_hours": "05:30 - 22:00",
        "frequency_minutes": 15,
        "ticket_price": 7000,
        "monthly_pass_price": 300000
    },
    "E02": {
        "origin": "Sân bay Tân Sơn Nhất",
        "destination": "Vinhomes Grand Park",
        "operating_hours": "06:00 - 21:30",
        "frequency_minutes": 20,
        "ticket_price": 8000,
        "monthly_pass_price": 320000
    },
    "E03": {
        "origin": "Vinhomes Grand Park",
        "destination": "Bến xe Miền Đông mới",
        "operating_hours": "05:00 - 23:00",
        "frequency_minutes": 10,
        "ticket_price": 6000,
        "monthly_pass_price": 280000
    }
}


def execute_route_lookup(origin: str, destination: str, departure_time: str = "") -> str:
    """Thực thi tra cứu tuyến xe bus điện VinBus theo điểm đi - điểm đến"""
    o_key = origin.strip().lower()
    d_key = destination.strip().lower()

    for route_code, route in MOCK_VINBUS_ROUTES.items():
        if route["origin"].strip().lower() == o_key and route["destination"].strip().lower() == d_key:
            return json.dumps({
                "status": "SUCCESS",
                "data": {"route_code": route_code, **route},
                "message": (
                    f"Tuyến {route_code} phù hợp: {route['origin']} → {route['destination']}. "
                    f"Hoạt động {route['operating_hours']} (mỗi {route['frequency_minutes']} phút/chuyến). "
                    f"Giá vé lượt: {route['ticket_price']}đ, giá vé tháng: {route['monthly_pass_price']}đ."
                )
            }, ensure_ascii=False)

    return json.dumps({
        "status": "NO_ROUTE",
        "message": f"Không tìm thấy tuyến VinBus phù hợp từ '{origin}' đến '{destination}'."
    }, ensure_ascii=False)


def execute_monthly_pass_registration(route_code: str, start_date: str, passenger_name: str = "Khách hàng VinBus") -> str:
    """Thực thi đăng ký vé tháng VinBus cho một tuyến xe cụ thể"""
    code = route_code.strip().upper()
    route = MOCK_VINBUS_ROUTES.get(code)

    if not route:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy tuyến VinBus có mã '{route_code}' để đăng ký vé tháng."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"VB-{code}-{start_date.replace('/', '').replace(' ', '')}",
        "data": {
            "route_code": code,
            "start_date": start_date,
            "passenger_name": passenger_name,
            "monthly_pass_price": route["monthly_pass_price"]
        },
        "message": (
            f"Đăng ký vé tháng thành công cho tuyến {code} ({route['origin']} → {route['destination']}) "
            f"bắt đầu từ ngày {start_date}, giá {route['monthly_pass_price']}đ/tháng."
        )
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "route_lookup": execute_route_lookup,
    "monthly_pass_registration": execute_monthly_pass_registration
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
