from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

class Model(DeclarativeBase):
    pass

class ModelTasks(Model):
    __tablename__="tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    status: Mapped[bool] = mapped_column(Boolean)
    deadline: Mapped[bool] = mapped_column(Boolean)
