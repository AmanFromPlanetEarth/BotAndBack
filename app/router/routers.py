from fastapi import APIRouter, HTTPException
from sqlalchemy import insert, select, update, delete
from schema.shema import TasksSchema, TasksUpdateSchema
from sqlalchemy.orm import Session
from database.database import engine
from models.models import ModelTasks


router = APIRouter(prefix="/tasks")


@router.post(path="/add_task/")
def create_task(task: TasksSchema):
    try:
        session = Session(engine)
        if_task = session.execute(select(ModelTasks).where(ModelTasks.title == task.title)).scalar_one_or_none()
        if if_task:
            raise HTTPException(status_code=400, detail="Такая задача уже есть")
        stmt = insert(ModelTasks).values(title = task.title,
                                        description = task.description,
                                        status = task.status,
                                        deadline = task.deadline)
        session.execute(stmt)
        session.commit()
        session.close()
        return task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(path="/get_task/")
def get_task(task_id: int | None = None):
    session = Session(engine)
    stmt = select(ModelTasks).where(ModelTasks.id == task_id)
    result = session.execute(stmt)
    task = result.scalars().one_or_none()
    session.close()
    return task

@router.put("/update_task/")
def update_task(new_task: TasksUpdateSchema, task_id: int | None = None):
    session = Session(engine)
    smtm = update(ModelTasks).where(ModelTasks.id == task_id).values(
                                        title = new_task.title,
                                        description = new_task.description,
                                        status = new_task.status,
                                        deadline = new_task.deadline
    )
    task = session.execute(smtm)
    session.commit()
    session.close()
    return task


@router.delete("/delete_task/")
def delete_task(task_id: int):
    session = Session(engine)
    smtm = delete(ModelTasks).where(ModelTasks.id == task_id)
    result = session.execute(smtm)
    session.commit()
    session.close()
    return result