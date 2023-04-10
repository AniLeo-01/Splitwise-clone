from sqlalchemy.orm import Session
from sqlalchemy.future import select
from pydantic import BaseModel
from ..dao import expense_model
from ..dto import expense_request_model

async def get_expense_by_search_criteria(
        session: Session, query_statement: BaseModel
):
    result = await session.execute(query_statement)
    expense_data = result.scalars().all()
    return expense_data

async def get_expense_by_id(
        id: int, session: Session
):
    query_statement = select(expense_model.Expense).where(
        id == expense_model.Expense.id
    )
    execute_query = session.execute(query_statement)
    response = execute_query.scalars().first()
    return response

async def create_expense(
        request_model_data: expense_request_model.CreateExpense, session: Session
):
    new_expense = expense_model.Expense.from_orm(request_model_data)
    session.add(new_expense)
    await session.commit()
    await session.refresh(new_expense)
    return new_expense

async def update_expense(
        session: Session, expense_data: expense_request_model.UpdateExpense
):
    session.add(expense_data)
    await session.commit()
    await session.refresh(expense_data)
    return expense_data

async def delete_expense(
        session: Session, expense_data: expense_model.Expense
):
    await session.delete(expense_data)
    await session.commit()
    return expense_data
