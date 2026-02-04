from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str = Field(unique=True)
    password: str = Field(max_length=250, nullable=False)
    name: str = Field(min_length=3, max_length=20, nullable=False)
