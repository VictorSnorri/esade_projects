# ESADE Projects – Victor Jansen

This repository contains selected projects from my MSc in Business Analytics at ESADE Business School.

---

## 🔍 Project 1: Predicting Loan Default with Machine Learning

**Files:**
- `AI2_victor_jansen_final.pdf`: Project summary slides
- `ai2_VictorJansen_final.ipynb`: Full Jupyter notebook

**Overview:**
A supervised learning project to predict loan defaults using various classification models. This project includes:
- Feature engineering and data cleaning
- SMOTE balancing and model tuning
- Evaluation using confusion matrices and threshold strategies
- Practical recommendations for lending strategy

**Key takeaway:**  
Even without a huge jump in accuracy, the model helps flag high-risk loans, enabling better risk management and loan portfolio decisions.

---

## 📊 Project 2: Customer Segmentation with Unsupervised Clustering

**Files:**
- `ai2_clustering_VictorJansen.pdf`: Project summary slides
- `AI2_Clustering.ipynb`: Full Jupyter notebook

**Overview:**
This project uses RFM analysis and clustering (K-Means & Hierarchical) to segment customers based on purchasing behavior. It includes:
- Data preparation and feature engineering
- Elbow method and dendrogram to determine optimal clusters
- Cluster interpretation (VIPs, dormant, casual, loyal)
- Targeted marketing strategy for each segment

**Key takeaway:**  
Unsupervised clustering reveals clear customer segments that support actionable marketing strategies to increase engagement and revenue.

---

# 🚖 Taxi Dispatch Optimization with Predictive Modeling and Cloud Deployment

This project was developed as part of the ESADE MSc in Business Analytics program. It focuses on improving taxi dispatching and fare competitiveness using machine learning and cloud infrastructure.

## 📄 Files Included
- `Business Proposal - Group 9.pdf` – Full business and technical proposal
- `taxi_dispatch_final.ipynb` – Jupyter notebook for model development and testing
- `flask_predictions.py` – Flask API used to deploy predictions
- *(Optional: include Dockerfile, cleaned datasets if needed)*

## 📈 Project Goal
Help traditional taxi services stay competitive by:
- Predicting fares based on ride details, time, and weather
- Optimizing fleet dispatch by identifying the most profitable locations by hour

## 🧠 Machine Learning
- **Model:** Random Forest Regressor
- **Target:** Fare price
- **Features:** Distance, location, weather (temperature, pressure, wind, cloud cover), time of day, rush hour, etc.
- **Performance:**
  - RMSE: `$1.52`
  - MAE: `$0.89`
  - R²: `0.63`
  - 70.7% of predictions within ±$1

## ☁️ Cloud Deployment
- Trained model stored in AWS S3
- Served via Flask API
- Dockerized and deployed on AWS EC2
- IAM permissions used for secure S3 access

## 🚦 Business Impact
- Generated pricing predictions per hour and location across Boston districts
- Built a deployment plan that adjusts taxi availability by area and time to maximize fare-per-mile
- Enabled traditional taxi operators to reduce idle time and improve margins

## 🔁 Future Work
- Live weather API integration
- Real-time request prediction and pricing
- Fully automated dispatch optimization system

## 📍 Team
Victor Snorri Jansen & Juan Pablo García Zapparoli


