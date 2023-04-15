from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from app.web.commons.enums import SplitTypeEnum

class ExpenseSplitTypeModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    split_type: Optional[SplitTypeEnum] = SplitTypeEnum.Equal
    expense_id: Optional[int] = Field(default=None, foreign_key = "expense.id")
    group_id: Optional[int] = Field(default=None, foreign_key = "GroupMembers.group_id")
    user_id: Optional[int] = Field(default=None, foreign_key = "GroupMembers.user_id")
    split_amount: Optional[float]
    remaining_amount: Optional[float]
    created_on: Optional[datetime] = datetime.utcnow()
    modified_on: Optional[datetime] = datetime.utcnow()

    class Config:
        orm_mode = True