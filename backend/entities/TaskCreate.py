from datetime import datetime
from pydantic import BaseModel


class CreateTask(BaseModel):
    title: str
    description: str
    due_date: datetime
    list_id: int
