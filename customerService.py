from sqlalchemy.orm import Session

from models import CustomerModel
from schema import CustomerUpdate
from exceptions import AppException


# Cập nhật thông tin khách hàng theo customer_id
def update_customer(db: Session, customer_id: int, customer_update: CustomerUpdate):
    # Tìm khách hàng trong database theo id
    customer = db.query(CustomerModel).filter(
        CustomerModel.id == customer_id
    ).first()

    # Nếu không tìm thấy khách hàng, trả về lỗi 404 Not Found
    if customer is None:
        raise AppException(status_code=404, message="Không tìm thấy khách hàng")

    # Cập nhật dữ liệu mới vào bản ghi cũ
    customer.full_name = customer_update.full_name
    customer.phone = customer_update.phone
    customer.address = customer_update.address

    # Lưu thay đổi thật vào MySQL
    db.commit()

    # Lấy lại dữ liệu mới nhất từ database sau khi commit
    db.refresh(customer)

    return customer
