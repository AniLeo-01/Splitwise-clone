from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..dao import group_model
from ..dto import group_request_model
from ..repositories import group_repository
from ..dao import group_model
from sqlalchemy.future import select

async def get_group_search_criteria_query(search_criteria: group_request_model.GroupSearchCriteria,
                                        session: Session):
        query_statement = select(group_model.Group)
        if search_criteria.id:
            query_statement = query_statement.where(
                group_model.Group.id == search_criteria.id
            )
        if search_criteria.name:
            query_statement = query_statement.where(
                group_model.Group.name.ilike("%{}%".format(search_criteria.name))
            )
    
        return query_statement

async def get_group_by_id(id: int, 
                        session: Session):
    if id:
        group_data = await group_repository.get_group_by_id(id = id, session = session)
    else:
        raise HTTPException(
            status_code=400,
            detail="id not provided"
            )
    return group_data

async def get_group_by_search_criteria(search_criteria: group_request_model.GroupSearchCriteria, session: Session):
    if search_criteria is None:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid search criteria"
        )
    query_statement = await get_group_search_criteria_query(search_criteria = search_criteria, session = session)
    group_data = await group_repository.get_group_by_search_criteria(query_statement = query_statement, session = session)
    if group_data:
        return group_data
    else:
        raise HTTPException(
            status_code=400,
            detail = "No group found!"
        )

async def create_group(request_model_data: group_request_model.CreateGroup, session: Session):
    group_data = await group_repository.create_group(request_model_data = request_model_data, session = session)
    return group_data

async def update_group(id: int, group_model: group_request_model.UpdateGroup, session: Session):
    group_data = await group_repository.get_group_by_id(
        id = id, session = session
    )
    if group_data:
        group_data = group_model.dict(exclude_unset=True)
        for key, value in group_data.items():
            if value:
                if hasattr(group_data, str(key)):
                    setattr(group_data, key, value)
    else:
        raise HTTPException(
            status_code=400,
            detail = "No group with the id found"
        )
    group_data = await group_repository.update_group(group_data = group_data, session = session)
    return group_data

async def delete_group_by_id(id: int, session: Session):
    group_data = await group_repository.get_group_by_id(id = id, session = session)
    if group_data:
        group_data = await group_repository.delete_group(
            session = session, group_data = group_data)
    else:
        raise HTTPException(status_code=400, 
                            detail="Group not found")
    return group_data