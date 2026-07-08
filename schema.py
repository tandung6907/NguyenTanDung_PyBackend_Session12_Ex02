from pydantic import BaseModel


# Schema dữ liệu client gửi lên để cập nhật thông tin khách hàng
class CustomerUpdate(BaseModel):
    full_name: str
    phone: str
    address: str


# Schema dữ liệu trả về cho client sau khi cập nhật thành công
class CustomerResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    address: str

    class Config:
        from_attributes = True
