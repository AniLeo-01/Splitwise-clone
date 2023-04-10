from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
from app.web.commons.enums import GroupTypeEnum

class CreateGroup(BaseModel):
    id : Optional[int]
    name: Optional[str]
    type: Optional[GroupTypeEnum]
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True

class UpdateGroup(BaseModel):
    id : Optional[int]
    name: Optional[str]
    type: Optional[GroupTypeEnum]
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True

class GroupSearchCriteria(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True