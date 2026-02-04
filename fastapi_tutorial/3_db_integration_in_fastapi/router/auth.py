from fastapi import APIRouter, HTTPException, status
from models.User import User
from response_model.UserResponse import UserResponse
from database.db import SessionDependency
from request_model.UserRequest import UserRequest
from sqlmodel import select
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Encrypt user password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


router = APIRouter(prefix="/auth")


@router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
async def create_user(userReq: UserRequest, session: SessionDependency):
    user = User.model_validate(userReq)

    existing_user = session.exec(
        select(User).where(User.email == userReq.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    user.password = hash_password(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
