# 💻 Laptop Price Predictor

## 📌 Project Overview
This Data Science project aims to predict the price of laptops based on their hardware specifications. It involves comprehensive data cleaning, advanced feature engineering, and the implementation of a robust Machine Learning pipeline.

## 🛠️ Data Cleaning & Feature Engineering
The dataset (`laptop_price.csv`) initially contained highly unstructured text columns. The following feature engineering steps were applied:
- **Memory Parsing:** Extracted capacities for `SSD`, `HDD`, `Flash`, and `Hybrid` drives from a single messy string.
- **CPU Information:** Parsed the raw CPU text to extract the `CPU Brand`, `CPU Category` (e.g., Core i5, Ryzen), and `Clock Speed (GHz)`.
- **Screen Resolution:** Extracted `X_res` and `Y_res`, and engineered boolean features for `IPS Panel` and `Touchscreen`.
- **Target Variable Transformation:** Applied a logarithmic transformation to `Price_euros` to handle right-skewness and improve model performance.

## 🧠 Modeling & Pipeline
To prevent data leakage and ensure production-ready code, a Scikit-Learn `Pipeline` was utilized:
- **ColumnTransformer:** Applied `OneHotEncoder` to categorical features (`Company`, `TypeName`, `OpSys`, `CPU_Brand`, `CPU_Category`, etc.) with `handle_unknown='ignore'`.
- **Algorithm:** The data was modeled using a **Random Forest Regressor** (and evaluated against other models like XGBoost and Ridge).
- **Validation:** 5-Fold Cross-Validation was implemented to ensure robust evaluation.

## 📈 Results
- **R2 Score:** ~0.865 (86.5% of variance explained)
The model successfully predicts laptop prices with high accuracy, proving that hardware specifications (specifically RAM and CPU/GPU class) are strong predictors of retail price.

## 📂 Files
- `laptop.ipynb`: The main Jupyter Notebook containing all EDA, preprocessing, and modeling code.
- `laptop_price.csv`: The raw dataset used for this project.

## 🚀 How to Run
1. Clone the repository.
2. Install the required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`).
3. Open and run `laptop.ipynb` in Jupyter Notebook or JupyterLab.
