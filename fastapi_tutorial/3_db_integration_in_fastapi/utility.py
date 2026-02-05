from sqlmodel import select
from database.db import SessionDependency
from models.User import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Encrypt user password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def validate_password(hashed_password: str, password: str) -> bool:
    return pwd_context.verify(hash=hashed_password, secret=password)


async def check_user_credentials(email: str, password: str,
                                 session: SessionDependency):
    # Read and get userby email
    db_user = session.exec(select(User).where(User.email == email)).first()

    # If user is not present in DB return false
    if not db_user:
        return False

    # Validate user password with hashed password
    # If password is not valid, return false

    if not validate_password(db_user.password, password):
        return False

    # If email and password are valid then return User
    return db_user
