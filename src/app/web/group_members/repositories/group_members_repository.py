from sqlalchemy.orm import Session
from sqlalchemy.future import select
from pydantic import BaseModel
from app.web.group_members.dao import group_members_model
from app.web.group_members.dto import group_members_request_model

async def get_all_group_members(
        session: Session
):
    query_statement = select(group_members_model.GroupMembers)
    result = await session.execute(query_statement)
    group_members_data = result.scalars().all()
    return group_members_data

async def get_group_members_by_id(
        id: int, session: Session
):

    query_statement = select(group_members_model.GroupMembers).where(
        id == group_members_model.GroupMembers.id
    )
    execute_query = session.execute(query_statement)
    response = execute_query.scalars().first()
    return response

async def create_group_members(
        session: Session, group_members_data: group_members_request_model.CreateGroupMembers
):
    new_group_member = group_members_model.GroupMembers.from_orm(group_members_data)
    session.add(new_group_member)
    await session.commit()
    await session.refresh(new_group_member)
    return new_group_member

async def update_group_members(
        session: Session, group_members_data: group_members_request_model.UpdateGroupMembers
):
    session.add(group_members_data)
    await session.commit()
    await session.refresh(group_members_data)
    return group_members_data

async def delete_group_members(
        session: Session, group_members_data: group_members_model.GroupMembers
):
    
    await session.delete(group_members_data)
    await session.commit()
    return group_members_data