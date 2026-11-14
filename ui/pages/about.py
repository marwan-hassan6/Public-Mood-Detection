import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
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
    load_sidebar(default_index=3)
    
    st.markdown("<h1 class='hero-title'>About This Project</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Graduation Project 2026 - Information Technology Department</p>", unsafe_allow_html=True)
    
    abstract_html = """
<div class='glass-card'>
<h3 style='color: #00ADB5; margin-top: 0;'>Project Abstract</h3>
<p style='line-height: 1.8; color: #EEEEEE;'>
The "Public Mood Detection" system is designed to provide real-time emotional analysis
in public spaces or private applications. By combining Natural Language Processing (NLP) 
for textual data and Computer Vision (CV) for facial expressions, the system offers a 
comprehensive view of the subject's emotional state.
</p>
<p style='line-height: 1.8; color: #EEEEEE;'>
This UI serves as the front-end dashboard for interacting with the backend machine learning
models. It is built to be modern, responsive, and highly intuitive, utilizing a dark-themed
glassmorphism design language suitable for AI applications.
</p>
</div>
"""
    st.markdown(abstract_html, unsafe_allow_html=True)
    
    tech_html = """
<div class='glass-card'>
<h3 style='color: #00ADB5; margin-top: 0;'>Technologies Used</h3>
<div style='display: flex; gap: 10px; flex-wrap: wrap; margin-top: 15px;'>
<span style='background: rgba(0, 173, 181, 0.2); border: 1px solid #00ADB5; padding: 8px 15px; border-radius: 20px; font-weight: 600;'>Python</span>
<span style='background: rgba(0, 173, 181, 0.2); border: 1px solid #00ADB5; padding: 8px 15px; border-radius: 20px; font-weight: 600;'>Streamlit</span>
<span style='background: rgba(0, 173, 181, 0.2); border: 1px solid #00ADB5; padding: 8px 15px; border-radius: 20px; font-weight: 600;'>Plotly</span>
<span style='background: rgba(0, 173, 181, 0.2); border: 1px solid #00ADB5; padding: 8px 15px; border-radius: 20px; font-weight: 600;'>Custom CSS</span>
<span style='background: rgba(255, 255, 255, 0.1); border: 1px dashed rgba(255,255,255,0.3); padding: 8px 15px; border-radius: 20px; font-weight: 600; color: #A0AAB2;'>TensorFlow (Backend)</span>
<span style='background: rgba(255, 255, 255, 0.1); border: 1px dashed rgba(255,255,255,0.3); padding: 8px 15px; border-radius: 20px; font-weight: 600; color: #A0AAB2;'>OpenCV (Backend)</span>
</div>
</div>
"""
    st.markdown(tech_html, unsafe_allow_html=True)
    
    team_html = """
<div class='glass-card' style='margin-top: 20px;'>
<div style='text-align: center; margin-bottom: 30px;'>
<h2 style='color: #00ADB5; margin-bottom: 10px; margin-top: 0;'>Project Team</h2>
<p style='color: #A0AAB2; font-size: 1.1rem; margin-top: 0;'>Meet the team behind the Public Mood Detection project.</p>
</div>

<style>
.team-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 30px;
}
@media (max-width: 1024px) {
    .team-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
    .team-grid { grid-template-columns: 1fr; }
}
.team-member-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 25px 20px;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}
.team-member-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 173, 181, 0.2);
    border-color: rgba(0, 173, 181, 0.3);
}
.member-avatar {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    margin-bottom: 15px;
}
.member-name {
    margin: 0 0 5px 0;
    color: #EEEEEE;
    font-size: 1.2rem;
    font-weight: 600;
}
.member-role {
    margin: 0;
    font-size: 0.9rem;
}
</style>

<div class="team-grid">
    <!-- Card 1 -->
    <div class="team-member-card">
        <div class="member-avatar" style="background: #4da6ff;">👨‍🔬</div>
        <h4 class="member-name">Yousef Saber</h4>
        <p class="member-role" style="color: #4da6ff;">AI Engineer</p>
    </div>
    <!-- Card 2 -->
    <div class="team-member-card">
        <div class="member-avatar" style="background: #00ADB5;">👨‍💻</div>
        <h4 class="member-name">Marwan Hassan</h4>
        <p class="member-role" style="color: #00ADB5;">Frontend UI/UX Designer</p>
    </div>
    <!-- Card 3 -->
    <div class="team-member-card">
        <div class="member-avatar" style="background: #00ADB5;">👨‍💻</div>
        <h4 class="member-name">Mohamed Reda</h4>
        <p class="member-role" style="color: #00ADB5;">Frontend UI/UX Designer</p>
    </div>
    <!-- Card 4 -->
    <div class="team-member-card">
        <div class="member-avatar" style="background: #FFDC00;">👨‍💻</div>
        <h4 class="member-name">Yousef Wahbi</h4>
        <p class="member-role" style="color: #FFDC00;">AI Engineer</p>
    </div>
    <!-- Card 5 -->
    <div class="team-member-card">
        <div class="member-avatar" style="background: #FFDC00;">👨‍💻</div>
        <h4 class="member-name">Amr Khaled</h4>
        <p class="member-role" style="color: #FFDC00;">AI Engineer</p>
    </div>
    <!-- Card 6 -->
    <div class="team-member-card">
        <div class="member-avatar" style="background: #ff6b6b;">👨‍🎓</div>
        <h4 class="member-name">Mohamed Sarhan</h4>
    </div>
    <!-- Card 7 -->
    <div class="team-member-card">
        <div class="member-avatar" style="background: #ff6b6b;">👨‍🎓</div>
        <h4 class="member-name">Ali Mahmoud</h4>
    </div>
</div>

<hr style='border: 1px solid rgba(255,255,255,0.1); margin: 30px 0;'>
<div style='text-align: center; color: #A0AAB2; font-size: 1rem; font-weight: 500;'>
    Supervised by: Dr. Sherif Aletriby
</div>
</div>
"""
    st.markdown(team_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
