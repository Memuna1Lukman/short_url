from fastapi import FastAPI
import psycopg2
from sqlalchemy.orm import Session
from . import models



app = FastAPI()