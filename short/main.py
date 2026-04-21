from fastapi import FastAPI
import psycopg2
from sqlalchemy.orm import Session
from . import models
from .router import urls


app = FastAPI()



app.include_router(urls.router)