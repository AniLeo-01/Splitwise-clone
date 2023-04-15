from fastapi import APIRouter, Depends
from sqlalchemy import Session
from app.db import get_session
from app.web.expense_split_type.dto import expense_split_type_request_model
from app.web.expense_split_type.services import expense_split_type_service

router = APIRouter()

@router.get("", status_code=200)
async def get_expense_split_types_by_search_criteria(
    search_criteria: expense_split_type_request_model,
    session: Session = Depends(get_session)
):
    expense_split_data = await expense_split_type_service.get_expense_split_types_by_search_criteria(
        search_criteria=search_criteria, session=session)
    return expense_split_data
    
@router.get("/{id}", status_code=200)
async def get_expense_split_type_by_id(
    id: int, session: Session = Depends(get_session)
):
    expense_split_data = await expense_split_type_service.get_expense_split_type_by_id(
        id=id, session=session
    )
    return expense_split_data

@router.post("", status_code=200)
async def create(
    expense_split_type_model: expense_split_type_request_model.CreateExpenseSplitType,
    session: Session = Depends(get_session),
):
    expense_split_data = await expense_split_type_service.create_expense_split_type(
        request_model_data=expense_split_type_model, session=session
    )
    return expense_split_data

@router.put("/{id}", status_code=200)
async def update(
    id: int,
    expense_split_type_model: expense_split_type_request_model.UpdateExpenseSplitType,
    session: Session = Depends(get_session),
):
    expense_split_data = await expense_split_type_service.update_expense_split_type(
        id=id, expense_split_type_model=expense_split_type_model, session=session
    )
    return expense_split_data

@router.delete("/{id}", status_code=200)
async def delete(id: id, session: Session = Depends(get_session)):
    expense_split_data = await expense_split_type_service.delete_expense_split_type_by_id(
        id=id, session=session
    )
    return expense_split_data