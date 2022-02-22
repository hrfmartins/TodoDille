from dependencies import db
from entities.Task import Task


class TaskRepository:
    def create_task(self, task: Task):
        query = "INSERT INTO tasks (title ,description, due_date, date_created, list_id, complete) VALUES (%s, %s, " \
                "%s, %s, %s, %s) "
        values = [task.title,
                  task.description,
                  task.due_date.strftime('%Y-%m-%d %H:%M:%S'),
                  task.date_created.strftime('%Y-%m-%d %H:%M:%S'),
                  task.list_id,
                  task.complete]
        db.execute(query, values)

    def get_tasks_from_list(self, list_id: int):
        query = "SELECT * FROM tasks WHERE list_id = %s"
        variables = [list_id]
        return db.get_result(query, variables=variables)

    def update_task(self, task: Task, task_id: int):
        query = "UPDATE tasks SET title = %s ,description = %s, due_date = %s WHERE id = %s AND list_id = %s;"
        values = [task.title, task.description, task.due_date, task_id, task.list_id]
        db.execute(query, values)

    def complete_task(self, task_id: int, list_id: int, state: bool):
        query = "UPDATE tasks SET complete = %s WHERE list_id = %s AND id = %s;"
        values = [state, list_id, task_id]
        db.execute(query, values)

    def delete_task(self, task_id: int, list_id):
        query = "DELETE FROM tasks WHERE id = %s AND list_id = %s;"
        values = [task_id, list_id]
        db.execute(query, values)

