# Toxic Triage API

> A low-latency text classification API built with FastAPI and PyTorch for real-time automated moderation.

## 📌 Project Overview

The Toxic Triage API provides a scalable inference engine for text moderation. At its core is a fine-tuned **DistilBERT** model optimized for computational efficiency. By analyzing the corpus token distribution and truncating sequence lengths to the 95th percentile (256 tokens), the data pipeline significantly reduces wasted compute on padding during both training and inference. 

Currently, the model serves as a robust baseline. Initial training was constrained by hardware to a highly imbalanced sample of 1,000 records, establishing a foundational architecture ready for future data ingestion and threshold tuning.

---

## 📊 Model Performance

Despite hardware constraints and severe class imbalance in the training sample, the initial model demonstrates strong overall discriminatory ability:

* **ROC-AUC:** `0.93` (Strong overall class separation)
* **F1 Score:** `0.23` (Reflects the precision-recall tradeoff inherent to highly imbalanced moderation data)
* **Qualitative Assessment:** Spot-checking of the deployed API demonstrates robust baseline performance for real-time triage.

---

## 🗂️ Project Structure

The codebase is organized to separate data exploration, model training, and API deployment logic:

```text
toxic_triage_api/
├── data/
│   └── train.csv            # Directory for raw/processed CSVs 
├── notebooks/
│   ├── execution.ipynb      # Execution starts here (training, testing, API)
│   └── eda.ipynb            # Notebook for EDA and sequence length analysis
├── src/
│   ├── __init__.py
│   ├── config.py            # Centralized static variables (paths, model names, hyperparams)
│   ├── data_loader.py       # PyTorch Dataset and DataLoader classes
│   ├── model.py             # OOP wrapper for DistilBERT
│   ├── train.py             # The training and validation engine
│   └── evaluate.py          # Logic for processing a single string into a prediction
├── app/
│   ├── __init__.py
│   └── api.py               # FastAPI application and endpoints
├── requirements.txt
└── README.md