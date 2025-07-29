from fastapi import FastAPI
from pydantic import BaseModel
from tasks import run_sentiment_analysis
from celery.result import AsyncResult
from celery_app import celery

app = FastAPI()

class JobRequest(BaseModel):
    text: str

@app.post("/submit/")
def submit_job(req: JobRequest):
    task = run_sentiment_analysis.delay(req.text)
    return {"job_id": task.id}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    result = AsyncResult(job_id, app=celery)
    if result.state == "PENDING":
        return {"status": "Pending"}
    elif result.state == "STARTED":
        return {"status": "Processing"}
    elif result.state == "SUCCESS":
        return {"status": "Success", "result": result.result}
    elif result.state == "FAILURE":
        return {"status": "Failed", "error": str(result.result)}
    return {"status": result.state}
