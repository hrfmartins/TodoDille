from dependencies import db
from entities.Task import Task
from entities.TaskCreate import CreateTask
from datetime import datetime


class TaskRepository:
    def create_task(self, task: CreateTask):
        query = "INSERT INTO tasks (title ,description, due_date, date_created, list_id, complete) VALUES (%s, %s, " \
                "%s, %s, %s, %s) "
        values = [task.title,
                  task.description,
                  task.due_date.strftime('%Y-%m-%d %H:%M:%S'),
                  datetime.now(),
                  task.list_id,
                  False]
        task_id = db.insert(query, values)

        return self.get_task_from_id(task.list_id, task_id)[0]



    def get_tasks_from_list(self, list_id: int):
        query = "SELECT * FROM tasks WHERE list_id = %s"
        variables = [list_id]
        return db.get_result(query, variables=variables)

    def get_task_from_id(self, list_id: int, task_id: int):
        query = "SELECT * FROM tasks WHERE list_id = %s AND id = %s"
        variables = [list_id, task_id]
        return db.get_result(query, variables=variables)

    def update_task(self, task: Task):
        query = "UPDATE tasks SET title = %s ,description = %s, due_date = %s WHERE id = %s AND list_id = %s;"
        values = [task.title, task.description, task.due_date, task.id, task.list_id]
        db.execute(query, values)

    def complete_task(self, task_id: int, list_id: int, state: bool):
        query = "UPDATE tasks SET complete = %s WHERE list_id = %s AND id = %s;"
        values = [state, list_id, task_id]
        db.execute(query, values)

    def delete_task(self, task_id: int, list_id):
        query = "DELETE FROM tasks WHERE id = %s AND list_id = %s;"
        values = [task_id, list_id]
        db.execute(query, values)

    def get_today_tasks(self):
        date = datetime.now()
        query = "SELECT * FROM tasks WHERE MONTH(due_date) = %s AND YEAR(due_date) = %s AND DAY(due_date) = %s;"
        values = [date.month, date.year, date.day]
        return db.get_result(query, values)

