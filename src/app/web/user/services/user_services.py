from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..dao import user_model
from ..dto import user_request_model
from ..repositories import user_repository
from ..dao import user_model
from sqlalchemy.future import select


async def get_user_search_criteria_query(search_criteria: user_request_model.UserSearchCriteria,
                                      session: Session):
    query_statement = select(user_model.User)
    if search_criteria.id:
        query_statement = query_statement.where(
            user_model.User.id == search_criteria.id
        )
    if search_criteria.name:
        query_statement = query_statement.where(
            user_model.User.name.ilike("%{}%".format(search_criteria.name))
        )
    if search_criteria.email:
        query_statement = query_statement.where(
            user_model.User.email.ilike("%{}%".format(search_criteria.email))
        )
    if search_criteria.mobile_number:
        query_statement = query_statement.where(
            user_model.User.mobile_number.ilike("%{}%".format(search_criteria.mobile_number))
        )

    return query_statement

async def get_user_by_search_criteria(
        search_criteria: user_request_model.UserSearchCriteria,
        session: Session
):
    if search_criteria is None:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid search criteria"
        )
    query = get_user_search_criteria_query(search_criteria=search_criteria,
                                           session=session)
    user_data = await user_repository.get_user_by_search_criteria(
        query_statement=query, session=session
    )
    
    if user_data:
        return user_data
    else:
        raise HTTPException(
            status_code=400,
            detail = "No user found!"
        )
    
async def get_user_by_id(
        id: int,
        session: Session
):
    if id:
        user_data = await user_repository.get_user_by_id(id=id, session=session)
    else:
        raise HTTPException(
            status_code=400,
            detail="id not provided"
        )
    return user_data

async def create_user(
        request_model_data: user_request_model.CreateUser,
        session: Session
):
    new_user = await user_repository.create_user(
        session=session, user_data=request_model_data
    )
    return new_user

        