from transformers import pipeline

# Load the sentiment-analysis model once at worker startup
nlp_pipeline = pipeline("sentiment-analysis")
