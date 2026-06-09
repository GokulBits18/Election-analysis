# 🗳️ Kerala Election Prediction Dashboard

A Full-Stack Machine Learning application that predicts election winners using Kerala Legislative Assembly election data. The system combines a trained Random Forest model, a FastAPI backend, and a Streamlit dashboard to provide election analytics and prediction capabilities.

---

## 📌 Project Overview

This project demonstrates the end-to-end workflow of a Machine Learning application:

* Data Processing and Analysis
* Model Training and Evaluation
* Model Deployment using FastAPI
* Interactive Dashboard using Streamlit
* Election Winner Prediction
* Turnout Scenario Simulation

Users can select a constituency from the Kerala Assembly Election dataset and view:

* LDF votes
* UDF votes
* NDA votes
* Predicted winner
* Vote share analysis
* Turnout simulation results

---

## 🚀 Features

### Constituency-Based Prediction

* Select any constituency from the Kerala Election dataset.
* Automatically loads constituency vote counts.
* Sends data to FastAPI for prediction.

### Machine Learning Prediction

* Random Forest Classifier.
* Predicts the winning alliance based on:

  * LDF Votes
  * UDF Votes
  * NDA Votes

### Vote Share Analysis

* Calculates vote percentages.
* Displays vote share metrics.

### Interactive Visualizations

* Vote Comparison Bar Chart
* Vote Share Pie Chart

### Scenario Simulation

* Simulates a 5% increase in voter turnout.
* Generates a new election prediction based on updated vote counts.

---

## 🏗️ System Architecture

```text
Kerala Election Dataset (CSV)
            │
            ▼
Machine Learning Model Training
            │
            ▼
Saved Model (.pkl)
            │
            ▼
FastAPI Backend
            │
            ▼
Streamlit Dashboard
            │
            ▼
Election Prediction Results
```

---

## 📂 Project Structure

```text
Election-Prediction-Dashboard/
│
├── backend/
│   ├── main.py
│   ├── election_model.pkl
│   └── label_encoder.pkl
│
├── frontend/
│   ├── app.py
│   └── Kerala_election_2021.csv
│
├── notebooks/
│   └── election_model_training.ipynb
│
├── requirements.txt
│
└── README.md
```

---

## 🛠️ Technologies Used

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit
* Requests

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* Joblib

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Seaborn

---

## 📊 Dataset

The project uses Kerala Legislative Assembly Election data containing:

* Constituency
* District
* LDF Votes
* UDF Votes
* NDA Votes
* NOTA Votes
* Total Votes
* Lead Margin
* Winner
* Vote Share Percentages

Dataset Size:

* 140 Constituencies
* 18 Features

---

## 🤖 Machine Learning Pipeline

### Data Preparation

* Load election dataset
* Select relevant features:

  * LDF
  * UDF
  * NDA
* Encode target labels

### Train-Test Split

* 80% Training Data
* 20% Testing Data

### Model Training

Random Forest Classifier:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

### Model Evaluation

* Accuracy Score
* Classification Report
* Feature Importance Analysis

### Model Persistence

```python
joblib.dump(model, "election_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
```

---

## 📡 API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Election Prediction API Running"
}
```

---

### Predict Winner

```http
POST /predict
```

Request:

```json
{
  "ldf": 50000,
  "udf": 45000,
  "nda": 10000
}
```

Response:

```json
{
  "ldf_votes": 50000,
  "udf_votes": 45000,
  "nda_votes": 10000,
  "predicted_winner": "LDF"
}
```

---

### Turnout Simulation

```http
POST /simulate
```

Response:

```json
{
  "scenario": "5% turnout increase",
  "predicted_winner": "LDF"
}
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/election-prediction-dashboard.git

cd election-prediction-dashboard
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Start FastAPI Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Start Streamlit Frontend

Open a new terminal:

```bash
cd frontend

streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 📈 Dashboard Workflow

```text
Select Constituency
        ↓
Load LDF/UDF/NDA Votes
        ↓
Send Data to FastAPI
        ↓
Predict Winner
        ↓
Display Results
        ↓
Visualize Vote Share
        ↓
Run Turnout Simulation
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Full-Stack Development
* Machine Learning Deployment
* REST API Development
* Data Visualization
* Streamlit Dashboard Design
* Model Serialization
* End-to-End ML Application Development

---

## 🔮 Future Enhancements

* Constituency Comparison
* Historical Election Trend Analysis
* Interactive Election Maps
* PostgreSQL Integration
* Advanced Scenario Simulation
* XGBoost Implementation
* Cloud Deployment

---

## 👨‍💻 Author

Gokul MP

---

## 📜 License

This project is intended for educational and learning purposes.
