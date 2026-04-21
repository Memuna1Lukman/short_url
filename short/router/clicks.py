from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils
from datetime import datetime


router = APIRouter(
    prefix= "/clicks",
    tags = ['Clicks']
)





@router.get("/url/{short_url}")
def stats_on_urls(short_url:str,db:Session=Depends(get_db)):
    count = db.query(models.Click).join(models.ShortUrl).filter(models.ShortUrl.short_url==short_url).count()
    url_exist = db.query(models.ShortUrl).filter(models.ShortUrl.short_url == short_url).first()
    if not url_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{short_url} is not found")
    
    return count


@router.get("/{short_url}")
def redirect_url(short_url:str,db:Session=Depends(get_db)):
    url_entry = db.query(models.ShortUrl).filter(models.ShortUrl.short_url == short_url).first()
    if not url_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{short_url} is not found")
    new_click = models.Click(access_count=url_entry.id)
    db.add(new_click)
    db.commit()
    return RedirectResponse(url=url_entry.long_url)