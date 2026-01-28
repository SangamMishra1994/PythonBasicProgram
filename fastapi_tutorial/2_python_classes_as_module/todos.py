from fastapi import FastAPI, Query, Path, HTTPException, status
from todo_model import Todo
from todo_request import TodoRequest
from todo_response import TodoResponse

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


@app.get(
    "/todos/all", response_model=list[TodoResponse],
    status_code=status.HTTP_200_OK
)
async def get_all():
    return TODOS


@app.get(
    "/todos/get_priority",
    response_model=list[TodoResponse],
    status_code=status.HTTP_200_OK,
)
async def get_by_priority(priority: int = Query(ge=1, le=5)):
    result = []

    for todo in TODOS:
        if todo.priority == priority:
            result.append(todo)

    return result


@app.post(
    "/todos/create", response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
async def create(todo: TodoRequest):
    # type casting dict() is depricated so we use model_dump()
    t = Todo(**todo.model_dump())
    TODOS.append(get_todo_id(t))
    return todo


@app.put(
    "/todos/update", response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
async def update_todo(todo: TodoRequest):
    not_found = True
    t = Todo(**todo.model_dump())
    for index in range(len(TODOS)):
        if TODOS[index].id == t.id:
            TODOS[index] = t
            return t

    if not_found is True:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id is not found"
        )


@app.delete("/todos/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(id: int = Path(ge=1)):
    not_found = True
    for index in range(len(TODOS)):
        if TODOS[index].id == id:
            TODOS.pop(index)
            return {"Message": "Deleted Successfully"}

    if not_found is True:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id is not found"
        )


def get_todo_id(todo):
    if len(TODOS) == 0:
        todo.id = 1
    else:
        todo.id = TODOS[-1].id + 1
    return todo
