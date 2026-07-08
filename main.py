from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session

from database import get_db
from schema import CustomerUpdate
from response import build_response
from exceptions import AppException, app_exception_handler
import customerService

app = FastAPI()

# Đăng ký handler xử lý AppException
app.add_exception_handler(AppException, app_exception_handler)


# API cập nhật thông tin khách hàng
@app.put("/customers/{customer_id}")
def update_customer_api(
    customer_id: int,
    customer_update: CustomerUpdate,
    request: Request,
    db: Session = Depends(get_db)
):
    # Gọi service xử lý logic cập nhật, service tự raise lỗi nếu không tìm thấy
    customer = customerService.update_customer(db, customer_id, customer_update)

    # Trả về thông tin khách hàng sau khi cập nhật thành công
    return build_response(
        status_code=200,
        message="Cập nhật khách hàng thành công",
        data={
            "id": customer.id,
            "full_name": customer.full_name,
            "phone": customer.phone,
            "address": customer.address
        },
        error=None,
        path=str(request.url.path)
    )
