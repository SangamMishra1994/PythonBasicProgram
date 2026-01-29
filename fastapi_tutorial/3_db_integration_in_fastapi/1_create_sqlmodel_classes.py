from datetime import datetime
from sqlmodel import SQLModel, Field


class Todo(SQLModel):
    id: int | None = Field(primary_key=True, default=None)
    title: str = Field(min_length=2, max_length=10, nullable=False)
    description: str = Field(min_length=5, max_length=50, nullable=True)
    priority: int = Field(le=5, ge=1, default=1)
    is_completed: bool = Field(default=False)
    created_ate: datetime = Field(default=datetime.now(), nullable=False)
