import streamlit as st
from streamlit_option_menu import option_menu

def load_sidebar(default_index=0):
    with st.sidebar:
        st.markdown("<h2 class='neon-text' style='text-align: center;'>AI Mood</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #A0AAB2;'>Public Emotion Tracker</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
        
        selected = option_menu(
            menu_title=None,
            options=["Home", "Text Detection", "Analytics", "About"],
            icons=["house", "chat-text", "bar-chart", "info-circle"],
            menu_icon="cast",
            default_index=default_index,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#00ADB5", "font-size": "18px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"5px 0px", "color": "var(--text-color)", "border-radius": "10px"},
                "nav-link-selected": {"background-color": "rgba(0, 173, 181, 0.15)", "color": "#00ADB5", "font-weight": "600", "border": "1px solid #00ADB5", "border-left": "4px solid #00ADB5"},
            }
        )
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: rgba(255,255,255,0.3); font-size: 12px;'>© 2026 Grad Project Team</div>", unsafe_allow_html=True)
        
    # Handle Navigation
    # We check if the selected option is different from the current page to avoid infinite re-runs
    if selected == "Home" and default_index != 0:
        st.switch_page("app.py")
    elif selected == "Text Detection" and default_index != 1:
        st.switch_page("pages/text_detection.py")
    elif selected == "Analytics" and default_index != 2:
        st.switch_page("pages/analytics.py")
    elif selected == "About" and default_index != 3:
        st.switch_page("pages/about.py")
        
    return selected
