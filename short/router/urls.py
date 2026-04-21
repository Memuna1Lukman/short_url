from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils

router = APIRouter(
    prefix="shorturl",
    tags=['URL']
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.GetUrl)
def create_short_url(url:schemas.UrlCreate,db:Session=Depends(get_db)):
    
    short_url=utils.encode_url(url.id)
    create_shorts = url.dict()
    create_shorts['short_url'] = short_url
    create_shorts = models.ShortUrl(id = url.id,short_url = url.short_url,long_url=url.long_url)
    db.add(create_shorts)
    db.commit()
    db.refresh(create_shorts)
    return create_shorts

