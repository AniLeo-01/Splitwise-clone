from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from app.web.commons.enums import SplitTypeEnum

class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total_expense: Optional[float]
    description: Optional[str]
    split_type: Optional[SplitTypeEnum]
    group_id: Optional[int] = Field(default=None, foreign_key="group.id")
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True