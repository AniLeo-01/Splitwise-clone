from ..dao import group_members_model
from ..dto import group_members_request_model
from ..repositories import group_members_repository
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from fastapi import HTTPException


async def get_all_group_members(session: Session):
    group_members_data = await group_members_repository.get_all_group_members(session=session)
    if group_members_data:
        return group_members_data
    else:
        raise HTTPException(
            status_code=404, detail="No group members found"
        )
    
async def get_group_members_by_id(id: int, session: Session):
    
    if id:
        group_members_data = await group_members_repository.get_group_members_by_id(id=id, session=session)
    else:
        raise HTTPException(
            status_code=400, detail="Group members id not provided"
        )
    if group_members_data:
        return group_members_data
    else:
        raise HTTPException(
            status_code=404, detail="No group members with the id found"
        )

async def create_group_members(request_model_data: group_members_request_model.CreateGroupMembers, session: Session):
    new_group_member = await group_members_repository.create_group_members(request_model_data=request_model_data, session=session)
    return new_group_member

async def update_group_members(id: int, group_members_model: group_members_request_model.UpdateGroupMembers, session: Session):
    group_members_data = await group_members_repository.get_group_members_by_id(
        id=id, session=session
    )
    if group_members_data:
        group_members_data = group_members_model.dict(exclude_unset=True)
        for key, value in group_members_data.items():
            if value:
                if hasattr(group_members_data, str(key)):
                    setattr(group_members_data, key, value)
    else:
        raise HTTPException(
            status_code=400,
            detail="No group members with the id found"
        )
    group_members_data = await group_members_repository.update_group_members(
        session=session, group_members_data = group_members_data
    )
    return group_members_data
    
async def delete_group_members_by_id(id: int, session: Session):
    
    group_members_data = await group_members_repository.get_group_members_by_id(
        id = id, session=session
    )
    if group_members_data:
        group_members_data = await group_members_repository.delete_group_members(
            group_members_data = group_members_data, session=session
        )
    else:
        raise HTTPException(
            status_code=400,
            detail="No group members with the id found"
        )
    return group_members_data

async def get_group_member_count_by_group_id(
        session: Session, group_id: int
):
    group_members_count = await group_members_repository.get_group_member_count_by_group_id(
        session=session, group_id=group_id
    )
    if group_members_count:
        return group_members_count
    else:
        raise HTTPException(
            status_code=404, detail="No group members found!"
        )