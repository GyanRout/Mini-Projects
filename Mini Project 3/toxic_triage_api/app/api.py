from fastapi import FastAPI
from pydantic import BaseModel
from src.model import ToxicClassifier
import src.config as config
import torch
from transformers import DistilBertTokenizer

tokenizer = DistilBertTokenizer.from_pretrained(config.MODEL_NAME)
app= FastAPI()

class CommentRequest(BaseModel):
    text: str

model = ToxicClassifier(config.MODEL_NAME)
model.load_state_dict(torch.load('toxic_model_weights.pth', map_location=config.DEVICE))
model.to(config.DEVICE)
model.eval()

LABELS = ['toxic','severe_toxic','obscene','threat','insult','identity_hate']

@app.post("/predict")
def predict(request: CommentRequest):
    text = request.text

    inputs = tokenizer(
        text,
        max_length=config.MAX_LEN,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    input_ids = inputs['input_ids'].to(config.DEVICE)
    attention_mask = inputs['attention_mask'].to(config.DEVICE)

    with torch.inference_mode():
        logits = model(input_ids=input_ids, attention_mask=attention_mask)
        probabilities = torch.sigmoid(logits).cpu().numpy()[0]

    results = {label: float(prob) for label, prob in zip(LABELS, probabilities)}
    return results