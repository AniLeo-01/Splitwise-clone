from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.web.commons.enums import SplitTypeEnum

class CreateExpense(BaseModel):
    total_expense: Optional[float]
    description: Optional[str]
    split_type: Optional[SplitTypeEnum] = SplitTypeEnum.Equal
    group_id: Optional[int]
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True

class UpdateExpense(BaseModel):
    total_expense: Optional[float]
    description: Optional[str]
    split_type: Optional[SplitTypeEnum]
    group_id: Optional[int]
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True

class ExpenseSearchCriteria(BaseModel):
    id: Optional[int]
    description: Optional[str]
    split_type: Optional[SplitTypeEnum]
    group_id: Optional[int]

    class Config: