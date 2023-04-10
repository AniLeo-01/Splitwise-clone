from sqlalchemy.orm import Session
from sqlalchemy.future import select
from pydantic import BaseModel
from app.web.group.dao import group_model
from app.web.group.dto import group_request_model

async def get_group_by_search_criteria(
        session: Session, query_statement: BaseModel
):

    result = await session.execute(query_statement)
    commodity_data = result.scalars().all()
    return commodity_data

async def get_group_by_id(
        id: int, session: Session
):

    query_statement = select(group_model.Group).where(
        id == group_model.Group.id
    )
    execute_query = session.execute(query_statement)
    response = execute_query.scalars().first()
    return response

async def create_group(
        request_model_data: group_request_model.CreateGroup, session: Session
):
    new_group = group_model.Group.from_orm(request_model_data)
    session.add(new_group)
    await session.commit()
    await session.refresh(new_group)
    return new_group

async def update_group(
        session: Session, group_data: group_request_model.UpdateGroup
):
    session.add(group_data)
    await session.commit()
    await session.refresh(group_data)
    return group_data

async def delete_group(
        session: Session, group_data: group_model.Group
):
    await session.delete(group_data)
    await session.commit()
    return group_data