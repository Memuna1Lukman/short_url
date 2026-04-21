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