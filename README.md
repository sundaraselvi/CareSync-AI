# CareSync AI 🩺

An offline AI health companion for elderly users. It predicts diabetes risk,
suggests diet and exercise, and sends medicine reminders.

**Tagline:** Predict. Remind. Care.

## Features
- Diabetes risk prediction (Logistic Regression, about 77% accuracy on the Pima Indians dataset)
- Diet and exercise suggestions based on the predicted risk
- Medicine reminder with an easy Hour / Minute / AM-PM picker
- Background popup notifications that work even when the browser is closed
- Runs fully offline after the one-time setup

## Tech Stack
Python, pandas, scikit-learn, Streamlit, schedule, plyer, joblib

## Setup
```
pip install -r requirements.txt
```

## How to Run
Open two terminals in the project folder.

Terminal 1 (main app):
```
streamlit run app.py
```

Terminal 2 (background reminders):
```
python reminder.py
```

## Retrain the Model (optional)
```
python train_model.py
```

## Dataset
Pima Indians Diabetes Dataset (Kaggle), saved as data/diabetes.csv.

## Disclaimer
This is a student project for learning and demonstration. It is not a medical
device and does not replace advice from a doctor.
