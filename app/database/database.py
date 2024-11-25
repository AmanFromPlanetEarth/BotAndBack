from sqlalchemy import create_engine

DB_URL = "sqlite:///tasks.db"

engine = create_engine(DB_URL, echo=True)