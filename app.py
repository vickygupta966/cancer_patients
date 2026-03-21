import streamlit as st
import pickle
import numpy as np
import gdown
import os

# ---------------- LOAD MODEL ----------------

url = "https://drive.google.com/uc?id=1Fk0c55IjpeVL9-6cF_vs-ZAmPiJ2Z8tr"

if not os.path.exists("model.pkl"):
    gdown.download(url, "model.pkl", quiet=False)

model = pickle.load(open("model.pkl", "rb"))

# ---------------- UI ----------------

st.title("Cancer Severity Prediction 🩺")
st.write("Predict cancer severity based on patient data.")

st.header("Enter Patient Details")

# ---------------- MAPPINGS ----------------

# Gender
gender_map = {"Female": 0, "Male": 1}
gender_input = st.selectbox("Gender", list(gender_map.keys()))
gender = gender_map[gender_input]

# Country
country_map = {"India": 0, "USA": 1, "UK": 2}
country_input = st.selectbox("Country", list(country_map.keys()))
country = country_map[country_input]

# Cancer Type
cancer_type_map = {
    "Breast Cancer": 0,
    "Lung Cancer": 1,
    "Skin Cancer": 2
}
cancer_type_input = st.selectbox("Cancer Type", list(cancer_type_map.keys()))
cancer_type = cancer_type_map[cancer_type_input]

# Cancer Stage
cancer_stage_map = {
    "Stage I": 0,
    "Stage II": 1,
    "Stage III": 2,
    "Stage IV": 3
}
cancer_stage_input = st.selectbox("Cancer Stage", list(cancer_stage_map.keys()))
cancer_stage = cancer_stage_map[cancer_stage_input]

# ---------------- NUMERIC INPUTS ----------------

age = st.number_input("Age", 0, 100)
year = st.number_input("Year", 2000, 2030)

genetic_risk = st.slider("Genetic Risk", 0.0, 9.9)
air_pollution = st.slider("Air Pollution", 0.0, 9.9)
alcohol = st.slider("Alcohol Use", 0.0, 9.9)
smoking = st.slider("Smoking", 0.0, 9.9)
obesity = st.slider("Obesity Level", 0.0, 9.9)

# ---------------- PREDICTION ----------------

if st.button("Predict"):
    
    input_data = np.array([[age, gender, country, year,
                            genetic_risk, air_pollution, alcohol,
                            smoking, obesity, cancer_type, cancer_stage]])

    prediction = model.predict(input_data)[0]

    # ---------------- SMART OUTPUT ----------------
    if prediction > 7:
        st.error(f"High Severity ⚠️ (Score: {round(prediction,2)})")
    elif prediction > 4:
        st.warning(f"Moderate Severity ⚡ (Score: {round(prediction,2)})")
    else:
        st.success(f"Low Severity ✅ (Score: {round(prediction,2)})")
