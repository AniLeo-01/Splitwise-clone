from fastapi import APIRouter, Depends
from sqlalchemy import Session
from app.db import get_session
from app.web.group_members.dto import group_members_request_model
from app.web.group_members.services import group_members_service

router = APIRouter()

@router.get("", status_code=200)
async def get_group_members(
    session: Session = Depends(get_session)
):
    group_members_data = await group_members_service.get_all_group_members(session = session)
    return group_members_data

@router.get("/{id}", status_code=200)
async def get_group_members_by_id(
    id: int, session: Session = Depends(get_session)
):
    group_members_data = await group_members_service.get_group_members_by_id(id = id, session=session)
    return group_members_data

@router.post("", status_code=200)
async def create(
    group_members: group_members_request_model.CreateGroupMembers,
    session: Session = Depends(get_session)
):
    group_members_data = await group_members_service.create_group_members(
        request_model_data = group_members, session=session
    )
    return group_members_data

@router.put("/{id}", status_code=200)
async def update(
    id: int, group_members_model: group_members_request_model.UpdateGroupMembers,
    session: Session = Depends(get_session)
):
    group_members_data = await group_members_service.update_group_members(
        id = id, group_members_model= group_members_model, session=session
    )
    return group_members_data

@router.delete("/{id}", status_code=200)
async def delete(
    id: id, session: Session = Depends(get_session)
):
    group_members_data = await group_members_service.delete_group_members_by_id(
        id = id, session = session
    )
    return group_members_data