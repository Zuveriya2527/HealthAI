import streamlit as st
from utils.watson_api import ask_granite

st.title("💊 Treatment Plan Generator")
st.write("Get a personalized treatment plan based on your condition.")

# Input section
condition = st.text_input("🔍 Enter your diagnosed condition")
age = st.number_input("🎂 Age", min_value=1, max_value=120, step=1)
weight = st.number_input("⚖️ Weight (kg)", min_value=1)
existing_conditions = st.text_input("📝 Existing health issues (e.g., Diabetes, Asthma)")
allergies = st.text_input("⚠️ Allergies (e.g., Penicillin, Pollen)")

# Submit
if st.button("Generate Treatment Plan"):
    if condition and age and weight:
        prompt = (
            f"A {age}-year-old patient weighing {weight} kg has been diagnosed with {condition}. "
            f"They have the following existing conditions: {existing_conditions}. "
            f"Known allergies: {allergies}. "
            "Generate a personalized treatment plan that includes medication suggestions, lifestyle changes, and follow-up recommendations."
        )

        response = ask_granite(prompt)

        # Display output
        st.success("🧠 AI-Generated Treatment Plan")
        st.markdown("```\n" + response + "\n```")
    else:
        st.warning("Please fill in all required fields.")
