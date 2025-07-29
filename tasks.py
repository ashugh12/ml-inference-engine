from celery_app import celery
from model import nlp_pipeline

@celery.task(name="run_sentiment_analysis")
def run_sentiment_analysis(text: str) -> dict:
    result = nlp_pipeline(text)
    return result[0]
