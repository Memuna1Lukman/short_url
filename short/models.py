from sqlalchemy import Column,Integer,String,TIMESTAMP,text,ForeignKey
from sqlalchemy.orm import relationship
from . database import Base


class ShortUrl(Base):
    __tablename__ = "urls"
    id = Column(Integer,primary_key=True)
    long_url = Column(String,index=True,nullable=False)
    short_url = Column(String,index=True,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    click = relationship("Click",back_populates="owner")
class Click(Base):
    __tablename__ = "clicks"
    id = Column(Integer,primary_key=True)
    access_count = Column(Integer,ForeignKey("urls.id",ondelete='CASCADE'),nullable=False)
    created_at =   Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')) 
    clicked_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner = relationship("ShortUrl",back_populates="click")