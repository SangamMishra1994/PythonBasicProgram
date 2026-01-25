from fastapi import FastAPI
from todo_model import Todo
from todo_request import TodoRequest

app = FastAPI()

TODOS = [
    Todo(1, "Task 1", "My Task 1", False, 1),
    Todo(2, "Task 2", "My Task 2", False, 1),
    Todo(3, "Task 3", "My Task 3", False, 1),
    Todo(4, "Task 4", "My Task 4", False, 1),
]


@app.get("/todos/all")
async def get_all():
    return TODOS


@app.post("/todos/create")
async def create(todo: TodoRequest):
    t = Todo(**todo.model_dump())
    TODOS.append(get_todo_id(t))
    return todo


def get_todo_id(todo):
    if len(TODOS) == 0:
        todo.id = 1
    else:
        todo.id = TODOS[-1].id + 1
    return todo
