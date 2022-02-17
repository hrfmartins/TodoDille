from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    due_date: datetime
    date_created: datetime
    complete: bool
    list_id: int
