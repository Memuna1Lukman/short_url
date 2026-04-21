from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils
from datetime import datetime
router = APIRouter(
    prefix="/shorturl",
    tags=['URL']
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.GetUrl)
def create_short_url(url:schemas.UrlCreate,db:Session=Depends(get_db)):


    create_shorts = models.ShortUrl(long_url=url.long_url,short_url="temp")
    db.add(create_shorts)
    # flush() a new method i learnt on postgres sqlalchemy
    db.flush()
    create_shorts.short_url= utils.encode_url(create_shorts.id)
    db.commit()
    db.refresh(create_shorts)
    return create_shorts

@router.get("/{short_url}",response_model=schemas.GetUrl)
def get_user_url(short_url:str,db:Session=Depends(get_db)):
    get_long_url = db.query(models.ShortUrl).filter(models.ShortUrl.short_url == short_url).first()
    if not get_long_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{short_url} is not found")
    return get_long_url


@router.put("/{short_url}",response_model=schemas.GetUrl)
def update_url(short_url:str,url:schemas.UrlCreate,db:Session=Depends(get_db)):
    
    update_long_url = db.query(models.ShortUrl).filter(
        models.ShortUrl.short_url == short_url
        )
    updated = update_long_url.first()
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{short_url} is not found")
    updated_data = url.dict(exclude_unset=True)
    updated_data['updated_at'] = datetime.utcnow()
    update_long_url.update(updated_data,synchronize_session=False)
    db.commit()
    
    return updated


@router.delete("/{short_url}")
def delete_url(short_url:str,db:Session=Depends(get_db)):
    delete_long_url = db.query(models.ShortUrl).filter(
        models.ShortUrl.short_url == short_url
        )
    deleted = delete_long_url.first()
    if deleted == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{short_url} is not found")
    db.delete(deleted)
    db.commit()
    return deleted



