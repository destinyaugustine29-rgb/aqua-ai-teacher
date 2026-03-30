import streamlit as st
from google import genai

st.title("Aqua AI Math Teacher 🌊")
st.write("Your personal math teacher that speaks any language!")

# Initialize Client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# User Inputs
name = st.text_input("What's your name?")
language = st.selectbox("What language?", ["English", "French", "Spanish", "Pidgin", "Chinese", "Yoruba"])
question = st.text_input("Ask Aqua any maths question:")

if st.button("Ask Aqua 🌊"):
    if question:
        try:
            # Using the correct model path and f-string for the new SDK
            response = client.models.generate_content(
                model="models/gemini-1.5-flash",
                contents=f"You are Aqua, a friendly maths teacher. Answer in {language}: {question}"
            )
            st.write(f"**Aqua:** {response.text}")
        except Exception as e:
            st.error(f"The API had a problem: {e}")
    else:
        st.warning("Please enter a question first!")
