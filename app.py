import streamlit as st
import joblib
import pandas as pd
import os

SAVE_DIR = r"c:\Users\Micaiah's PC\Downloads\disease_app"

model_path = os.path.join(SAVE_DIR, "disease_model.pkl")
encoder_path = os.path.join(SAVE_DIR, "symptom_encoder.pkl")

st.write("Model exists:", os.path.exists(model_path))
st.write("Encoder exists:", os.path.exists(encoder_path))

model = joblib.load(model_path)
mlb = joblib.load(encoder_path)

st.title("STELAR Disease Prediction App")
st.write("Select the symptoms you are experiencing, then click the button to predict the possible disease.")

st.warning(
    "Disclaimer: This is a school/demo-style app, not a real medical diagnosis system. "
    "The prediction is based only on dataset patterns and should not be treated as medical advice."
)

all_symptoms = list(mlb.classes_)
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

        st.success(f"Most Likely Disease: {prediction}")
        st.write("Top 3 Predictions:")
        st.dataframe(results)
    else:
        st.warning("Please select at least one symptom.")