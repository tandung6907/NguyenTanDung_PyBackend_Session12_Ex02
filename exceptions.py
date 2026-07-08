import http.client

from fastapi import Request
from fastapi.responses import JSONResponse

from response import build_response


# Exception dùng chung cho toàn hệ thống
# Nếu không truyền message, tự động lấy reason phrase chuẩn từ http.client.responses
class AppException(Exception):
    def __init__(self, status_code: int, message: str = None):
        self.status_code = status_code
        self.message = message or http.client.responses.get(status_code, "Lỗi không xác định")


# Handler bắt AppException và trả về response theo cấu trúc thống nhất
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=build_response(
            status_code=exc.status_code,
            message=exc.message,
            error=http.client.responses.get(exc.status_code, "Error"),
            data=None,
            path=str(request.url.path)
        )
    )
