from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Predictions import makePrediction, main
from typing import Optional

app = FastAPI()

# Initialize predictions
main()

# Allow frontend (React) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Environmental Data API"}

@app.get("/predict")
def predict(metric: str, year: int, min: float, max: float):
    prediction = makePrediction(metric, year, min, max)
    return {
        "metric": metric,
        "year": year,
        "prediction": prediction
    } 