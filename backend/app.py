from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load trained model
model = joblib.load("election_model.pkl")
encoder = joblib.load("label_encoder.pkl")

app = FastAPI(
    title="Election Prediction API",
    description="Kerala Election Winner Prediction",
    version="1.0"
)


class ElectionInput(BaseModel):
    ldf: int
    udf: int
    nda: int


@app.get("/")
def home():
    return {
        "message": "Election Prediction API Running"
    }


@app.post("/predict")
def predict(data: ElectionInput):

    sample = pd.DataFrame({
        "LDF": [data.ldf],
        "UDF": [data.udf],
        "NDA": [data.nda]
    })

    prediction = model.predict(sample)

    winner = encoder.inverse_transform(prediction)

    return {
        "ldf_votes": data.ldf,
        "udf_votes": data.udf,
        "nda_votes": data.nda,
        "predicted_winner": winner[0]
    }


@app.post("/simulate")
def simulate(data: ElectionInput):

    ldf = int(data.ldf * 1.05)
    udf = int(data.udf * 1.05)
    nda = int(data.nda * 1.05)

    sample = pd.DataFrame({
        "LDF": [ldf],
        "UDF": [udf],
        "NDA": [nda]
    })

    prediction = model.predict(sample)

    winner = encoder.inverse_transform(prediction)

    return {
        "scenario": "5% turnout increase",
        "ldf_votes": ldf,
        "udf_votes": udf,
        "nda_votes": nda,
        "predicted_winner": winner[0]
    }