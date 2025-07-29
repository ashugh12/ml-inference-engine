from celery import Celery
import os

broker = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
backend = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

celery = Celery("ml_tasks", broker=broker, backend=backend)
