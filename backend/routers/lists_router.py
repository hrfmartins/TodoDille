from fastapi import APIRouter, HTTPException
from entities.List import TaskList
from dependencies import db
from repositories.list_repository import ListRepository

router = APIRouter(prefix="/list", tags=["lists"])


@router.get("/", response_model=list)
def get_all_lists():
    return ListRepository().get_all_lists()


@router.put("/update")
def update_list_name(name: str, id: int):
    task = db.getByQuery({"id": id})[0]
    if task and name:
        db.updateByQuery({"title": name}, {"id": id})
    else:
        raise HTTPException(status_code=400, detail="ID does not exist or name is impossible to use")


@router.post("/create")
def add_list(task_list: TaskList):
    ListRepository().create_list(task_list)
    return "OK"


def output(task):
    return {
        "name": task["name"],
        "date_created": task["date_created"].strftime('%Y-%m-%d %H:%M:%S')
    }
