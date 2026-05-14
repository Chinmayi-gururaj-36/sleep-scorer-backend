# 😴 SleepScore – AI-Based Sleep Quality Prediction System

## 🌐 Live Demo

🔗 Frontend: https://sleep-score-tracker.lovable.app
🔗 Backend API: https://sleep-scorer-backend.vercel.app

SleepScore is an AI-powered web application that predicts a user's sleep quality score based on lifestyle habits such as sleep duration, screen time, caffeine intake, exercise, and stress level.

The system uses a Machine Learning model trained using Random Forest Regression and provides personalized sleep improvement recommendations.

---
## ✨ Features

- Predicts sleep quality score (0–100)
- Provides personalized recommendations
- Analyzes lifestyle factors affecting sleep
- Interactive and responsive UI
- Real-time backend API integration
- Fully deployed online

---

## 🧠 Machine Learning

### Model Used
- Random Forest Regressor

### Input Features
- Sleep Duration
- Screen Time Before Bed
- Caffeine Intake
- Physical Activity Level
- Stress Level

### Output
- Sleep Quality Score
- Sleep Quality Label
- Personalized Improvement Tip

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript
- Lovable AI

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Deployment
- Vercel (Backend)
- Lovable (Frontend)

---

## 📂 Project Structure

```bash
sleep-scorer-backend/
│
├── api/
│   └── app.py
│
├── model.pkl
├── requirements.txt
├── vercel.json
└── README.md
```

---

## ⚙️ API Endpoint

### POST /predict

Example Request:

```json
{
  "sleep_hours": 7,
  "screen_time_mins": 60,
  "caffeine_cups": 2,
  "exercise_mins": 30,
  "stress_level": 5
}
```

Example Response:

```json
{
  "score": 61,
  "label": "Good",
  "worst_factor": "Physical_Activity_Level",
  "tip": "A 20-minute walk today improves deep sleep significantly."
}
```

---

## 🎯 Problem Statement

Many people suffer from poor sleep quality due to stress, screen addiction, caffeine consumption, and unhealthy lifestyles. However, they often lack awareness of how these habits impact sleep.

This project aims to develop an AI-powered system that predicts sleep quality and provides personalized recommendations to improve sleep health.

---

## 👩‍💻 Author

Chinmayi Gururaj Chimmalagi

---
