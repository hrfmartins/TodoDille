from pydantic import BaseModel
from datetime import datetime


class TaskList(BaseModel):
    name: str
    date_created: datetime

    def output(self):
        return {
            "name": self.name,
            "date_created": self.date_created.strftime('%Y-%m-%d %H:%M:%S')
        }
