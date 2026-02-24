from typing import List

from fastapi import HTTPException, status

from app.repositories.task_repository import TaskRepository
from app.models.task import Task

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: str) -> int:
        return self.repository.create_task(title, description)

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get_task(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.repository.get_all_tasks()

    def update_task(self, task_id: int, fields: dict):
        self.repository.update_task(task_id, fields)

    def delete_task(self, task_id: int):
        self.repository.delete_task(task_id)