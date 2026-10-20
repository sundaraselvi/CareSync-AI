import streamlit as st
import pandas as pd
import joblib
import datetime

model = joblib.load("model/diabetes_model.pkl")
# Load the trained model
model = joblib.load("model/diabetes_model.pkl")

st.title("CareSync AI 🩺")
st.write("Your AI health companion for diabetes risk, diet, and exercise guidance")

st.header("Enter Your Health Details")

pregnancies = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose Level", 0, 300, 100)
bp = st.number_input("Blood Pressure", 0, 200, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

if st.button("Predict Risk"):
    input_data = pd.DataFrame([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]],
                               columns=["Pregnancies","Glucose","BloodPressure","SkinThickness",
                                        "Insulin","BMI","DiabetesPedigreeFunction","Age"])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High risk of Diabetes")
        st.subheader("🍎 Suggested Diet")
        st.write("- Avoid sugar, white rice, and sweets\n- Eat more leafy vegetables, whole grains\n- Prefer small, frequent meals")
        st.subheader("🏃 Suggested Exercise")
        st.write("- 30 min brisk walking daily\n- Light yoga\n- Avoid heavy exertion without doctor's advice")
    else:
        st.success("✅ Low risk of Diabetes")
        st.write("Keep maintaining a balanced diet and regular activity!")

st.header("💊 Medicine Reminder")

med_name = st.text_input("Medicine Name", placeholder="e.g. Metformin")
st.write("Set Reminder Time")
col1, col2, col3 = st.columns(3)
with col1:
    hour_12 = st.selectbox("Hour", list(range(1, 13)), index=7)
with col2:
    minute = st.selectbox("Minute", list(range(0, 60)), index=0)
with col3:
    am_pm = st.selectbox("AM/PM", ["AM", "PM"], index=1)

hour_24 = hour_12 % 12
if am_pm == "PM":
    hour_24 += 12
reminder_time = datetime.time(hour_24, minute)

import json

if st.button("Set Reminder"):
    reminder_data = {
        "medicine": med_name,
        "time": reminder_time.strftime("%H:%M")  # 24-hour format for reminder.py
    }
    with open("reminder_data.json", "w") as f:
        json.dump(reminder_data, f)

    st.success(f"✅ Reminder set for **{med_name}** at **{reminder_time.strftime('%I:%M %p')}**")
    st.info("The background reminder script will now use this time automatically.")
