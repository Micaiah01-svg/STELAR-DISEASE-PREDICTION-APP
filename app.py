import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# Get the folder where app.py is located
BASE_DIR = Path(__file__).resolve().parent

# Build paths relative to app.py
model_path = BASE_DIR / "disease_model.pkl"
encoder_path = BASE_DIR / "symptom_encoder.pkl"

# Debug info
st.write("Model exists:", model_path.exists())
st.write("Encoder exists:", encoder_path.exists())

# Stop early if files are missing
if not model_path.exists():
    st.error("disease_model.pkl was not found in the app folder.")
    st.stop()

if not encoder_path.exists():
    st.error("symptom_encoder.pkl was not found in the app folder.")
    st.stop()

# Load files
model = joblib.load(model_path)
mlb = joblib.load(encoder_path)

# App UI
st.title("STELAR Disease Prediction App")
st.write("Select the symptoms you are experiencing, then click the button to predict the possible disease.")

st.warning(
    "Disclaimer: This is a school/demo-style app, not a real medical diagnosis system. "
    "The prediction is based only on dataset patterns and should not be treated as medical advice."
)

all_symptoms = sorted(list(mlb.classes_))
selected_symptoms = st.multiselect("Choose your symptoms:", all_symptoms)

if st.button("Predict Disease"):
    if selected_symptoms:
        input_data = mlb.transform([selected_symptoms])

        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        results = pd.DataFrame({
            "Disease": model.classes_,
            "Probability": probabilities
        }).sort_values(by="Probability", ascending=False).head(3)

        results["Probability"] = (results["Probability"] * 100).round(2).astype(str) + "%"

        st.success(f"Most Likely Disease: {prediction}")
        st.write("Top 3 Predictions:")
        st.dataframe(results, use_container_width=True, hide_index=True)
    else:
        st.warning("Please select at least one symptom.")