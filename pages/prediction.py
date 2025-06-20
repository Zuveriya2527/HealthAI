import streamlit as st
from utils.watson_api import ask_granite

# Sample rule-based prediction logic
def predict_disease(symptoms):
    symptoms = [s.lower() for s in symptoms]
    
    if "fever" in symptoms and "fatigue" in symptoms:
        return "Flu", "Rest well, stay hydrated, and consult a doctor if it persists."
    elif "headache" in symptoms and "nausea" in symptoms:
        return "Migraine", "Avoid light, rest, and consider over-the-counter pain relief."
    elif "cough" in symptoms and "sore throat" in symptoms:
        return "Common Cold", "Gargle warm salt water, rest, and monitor symptoms."
    else:
        return "Unknown", "Please consult a physician or re-check symptoms."

# Streamlit page
st.title("🧠 Disease Prediction")
st.write("Select the symptoms you're experiencing:")

# Symptom input
symptom_options = [
    "Fever", "Fatigue", "Headache", "Nausea", "Cough",
    "Sore Throat", "Body Ache", "Chills", "Dizziness", "Shortness of Breath"
]

selected_symptoms = st.multiselect("Symptoms", symptom_options)

if st.button("Predict Condition"):
    if selected_symptoms:
        condition, advice = predict_disease(selected_symptoms)

        # Optional: Ask Granite for confirmation
        prompt = f"Given these symptoms: {', '.join(selected_symptoms)} — what possible condition might the user have?"
        ai_response = ask_granite(prompt)

        st.success(f"🩺 **Predicted Condition:** {condition}")
        st.info(f"📋 **Advice:** {advice}")
        st.markdown("---")
        st.markdown("🧠 **AI says:**")
        st.write(ai_response)
