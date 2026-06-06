from core.database import SessionLocal
from user.model import User
from core.security import hash_password
from core.config import settings


def create_admin():

    db = SessionLocal()

    admin = db.query(User).filter( User.email == settings.ADMIN_EMAIL).first()

    if admin:
        db.close()
        return

    admin = User( username=settings.ADMIN_USERNAME, email=settings.ADMIN_EMAIL, password=hash_password(settings.ADMIN_PASSWORD), role="admin")

    db.add(admin)
    db.commit()

    db.close()

    print("Admin created")