# Hospital Readmission Risk Prediction Model

**Predicting 30-Day Hospital Readmission Risk using Machine Learning on Clinical Data**

---

## Abstract

This project builds a machine learning pipeline to predict the risk of hospital readmission within 30 days using the **Diabetes 130-US Hospitals** dataset. Multiple models were developed and evaluated, with a strong emphasis on clinical interpretability using SHAP values. The best model (XGBoost) achieved a test ROC-AUC of **0.6476**, demonstrating moderate predictive power on this imbalanced clinical dataset.

## Objectives

- Perform comprehensive exploratory data analysis and preprocessing on hospital readmission data.
- Develop and compare Logistic Regression, Random Forest, and XGBoost models.
- Optimize models for imbalanced classification (readmission rate ≈ 9%).
- Provide model interpretability using SHAP for clinical trust and insights.
- Document the full reproducible workflow.

## Dataset Description

**Source**: Diabetes 130-US Hospitals for years 1999-2008 (UCI / Kaggle version)

- **Total Records**: ~70,000 (after processing)
- **Train/Test Split**: 55,997 / 14,000
- **Positive Class (Readmitted <30 days)**: ~9%
- **Features**: 31 engineered features including demographics, admission details, diagnoses, procedures, medications, lab results, and time in hospital.

## Methods

### 1. Data Preprocessing
- Extensive feature engineering
- Handling of categorical variables and missing values
- Train-test split with stratification
- Scaling (where applicable)

### 2. Exploratory Data Analysis
- Class imbalance analysis
- Feature distributions and correlations
- Risk factor identification

### 3. Model Development
- **Baseline**: Logistic Regression
- **Ensemble**: Random Forest
- **Advanced**: XGBoost with early stopping and class weighting

### 4. Interpretability
- SHAP values for global and local explanations
- Feature importance analysis

## 📈 Results & Interpretation

### Model Performance Comparison (Test Set)

| Model                  | ROC-AUC   | PR-AUC    | Accuracy | Recall (Readmitted) | Precision (Readmitted) | F1 (Readmitted) |
|------------------------|-----------|-----------|----------|---------------------|------------------------|-----------------|
| Logistic Regression   | ~0.63     | -         | -        | -                   | -                      | -               |
| Random Forest         | **0.6444**| 0.1595    | 0.81     | 0.30                | 0.17                   | 0.22            |
| **XGBoost (Best)**    | **0.6476**| **0.1764**| 0.67     | **0.52**            | 0.14                   | 0.22            |

**Key Observations**:
- XGBoost slightly outperforms other models in discrimination (ROC-AUC).
- All models struggle with the minority class due to severe imbalance (typical in readmission prediction).
- XGBoost shows better recall (0.52) for high-risk patients — important for clinical intervention.
- 5-Fold CV AUC for XGBoost: **0.6489 ± 0.0151**

**Top Predictive Features** (from SHAP and importance analysis):
- Time in hospital
- Number of diagnoses / procedures
- Specific diabetes-related complications
- Number of medications / lab procedures
- Admission type and previous visits

## Conclusions & Recommendations

- The models demonstrate reasonable predictive capability given the challenging nature of readmission prediction.
- XGBoost + SHAP provides the best balance of performance and explainability.
- Clinical utility: The system can help flag patients for enhanced discharge planning and follow-up.
- **Limitations**: Moderate AUC reflects real-world difficulty; further gains possible with richer features (e.g., vital signs, social determinants).
- **Future Work**:
  - Advanced imbalance techniques (SMOTE, focal loss)
  - Hyperparameter tuning & ensemble stacking
  - Real-time deployment as a clinical decision support tool
  - External validation on new hospital data

This project showcases the practical application of machine learning to improve hospital outcomes and reduce readmissions.

## Technologies Used

- **Languages**: Python, Jupyter Notebooks
- **Core**: Pandas, NumPy, Scikit-learn
- **Boosting**: XGBoost
- **Interpretability**: SHAP
- **Visualization**: Matplotlib, Seaborn

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Stellamarries-Syombua/redmission_model_data.git
   cd redmission_model_data
