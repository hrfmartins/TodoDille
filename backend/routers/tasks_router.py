from fastapi import APIRouter, HTTPException
from entities.List import TaskList
from entities.Task import Task
from repositories.task_repository import TaskRepository


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/create")
def add_task(task: Task):
    TaskRepository().create_task(task)
    return "OK"


@router.get("/", response_model=list)
def get_tasks_from_list(task_id: int):
    try:
        return TaskRepository().get_tasks_from_list(task_id)
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


@router.put("/update")
def update_task(task: Task, task_list: int):
    try:
        task_list: TaskList = db.getById(task_list)
        task_list.updateTask(task)
        db.updateById(task_list, task_list)

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

