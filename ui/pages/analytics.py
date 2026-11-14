import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Configure the Streamlit page
st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

from components.sidebar import load_sidebar

def main():
    load_sidebar(default_index=2)
    
    st.markdown("<h1 class='hero-title'>Analytics Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Aggregate mood trends and system performance metrics.</p>", unsafe_allow_html=True)
    
    # Fake Data Generation
    emotions = ["Happy", "Sad", "Angry", "Neutral", "Surprised"]
    counts = [450, 120, 80, 300, 50]
    
    # KPIs
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    kpi1.metric(label="Total Scans", value="1,000", delta="12% from yesterday")
    kpi2.metric(label="Dominant Mood", value="Happy", delta="Positive Trend", delta_color="normal")
    kpi3.metric(label="Average Confidence", value="92.4%", delta="0.5%", delta_color="normal")
    kpi4.metric(label="Active Users", value="24", delta="-2", delta_color="inverse")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Model Performance Section
    st.markdown("<div class='glass-card' style='margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00ADB5; margin-top: 0;'>Model Performance</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #EEEEEE; font-size: 0.95rem;'><strong>Model:</strong> <code>cardiffnlp/twitter-roberta-base-sentiment</code><br><strong>Architecture:</strong> RoBERTa</p>", unsafe_allow_html=True)
    
    model_note_html = """
<p style='color: #A0AAB2; font-size: 0.85rem; margin-bottom: 15px; border-left: 3px solid #00ADB5; padding-left: 10px;'>
<em>The model is a pre-trained CardiffNLP TweetEval sentiment model. The officially published evaluation metric available for this model is Macro-F1 = 72.8%. Accuracy, Precision, and Recall are not published in the official model documentation and therefore are intentionally not displayed.</em>
</p>
"""
    st.markdown(model_note_html, unsafe_allow_html=True)
    
    col_f1, _ = st.columns([1, 3])
    with col_f1:
        st.metric(label="Published Macro-F1", value="72.8%")
        
    st.markdown("</div>", unsafe_allow_html=True)

    # Charts Area
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ADB5; margin-top: 0;'>Overall Mood Distribution</h3>", unsafe_allow_html=True)
        
        # Plotly Pie Chart
        fig_pie = px.pie(
            names=emotions, 
            values=counts, 
            hole=0.4,
            color=emotions,
            color_discrete_map={
                "Happy": "#1d7a1d",
                "Sad": "#4da6ff",
                "Angry": "#FF4136",
                "Neutral": "#A0AAB2",
                "Surprised": "#FFDC00"
            }
        )
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#EEEEEE"),
            margin=dict(t=30, b=10, l=10, r=10),
            showlegend=True
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ADB5; margin-top: 0;'>Hourly Mood Trend (Today)</h3>", unsafe_allow_html=True)
        
        # Fake Time Series Data
        hours = [f"{i}:00" for i in range(8, 18)]
        happy_trend = np.random.randint(20, 50, size=10)
        sad_trend = np.random.randint(5, 20, size=10)
        
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(x=hours, y=happy_trend, name='Positive', marker_color='#1d7a1d'))
        fig_bar.add_trace(go.Bar(x=hours, y=sad_trend, name='Negative', marker_color='#FF4136'))
        
        fig_bar.update_layout(
            barmode='stack',
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#EEEEEE"),
            xaxis=dict(gridcolor="rgba(255,255,255,0.1)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.1)"),
            margin=dict(t=30, b=10, l=10, r=10),
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
