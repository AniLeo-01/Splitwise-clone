from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.web.commons.enums import SplitTypeEnum
from sqlalchemy import Column, DateTime

class CreateExpenseSplitType(BaseModel):
    id: Optional[int]
    split_type: Optional[SplitTypeEnum] = SplitTypeEnum.Equal
    expense_id: Optional[int]
    user_id: int
    split_amount: Optional[float]
    remaining_amount: Optional[float]
    created_on: Optional[datetime] = datetime.now()
    modified_on: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True
    
class UpdateExpenseSplitType(BaseModel):
    id: Optional[int]
    split_type: Optional[SplitTypeEnum]
    expense_id: Optional[int]
    user_id: Optional[int]
    split_amount: Optional[float]
    remaining_amount: Optional[float]
    modified_on: Optional[datetime] = Field(
        sa_column = Column(
        "modified_on",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        )
    )

    class Config:
        orm_mode = True


class ExpenseSplitTypeSearchCriteria(BaseModel):
    id: Optional[int]           
    split_type: Optional[SplitTypeEnum]
    expense_id: Optional[int]
    user_id: Optional[int]

    class Config:
        orm_mode = True



