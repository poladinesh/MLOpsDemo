# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("regression_model.pkl")

class CustomerInput(BaseModel):
    age: int
    income: float
    loyalty_score: float
    region: str
    visits_per_month: int

# sample = pd.DataFrame([{
#     "age": 32,
#     "income": 72000,
#     "loyalty_score": 7,
#     "region": "North",
#     "visits_per_month": 5
# }])

@app.get("/")
def read_root():
    print("API is live now...")
    return {"message": "Our Regression Model API is live"}

@app.post("/predict")
def predict(data: CustomerInput):
    input_data = pd.DataFrame([{
        "age": data.age,
        "income": data.income,
        "loyalty_score": data.loyalty_score,
        "region": data.region,
        "visits_per_month": data.visits_per_month
    }])
    prediction = model.predict(input_data)[0]
    return {"Inference Prediction ": prediction}