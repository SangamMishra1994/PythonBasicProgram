from datetime import datetime
from sqlmodel import Field
from models.TodoBase import TodoBase


class Todo(TodoBase, table=True):
    id: int | None = Field(primary_key=True, default=None)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    user_id: int | None = Field(foreign_key="user.id")
