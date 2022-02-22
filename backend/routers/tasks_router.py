from fastapi import APIRouter, HTTPException
from entities.List import TaskList
from entities.Task import Task
from entities.UpdateTaskDto import UpdateTaskDto
from entities.TaskCreate import CreateTask
from repositories.task_repository import TaskRepository
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/create", response_model=Task)
def add_task(task: CreateTask):
    return TaskRepository().create_task(task)


@router.get("/", response_model=List[Task])
def get_tasks_from_list(list_id: int):
    try:
        return TaskRepository().get_tasks_from_list(list_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.put("/update")
def delete_task(task: Task):
    try:
        return TaskRepository().update_task(task)

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.put("/complete")
def update_task(change: UpdateTaskDto):
    try:
        return TaskRepository().complete_task(change.task_id, change.list_id, change.complete)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.get("/today", response_model=List[Task])
def today_tasks():
    try:
        return TaskRepository().get_today_tasks()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
