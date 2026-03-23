import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Cancer Severity Prediction 🔬")
st.write("Predict cancer severity based on patient data.")

st.header("Enter Patient Details")

# ------------------ MAPPINGS ------------------

# Gender
gender_map = {"Female": 0, "Male": 1}
gender = gender_map[st.selectbox("Gender", gender_map.keys())]

# Country (UPDATED)
country_map = {
    "UK": 0,
    "China": 1,
    "Pakistan": 2,
    "Brazil": 3,
    "USA": 4
}
country = country_map[st.selectbox("Country", country_map.keys())]

# Cancer Type (UPDATED)
cancer_type_map = {
    "Lung": 0,
    "Leukemia": 1,
    "Breast": 2,
    "Colon": 3,
    "Skin": 4,
    "Liver": 5
}
cancer_type = cancer_type_map[st.selectbox("Cancer Type", cancer_type_map.keys())]

# Cancer Stage (UPDATED)
cancer_stage_map = {
    "Stage 0": 0,
    "Stage I": 1,
    "Stage II": 2,
    "Stage III": 3,
    "Stage IV": 4
}
cancer_stage = cancer_stage_map[st.selectbox("Cancer Stage", cancer_stage_map.keys())]

# ------------------ NUMERIC INPUTS ------------------

age = st.number_input("Age", 0, 100)
year = st.number_input("Year", 2015, 2024)

# IMPORTANT FIX (0–10 range)
genetic_risk = st.slider("Genetic Risk", 0.0, 10.0)
air_pollution = st.slider("Air Pollution", 0.0, 10.0)
alcohol = st.slider("Alcohol Use", 0.0, 10.0)
smoking = st.slider("Smoking", 0.0, 10.0)
obesity = st.slider("Obesity Level", 0.0, 10.0)

# ------------------ PREDICTION ------------------

if st.button("Predict"):
    
    input_data = np.array([[age, gender, country, year,
                            genetic_risk, air_pollution, alcohol,
                            smoking, obesity, cancer_type,
                            cancer_stage]])
    
    prediction = model.predict(input_data)[0]
    
    if prediction > 7:
        st.error(f"High Cancer Severity ⚠️ ({prediction:.2f})")
    elif prediction > 4:
        st.warning(f"Moderate Severity ⚠️ ({prediction:.2f})")
    else:
        st.success(f"Low Severity ✅ ({prediction:.2f})")

# redeploy trigger
