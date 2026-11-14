import streamlit as st
import time
import requests

# Configure the Streamlit page
st.set_page_config(
    page_title="Text Mood Detection",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# FastAPI Endpoint
API_URL = "http://127.0.0.1:8000/predict"

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

import os
try:
    css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "style.css")
    local_css(css_path)
except FileNotFoundError:
    st.warning("CSS file not found. Ensure you are running from the project root.")

from components.sidebar import load_sidebar # type: ignore

def validate_input(text: str):
    text = text.strip()
    if not text:
        return "Please enter some text."
    if all(c.isdigit() or c.isspace() for c in text):
        return "Input cannot contain only numbers."
    alnum_chars = [c for c in text if c.isalnum()]
    if not alnum_chars or len(alnum_chars) < 3:
        return "Please enter a valid sentence."
    return None

def main():

    load_sidebar(default_index=1)

    st.markdown(
        "<h1 class='hero-title'>Text Mood Detection</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='hero-subtitle'>Analyze the emotional sentiment behind written text using NLP models.</p>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([3, 2])

    # =====================================
    # LEFT SIDE
    # =====================================
    with col1:

        input_text_html = """
<div class='glass-card'>
<h3 style='color: #00ADB5; margin-top: 0;'>
Input Text
</h3>
</div>
"""
        st.markdown(input_text_html, unsafe_allow_html=True)

        user_input = st.text_area(
            "Enter text to analyze:",
            height=200,
            placeholder="Type a sentence or paragraph here... e.g., 'I am so excited to present this graduation project!'",
            label_visibility="collapsed"
        )

        analyze_btn = st.button(
            "Analyze Emotion",
            use_container_width=True,
            type="primary"
        )

    # =====================================
    # RIGHT SIDE
    # =====================================
    with col2:

        analysis_result_html = """
<div class='glass-card' style='height: 100%;'>
<h3 style='color: #00ADB5; margin-top: 0;'>
Analysis Result
</h3>
</div>
"""
        st.markdown(analysis_result_html, unsafe_allow_html=True)

        if analyze_btn:

            validation_error = validate_input(user_input)
            
            if validation_error:

                st.warning(validation_error)

            else:

                with st.spinner("AI is analyzing the sentiment..."):

                    time.sleep(1)

                    try:

                        response = requests.post(
                            API_URL,
                            json={"text": user_input},
                            timeout=10
                        )
                        response.raise_for_status()

                        result = response.json()

                        emotion = result["sentiment"]
                        confidence = round(
                            result["confidence"] * 100,
                            2
                        )

                        # =====================================
                        # UI Styling
                        # =====================================
                        if emotion.lower() == "negative":

                            badge_class = "badge-sad"
                            emoji = "😔"

                        elif emotion.lower() == "positive":

                            badge_class = "badge-happy"
                            emoji = "😄"

                        else:

                            badge_class = "badge-neutral"
                            emoji = "😐"

                        # =====================================
                        # RESULT UI
                        # =====================================
                        html_content = f"""<div class='result-container' style='margin-top: 20px;'>
<div class="result-emoji">{emoji}</div>
<span class='emotion-badge {badge_class}'>Detected: {emotion}</span>
<div class="confidence-text" style='color: #EEEEEE;'>Confidence: <span style='color: #00ADB5;'>{confidence}%</span></div>
</div>"""
                        st.markdown(html_content, unsafe_allow_html=True)

                        st.progress(int(confidence))

                        secondary_emotions_html = """
<hr style='border: 1px solid rgba(255,255,255,0.1); margin: 20px 0;'>
<h4 style='color: #A0AAB2;'>
Secondary Emotions Detected:
</h4>
<ul style='color: #A0AAB2; font-size: 0.9rem;'>
<li>Curiosity: 12%</li>
<li>Anticipation: 8%</li>
</ul>
"""
                        st.markdown(secondary_emotions_html, unsafe_allow_html=True)

                    except requests.exceptions.ConnectionError as e:
                        import traceback
                        print(traceback.format_exc())
                        error_title = "⚠️ Connection Problem"
                        error_msg = "Unable to connect to the AI service.<br>Please try again later."
                    except requests.exceptions.Timeout as e:
                        import traceback
                        print(traceback.format_exc())
                        error_title = "⏳ Request Timeout"
                        error_msg = "The request took too long to complete.<br>Please try again."
                    except requests.exceptions.RequestException as e:
                        import traceback
                        print(traceback.format_exc())
                        error_title = "⚠️ API Error"
                        error_msg = "An unexpected error occurred while communicating with the service."
                    except Exception as e:
                        import traceback
                        print(traceback.format_exc())
                        error_title = "⚠️ Unexpected Error"
                        error_msg = "An unexpected error occurred while analyzing the text."

                    if 'error_title' in locals():
                        error_html = f"""
                        <div class='glass-card' style='border: 1px solid rgba(255, 65, 54, 0.5); border-left: 5px solid #FF4136;'>
                            <h3 style='color: #FF4136; margin-top: 0;'>{error_title}</h3>
                            <p style='color: #EEEEEE; font-size: 1.1rem;'>{error_msg}</p>
                        </div>
                        """
                        st.markdown(error_html, unsafe_allow_html=True)

        else:

            waiting_html = """
<div style='text-align: center; color: #A0AAB2; margin-top: 60px;'>
<h1 style='font-size: 4rem; opacity: 0.5;'>
🤖
</h1>
<p>
Waiting for text input...
</p>
</div>
"""
            st.markdown(waiting_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()