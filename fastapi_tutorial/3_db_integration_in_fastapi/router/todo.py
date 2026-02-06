from typing import Annotated
from fastapi import Depends, HTTPException, Path, Query, status, APIRouter
from sqlmodel import select
from models.Todo import Todo
from request_model.TodoRequest import TodoRequest
from response_model.TodoResponse import TodoResponse
from database.db import SessionDependency
from utility import validate_token

router = APIRouter(prefix="/todo", tags=["Todo"])


auth_user_dependency = Annotated[dict, Depends(validate_token)]


@router.post(
    "/create", response_model=TodoResponse, status_code=status.HTTP_201_CREATED
)
async def create_todo(
    todoReq: TodoRequest, user: auth_user_dependency,
    session: SessionDependency
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unable to authorized"
        )

    todo_data = todoReq.model_dump()
    todo_data["user_id"] = user.get("id")
    todo = Todo.model_validate(todo_data)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


@router.get("/all", response_model=list[TodoResponse],
            status_code=status.HTTP_200_OK)
async def get_all(user: auth_user_dependency, session: SessionDependency):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unable to authorized"
        )
    query = select(Todo).where(Todo.user_id == user.get("id"))
    result = session.exec(query).all()
    return result


@router.get(
    "/priority", response_model=list[TodoResponse],
    status_code=status.HTTP_200_OK
)
async def get_todo_by_priority(
    user: auth_user_dependency,
    session: SessionDependency,
    priority: int = Query(ge=1, le=5),
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unable to authorized"
        )
    userId = user.get("id")
    query = select(Todo).where(Todo.priority == priority,
                               Todo.user_id == userId)
    result = session.exec(query).all()
    return result


@router.get("/{id}", response_model=TodoResponse)
async def get_todo_by_id(user: auth_user_dependency,
                         session: SessionDependency,
                         id: int = Path(ge=1)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unable to authorized"
        )
    userId = user.get("id")
    todo = session.exec(select(Todo).where(Todo.id == id,
                                           Todo.user_id == userId)).first()
    if not todo:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Id not found")
    return todo


@router.put("/{id}", response_model=TodoResponse)
def update_todo(user: auth_user_dependency,
                todoRequest: TodoRequest,
                session: SessionDependency,
                id: int = Path(ge=1)
                ):

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unable to authorized"
        )
    userId = user.get("id")
    todo = session.exec(select(Todo).where(Todo.id == id,
                                           Todo.user_id == userId)).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id not found"
        )
    todo.title = todoRequest.title
    todo.description = todoRequest.description
    todo.priority = todoRequest.priority
    todo.is_completed = todoRequest.is_completed
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


@router.delete("/{id}")
def delete_todo_by_id(user: auth_user_dependency,
                      session: SessionDependency,
                      id: int = Path(ge=1)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unable to authorized"
        )
    userId = user.get("id")
    todo = session.exec(select(Todo).where(Todo.id == id,
                                           Todo.user_id == userId)).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id not Found"
        )
    session.delete(todo)
    session.commit()
    return "Record Deleted Successfully"
