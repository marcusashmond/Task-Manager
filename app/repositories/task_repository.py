from typing import List, Optional
from app.models.task import Task
from datetime import datetime

class TaskRepository:

    def __init__(self, db):
        self.db = db

    def create_task(self, title: str, description: str) -> int:
        cursor = self.db.cursor()
        query = """
            INSERT INTO tasks (title, description, completed, created_at)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (title, description, False, datetime.now(datetime.UTC)))
        self.db.commit()
        task_id = cursor.lastrowid
        cursor.close()
        return task_id

    def get_task(self, task_id: int) -> Optional[Task]:
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Task(**row)
        return None

    def get_all_tasks(self) -> List[Task]:
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        cursor.close()
        return [Task(**row) for row in rows]

    def update_task(self, task_id: int, fields: dict):
        cursor = self.db.cursor()
        set_clause = ", ".join([f"{key} = %s" for key in fields])
        values = list(fields.values())
        values.append(task_id)

        query = f"UPDATE tasks SET {set_clause} WHERE id = %s"
        cursor.execute(query, tuple(values))
        self.db.commit()
        cursor.close()

    def delete_task(self, task_id: int):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        self.db.commit()
        cursor.close()