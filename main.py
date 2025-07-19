from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model_name = "roberta-base-openai-detector"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def analyze(request: Request, user_input: str = Form(...)):
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=1)
        human_prob = round(probs[0][0].item() * 100, 2)
        ai_prob = round(probs[0][1].item() * 100, 2)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "user_input": user_input,
        "ai_prob": ai_prob,
        "human_prob": human_prob
    })