# Used Car Price Prediction (Mercedes-Benz) 🚗

A machine learning project that predicts the price of used Mercedes-Benz vehicles using a regression model. This repository contains the full workflow from data cleaning and exploratory data analysis (EDA) to feature engineering and model comparison.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-red)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-purple)
![Model](https://img.shields.io/badge/Model-Random%20Forest-brightgreen)
![R² Score](https://img.shields.io/badge/R²%20Score-94.4%25-green)
![RMSE](https://img.shields.io/badge/RMSE-%242,948-green)

---

## 🧭 Table of Contents
- [Project Objective](#project-objective)
- [The Dataset](#the-dataset)
- [Project Workflow](#project-workflow)
  - [1. Exploratory Data Analysis (EDA)](#1-exploratory-data-analysis-eda-)
  - [2. Feature Engineering](#2-feature-engineering-)
  - [3. Modeling & Results](#3-modeling--results-)
- [Conclusion](#conclusion)
- [How to Run This Project](#how-to-run-this-project-)

---

## 🎯 Project Objective

The core objective of this analysis is to develop a reliable regression model that can accurately predict the price of a used Mercedes-Benz vehicle based on its key features, such as `year`, `mileage`, `fuelType`, `engineSize`, and `transmission`.

---

## 💾 The Dataset

The dataset contains information on 13,119 used Mercedes-Benz vehicles. The key features are:

* **model:** The model of the car (e.g., C Class, SLK)
* **year:** The registration year
* **price:** The price in Euros (Our **Target Variable**)
* **transmission:** The gearbox type (Automatic, Manual, etc.)
* **mileage:** The distance driven
* **fuelType:** The engine's fuel type (Petrol, Diesel, Hybrid)
* **tax:** Road tax
* **mpg:** Miles Per Gallon
* **engineSize:** The engine's size in litres

A preliminary check (`df.info()`) confirmed the dataset is **100% complete**, with no missing or null values, allowing us to proceed directly to analysis.

---

## 🚀 Project Workflow

### 1. Exploratory Data Analysis (EDA) 📊

Before modeling, I investigated the relationships between the features and the target variable, `price`. This revealed complex, non-linear patterns that a simple model would miss.

<details>
<summary><strong>Click to see Key EDA Findings</strong></summary>

* 📈 **Price vs. Year:** A fascinating non-linear relationship. It shows a **"vintage premium"** for cars from the 1970s and the expected depreciation/appreciation for modern cars. A simple straight line cannot capture this.
* 📉 **Price vs. Mileage:** A clear and strong **negative correlation**. As mileage increases, the price predictably decreases.
* 🏎️ **Price vs. Engine Size:** A general positive trend (bigger engines = more expensive) but with high variance. This suggests the `model` or `year` strongly influences this feature's impact on price.
* ⛽ **Price vs. MPG:** A counter-intuitive but critical insight. The **highest-priced vehicles are concentrated in the 0-50 MPG range**. This indicates a significant luxury/performance segment where power and features are the dominant price drivers, not fuel efficiency.

</details>

### 2. Feature Engineering ⚙️

To prepare the data for modeling, all non-numeric categorical features (`model`, `transmission`, `fuelType`) were converted into a machine-readable format using **One-Hot Encoding** (`pd.get_dummies`).

To prevent creating too many columns, the `model` feature was processed to keep only the **Top 10 most frequent models**, with all others grouped into a single "Other" category.

### 3. Modeling & Results 🏆

An 80/20 train-test split was used. I first established a baseline with `LinearRegression` and then trained a more complex `RandomForestRegressor` to capture the non-linearities discovered in the EDA.

#### **Baseline Model: `LinearRegression`**
* **Why:** To see how well a simple, fast model performs.
* **Preprocessing:** `StandardScaler` was applied, as linear models are sensitive to feature scales.
* **Results:**
    * **R² Score:** 0.721 (72.1%)
    * **Root Mean Square Error (RMSE):** $6,601.85
* **Analysis:** A moderate score, but 28% of the price variance is unexplained. The $6,601 average error is too high for a reliable predictor. This confirms the model is struggling with the non-linear data.

#### **Final Model: `RandomForestRegressor`**
* **Why:** This ensemble method excels at capturing complex, non-linear patterns and feature interactions without needing feature scaling.
* **Hyperparameters:** `n_estimators=100`
* **Results:**
    * **R² Score:** **0.944 (94.4%)**
    * **Root Mean Square Error (RMSE):** **$2,948.20**
* **Analysis:** A massive performance uplift! The R² score shows the model now explains over 94% of the price variance. Most importantly, the **average prediction error (RMSE) was cut by more than 55%** compared to the baseline.

---

## 🏁 Conclusion

We have successfully developed a reliable pricing model. The `RandomForestRegressor` is far better suited for this task, as it effectively captures the complex, real-world relationships (like the "vintage premium" for `year` and the "luxury segment" for `mpg`) that the simple linear model could not.

The final model can predict a used Mercedes-Benz's price with an **average error margin of approximately ±$2,948**, making it a robust and accurate tool for this dataset.

---

## 🛠️ How to Run This Project

<details>
<summary><strong>Click to see setup and run instructions</strong></summary>

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```
    *(Or, if you have a `requirements.txt` file: `pip install -r requirements.txt`)*

4.  **Get the data:**
    You will need the `merc_mini_proj_2.csv` file. Add it to the root directory of the project.

5.  **Run the analysis:**
    Open and run the Jupyter Notebook (`.ipynb`) or Python script (`.py`) file included in this repository.
</details>
