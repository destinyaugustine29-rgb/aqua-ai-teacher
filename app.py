import streamlit as st
from google import genai

st.title("Aqua AI Math Teacher 🌊")
st.write("Your personal math teacher that speaks any language!")

# This looks for the name you saved in the Streamlit Secrets box
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

name = st.text_input("What's your name?")
language = st.selectbox("What language?", ["English", "French", "Spanish", "Pidgin", "Chinese", "Yoruba"])
question = st.text_input("Ask Aqua any maths question:")

if st.button("Ask Aqua 🌊"):
    if question:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents="You are Aqua, friendly maths teacher. Answer in " + language + ": " + question
        )
        st.write("**Aqua:** " + response.text)
