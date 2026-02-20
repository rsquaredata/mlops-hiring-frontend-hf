import streamlit as st
import requests

API_URL = "https://rsquaredata-mlops-hiring-backend.hf.space/predict"

st.title("Hiring Probability Predictor")

age = st.number_input("Age", 18, 70, 30)
gender = st.selectbox("Gender", [0, 1])
education = st.selectbox("Education Level", [1, 2, 3, 4])
experience = st.number_input("Experience Years", 0, 40, 5)
previous = st.number_input("Previous Companies", 0, 20, 1)
distance = st.number_input("Distance From Company", 0.0, 100.0, 10.0)
interview = st.slider("Interview Score", 0, 100, 50)
skill = st.slider("Skill Score", 0, 100, 50)
personality = st.slider("Personality Score", 0, 100, 50)
strategy = st.selectbox("Recruitment Strategy", [1, 2, 3])

if st.button("Predict"):
    payload = {
        "Age": age,
        "Gender": gender,
        "EducationLevel": education,
        "ExperienceYears": experience,
        "PreviousCompanies": previous,
        "DistanceFromCompany": distance,
        "InterviewScore": interview,
        "SkillScore": skill,
        "PersonalityScore": personality,
        "RecruitmentStrategy": strategy
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            probability = response.json()["hiring_probability"]
            st.success(f"Hiring Probability: {probability}")
        else:
            st.error("Backend error.")
    except Exception:
        st.error("Cannot reach backend.")
