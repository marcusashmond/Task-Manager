from fastapi import FastAPI
from app.core.logger import setup_logger
from app.api.routes.task_routes import router as task_router

setup_logger()

app = FastAPI(title="Task Manager API")

app.include_router(task_router)