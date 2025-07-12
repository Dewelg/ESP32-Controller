from fastapi import FastAPI
from api import routes
from models import Base
from database import engine

app = FastAPI()


Base.matadata.create_all(bind=engine)

app.inculde_router(routes.router)


