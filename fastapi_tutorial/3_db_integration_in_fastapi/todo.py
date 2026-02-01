from fastapi import FastAPI, status
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
async def create_todo(
    todoReq: TodoRequest, session: SessionDependency
):
    todo = Todo.model_validate(todoReq)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo
