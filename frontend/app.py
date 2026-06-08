import streamlit as st
import requests

st.set_page_config(
    page_title="Election Prediction Dashboard",
    page_icon="🗳️",
    layout="wide"
)

st.title("🗳️ Kerala Election Prediction Dashboard")

st.markdown("Predict election winners and run turnout simulations.")

# Inputs
ldf = st.number_input("LDF Votes", min_value=0, value=50000)
udf = st.number_input("UDF Votes", min_value=0, value=45000)
nda = st.number_input("NDA Votes", min_value=0, value=10000)

api_url = "http://127.0.0.1:8000"

col1, col2 = st.columns(2)

with col1:
    if st.button("Predict Winner"):

        payload = {
            "ldf": ldf,
            "udf": udf,
            "nda": nda
        }

        response = requests.post(
            f"{api_url}/predict",
            json=payload
        )

        result = response.json()

        st.success(
            f"Predicted Winner: {result['predicted_winner']}"
        )

with col2:
    if st.button("Run 5% Turnout Simulation"):

        payload = {
            "ldf": ldf,
            "udf": udf,
            "nda": nda
        }

        response = requests.post(
            f"{api_url}/simulate",
            json=payload
        )

        result = response.json()

        st.info(
            f"Scenario Winner: {result['predicted_winner']}"
        )

        st.write("Updated Vote Counts")

        st.write({
            "LDF": result["ldf_votes"],
            "UDF": result["udf_votes"],
            "NDA": result["nda_votes"]
        })