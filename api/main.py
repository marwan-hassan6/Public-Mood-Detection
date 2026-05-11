# api/main.py

from fastapi import FastAPI
from pydantic import BaseModel

from model import predict_sentiment

app = FastAPI(title="Public Mood Detection API")

# Request body schema
class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Sentiment Analysis API is running"
    }

@app.post("/predict")
async def predict(request: TextRequest):

    result = predict_sentiment(request.text)

    return result