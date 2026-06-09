from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model
model = joblib.load("election_model.pkl")
encoder = joblib.load("label_encoder.pkl")

app = FastAPI(
    title="Election Prediction API",
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

    total_votes = data.ldf + data.udf + data.nda

    return {
        "predicted_winner": winner[0],
        "ldf_votes": data.ldf,
        "udf_votes": data.udf,
        "nda_votes": data.nda,
        "total_votes": total_votes
    }


@app.post("/simulate")
def simulate(data: ElectionInput):

    turnout_factor = 1.05

    ldf = int(data.ldf * turnout_factor)
    udf = int(data.udf * turnout_factor)
    nda = int(data.nda * turnout_factor)

    sample = pd.DataFrame({
        "LDF": [ldf],
        "UDF": [udf],
        "NDA": [nda]
    })

    prediction = model.predict(sample)

    winner = encoder.inverse_transform(prediction)

    return {
        "scenario": "5% Turnout Increase",
        "predicted_winner": winner[0],
        "ldf_votes": ldf,
        "udf_votes": udf,
        "nda_votes": nda
    }