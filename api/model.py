# api/model.py

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Labels
class_names = ["negative", "neutral", "positive"]

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# HuggingFace model
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Load model
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

model.to(device)
model.eval()

print(f"Model loaded on {device}")

def predict_sentiment(text: str):

    # Tokenization
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    # Move tensors to device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Inference
    with torch.inference_mode():

        outputs = model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=1)[0]

        predicted_class = probabilities.argmax().item()

        confidence = probabilities[predicted_class].item()

    return {
        "text": text,
        "sentiment": class_names[predicted_class],
        "confidence": round(confidence, 4),
        "probabilities": {
            class_names[i]: round(probabilities[i].item(), 4)
            for i in range(len(class_names))
        }
    }