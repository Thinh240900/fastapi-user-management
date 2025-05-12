from fastapi import FastAPI
from app import auth, crud, models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(crud.router)
