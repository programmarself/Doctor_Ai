import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv("API_KEY")

def chatbot():
    st.title("Medication Chatbot")
    st.write("Ask me about symptoms, medications, or health conditions.")

    user_input = st.text_input("You: ")
    if user_input:
        if api_key:
            # Configure OpenAI API with the key
            openai.api_key = api_key
            try:
                response = openai.Completion.create(
                    engine="davinci-codex",
                    prompt=user_input,
                    max_tokens=50
                )
                st.write(f"Bot: {response.choices[0].text.strip()}")
            except Exception as e:
                st.write(f"Error: {e}")
        else:
            st.write("API key is not set.")
