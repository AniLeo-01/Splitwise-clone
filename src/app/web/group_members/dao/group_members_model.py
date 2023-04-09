from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from app.web.user.dao.user_model import User
from app.web.group.dao.group_model import Group

class GroupMembers(SQLModel, table=True):
    id: Optional[int]= Field(default=None, primary_key=True, index=True)
    group_id: Optional[int]= Field(default=None, foreign_key="Group.id")
    user_id: Optional[int]= Field(default=None, foreign_key="User.id")

    groups: Optional["Group"] = Relationship(
        back_populates="GroupMembers"
    )
    users: Optional["User"] = Relationship(
        back_populates="GroupMembers"
    )

    __tablename__ = "GroupMembers"
    class Config:
        orm_mode=True