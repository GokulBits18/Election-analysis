import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(
    page_title="Election Prediction Dashboard",
    page_icon="🗳️",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# Load dataset
df = pd.read_csv("Kerala_election_2021.csv")

st.title("🗳️ Kerala Election Prediction Dashboard")

st.markdown("Select a constituency and predict the winner.")

st.markdown("---")

# Constituency Selection

constituency = st.selectbox(
    "Select Constituency",
    sorted(df["CONSTITUENCY"].unique())
)

# Get selected row

row = df[df["CONSTITUENCY"] == constituency].iloc[0]

ldf = int(row["LDF"])
udf = int(row["UDF"])
nda = int(row["NDA"])

# Display votes

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("LDF Votes", f"{ldf:,}")

with col2:
    st.metric("UDF Votes", f"{udf:,}")

with col3:
    st.metric("NDA Votes", f"{nda:,}")

st.markdown("---")

tab1, tab2 = st.tabs([
    "Prediction",
    "Simulation"
])

# ==========================================
# Prediction Tab
# ==========================================

with tab1:

    if st.button("Predict Winner"):

        payload = {
            "ldf": ldf,
            "udf": udf,
            "nda": nda
        }

        response = requests.post(
            f"{API_URL}/predict",
            json=payload
        )

        result = response.json()

        winner = result["predicted_winner"]

        st.markdown(
            f"""
            <div style="
                padding:20px;
                border-radius:10px;
                background:#d4edda;
                text-align:center;
                font-size:28px;
                font-weight:bold;
            ">
                🏆 Predicted Winner: {winner}
            </div>
            """,
            unsafe_allow_html=True
        )

        total_votes = ldf + udf + nda

        ldf_share = round((ldf / total_votes) * 100, 2)
        udf_share = round((udf / total_votes) * 100, 2)
        nda_share = round((nda / total_votes) * 100, 2)

        st.markdown("## Vote Share")

        c1, c2, c3 = st.columns(3)

        c1.metric("LDF", f"{ldf_share}%")
        c2.metric("UDF", f"{udf_share}%")
        c3.metric("NDA", f"{nda_share}%")

        chart_data = pd.DataFrame({
            "Alliance": ["LDF", "UDF", "NDA"],
            "Votes": [ldf, udf, nda]
        })

        st.markdown("## Vote Comparison")

        st.bar_chart(
            chart_data.set_index("Alliance")
        )

        fig = px.pie(
            chart_data,
            names="Alliance",
            values="Votes",
            title="Vote Share Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ==========================================
# Simulation Tab
# ==========================================

with tab2:

    if st.button("Run 5% Turnout Simulation"):

        payload = {
            "ldf": ldf,
            "udf": udf,
            "nda": nda
        }

        response = requests.post(
            f"{API_URL}/simulate",
            json=payload
        )

        result = response.json()

        st.markdown(
            f"""
            <div style="
                padding:20px;
                border-radius:10px;
                background:#cce5ff;
                text-align:center;
                font-size:28px;
                font-weight:bold;
            ">
                📈 Scenario Winner:
                {result['predicted_winner']}
            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "LDF",
            result["ldf_votes"],
            result["ldf_votes"] - ldf
        )

        c2.metric(
            "UDF",
            result["udf_votes"],
            result["udf_votes"] - udf
        )

        c3.metric(
            "NDA",
            result["nda_votes"],
            result["nda_votes"] - nda
        )