import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user.model import User
from core.security import hash_password
from main import app
from core.database import Base
from core.dependencies import get_db
from core.config import settings
# =========================
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)

# =========================
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():

    # clean before
    if os.path.exists("test.db"):
        os.remove("test.db")

    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
       # create admin
    db = TestingSessionLocal()
    admin = db.query(User).filter(User.email == "admin@example.com" ).first()
    if not admin:
        admin = User(username=settings.TEST_ADMIN_USERNAME,email=settings.TEST_ADMIN_EMAIL,password=hash_password(settings.TEST_ADMIN_PASSWORD),role="admin")
        db.add(admin)
        db.commit()
        db.close()



    yield
    engine.dispose()
    if os.path.exists("test.db"):
        os.remove("test.db")

# =========================
@pytest.fixture
def client():
    return TestClient(app)









# test_register_duplicate_email
# test_register_duplicate_username

# test_login_wrong_password
# test_login_user_not_found

# test_get_me_without_token

# test_get_users_non_admin

# test_delete_user_non_admin

# test_refresh_invalid_token