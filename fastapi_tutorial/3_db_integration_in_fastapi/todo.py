from fastapi import FastAPI, HTTPException, Path, Query, status
from sqlmodel import select
from models.Todo import Todo
from request_model.TodoRequest import TodoRequest
from response_model.TodoResponse import TodoResponse
from database.db import SessionDependency, create_table


app = FastAPI(
    title="Fast api Tutorial",
    version="0.0.1",
    description="Chapter 3: How to connect to database",
)


@app.on_event("startup")
def on_startup():
    create_table()


@app.get("/")
async def hello():
    return "hello"


@app.post(
    "/todo/create", response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_todo(todoReq: TodoRequest, session: SessionDependency):
    todo = Todo.model_validate(todoReq)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


@app.get("/todo/all", response_model=list[TodoResponse],
         status_code=status.HTTP_200_OK
         )
async def get_all(session: SessionDependency):
    query = select(Todo)
    result = session.exec(query).all()
    return result


@app.get("/todo/priority", response_model=list[TodoResponse],
         status_code=status.HTTP_200_OK)
async def get_todo_by_priority(session: SessionDependency,
                               priority: int = Query(ge=1, le=5)
                               ):
    query = select(Todo).where(Todo.priority == priority)
    result = session.exec(query).all()
    return result


@app.get("/todo/{id}", response_model=TodoResponse)
async def get_todo_by_id(session: SessionDependency, id: int = Path(ge=1)):
    todo = session.get(Todo, id)
    if not todo:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Id not found")
    return todo



