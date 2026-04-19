from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils

router = APIRouter(
    prefix="shorturl",
    tags=['URL']
)


