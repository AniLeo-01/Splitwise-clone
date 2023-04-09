from typing import Optional
from app.web.user.dao.user_model import User
from sqlmodel import SQLModel, Field, Relationship

class Group(SQLModel, table=True):
    id: Optional[int]= Field(default=None, primary_key=True, index=True)
    name: Optional[str]
    type: Optional[str]

    __tablename__ = "Group"
    class Config:
        orm_mode=True

