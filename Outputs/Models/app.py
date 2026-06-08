import streamlit as st

st.set_page_config(
    page_title="Hospital Readmission Risk Analytics",
    page_icon="🏨",
    layout="wide"
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🏨 Hospital Readmission Risk Analytics")
st.markdown(
    "Predictive analytics pipeline identifying 30-day hospital readmission risk "
    "from structured clinical data — covering EDA, feature analysis, model "
    "comparison, threshold tuning, and SHAP explainability."
)

st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Exploratory Analysis",
    "🔧 Feature Analysis",
    "🤖 Model Performance",
    "📈 Threshold & Curves",
    "🔍 SHAP Explainability"
])

# ── Tab 1: EDA ────────────────────────────────────────────────────────────────
with tab1:
    st.subheader("Exploratory Data Analysis")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Target Class Distribution")
        st.image("Outputs/figures/target_class_distribution.png", use_column_width=True)
    with c2:
        st.markdown("#### Missing Value Rate")
        st.image("Outputs/figures/Missing_Value_Rate.png", use_column_width=True)

    st.markdown("#### Dashboard Summary")
    st.image("Outputs/figures/readmission_dashboard_summary.png", use_column_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("#### 30-Day Readmission Rate")
        st.image("Outputs/figures/Readmission_Rate.png", use_column_width=True)
    with c4:
        st.markdown("#### Readmission Rate by Age Group")
        st.image("Outputs/figures/30-Day_Readmission_Rate_by_Age_Group.png", use_column_width=True)

    c5, c6 = st.columns(2)
    with c5:
        st.markdown("#### Readmission Rate by Primary Diagnosis")
        st.image("Outputs/figures/Readmission Rate_by_Primary_Diagnosis.png", use_column_width=True)
    with c6:
        st.markdown("#### Readmission Rate by Prior Inpatient Visits")
        st.image("Outputs/figures/Readmission_Rate_by_Prior_Inpatient_Visits.png", use_column_width=True)

    st.markdown("#### Readmission Rate vs Time in Hospital")
    st.image("Outputs/figures/Readmission_Rate_vs Time_in_Hospital.png", use_column_width=True)

# ── Tab 2: Feature Analysis ───────────────────────────────────────────────────
with tab2:
    st.subheader("Feature Analysis")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Feature Correlation Matrix")
        st.image("Outputs/figures/Feature_Correlation_Matrix.png", use_column_width=True)
    with c2:
        st.markdown("#### Top 4 Features")
        st.image("Outputs/figures/Top_4_features .png", use_column_width=True)

    st.markdown("#### Random Forest Feature Importances")
    st.image("Outputs/figures/Random_Forest_Feature_Importances.png", use_column_width=True)

# ── Tab 3: Model Performance ──────────────────────────────────────────────────
with tab3:
    st.subheader("Model Performance")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Confusion Matrix")
        st.image("Outputs/figures/Confusion_Matrix.png", use_column_width=True)
    with c2:
        st.markdown("#### XGBoost Readmission Model")
        st.image("Outputs/figures/XGBoost_Readmission_Model.png", use_column_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("#### Logistic Regression")
        st.image("Outputs/figures/Logistic_Regression.png", use_column_width=True)
    with c4:
        st.markdown("#### Logistic Regression Odds Ratios")
        st.image("Outputs/figures/Logistic_Regression_Odds Ratios.png", use_column_width=True)

    st.markdown("#### Random Forest Learning Curves")
    st.image("Outputs/figures/Random_Forest_Learning_Curves.png", use_column_width=True)

# ── Tab 4: Threshold & Curves ─────────────────────────────────────────────────
with tab4:
    st.subheader("Threshold Tuning & Performance Curves")

    st.markdown("#### Precision, Recall & F1 vs Classification Threshold")
    st.image("Outputs/figures/Precision_Recall_F1_vs_Classification_Threshold.png", use_column_width=True)
    st.info(
        "Threshold tuning balances precision and recall to minimise "
        "missed readmissions while controlling false positives — "
        "critical for practical clinical deployment."
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### ROC Curve")
        st.image("Outputs/figures/ROC_Curve.png", use_column_width=True)
    with c2:
        st.markdown("#### Precision-Recall Curve")
        st.image("Outputs/figures/Precision-Recall_Curve.png", use_column_width=True)

    st.markdown("#### ROC & Precision-Recall Combined")
    st.image("Outputs/figures/ROC_Precision_Recall.png", use_column_width=True)

# ── Tab 5: SHAP ───────────────────────────────────────────────────────────────
with tab5:
    st.subheader("SHAP Explainability")
    st.markdown(
        "SHAP values reveal which features drive each individual readmission "
        "prediction — making the model interpretable for clinical teams."
    )

    st.markdown("#### Global SHAP Feature Importance")
    st.image("Outputs/figures/SHAP_Feature_Importance.png", use_column_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### SHAP Force Plot")
        st.image("Outputs/figures/Patient_Readmission_Risk_SHAP_Force_Plot.png", use_column_width=True)
    with c2:
        st.markdown("#### Individual Patient Waterfall")
        st.image("Outputs/figures/Individual_Patient_Explanation_waterfall.png", use_column_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Built by Stellamaries Syombua · "
    "Hospital Readmission Risk Analytics · "
    "Models: Logistic Regression, Random Forest, XGBoost"
)
