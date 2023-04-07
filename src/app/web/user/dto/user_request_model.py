from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class CreateUser(BaseModel):
    id : Optional[int]
    name: Optional[str]
    email: Optional[str]
    mobile_number: str
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    id: Optional[int]
    name: Optional[str]
    email: Optional[str]
    mobile_number: Optional[str]
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True

class UserSearchCriteria(BaseModel):
    pass