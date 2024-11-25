from pydantic import BaseModel

class TasksSchema(BaseModel):
    title: str
    description: str
    status: bool | None = None
    deadline: bool | None = None

class TasksUpdateSchema(BaseModel):
    title: str
    description: str
    status: bool | None = None
    deadline: bool | None = None