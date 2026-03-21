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

# ------------------ NUMERIC INPUTS ------------------

age = st.number_input("Age", 0, 100, 30)
year = st.number_input("Year", 2000, 2030, 2020)

genetic_risk = st.slider("Genetic Risk", 0.0, 9.9)
air_pollution = st.slider("Air Pollution", 0.0, 9.9)
alcohol = st.slider("Alcohol Use", 0.0, 9.9)
smoking = st.slider("Smoking", 0.0, 9.9)
obesity = st.slider("Obesity Level", 0.0, 9.9)

# ------------------ PREDICTION ------------------

if st.button("Predict"):

    # ✅ CORRECT ORDER (VERY IMPORTANT)
    input_data = np.array([[
        gender,
        country,
        cancer_type,
        cancer_stage,
        age,
        year,
        genetic_risk,
        air_pollution,
        alcohol,
        smoking,
        obesity
    ]])

    prediction = model.predict(input_data)[0]

    # ------------------ OUTPUT ------------------

    if prediction > 7:
        st.error(f"High Cancer Severity ⚠️ ({prediction:.2f})")
    elif prediction > 4:
        st.warning(f"Moderate Severity ⚠️ ({prediction:.2f})")
    else:
        st.success(f"Low Severity ✅ ({prediction:.2f})")
