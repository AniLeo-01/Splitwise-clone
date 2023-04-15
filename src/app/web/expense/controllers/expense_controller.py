from fastapi import APIRouter, Depends
from sqlalchemy import Session
from app.db import get_session
from app.web.expense.dto import expense_request_model
from app.web.expense.services import expense_service

router = APIRouter()

@router.get("", status_code=200)
async def get_expense_by_search_criteria(
    search_criteria: expense_request_model.ExpenseSearchRequestModel,
    session: Session = Depends(get_session)
):
    expense_data = await expense_service.get_expense_by_search_criteria(
        search_criteria=search_criteria, session=session
    )
    return expense_data

@router.get("/{id}", status_code=200)
async def get_expense_by_id(
    id: int, session: Session = Depends(get_session)
):
    expense_data = await expense_service.get_expense_by_id(
        id=id, session=session
    )
    return expense_data

@router.post("", status_code=200)
async def create(
    expense: expense_request_model.CreateExpense,
    session: Session = Depends(get_session),
):
    expense_data = await expense_service.create_expense(
        request_model_data=expense, session=session
    )
    return expense_data

@router.put("/{id}", status_code=200)
async def update(
    id: int,
    expense_model: expense_request_model.UpdateExpense,
    session: Session = Depends(get_session),
):
    expense_data = await expense_service.update_expense(
        id=id, expense_model=expense_model, session=session
    )
    return expense_data

@router.delete("/{id}", status_code=200)
async def delete(id: id, session: Session = Depends(get_session)):
    expense_data = await expense_service.delete_expense_by_id(
        id=id, session=session
    )
    return expense_data
