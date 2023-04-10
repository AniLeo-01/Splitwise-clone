from fastapi import APIRouter, Depends
from sqlalchemy import Session
from app.db import get_session


from app.web.group.dto import group_request_model
from app.web.group.services import group_services

router = APIRouter()

@router.get("/{id}", status_code=200)
async def get_group_by_id(id: int, session: Session = Depends(get_session)):
    group_data = await group_services.get_group_by_id(id = id, session=session)
    return group_data

@router.get("", status_code=200)
async def get_group_by_search_criteria(search_criteria: group_request_model.GroupSearchCriteria = Depends(), session: Session = Depends(get_session)):
    group_data = await group_services.get_group_by_search_criteria(search_criteria = search_criteria, session = session)
    return group_data

@router.post("", status_code=200)
async def create(group: group_request_model.CreateGroup,
                 session: Session = Depends(get_session)):
    group_data = await group_services.create_group(
        request_model_data = group, session=session
    )
    return group_data

@router.patch("/{id}", status_code=200)
async def update(id: int, group_model: group_request_model.UpdateGroup,
                 session: Session = Depends(get_session)):
    group_data = await group_services.update_group(
        id = id, group_model= group_model, session=session
    )
    return group_data

@router.delete("/{id}", status_code=200)
async def delete(id: id, session: Session = Depends(get_session)):
    group_data = await group_services.delete_group_by_id(
        id = id, session = session
    )
    return group_data

