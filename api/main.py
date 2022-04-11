# Import libraries
from api import models
from fastapi import FastAPI
from dto import dto

# Instantiating the model
model = models.BERT_MODEL()

# Determining how queries work
app = FastAPI()

@app.get("/health_check")
def health_check():
    return {"code": 200, "status": "OK"}

@app.post("/api/predict", response_model = dto.PredictionOut)
async def answer(user_request: dto.UserRequestIn):
    input = user_request.input
    print(input)
    prediction = model.predict(input["texts"])
    print(prediction)
    return {'prediction': prediction}

    