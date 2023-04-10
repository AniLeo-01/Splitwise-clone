from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateGroupMembers(BaseModel):
    id: Optional[int]
    group_id: int
    user_id: int
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True

class UpdateGroupMembers(BaseModel):
    id: Optional[int]
    group_id: int
    user_id: int
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True

