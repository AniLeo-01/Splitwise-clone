from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..dao import user_model
from ..dto import user_request_model
from ..repositories import user_repository
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
    query = await get_user_search_criteria_query(search_criteria=search_criteria,
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
            detail="user id not provided"
        )
    if user_data:
        return user_data
    else:
        raise HTTPException(
            status_code=400,
            detail = "No user found!"
        )

async def create_user(
        request_model_data: user_request_model.CreateUser,
        session: Session
):
    if request_model_data is None:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid user data"
        )
    new_user = await user_repository.create_user(
        session=session, user_data=request_model_data
    )
    return new_user

async def update_user(
        id : int, user_model: user_request_model.UpdateUser,
        session: Session
):
    user_data = await user_repository.get_user_by_id(session = session, id = id)
    if user_data:
        user_data = user_model.dict(exclude_unset=True)
        for key, value in user_data.items():
            if value:
                if hasattr(user_data, str(key)):
                    setattr(user_data, key, value)
    else:
        raise HTTPException(
            status_code=400,
            detail = "No user with the id found"
        )
    user_data = await user_repository.update_user(session=session, user_data=user_data)
    return user_data

async def delete_user_by_id(
        id: int, 
        session: Session
):
    user_data = await user_repository.get_user_by_id(
        id = id, session=session
    )
    if user_data:
        user_data = await user_repository.delete_user(
            user_data=user_data, session=session
        )
    else:
        raise HTTPException(
            status_code = 400,
            detail = "No user data found by the provided id"
        )
    return user_data