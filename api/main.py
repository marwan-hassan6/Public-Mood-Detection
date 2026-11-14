# api/main.py

# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException

# pyrefly: ignore [missing-import]
from pydantic import BaseModel
import re

from model import predict_sentiment

app = FastAPI(title="Public Mood Detection API")

# Request body schema
class TextRequest(BaseModel):
    text: str

def validate_input(text: str):
    text = text.strip()
    if not text:
        return "Please enter some text."
    if all(c.isdigit() or c.isspace() for c in text):
        return "Input cannot contain only numbers."
    alnum_chars = [c for c in text if c.isalnum()]
    if not alnum_chars or len(alnum_chars) < 3:
        return "Please enter a valid sentence."
    return None

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Sentiment Analysis API is running"
    }

@app.post("/predict")
async def predict(request: TextRequest):
    error_msg = validate_input(request.text)
    if error_msg:
        raise HTTPException(status_code=400, detail=error_msg)

    result = predict_sentiment(request.text)

    return result