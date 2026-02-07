from fastapi import FastAPI
from database.db import create_table
from router.auth import router as auth_router
from router.todo import router as todo_router
from router.user import router as user_router

# implement the CORS in the fastapi when we impleemnt the UI in our application
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Fast api Tutorial",
    version="0.0.1",
    description="Chapter 3: How to connect to database",
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
#     allow_credentials=True,
# )

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(todo_router)


@app.on_event("startup")
def on_startup():
    create_table()
