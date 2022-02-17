from dependencies import db
from entities.List import TaskList


class ListRepository:

    def create_list(self, list: TaskList):
        query = "INSERT INTO lists (name, date_created) VALUES (%s, %s) "
        values = [list.name, list.date_created.strftime('%Y-%m-%d %H:%M:%S')]
        db.execute(query, values)

    def get_all_lists(self):
        query = "SELECT * FROM lists"
        return db.get_result(query)

    def delete_list(self, task_id: int, list_id):
        query = "DELETE FROM lists WHERE id = %s"
        values = [task_id, list_id]
        db.execute(query, values)
