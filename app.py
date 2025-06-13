import streamlit as st

# Title of the app
st.title("📈 Welcome to My First Streamlit App")

# Sidebar input
user_name = st.sidebar.text_input("Enter your name:")

# Display message
if user_name:
    st.success(f"Hello, {user_name}! 🎉 This is your first Streamlit web app.")

# Sample chart
st.subheader("Sample Data Visualization")
st.line_chart({"Data": [10, 20, 15, 30, 45, 35]})
