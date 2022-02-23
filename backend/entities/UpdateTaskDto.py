from pydantic import BaseModel


class UpdateTaskDto(BaseModel):
    task_id: int
    list_id: int
    complete: bool
