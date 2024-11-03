import streamlit as st

st.title("Registration Page")

if 'registered' not in st.session_state:
    st.session_state['registered'] = False

if not st.session_state['registered']:
    st.subheader("Create an account")

    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")
    password_confirm = st.text_input("Confirm Password", type="password", key="password_confirm_input")
    
    if st.button("Register", key="register_button"):
        if password == password_confirm and len(password) > 5:
            st.session_state['registered'] = True
        else:
            st.error("Passwords do not match or are too short (must be over 5 characters).", key="error_message")
else:
    st.success("Successfully registered", key="success_message")