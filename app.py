import streamlit as st
from google import genai

st.title("Aqua AI Math Teacher 🌊")
st.write("Your personal math teacher!")

# 1. Initialize with the secret key
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# 2. Setup inputs
language = st.selectbox("Language", ["English", "French", "Pidgin", "Spanish"])
question = st.text_input("Ask a math question:")

if st.button("Ask Aqua 🌊"):
    if question:
        try:
            # TRUTH: You MUST include 'models/' and use 1.5 to bypass your 2.0 quota limit
            response = client.models.generate_content(
                model="models/gemini-1.5-flash", 
                contents=f"You are Aqua, a math teacher. Answer in {language}: {question}"
            )
            st.write(f"**Aqua:** {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please type a question.")
