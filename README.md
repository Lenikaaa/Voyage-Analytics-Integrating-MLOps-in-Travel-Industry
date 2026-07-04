

---

# ✈️ Voyage Analytics: End-to-End Travel Intelligence Platform with MLOps

## Project Overview

Voyage Analytics is an **end-to-end Machine Learning and MLOps project** built for the travel industry.
It demonstrates how multiple ML use cases can be **designed, trained, orchestrated, tracked, and deployed** using production-grade tools and workflows.

The platform covers:

* **Flight price prediction**
* **User profiling (gender classification)**
* **Hotel recommendation system**

and integrates **MLflow, Airflow, Docker, Kubernetes, Jenkins, APIs, and Streamlit** to simulate a real-world ML system.

---

## 🔍 Key Features

* **Flight Price Prediction**

  * Regression models: Decision Tree, Random Forest, XGBoost
  * Feature engineering with target encoding and ordinal mapping
  * REST API for real-time inference

* **Gender Classification**

  * TF-IDF (character-level) + Logistic Regression
  * Classes: `male`, `female`, `none`
  * Streamlit UI for interactive predictions

* **Hotel Recommendation System**

  * Collaborative filtering using implicit feedback
  * Learns from booking frequency and total spend
  * Streamlit dashboard for recommendations and insights

* **MLOps & Engineering**

  * Experiment tracking & model versioning with MLflow
  * Workflow orchestration with Apache Airflow
  * CI/CD pipeline using Jenkins
  * Containerized deployment using Docker
  * Scalable serving via Kubernetes (HPA enabled)

---

## 🏗️ Project Structure

```
.
├── airflow/                     # Apache Airflow DAGs
│   └── dags/
│       └── travel_price_regression_dag.py
│
├── app/                         # APIs & Streamlit apps
│   ├── api_price_predictor.py
│   ├── st_gender_classifier.py
│   └── st_travel_recommander.py
│
├── data/                        # Raw datasets
│   ├── flight_prediction/
│   │   ├── flights.csv
│   │   └── processed_flights.csv
│   ├── gender_classifier/
│   │   └── users.csv
│   └── hotel_recommander/
│       └── hotels.csv
│
├── src/                         # Core ML logic
│   ├── flight_prediction/
│   │   ├── preprocessing.py
│   │   └── train.py
│   ├── gender_classifier/
│   │   ├── gender_train.py
│   │   └── inference.py
│   └── recommander/
│       ├── preprocessor.py
│       ├── similarity.py
│       └── recommander.py
│
├── notebooks/                   # Experimentation & analysis
│   └── Gender_Classification_Model (1).ipynb
│   └── Regression_Model.ipynb
│   └── Travel_Recommendation_Model.ipynb
│
├── k8s/                         # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── .gitignore
├── .dockerignore
├── README.md
└── LICENSE
```

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* TF-IDF
* Collaborative Filtering

### MLOps & Deployment

* Apache Airflow
* MLflow
* Docker
* Kubernetes (HPA)
* Jenkins (CI/CD)

### Serving & Visualization

* Flask (REST APIs)
* Streamlit (interactive dashboards)

---

## ▶️ Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/bsshewale/Voyage-Analytics-Integrating-MLOps-in-Travel-Industry-.git
cd Voyage-Analytics-Integrating-MLOps-in-Travel-Industry-
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📈 Flight Price Model Training

```bash
python src/flight_prediction/train.py
```

* Trains regression models
* Logs parameters, metrics, and artifacts to MLflow
* Supports experiment comparison and model versioning

---

## 📊 MLflow Model Tracking

Start MLflow UI:

```bash
mlflow ui
```

Access at:

```
http://localhost:5000
```

Track:

* Experiments
* Model parameters
* Metrics
* Artifacts

---

## 🌐 APIs & Streamlit Apps

### Flight Price Prediction API

```bash
python app/api_price_predictor.py
```
![Price_predictor](https://github.com/user-attachments/assets/a2419305-8688-4d03-95e7-810866b0fd96)
Example request:

```json
{
  "from": "Recife (PE)",
  "to": "Florianopolis (SC)",
  "flightType": "firstClass",
  "time": 1.76,
  "distance": 676.53,
  "agency": "FlyingDrops",
  "day": 26,
  "month": 9,
  "year": 2019
}
```

---

### Streamlit Dashboards

```bash
streamlit run app/st_travel_recommander.py
streamlit run app/st_gender_classifier.py
```
Hotel Recommander
![Hotel recommander](https://github.com/user-attachments/assets/3002854b-f893-4d02-9933-96d036c817b7)

Gender Classifier
![gender classification](https://github.com/user-attachments/assets/0f45b9dd-1ddb-4243-ab90-c0337055e901)

---

## ⚙️ Workflow Automation with Airflow

Airflow DAG:

* `travel_price_regression_dag.py`

Pipeline stages:

* Data ingestion
* Preprocessing
* Model training
* MLflow logging

Start Airflow:

```bash
airflow db init
airflow webserver --port 8080
airflow scheduler
```

Access UI:

```
http://localhost:8080
```

---

## 🐳 Docker & Kubernetes Deployment

```bash
docker build -t bsshewale/flight-price-predictor:latest .
docker push bsshewale/flight-price-predictor:latest
kubectl apply -f k8s/
```

Supports **Horizontal Pod Autoscaling (HPA)**.

---

## 🔁 CI/CD with Jenkins

Pipeline stages:

* Code checkout
* Dependency installation
* Model & app validation
* Docker build & push
* Kubernetes deployment

Secrets managed via Jenkins credentials.

---

## ⚠️ Important Note

> Trained model artifacts (`.pkl`, `.joblib`, `mlruns/`) are **not committed** to GitHub.
> Models are generated via pipelines and tracked using **MLflow**, ensuring clean version control and reproducibility.

---

## 📌 Project Highlights

* Multi-model ML system in a single platform
* Production-style MLOps workflows
* Modular and scalable architecture
* Resume-ready industry project

---

## 👤 Author

**Lenika Yogi**
MS in Data Science & AI

---


