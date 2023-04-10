from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..dao import expense_model
from ..dto import expense_request_model
from ..repositories import expense_repository
from sqlalchemy.future import select

async def get_expense_search_criteria_query(
        search_criteria: expense_request_model.ExpenseSearchCriteria,
        session: Session
):
    query_statement = select(expense_model.Expense)
    if search_criteria.id:
        query_statement = query_statement.where(
            expense_model.Expense.id == search_criteria.id 
        )
    if search_criteria.description:
        query_statement = query_statement.where(
            expense_model.Expense.description.ilike("%{}%".format(search_criteria.description))
        )
    if search_criteria.split_type:
        query_statement = query_statement.where(
            expense_model.Expense.split_type.ilike("{}".format(search_criteria.split_type))
        )
    if search_criteria.group_id:
        query_statement = query_statement.where(
            expense_model.Expense.group_id == search_criteria.group_id
        )
    return query_statement

async def get_expense_by_search_criteria(
        search_criteria: expense_request_model.ExpenseSearchCriteria,
        session: Session
):
    if search_criteria is None:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid search criteria"
        )
    query = await get_expense_search_criteria_query(
        search_criteria=search_criteria,
        session=session
    )
    expense_data = await expense_repository.get_expense_by_search_criteria(
        query_statement=query, session=session
    )
    if expense_data:
        return expense_data
    else:
        raise HTTPException(
            status_code=400,
            detail = "No expense found!"
        )

async def get_expense_by_id(
        id: int,
        session: Session
):
    if id:
        expense_data = await expense_repository.get_expense_by_id(id=id, session=session)
    else:
        raise HTTPException(
            status_code=400,
            detail = "No expense found!"
        )
    return expense_data

async def create_expense(
        request_model_data: expense_request_model.CreateExpense,
        session: Session
):
    if request_model_data is None:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid request model"
        )
    new_expense_data = await expense_repository.create_expense(
        request_model_data=request_model_data,
        session=session
    )
    return new_expense_data

async def update_expense(
        id: int,
        request_model_data: expense_request_model.UpdateExpense,
        session: Session
):
    expense_data = await expense_repository.get_expense_by_id(id=id, session=session)
    if expense_data:
        expense_data = expense_data.dict(exclude_unset=True)
        for key, value in expense_data.items():
            if value:
                if hasattr(expense_data, str(key)):
                    setattr(expense_data, key, value)
    else:
        raise HTTPException(
            status_code=400,
            detail="No expense with the id found!"
        )
    
async def delete_expense(
        id: int,
        session: Session
):
    expense_data = await expense_repository.get_expense_by_id(id=id, session=session)
    if expense_data:
        expense_data = await expense_repository.delete_expense(expense_data= expense_data, session=session)
    else:
        raise HTTPException(
            status_code=400,
            detail="No expense with the id found!"
        )
    return expense_data