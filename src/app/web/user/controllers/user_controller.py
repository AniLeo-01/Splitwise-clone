from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Session
from app.db import get_session


from app.web.expense.controllers import expense_controller
from app.web.expense.dao import expense_controller
from app.web.expense.dto import expense_controller
from app.web.expense.services import expense_controller
from app.web.user.dto import user_request_model
from app.web.user.services import user_services


router = APIRouter()

@router.get("", status_code=200)
async def get_user_by_search_criteria(search_criteria: user_request_model.UserSearchCriteria = Depends(), session: Session = Depends(get_session)):
    user_data = await user_services.get_user_by_search_criteria(search_criteria = search_criteria, session = session)
    return user_data

@router.get("/{id}", status_code=200)
async def get_user_by_id(id: int, session: Session = Depends(get_session)):
    user_data = await user_services.get_user_by_id(id = id, session=session)
    return user_data

@router.post("", status_code=200)
async def create(user: user_request_model.CreateUser,
                 session: Session = Depends(get_session)):
    user_data = await user_services.create_user(
        request_model_data = user, session=session
    )
    return user_data