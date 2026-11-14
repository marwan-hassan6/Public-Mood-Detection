import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="Public Mood Detection AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

import os
try:
    css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
    local_css(css_path)
except FileNotFoundError:
    st.warning("CSS file not found. Ensure you are running from the project root.")

# Import Sidebar after configuring page to ensure st variables are ready
from components.sidebar import load_sidebar

def main():
    # Load sidebar with default index 0 (Home)
    load_sidebar(default_index=0)
    
    # Hero Section
    st.markdown("<h1 class='hero-title'>Public Mood Detection AI</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Advanced biometric and text analysis to detect crowd sentiment and individual mood in real-time.</p>", unsafe_allow_html=True)
    
    # Main Content Area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        overview_html = """
<div class='glass-card'>
<h3 style='color: #00ADB5; text-align: center; margin-bottom: 20px;'>System Overview</h3>
<p style='text-align: center; line-height: 1.6;'>
Welcome to the Public Mood Detection Dashboard. This graduation project leverages state-of-the-art 
artificial intelligence to analyze human emotion through multiple modalities. 
</p>
</div>
"""
        st.markdown(overview_html, unsafe_allow_html=True)
        
        st.write("")
        
        # Action Buttons
        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button("Text Detection Mode", use_container_width=True):
                st.switch_page("pages/text_detection.py")
                
    st.write("---")
    
    # Feature Cards
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Core Capabilities</h2>", unsafe_allow_html=True)
    
    fcol1, fcol2 = st.columns(2)
    
    with fcol1:
        text_sentiment_html = """
<div class='glass-card' style='text-align: center;'>
<h1 style='color: #00ADB5;'>📝</h1>
<h4>Text Sentiment</h4>
<p style='font-size: 0.9rem; color: #A0AAB2;'>Analyze the underlying emotion of written text using NLP.</p>
</div>
"""
        st.markdown(text_sentiment_html, unsafe_allow_html=True)
        
    with fcol2:
        analytics_dashboard_html = """
<div class='glass-card' style='text-align: center;'>
<h1 style='color: #00ADB5;'>📊</h1>
<h4>Analytics Dashboard</h4>
<p style='font-size: 0.9rem; color: #A0AAB2;'>Comprehensive metrics and visualizations of mood trends.</p>
</div>
"""
        st.markdown(analytics_dashboard_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
