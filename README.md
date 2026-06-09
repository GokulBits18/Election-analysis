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


├── frontend/### Vote Share Analysis

* Calculates vote percentages.
* Displays vote share metrics.

