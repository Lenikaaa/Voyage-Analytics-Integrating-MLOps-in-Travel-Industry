# ✈️ Voyage Analytics - Integrating MLOps in Travel Industry

## 📌 Project Overview

Voyage Analytics is an end-to-end MLOps project developed in the travel and tourism domain. The project leverages machine learning and modern MLOps practices to build, deploy, and automate multiple intelligent systems using travel datasets.

The project consists of:

1. Flight Price Prediction Model (Regression)
2. Gender Classification Model (Classification)
3. Hotel Recommendation System (Recommendation Engine)
4. Flask REST API
5. Streamlit Web Applications
6. Docker Containerization
7. Kubernetes Deployment
8. Apache Airflow Workflow Automation
9. Jenkins CI/CD Pipeline
10. MLflow Experiment Tracking

---

# 🎯 Business Problem

The travel industry generates a large amount of user, flight, and hotel data. This project aims to utilize this data to:

- Predict flight prices for better travel planning.
- Classify user gender for customer segmentation.
- Recommend hotels based on user preferences and historical booking data.
- Build a scalable and production-ready machine learning system using MLOps practices.

---

# 📂 Dataset Information

## Users Dataset
- code
- company
- name
- gender
- age

## Flights Dataset
- travelCode
- userCode
- from
- to
- flightType
- price
- time
- distance
- agency
- date

## Hotels Dataset
- travelCode
- userCode
- name
- place
- days
- price
- total
- date

---

# 🚀 Project Architecture

```text
Datasets
     ↓
Data Preprocessing
     ↓
Machine Learning Models
     ↓
MLflow Tracking
     ↓
Flask API & Streamlit
     ↓
Docker Containerization
     ↓
Kubernetes Deployment
     ↓
Airflow + Jenkins Automation
```

---

# 🧠 Machine Learning Models

## 1. Flight Price Prediction
- Problem Type: Regression
- Algorithm: XGBoost Regressor
- Evaluation Metrics:
  - Mean Squared Error (MSE)
  - R² Score

### Model Performance
- MSE: 26005.84
- R² Score: 0.80

---

## 2. Gender Classification
- Problem Type: Classification
- Algorithm: Logistic Regression
- Feature Engineering:
  - TF-IDF Vectorization on names
  - Age feature integration

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score

---

## 3. Hotel Recommendation System
- Problem Type: Recommendation Engine
- Technique:
  - User-Hotel Matrix
  - Cosine Similarity

---

# 🛠️ Tech Stack

## Programming
- Python

## Libraries
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Joblib

## MLOps Tools
- Flask
- Streamlit
- Docker
- Kubernetes
- Apache Airflow
- Jenkins
- MLflow
- Git & GitHub

---

# 📁 Project Structure

```text
Voyage-Analytics-Integrating-MLOps-in-Travel-Industry
│
├── airflow
│   └── dags
├── app
├── data
├── k8s
├── model
├── notebooks
├── src
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
```

---

# 🌐 REST API

Run:

```bash
python app/api_price_predictor.py
```

API Endpoint:

```text
http://127.0.0.1:5000/predict
```

---

# 💻 Streamlit Applications

Flight Price Prediction:

```bash
streamlit run app/regression.py
```

Gender Classification:

```bash
streamlit run app/st_gender_classifier.py
```

Hotel Recommendation:

```bash
streamlit run app/st_travel_recommander.py
```

---

# 🐳 Docker

Build:

```bash
docker build -t voyage-analytics .
```

Run:

```bash
docker run -p 8501:8501 voyage-analytics
```

---

# ☸️ Kubernetes

Deploy:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

---

# 🔄 Apache Airflow

DAG:

```text
airflow/dags/travel_price_regression_dag.py
```

Workflow:

```text
Load Data
    ↓
Preprocess Data
    ↓
Train Model
    ↓
Evaluate Model
    ↓
Deploy Model
```

---

# ⚙️ Jenkins CI/CD Pipeline

Pipeline Stages:

- Checkout Code
- Install Dependencies
- Run Basic Tests
- Build Docker Image
- Push Docker Image
- Deploy to Kubernetes

---

# 📈 MLflow

Features:

- Experiment Tracking
- Metric Logging
- Parameter Logging
- Model Versioning

---

# 📸 Project Demonstration

The project includes:

✅ Regression Model

✅ Classification Model

✅ Recommendation System

✅ Flask REST API

✅ Streamlit Applications

✅ Docker Deployment

✅ Kubernetes Deployment

✅ Airflow Automation

✅ Jenkins CI/CD

✅ MLflow Tracking

---

# 🔮 Future Improvements

- Model Monitoring
- Automated Retraining Pipelines
- Authentication & Authorization
- Cloud Deployment
- Enhanced Recommendation System
- Performance Monitoring using Prometheus and Grafana

---

# 👩‍💻 Author

**Lenika Yogi**

M.Sc. Artificial Intelligence & Machine Learning

End-to-End MLOps Capstone Project

---

# ⭐ If you found this project useful, please consider giving it a star.
