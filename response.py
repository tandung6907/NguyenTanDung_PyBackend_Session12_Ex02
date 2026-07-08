from datetime import datetime
from typing import Any, Optional


# Hàm dựng response theo cấu trúc thống nhất cho toàn bộ hệ thống
def build_response(
    status_code: int,
    message: str,
    data: Any = None,
    error: Optional[str] = None,
    path: str = ""
):
    return {
        "statusCode": status_code,
        "message": message,
        "error": error,
        "data": data,
        "path": path,
        "timestamp": datetime.now().isoformat()
    }
