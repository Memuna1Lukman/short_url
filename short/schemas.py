from pydantic import BaseModel,HttpUrl
from typing import Optional
from datetime import datetime


class UrlCreate(BaseModel):
    id: Optional[int] = None
    long_url: str
    short_url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class GetUrl(BaseModel):
    id: Optional[int] = None
    long_url: str
    short_url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class CountClicks(BaseModel):
    id:  Optional[int] = None
    access_count : Optional[int] = None
    created_at : Optional[datetime] = None
    clicked_at:  Optional[datetime] = None


class Count(BaseModel):
    id:  Optional[int] = None
    access_count : Optional[int] = None
    created_at : Optional[datetime] = None
    clicked_at:  Optional[datetime] = None
    model_config = {"from_attributes": True}