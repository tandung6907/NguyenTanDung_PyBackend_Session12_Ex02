from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://Ntandung:123456@localhost:3306/shop_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# Dependency Injection để quản lý Session an toàn
# Mỗi request sẽ mở 1 Session riêng, dùng xong tự đóng lại
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
