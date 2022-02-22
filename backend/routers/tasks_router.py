from fastapi import APIRouter, HTTPException
from entities.List import TaskList
from entities.Task import Task
from entities.UpdateTaskDto import UpdateTaskDto
from repositories.task_repository import TaskRepository
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/create")
def add_task(task: Task):
    TaskRepository().create_task(task)
    return "OK"


@router.get("/", response_model=List[Task])
def get_tasks_from_list(list_id: int):
    try:
        return TaskRepository().get_tasks_from_list(list_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.delete("/delete")
def delete_task(task_list: int, task_name: int):
    try:
        task_list: TaskList = db.getById(task_list)
        task_list.remove_task(task_name)
        db.updateById(task_list, task_list)

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.put("/complete")
def update_task(change: UpdateTaskDto):
    try:
        return TaskRepository().complete_task(change.task_id, change.list_id, change.complete)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
