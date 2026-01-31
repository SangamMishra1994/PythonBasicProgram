from dotenv import load_dotenv
import os
from sqlmodel import create_engine, SQLModel

load_dotenv()

USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")

DB_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/" \
         f"fastapi_tutorial"

engine = create_engine(DB_URL, echo=True)


def create_table():
    SQLModel.metadata.create_all(engine)
