from pydantic import BaseModel

class ToDoCreate(BaseModel):
    task: str

class ToDo(BaseModel):
        id: int
        task: str
        class config:

            orm_mode=True      

