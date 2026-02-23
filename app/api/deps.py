from fastapi import Depends
from app.db.session import get_db
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService

def get_task_repository(db = Depends(get_db)):
    return TaskRepository(db)

def get_task_service(
    repository: TaskRepository = Depends(get_task_repository)
):
    return TaskService(repository)