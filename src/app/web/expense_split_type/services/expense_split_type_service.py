from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..dao import expense_split_type_model
from ..dto import expense_split_type_request_model
from ..repositories import expense_split_type_repository
from sqlalchemy.future import select
from app.web.commons.enums import SplitTypeEnum
from app.web.group_members.services import group_members_service

async def get_expense_split_type_search_criteria_query(
        search_criteria: expense_split_type_request_model.ExpenseSplitTypeSearchCriteria,
        session: Session
):
    query_statement = select(expense_split_type_model.ExpenseSplitTypeModel)
    if search_criteria.id:
        query_statement = query_statement.where(
            expense_split_type_model.ExpenseSplitType.id == search_criteria.id 
        )
    if search_criteria.split_type:
        query_statement = query_statement.where(
            expense_split_type_model.ExpenseSplitType.split_type.ilike("{}".format(search_criteria.split_type))
        )
    if search_criteria.expense_id:
        query_statement = query_statement.where(
            expense_split_type_model.ExpenseSplitType.expense_id == search_criteria.expense_id
        )``
    if search_criteria.user_id:
        query_statement = query_statement.where(
            expense_split_type_model.ExpenseSplitType.user_id == search_criteria.user_id
        )
    return query_statement

async def get_expense_split_type_by_id(
        id: int,
        session: Session
):
    if id:
        expense_split_type_data = await expense_split_type_repository.get_expense_split_type_by_id(id=id, session=session)
    else:
        raise HTTPException(status_code=400, detail="Enter a valid expense split type id")
    
    if expense_split_type_data:
        return expense_split_type_data
    else:
        raise HTTPException(status_code=404, detail="Expense Split Type not found")
    
async def get_expense_split_type_by_search_criteria(
        search_criteria: expense_split_type_request_model.ExpenseSplitTypeSearchCriteria,
        session: Session
):
    if search_criteria is None:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid search criteria"
        )
    query = await get_expense_split_type_search_criteria_query(
        search_criteria=search_criteria,
        session=session
    )
    expense_split_type_data = await expense_split_type_repository.get_expense_split_type_by_search_criteria(
        query_statement=query, session=session
    )
    if expense_split_type_data:
        return expense_split_type_data
    else:
        raise HTTPException(
            status_code=400,
            detail = "No expense split type found!"
        )

async def create_expense_split_type(
        expense_split_type_model: expense_split_type_request_model.CreateExpenseSplitType,
        session: Session
):
    if expense_split_type_model is None:
        raise HTTPException(status_code=400, detail="Enter a valid expense split type")
    if expense_split_type_model:
        if expense_split_type_model.split_type is SplitTypeEnum.Equal:
            user_count = await group_members_service.get_group_member_count_by_group_id(
                group_id=expense_split_type_model.group_id, session=session
            )
            setattr(expense_split_type_model, "split_amount", 
                        expense_split_type_model.expense_amount / user_count)
        
        if expense_split_type_model.split_type is SplitTypeEnum.Unequal:
            if hasattr(expense_split_type_model, "split_amount"):
                setattr(expense_split_type_model, "split_amount", )

            expense_split_type_data = expense_split_type_model.from_orm(expense)
  

        expense_split_type_model.split_amount = expense_split_type_model.expense_amount / expense_split_type_model.split_count
    new_expense_split_type_data = await expense_split_type_repository.create_expense_split_type(
        expense_split_type=expense_split_type_model, session=session
    )
    if new_expense_split_type_data:
        return new_expense_split_type_data
    else:
        raise HTTPException(status_code=400, detail="Expense Split Type not created")

async def update_expense_split_type(
        id: int,
        expense_split_type_model: expense_split_type_request_model.UpdateExpenseSplitType,
        session: Session
):
    if id is None:
        raise HTTPException(status_code=400, detail="Enter a valid expense split type")
    updated_expense_split_type_data = await expense_split_type_repository.get_expense_split_type_data_by_id(
        expense_split_type=expense_split_type_model, session=session
    )
    if updated_expense_split_type_data:
        updated_expense_split_type_data = expense_split_type_model.dict(exclude_unset=True)
        for key, value in updated_expense_split_type_data.items():
            if value:
                if hasattr(updated_expense_split_type_data, str(key)):
                    setattr(updated_expense_split_type_data, key, value)

    else:
        raise HTTPException(
            status_code=400,
            detail= "Expense Split Type Data not provided!"
        )            
    updated_expense_split_type_data = await expense_split_type_repository.update_group_members(
        session=session, 
    )
    return updated_expense_split_type_data

async def delete_expense_split_type(
        id: int,
        session: Session
):
    if id is None:
        raise HTTPException(
            status_code=400,
            detail = "Enter a valid expense split type id"
        )
    expense_split_type_data = await expense_split_type_repository.get_expense_split_type_by_id(
        id=id, session=session
    )
    if expense_split_type_data:
        delete_expense_split_type_data = await expense_split_type_repository.delete_expense_split_type(
            expense_split_type_data=expense_split_type_data, session=session
        )
        return delete_expense_split_type_data
    else:
        raise HTTPException(
            status_code=400,
            detail = "Expense Split Type not found!"
        )
