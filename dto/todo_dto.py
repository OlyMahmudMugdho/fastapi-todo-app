from pydantic import BaseModel

# Data Transfer Object for Todo
class TodoDto(BaseModel):
    id: int
    title: str
    body: str