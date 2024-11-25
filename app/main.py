from fastapi import FastAPI
from database.database import engine
from models.models import Model
from router.routers import router

app = FastAPI(title="ToDo")


app.include_router(router)


if __name__=="__main__":
    import uvicorn
    Model.metadata.create_all(engine)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)