from fastapi import FastAPI
from models.Todo import Todo
from database.db import create_table

app = FastAPI(
    title="Fast api Tutorial",
    version="0.0.1",
    description="Chapter 3: How to connect to database",
)


@app.on_event("startup")
def on_startup():
    create_table()
