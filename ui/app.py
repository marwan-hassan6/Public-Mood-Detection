# ui/app.py

import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.set_page_config(
    page_title="Public Mood Detection",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Powered Sentiment Analysis")
st.write(
    "Enter a sentence and the AI model will detect the sentiment."
)

# Text input
user_text = st.text_area(
    "Enter your text:",
    height=150
)

if st.button("Analyze Sentiment"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        with st.spinner("Analyzing sentiment..."):

            payload = {
                "text": user_text
            }

            response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()

            sentiment = result["sentiment"]
            confidence = result["confidence"]

            # Emoji
            if sentiment == "positive":
                emoji = "😊"
            elif sentiment == "negative":
                emoji = "😠"
            else:
                emoji = "😐"

            st.success(
                f"{emoji} Sentiment: {sentiment.upper()} "
                f"({confidence*100:.1f}% confidence)"
            )

            st.write("### Probabilities")

            for label, prob in result["probabilities"].items():

                st.write(f"**{label}**")

                st.progress(prob)

        else:
            st.error("API request failed.")

# Sidebar
with st.sidebar:

    st.header("About")

    st.write(
        "This project uses a Transformer-based BERT model "
        "for sentiment analysis and public mood detection."
    )

    st.write(
        "Built with HuggingFace Transformers, FastAPI, "
        "PyTorch, and Streamlit."
    )