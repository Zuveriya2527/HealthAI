import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 HealthAI - User Login")

# Simulated user credentials (later can connect to DB)
USER_CREDENTIALS = {
    "riya@example.com": "riya123",
    "admin@healthai.com": "admin"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_profile = {}

if not st.session_state.logged_in:
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if email in USER_CREDENTIALS and USER_CREDENTIALS[email] == password:
            st.session_state.logged_in = True
            st.session_state.user_profile["email"] = email
            st.success("✅ Logged in successfully!")
            st.rerun()
        else:
            st.error("❌ Invalid credentials")
else:
    st.sidebar.success(f"👤 Welcome, {st.session_state.user_profile.get('email')}")

    # Profile form
    with st.form("profile_form"):
        name = st.text_input("Full Name", value=st.session_state.user_profile.get("name", ""))
        age = st.number_input("Age", 1, 120, value=st.session_state.user_profile.get("age", 25))
        gender = st.selectbox("Gender", ["Female", "Male", "Other"], index=0)
        submit = st.form_submit_button("Save Profile")

        if submit:
            st.session_state.user_profile.update({
                "name": name,
                "age": age,
                "gender": gender
            })
            st.success("🧾 Profile updated!")
