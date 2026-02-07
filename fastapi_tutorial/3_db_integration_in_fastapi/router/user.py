from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from request_model.ChangePasswordRequest import ChangePasswordRequest
from database.db import SessionDependency
from utility import hash_password, validate_password, validate_token
from models.User import User

router = APIRouter(prefix="/User", tags=["User"])

auth_user_dependency = Annotated[dict, Depends(validate_token)]


@router.put("/change_password")
async def change_password(
    user_password: ChangePasswordRequest,
    user: auth_user_dependency,
    session: SessionDependency,
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unable to authorized"
        )

    # Read user by user_id
    db_user = session.get(User, user.get("id"))

    # check if db password == user_password.current_password
    db_password = db_user.password
    isSame = validate_password(
        hashed_password=db_password, password=user_password.current_password
    )

    # If False, return 404
    if not isSame:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Your password is Incorrect",
        )

    # If True, update new password
    db_user.password = hash_password(user_password.new_password)
    session.add(db_user)
    session.commit()
    return {"message": "Password changed Successfully"}
