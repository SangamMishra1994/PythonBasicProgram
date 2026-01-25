from fastapi import FastAPI, Query, Path
from todo_model import Todo
from todo_request import TodoRequest

app = FastAPI(
    title="FastApi Tutorials",
    version="0.01",
    description="This is chapter 2 and project 1",
)

TODOS = [
    Todo(1, "Task 1", "My Task 1", False, 1),
    Todo(2, "Task 2", "My Task 2", False, 1),
    Todo(3, "Task 3", "My Task 3", False, 1),
    Todo(4, "Task 4", "My Task 4", False, 1),
]


@app.get("/todos/all")
async def get_all():
    return TODOS


@app.get("/todos/get_priority")
async def get_by_priority(priority: int = Query(ge=1, le=5)):
    result = []

    for todo in TODOS:
        if todo.priority == priority:
            result.append(todo)

    return result


@app.post("/todos/create")
async def create(todo: TodoRequest):
    # type casting dict() is depricated so we use model_dump()
    t = Todo(**todo.model_dump())
    TODOS.append(get_todo_id(t))
    return todo


@app.put("/todos/update")
async def update_todo(todo: TodoRequest):
    t = Todo(**todo.model_dump())
    for index in range(len(TODOS)):
        if TODOS[index].id == t.id:
            TODOS[index] = t
            return t


@app.delete("/todos/delete/{id}")
async def delete_todo(id: int = Path(ge=1)):
    for index in range(len(TODOS)):
        if TODOS[index].id == id:
            TODOS.pop(index)
            return {"Message": "Deleted Successfully"}


def get_todo_id(todo):
    if len(TODOS) == 0:
        todo.id = 1
    else:
        todo.id = TODOS[-1].id + 1
    return todo
