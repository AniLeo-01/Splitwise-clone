from sqlalchemy.orm import Session
from sqlalchemy.future import select
from pydantic import BaseModel
from ..dao import expense_split_type_model
from ..dto import expense_split_type_request_model
from sqlalchemy import and_

async def get_expense_split_type_by_search_criteria(
        session: Session, query_statement: BaseModel
):
    result = await session.execute(query_statement)
    expense_split_type_data = result.scalars().all()
    return expense_split_type_data

async def get_expense_split_type_by_id(
        id: int, session: Session
):
    query_statement = select(expense_split_type_model.ExpenseSplitTypeModel).where(
        id == expense_split_type_model.ExpenseSplitTypeModel.id
    )
    execute_query = session.execute(query_statement)
    response = execute_query.scalars().first()
    return response

async def create_expense_split_type(
        request_model_data: expense_split_type_request_model.CreateExpenseSplitType,
        session: Session
):
    new_expense_split_type = expense_split_type_model.ExpenseSplitTypeModel.from_orm(request_model_data)
    session.add(new_expense_split_type)
    await session.commit()
    await session.refresh(new_expense_split_type)
    return new_expense_split_type

async def update_expense_split_type(
        session: Session, expense_split_type_data: expense_split_type_request_model.UpdateExpenseSplitType
):
    session.add(expense_split_type_data)
    await session.commit()
    await session.refresh(expense_split_type_data)
    return expense_split_type_data

async def delete_expense_split_type(
        session: Session, expense_split_type_data: expense_split_type_model.ExpenseSplitTypeModel
):
    await session.delete(expense_split_type_data)
    await session.commit()
    return expense_split_type_data

