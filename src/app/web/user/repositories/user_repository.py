from sqlalchemy.orm import Session
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import Optional
from app.web.user.dao import user_model
from app.web.user.dto import user_request_model

async def get_user_by_search_criteria(
        session: Session, query_statement: BaseModel
):

    result = await session.execute(query_statement)
    commodity_data = result.scalars().all()
    return commodity_data

async def get_user_by_id(
        id: int, session: Session
):

    query_statement = select(user_model.User).where(
        id == user_model.User.id
    )
    execute_query = session.execute(query_statement)
    response = execute_query.scalars().all()
    return response

async def create_user(
        session: Session, user_data = user_request_model.CreateUser
):
    new_user = user_model.User.from_orm(user_data)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def update_user(
        session: Session, user_data = user_model.User
):
    session.add(user_data)
    await session.commit()
    await session.refresh(user_data)
    return user_data

async def delete_user(
        session: Session, id: int
):
    user_data = await get_user_by_id(session=session, id=id)
    await session.delete(user_data)
    await session.commit()
    return user_data
