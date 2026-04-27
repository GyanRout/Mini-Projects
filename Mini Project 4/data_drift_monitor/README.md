# 🚀 Automated Data Drift Detector

## 📌 Overview
Machine learning models often fail silently in production not because the code breaks, but because the data changes. This project is an **Automated MLOps Utility** designed to act as a tripwire for data drift. It automatically compares a reference dataset (the data the model was trained on) against live incoming data batches and mathematically calculates distribution shifts.

## ⚠️ The Problem
Once a model is deployed, the real world keeps evolving. Consumer behavior changes, sensor calibrations drift, and macroeconomic factors shift. This phenomenon, known as **Data Drift**, degrades model performance over time without throwing explicit code errors. 

## 💡 The Solution
This project provides a Python-based engine that acts as an automated tripwire. It detects data drift by applying robust statistical tests to compare the baseline (training) dataset against new data:
* **Continuous Data:** Kolmogorov-Smirnov (K-S) Test
* **Categorical Data:** Population Stability Index (PSI) / Jensen-Shannon Divergence (JSD)

If the calculated drift breaches a predefined threshold, the system automatically triggers a retraining alert, ensuring the model remains accurate and reliable.

## 🛠️ Key Features
* **Automated Monitoring:** Continuously compares live data batches against reference data.
* **Statistical Rigor:** Uses industry-standard mathematical tests (K-S, PSI, JSD) to quantify drift.
* **Alerting Mechanism:** Triggers actionable alerts (e.g., Webhooks, Email, or log flags) for model retraining when thresholds are exceeded.
* **Extensible:** Easily integrable into broader MLOps pipelines (e.g., Airflow, MLflow).

## 🧠 What I Learned Building This
Building this utility provided hands-on experience bridging the gap between theoretical data science and practical MLOps:
1.  **Practical Data Drift:** Transitioned from understanding drift as a concept to mathematically detecting it in live pipelines.
2.  **Statistical Testing:** Gained practical implementation skills using K-S tests, PSI, and JSD to measure distribution shifts.
3.  **MLOps Fundamentals:** Learned how to build automated, production-ready tripwires that ensure models remain reliable post-deployment.
