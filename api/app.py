from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

import os

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "..", "model.pkl")

try:
    model_data = joblib.load(model_path)
    model = model_data["model"]
    feature_columns = model_data["feature_columns"]
except Exception as e:
    print("MODEL LOAD ERROR:", str(e))
    raise e

TIPS = {
    "Sleep_Duration":         "Aim for 7–9 hours tonight. Even 30 mins more makes a real difference.",
    "Screen_Time_Before_Bed": "Put your phone down 45 mins before bed. Blue light delays melatonin.",
    "Caffeine_intake":        "Avoid caffeine after 2pm — even tea can disrupt deep sleep.",
    "Physical_Activity_Level":"A 20-minute walk today improves deep sleep significantly.",
    "Stress_Level":           "Try 4-7-8 breathing: inhale 4s, hold 7s, exhale 8s before bed."
}

def get_factor_scores(sleep, screen, caffeine, exercise, stress):
    return {
        "Sleep_Duration":         100 if 7<=sleep<=9 else (60 if sleep>=6 else 20),
        "Screen_Time_Before_Bed": max(0, int(100 - screen / 1.8)),
        "Caffeine_intake":        max(0, 100 - caffeine * 14),
        "Physical_Activity_Level":min(100, int(exercise * 0.85)),
        "Stress_Level":           max(0, 100 - stress * 10)
    }

def get_label(score):
    if score >= 80: return "Excellent"
    if score >= 60: return "Good"
    if score >= 40: return "Fair"
    return "Poor"

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({
            "error": "Model not loaded properly"
        }), 500
    data = request.get_json()
    sleep    = float(data.get("sleep_hours", 7))
    screen   = float(data.get("screen_time_mins", 60))
    caffeine = float(data.get("caffeine_cups", 2))
    exercise = float(data.get("exercise_mins", 30))
    stress   = float(data.get("stress_level", 5))

    features = np.array([[sleep, screen, caffeine, exercise, stress]])
    raw_score = model.predict(features)[0]
    score = int(np.clip(raw_score, 0, 100))

    factors = get_factor_scores(sleep, screen, caffeine, exercise, stress)
    worst = min(factors, key=factors.get)

    return jsonify({
        "score":        score,
        "label":        get_label(score),
        "worst_factor": worst,
        "tip":          TIPS[worst],
        "factors":      factors
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Sleep Scorer API is running!"})

if __name__ == "__main__":
    app.run(debug=True)