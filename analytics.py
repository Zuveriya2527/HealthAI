import streamlit as st
import pandas as pd
import plotly.express as px
from utils.watson_api import ask_granite

st.set_page_config(layout="wide")
st.title("📊 Health Analytics Dashboard")

# Sample Data Generation (replace with real data)
data = pd.DataFrame({
    "Date": pd.date_range(start="2024-06-01", periods=7),
    "Heart Rate": [72, 75, 80, 77, 76, 74, 73],
    "Systolic BP": [120, 122, 124, 121, 119, 123, 122],
    "Diastolic BP": [80, 82, 81, 79, 78, 83, 80],
    "Blood Glucose": [95, 100, 110, 105, 108, 102, 98]
})

# Layout with metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("❤️ Heart Rate (BPM)", "73", "+1")

with col2:
    st.metric("🩸 Systolic BP", "122", "+2")

with col3:
    st.metric("🍬 Glucose Level", "98", "-4")

st.markdown("---")

# Trend Line Charts
st.subheader("📈 Health Trends")

# Heart Rate Trend
fig1 = px.line(data, x="Date", y="Heart Rate", title="Heart Rate Over Time")
st.plotly_chart(fig1, use_container_width=True)

# Blood Pressure Trend
fig2 = px.line(data, x="Date", y=["Systolic BP", "Diastolic BP"], title="Blood Pressure Trend")
st.plotly_chart(fig2, use_container_width=True)

# Blood Glucose Trend
fig3 = px.line(data, x="Date", y="Blood Glucose", title="Blood Glucose Trend")
fig3.add_hline(y=100, line_dash="dot", annotation_text="Normal Range", line_color="green")
st.plotly_chart(fig3, use_container_width=True)

# AI Insights
st.markdown("---")
st.subheader("🧠 AI Insights")

prompt = (
    f"Analyze the following health trends:\n"
    f"Heart Rate: {data['Heart Rate'].tolist()}\n"
    f"Systolic BP: {data['Systolic BP'].tolist()}\n"
    f"Blood Glucose: {data['Blood Glucose'].tolist()}\n"
    f"Provide summary and suggest any possible health risks or improvements."
)

ai_insight = ask_granite(prompt)
st.success("🩺 Insight Summary")
st.write(ai_insight)
