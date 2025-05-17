import os
from fastapi import APIRouter
from database.db import session
from dto.todo_dto import TodoDto
from model.todo import Todo
from repository.todo_repository import TodoRepository


# router
router: APIRouter = APIRouter()

# setup the repository
repository = TodoRepository(session)

@router.post("/", response_model=TodoDto)
def create_todo(todo_dto: TodoDto):
    todo: Todo = Todo()
    todo.title = todo_dto.title
    todo.body = todo_dto.body
    return repository.create_todo(todo)