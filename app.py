import streamlit as st
from utils.watson_api import ask_granite

st.set_page_config(page_title="HealthAI", page_icon="🩺", layout="wide")
st.title("🩺 HealthAI - Patient Chat Assistant")

# Initialize chat history in session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
st.subheader("💬 Ask your health question")
user_input = st.text_input("Enter your query:", key="chat_input")

if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append(("🧑‍⚕️ You", user_input))

        # Call Granite model
        ai_reply = ask_granite(f"Answer medically: {user_input}")
        st.session_state.chat_history.append(("🤖 HealthAI", ai_reply))

# Display chat history
st.subheader("📜 Chat History")
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)
