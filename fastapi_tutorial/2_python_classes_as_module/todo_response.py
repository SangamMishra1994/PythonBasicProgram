from pydantic import BaseModel


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    priority: int
