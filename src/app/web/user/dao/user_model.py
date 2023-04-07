from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int]= Field(default=None, primary_key=True, index=True)
    name: Optional[str]
    email: Optional[str]
    mobile_number: str

    __tablename__ = "User"
    class Config:
        orm_mode=True