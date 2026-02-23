from fastapi import APIRouter, Depends
from typing import List
from app.schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService
from app.api.deps import get_task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=int)
def create_task(
    task: TaskCreate,
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task.title, task.description)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    return service.get_task(task_id)

@router.get("/", response_model=List[TaskResponse])
def get_all_tasks(
    service: TaskService = Depends(get_task_service)
):
    return service.get_all_tasks()

@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    service: TaskService = Depends(get_task_service)
):
    service.update_task(task_id, task.dict(exclude_unset=True))
    return {"message": "Task updated"}

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    service.delete_task(task_id)
    return {"message": "Task deleted"}