from pydantic import BaseModel

class TaskData(BaseModel):
    name: str
    done: bool

class TaskID(TaskData):
    id: int
