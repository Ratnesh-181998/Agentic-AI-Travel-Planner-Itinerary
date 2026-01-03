import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz
from pathlib import Path
import time

# Load environment variables
load_dotenv()

# Dynamic Path Configuration for Cloud & Local Compatibility
try:
    # Get the directory where this script is located (e.g., .../Local Run/CODE)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Go one level up to get the project root (e.g., .../Local Run)
    PROJECT_ROOT = os.path.dirname(BASE_DIR)
    
    # Define paths to asset directories relative to project root
    ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
    DIAGRAMS_DIR = os.path.join(PROJECT_ROOT, 'Diagarm', 'Architeure Diagram') # Preserving folder name 'Diagarm'
    HLD_LLD_DIR = os.path.join(PROJECT_ROOT, 'Diagarm', 'HLD & LLD Daigram') # Preserving typo 'Daigram'
    ABOUT_DIAGRAM_DIR = os.path.join(PROJECT_ROOT, 'Diagarm', 'About Diagram')
except Exception as e:
    st.error(f"Error configuring paths: {str(e)}")
    # Fallback to current directory if something goes wrong
    ASSETS_DIR = '.'
    DIAGRAMS_DIR = '.'
    HLD_LLD_DIR = '.'
    ABOUT_DIAGRAM_DIR = '.'

# Page configuration
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium design - Matching Multi-Agent Style
st.markdown("""
<style>
    /* Enhanced Multi-Color Theme */
    :root {
        --primary-gold: #FFD700;
        --secondary-gold: #FFC800;
        --accent-blue: #2874f0;
        --accent-green: #2ecc71;
        --accent-orange: #ff9f43;
        --accent-purple: #9b59b6;
        --accent-cyan: #00d4ff;
        --background-dark: #141E30; 
        --card-bg: rgba(36, 59, 85, 0.6); 
        --text-light: #ecf0f1; 
        --text-dim: #bdc3c7;   
        --hover-glow: rgba(46, 204, 113, 0.6);
    }
    
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55);
        color: var(--text-light);
        font-family: 'Inter', sans-serif;
    }

    strong, b {
        color: var(--primary-gold);
        font-weight: 700;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 3px solid var(--accent-green);
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: var(--accent-cyan);
    }
    
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] li, [data-testid="stSidebar"] a {
        color: #e0e0e0;
    }
    
    [data-testid="stSidebar"] .info-card {
        background: linear-gradient(135deg, rgba(155, 89, 182, 0.2) 0%, rgba(40, 116, 240, 0.2) 100%);
        border: 2px solid rgba(155, 89, 182, 0.4);
        backdrop-filter: blur(10px);
    }
    
    [data-testid="stSidebar"] .info-card h3 {
        color: var(--accent-cyan);
    }
    
    [data-testid="stSidebar"] .info-card p {
        color: #e8e8e8;
    }

    h1 { color: var(--accent-cyan) !important; text-shadow: 0 0 40px rgba(0, 212, 255, 0.6); }
    h2 { color: var(--accent-blue) !important; }
    h3 { color: var(--accent-green) !important; }
    
    /* Header Box - Top Right Corner */
    .header-box {
        position: fixed;
        top: 60px;
        right: 20px;
        background: linear-gradient(135deg, #2874f0 0%, #9b59b6 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(40, 116, 240, 0.4);
        z-index: 999;
        font-size: 13px;
        font-weight: 600;
        text-align: center;
        border: 2px solid rgba(155, 89, 182, 0.3);
    }
    
    .header-box .name {
        font-size: 15px;
        font-weight: 700;
        margin-bottom: 2px;
    }
    
    .header-box .title {
        font-size: 11px;
        opacity: 0.95;
        font-weight: 500;
    }
    
    /* Main Title Styling */
    .main-title {
        color: #00d4ff;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
        padding: 20px 0;
        text-shadow: 0 0 40px rgba(0, 212, 255, 0.6);
        letter-spacing: 1px;
    }
    
    .subtitle {
        text-align: center;
        color: #e8e8e8;
        font-size: 1.1rem;
        margin-bottom: 30px;
        font-weight: 500;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%);
        padding: 10px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background: linear-gradient(135deg, rgba(26, 31, 46, 0.9) 0%, rgba(37, 43, 59, 0.9) 100%);
        border-radius: 8px;
        padding: 0 24px;
        font-weight: 600;
        border: 2px solid rgba(40, 116, 240, 0.3);
        color: #e8e8e8;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, rgba(40, 116, 240, 0.2) 0%, rgba(155, 89, 182, 0.2) 100%);
        border-color: var(--accent-cyan);
        transform: translateY(-2px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-purple) 100%);
        color: white !important;
        border-color: var(--accent-cyan);
        box-shadow: 0 4px 15px rgba(40, 116, 240, 0.4);
    }
    
    /* Card Styling */
    .info-card {
        background: linear-gradient(135deg, rgba(26, 31, 46, 0.9) 0%, rgba(37, 43, 59, 0.9) 100%);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(40, 116, 240, 0.2);
        margin: 15px 0;
        border: 2px solid rgba(40, 116, 240, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(40, 116, 240, 0.4);
        border-color: var(--accent-cyan);
    }
    
    .info-card h3, .info-card h4 {
        color: var(--accent-cyan) !important;
    }
    
    .info-card p, .info-card li {
        color: #e8e8e8;
    }
    
    /* Tech Stack Grid */
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }
    
    .tech-item {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-purple) 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(40, 116, 240, 0.3);
        transition: transform 0.3s ease;
        border: 2px solid rgba(155, 89, 182, 0.3);
    }
    
    .tech-item:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(155, 89, 182, 0.5);
    }
    
    /* Log Entry Styling */
    .log-entry {
        background: linear-gradient(135deg, rgba(26, 31, 46, 0.95) 0%, rgba(42, 49, 66, 0.95) 100%);
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 4px solid var(--accent-cyan);
        font-family: 'Courier New', monospace;
        font-size: 14px;
        color: #e8e8e8;
    }
    
    .log-timestamp {
        color: var(--accent-cyan);
        font-weight: 700;
    }
    
    /* Success/Info/Warning Boxes */
    .success-box {
        background: linear-gradient(135deg, rgba(46, 204, 113, 0.2) 0%, rgba(39, 174, 96, 0.2) 100%);
        color: #e8e8e8;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        font-weight: 600;
        border: 2px solid var(--accent-green);
        border-left: 5px solid var(--accent-green);
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%);
        color: #e8e8e8;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        font-weight: 600;
        border: 2px solid rgba(40, 116, 240, 0.4);
        border-left: 5px solid var(--accent-cyan);
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-purple) 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 700;
        transition: all 0.3s ease;
        border: 2px solid rgba(155, 89, 182, 0.3);
        min-height: 0px;
        line-height: normal;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(155, 89, 182, 0.6);
    }
    
    /* Image Styling */
    img {
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        border: 2px solid rgba(40, 116, 240, 0.2);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: var(--accent-cyan);
        font-weight: 700;
    }
    
    /* Form Inputs */
    .stTextInput>div>div>input {
        background: rgba(26, 31, 46, 0.8);
        color: #e8e8e8;
        border: 2px solid rgba(40, 116, 240, 0.3);
        border-radius: 8px;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: var(--accent-cyan);
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="info-card">
        <h3 style="color: #00d4ff; margin-top: 0;">🧠 AI Travel Planner</h3>
        <p style="color: #e8e8e8; line-height: 1.6;">
            An <b>Agentic GenAI Application</b> that generates personalized travel itineraries 
            using LangChain and Groq LLM, deployed on Kubernetes with full ELK Stack monitoring.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Key Features")
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.2) 0%, rgba(40, 116, 240, 0.2) 100%); 
                padding: 15px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.4);'>
        <ul style='margin: 0; padding-left: 20px; color: #e8e8e8; line-height: 1.8;'>
            <li>AI-Powered Itinerary Generation</li>
            <li>Kubernetes Orchestration</li>
            <li>Docker Containerization</li>
            <li>ELK Stack Monitoring</li>
            <li>Production-Ready Architecture</li>
            <li>LLMOps Best Practices</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 👨‍💻 Developer")
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.2) 0%, rgba(40, 116, 240, 0.2) 100%); 
                padding: 15px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.4);'>
        <p style='margin: 5px 0; color: #00d4ff; font-weight: 600;'>Ratnesh Kumar Singh</p>
        <p style='margin: 5px 0; font-size: 0.85rem; color: #e8e8e8;'>Data Scientist (AI/ML Engineer)</p>
        <div style='margin-top: 10px; display: flex; flex-wrap: wrap; gap: 10px;'>
            <a href='https://github.com/Ratnesh-181998' target='_blank' style='text-decoration: none; color: #2874f0; font-weight: bold; font-size: 0.8rem;'>🔗 GitHub</a>
            <a href='https://www.linkedin.com/in/ratneshkumar1998/' target='_blank' style='text-decoration: none; color: #0077b5; font-weight: bold; font-size: 0.8rem;'>💼 LinkedIn</a>
            <a href='https://share.streamlit.io/user/ratnesh-181998' target='_blank' style='text-decoration: none; color: #00d4ff; font-weight: bold; font-size: 0.8rem;'>📊 Portfolio</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Top Right Professional Badge
col_space, col_badge = st.columns([3, 1.25])
with col_badge:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2874f0 0%, #9b59b6 100%); 
                padding: 10px; border-radius: 8px; 
                box-shadow: 0 4px 12px rgba(40, 116, 240, 0.5);
                border: 1px solid rgba(255, 255, 255, 0.1);
                text-align: center;
                margin-bottom: 10px;'>
        <p style='margin: 0; color: #ffffff; font-weight: 700; font-size: 0.75rem; line-height: 1.4;'>
            <strong>Ratnesh Kumar Singh</strong><br>
            <span style='font-size: 0.65rem; opacity: 0.9;'>Data Scientist (AI/ML Engineer 4+ Yrs Exp)</span>
        </p>
        <div style='display: flex; justify-content: center; gap: 8px; margin-top: 5px;'>
            <a href='https://github.com/Ratnesh-181998' target='_blank' style='color: white; font-size: 0.65rem; text-decoration: none;'>📂 GitHub</a>
            <a href='https://www.linkedin.com/in/ratneshkumar1998/' target='_blank' style='color: white; font-size: 0.65rem; text-decoration: none;'>💼 LinkedIn</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Helper to load image as base64
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

header_bg_path = os.path.join(ASSETS_DIR, "travel_hill.png")
header_bg_base64 = get_base64_of_bin_file(header_bg_path)

# Main Header with Realistic Background
st.markdown(f"""
<div style='text-align: center; padding: 40px 20px; 
            background-image: linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.4)), url("data:image/png;base64,{header_bg_base64}"); 
            background-size: cover; background-position: center; 
            border-radius: 15px; margin-bottom: 25px; 
            border: 1px solid rgba(255, 255, 255, 0.3); 
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);'>
    <div style='display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 5px;'>
        <span style='font-size: 3.5rem; filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.8)); text-shadow: 0 4px 8px rgba(0,0,0,0.5);'>✈️</span>
        <h1 style='margin: 0; font-size: 3.0rem; color: #ffffff; 
                   text-shadow: 0 2px 10px rgba(0,0,0,0.8); 
                   font-weight: 900; letter-spacing: 3px; text-transform: uppercase;'>
            AI TRAVEL PLANNER
        </h1>
    </div>
    <p style='font-size: 1.1rem; color: #f1f2f6; margin-top: 5px; font-weight: 500; text-shadow: 0 2px 4px rgba(0,0,0,0.8); letter-spacing: 1px;'>
        🚀 Agentic GenAI Application with Production-Grade LLMOps
    </p>
</div>
""", unsafe_allow_html=True)

# Create Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🎯 Demo", 
    "📖 About", 
    "🛠️ Tech Stack", 
    "🏗️ HLD & LLD", 
    "📐 Architecture", 
    "📊 System Logs"
])

# Tab 1: Demo
with tab1:
    # Welcome Banner
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%); 
                padding: 20px; border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 25px;'>
        <h3 style='color: #00d4ff; margin: 0 0 10px 0;'>👋 Welcome to AI Travel Planner</h3>
        <p style='color: #e8e8e8; margin: 0; font-size: 0.95rem;'>
            Experience the power of <b>Agentic AI</b>! Simply enter your destination and interests below, 
            and our AI will craft a personalized travel itinerary just for you. 🌍✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Visual Showcase Section (5-Column Grid with Uniform Sizing)
    st.markdown("### ✨ Experience the Journey")
    
    # Load all images as base64 for reliable HTML embedding
    img_paths = [
        os.path.join(ASSETS_DIR, "travel_hill.png"),
        os.path.join(ASSETS_DIR, "travel_beach.png"),
        os.path.join(ASSETS_DIR, "travel_sun.png"),
        os.path.join(ASSETS_DIR, "travel_snow.png"),
        os.path.join(ASSETS_DIR, "travel_mix.png")
    ]
    img_captions = ["⛰️ Green Hills", "🏖️ Sunny Beaches", "☀️ Bright Sunshine", "🏔️ Snowy Mountains", "🌅 Panoramic View"]
    
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            # Smaller, centered heading
            st.markdown(f"<p style='text-align: center; font-size: 0.8rem; font-weight: 600; margin: 0 0 5px 0;'>{img_captions[i]}</p>", unsafe_allow_html=True)
            st.image(img_paths[i], use_container_width=True)

    # How to Use Section - Now collapsible
    with st.expander("📚 How to Use This AI Travel Planner", expanded=False):
        col_guide1, col_guide2 = st.columns(2)
        
        with col_guide1:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(46, 204, 113, 0.15) 0%, rgba(40, 116, 240, 0.15) 100%); 
                        padding: 12px; border-radius: 10px; border: 2px solid rgba(46, 204, 113, 0.3); margin-bottom: 10px;'>
                <h4 style='color: #2ecc71; margin: 0 0 8px 0; font-size: 1rem;'>🎯 Method 1: Quick Start (Recommended for First-Time Users)</h4>
                <ol style='color: #e8e8e8; margin: 0; padding-left: 20px; line-height: 1.5; font-size: 0.9rem;'>
                    <li><b>Click</b> any destination button below (e.g., 🗼 Paris, 🗾 Tokyo)</li>
                    <li>The form will <b>auto-fill</b> with city and interests</li>
                    <li>Click <b>"🚀 Generate Itinerary"</b> button</li>
                    <li>Wait 5-10 seconds for AI to create your plan</li>
                    <li><b>Download</b> or view your personalized itinerary!</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        with col_guide2:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.15) 0%, rgba(40, 116, 240, 0.15) 100%); 
                        padding: 12px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.3); margin-bottom: 10px;'>
                <h4 style='color: #9b59b6; margin: 0 0 8px 0; font-size: 1rem;'>✍️ Method 2: Custom Planning (For Specific Needs)</h4>
                <ol style='color: #e8e8e8; margin: 0; padding-left: 20px; line-height: 1.5; font-size: 0.9rem;'>
                    <li><b>Enter your city</b> in the "City Name" field</li>
                    <li><b>List your interests</b> separated by commas<br>
                        <small style='color: #bdc3c7;'>Example: museums, food, shopping, history</small></li>
                    <li><b>Select travel dates</b> - Start Date and End Date (DD/MM/YYYY)</li>
                    <li><b>Enter number of travelers</b> - Adults and Children</li>
                    <li>Click <b>"💡 Need ideas?"</b> for interest suggestions</li>
                    <li>Click <b>"🚀 Generate Itinerary"</b></li>
                    <li>Get your <b>customized travel plan</b>!</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        # Pro Tips Section
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 165, 0, 0.1) 100%); 
                    padding: 10px; border-radius: 8px; border-left: 3px solid #FFD700; margin-bottom: 12px;'>
            <h4 style='color: #FFD700; margin: 0 0 6px 0; font-size: 0.95rem;'>💎 Pro Tips for Best Results:</h4>
            <ul style='color: #e8e8e8; margin: 0; padding-left: 20px; line-height: 1.5; font-size: 0.85rem;'>
                <li><b>Be Specific:</b> Instead of "sightseeing", try "historical monuments, art museums"</li>
                <li><b>Mix Interests:</b> Combine different types like "food, culture, adventure" for variety</li>
                <li><b>Popular Cities:</b> Well-known destinations get more detailed recommendations</li>
                <li><b>Multiple Interests:</b> Add 3-5 interests for a well-rounded itinerary</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## 📊 Quick Info & Statistics")
    
    # Tips, Statistics, and Did You Know - moved here from sidebar
    info_col1, info_col2, info_col3 = st.columns(3)
    
    with info_col1:
        st.markdown("##### 💡 Tips for Best Results")
        st.markdown("""
        <div class="info-card" style="padding: 10px;">
            <p style="margin: 4px 0; font-size: 0.85rem;"><b>🎯 Be Specific:</b> Mention exact interests</p>
            <p style="margin: 4px 0; font-size: 0.85rem;"><b>🌍 Popular Cities:</b> Better recommendations</p>
            <p style="margin: 4px 0; font-size: 0.85rem;"><b>🎨 Multiple Interests:</b> More diverse itinerary</p>
            <p style="margin: 4px 0; font-size: 0.85rem;"><b>⏱️ Response Time:</b> 5-10 seconds</p>
        </div>
        """, unsafe_allow_html=True)
    
    with info_col2:
        st.markdown("##### 📊 Demo Statistics")
        stat_col_a, stat_col_b = st.columns(2)
        with stat_col_a:
            st.metric("Total Requests", len(st.session_state.get('logs', [])))
        with stat_col_b:
            success_count = sum(1 for log in st.session_state.get('logs', []) if log['status'] == 'Success')
            st.metric("Successful", success_count)
    
    with info_col3:
        st.markdown("##### 🌟 Did You Know?")
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 165, 0, 0.1) 100%); 
                    padding: 8px; border-radius: 8px; border-left: 3px solid #FFD700;'>
            <p style='color: #e8e8e8; margin: 0 0 6px 0; font-size: 0.8rem;'>
                Our AI uses <b>Groq's ultra-fast LLM</b> to generate itineraries in seconds! ⚡
            </p>
            <p style='color: #e8e8e8; margin: 0; font-size: 0.8rem;'>
                It analyzes thousands of travel patterns to create the perfect plan for you. 🌍
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Start Section - moved to just before Generate form
    st.markdown("<h4 style='color: #2ecc71; margin: 0 0 5px 0; font-size: 1rem;'>🚀 Quick Start - Popular Destinations</h4>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(40, 116, 240, 0.1) 100%); 
                padding: 6px 12px; border-radius: 6px; margin-bottom: 8px;'>
        <p style='color: #2ecc71; margin: 0; font-size: 0.8rem; line-height: 1.2;'>
            💡 <b>New to AI Travel Planning?</b> Try these popular destinations to see the magic in action!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Start Buttons
    q1, q2, q3, q4 = st.columns(4)
    
    # Initialize session state for quick selections
    if 'quick_city' not in st.session_state:
        st.session_state.quick_city = ""
    if 'quick_interests' not in st.session_state:
        st.session_state.quick_interests = ""
    
    if q1.button("🗼 Paris", use_container_width=True, help="Romantic city with art and culture"):
        st.session_state.quick_city = "Paris"
        st.session_state.quick_interests = "museums, food, history, art"
    
    if q2.button("🗾 Tokyo", use_container_width=True, help="Modern metropolis with tradition"):
        st.session_state.quick_city = "Tokyo"
        st.session_state.quick_interests = "technology, food, temples, shopping"
    
    if q3.button("🗽 New York", use_container_width=True, help="The city that never sleeps"):
        st.session_state.quick_city = "New York"
        st.session_state.quick_interests = "museums, food, broadway, shopping"
    
    if q4.button("🏖️ Dubai", use_container_width=True, help="Luxury and adventure combined"):
        st.session_state.quick_city = "Dubai"
        st.session_state.quick_interests = "luxury, shopping, desert safari, architecture"
    
    # Second row of quick buttons
    q5, q6, q7, q8 = st.columns(4)
    
    if q5.button("🏛️ Rome", use_container_width=True, help="Ancient history and Italian cuisine"):
        st.session_state.quick_city = "Rome"
        st.session_state.quick_interests = "history, food, architecture, art"
    
    if q6.button("🌴 Bali", use_container_width=True, help="Tropical paradise"):
        st.session_state.quick_city = "Bali"
        st.session_state.quick_interests = "beaches, temples, nature, wellness"
    
    if q7.button("🎭 London", use_container_width=True, help="Royal heritage and modern culture"):
        st.session_state.quick_city = "London"
        st.session_state.quick_interests = "museums, history, theater, food"
    
    if q8.button("🏔️ Switzerland", use_container_width=True, help="Alpine beauty and adventure"):
        st.session_state.quick_city = "Switzerland"
        st.session_state.quick_interests = "mountains, skiing, nature, chocolate"
    
    # Third row of quick buttons
    q9, q10, q11, q12 = st.columns(4)
    
    if q9.button("🏖️ Barcelona", use_container_width=True, help="Beach city with vibrant culture"):
        st.session_state.quick_city = "Barcelona"
        st.session_state.quick_interests = "beaches, architecture, food, nightlife"
    
    if q10.button("🌆 Singapore", use_container_width=True, help="Modern city-state with diverse culture"):
        st.session_state.quick_city = "Singapore"
        st.session_state.quick_interests = "food, shopping, gardens, architecture"
    
    if q11.button("🌋 Iceland", use_container_width=True, help="Land of fire and ice"):
        st.session_state.quick_city = "Iceland"
        st.session_state.quick_interests = "nature, hot springs, northern lights, hiking"
    
    if q12.button("🏝️ Maldives", use_container_width=True, help="Tropical island paradise"):
        st.session_state.quick_city = "Maldives"
        st.session_state.quick_interests = "beaches, diving, luxury resorts, relaxation"
    
    # Fourth row - Indian destinations
    q13, q14, q15, q16 = st.columns(4)
    
    if q13.button("🏖️ Goa", use_container_width=True, help="Beach paradise with vibrant nightlife"):
        st.session_state.quick_city = "Goa"
        st.session_state.quick_interests = "beaches, nightlife, water sports, Portuguese heritage"
    
    if q14.button("🏰 Jaipur", use_container_width=True, help="The Pink City with royal palaces"):
        st.session_state.quick_city = "Jaipur"
        st.session_state.quick_interests = "palaces, forts, culture, shopping, food"
    
    if q15.button("🌴 Kerala", use_container_width=True, help="God's Own Country with backwaters"):
        st.session_state.quick_city = "Kerala"
        st.session_state.quick_interests = "backwaters, beaches, ayurveda, nature, houseboats"
    
    if q16.button("🕌 Agra", use_container_width=True, help="Home of the Taj Mahal"):
        st.session_state.quick_city = "Agra"
        st.session_state.quick_interests = "Taj Mahal, monuments, history, Mughal architecture"
    
    # Fifth row - More Indian destinations
    q17, q18, q19, q20 = st.columns(4)
    
    if q17.button("🏛️ Udaipur", use_container_width=True, help="City of Lakes and palaces"):
        st.session_state.quick_city = "Udaipur"
        st.session_state.quick_interests = "lakes, palaces, heritage, culture, romantic settings"
    
    if q18.button("🕉️ Varanasi", use_container_width=True, help="Spiritual capital on the Ganges"):
        st.session_state.quick_city = "Varanasi"
        st.session_state.quick_interests = "spirituality, Ganges, temples, culture, rituals"
    
    if q19.button("🧘 Rishikesh", use_container_width=True, help="Yoga capital and adventure hub"):
        st.session_state.quick_city = "Rishikesh"
        st.session_state.quick_interests = "yoga, rafting, adventure, spirituality, nature"
    
    if q20.button("🏔️ Manali", use_container_width=True, help="Hill station with snow-capped peaks"):
        st.session_state.quick_city = "Manali"
        st.session_state.quick_interests = "mountains, skiing, trekking, adventure, nature"
    
    # Sixth row - Final Indian destinations
    q21, q22, q23, q24 = st.columns(4)
    
    if q21.button("⛰️ Ladakh", use_container_width=True, help="Land of high passes and monasteries"):
        st.session_state.quick_city = "Ladakh"
        st.session_state.quick_interests = "mountains, monasteries, adventure, biking, landscapes"
    
    if q22.button("🌆 Mumbai", use_container_width=True, help="City of dreams and Bollywood"):
        st.session_state.quick_city = "Mumbai"
        st.session_state.quick_interests = "Bollywood, beaches, food, nightlife, shopping"
    
    if q23.button("🎭 Kolkata", use_container_width=True, help="Cultural capital with colonial heritage"):
        st.session_state.quick_city = "Kolkata"
        st.session_state.quick_interests = "culture, food, heritage, art, literature"
    
    if q24.button("🏺 Hampi", use_container_width=True, help="Ancient ruins and boulder landscapes"):
        st.session_state.quick_city = "Hampi"
        st.session_state.quick_interests = "ruins, history, temples, architecture, bouldering"
    
    st.markdown("---")
    
    # Header with Reset Button
    col_header, col_reset = st.columns([4, 1])
    
    with col_header:
        st.markdown("<h4 style='color: #2ecc71; margin: 0;'>✍️ Generate Your Personalized Travel Itinerary By RatneshAI</h4>", unsafe_allow_html=True)
        
    with col_reset:
        if st.button("🔄 Reset Form", help="Clear all fields and start over", use_container_width=True):
            # Clear specific session state keys
            keys_to_clear = ['quick_city', 'quick_interests', 'current_itinerary', 'current_city', 'current_interests', 'feedback']
            for key in keys_to_clear:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.1) 0%, rgba(40, 116, 240, 0.1) 100%); 
                padding: 10px; border-radius: 8px; margin-bottom: 12px;'>
        <p style='color: #2ecc71; margin: 0; font-size: 0.85rem;'>
            📝 <b>Custom Planning:</b> Enter your own destination and interests below, or use the Quick Start buttons above!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("planner_form"):
        st.markdown("#### 📍 Trip Details")
        
        # Use session state values if available
        city_value = st.session_state.get('quick_city', '')
        interests_value = st.session_state.get('quick_interests', '')
        
        city = st.text_input(
            "🌍 Enter the city name for your trip",
            value=city_value,
            placeholder="e.g., Paris, Tokyo, New York, Dubai",
            help="Enter any city or destination you'd like to visit"
        )
        interests = st.text_input(
            "🎨 Enter your interests (comma-separated)",
            value=interests_value,
            placeholder="e.g., museums, food, history, adventure, shopping",
            help="List your interests to get personalized recommendations"
        )
        
        # Date inputs for trip planning
        from datetime import date, timedelta
        
        st.markdown("#### 📅 Travel Dates")
        col_date1, col_date2 = st.columns(2)
        
        with col_date1:
            start_date = st.date_input(
                "🛫 Start Date",
                value=date.today() + timedelta(days=7),  # Default to 1 week from now
                min_value=date.today(),
                help="When does your trip start?",
                format="DD/MM/YYYY"
            )
        
        with col_date2:
            end_date = st.date_input(
                "🛬 End Date",
                value=date.today() + timedelta(days=10),  # Default to 3 days trip
                min_value=date.today(),
                help="When does your trip end?",
                format="DD/MM/YYYY"
            )

        
        # Traveler details
        st.markdown("#### 👥 Travelers")
        col_travelers1, col_travelers2 = st.columns(2)
        
        with col_travelers1:
            num_adults = st.number_input(
                "👨 Number of Adults",
                min_value=1,
                max_value=20,
                value=2,
                help="How many adults are traveling?"
            )
        
        with col_travelers2:
            num_children = st.number_input(
                "👶 Number of Children",
                min_value=0,
                max_value=10,
                value=0,
                help="How many children are traveling?"
            )
        
        # Sample Interests Helper
        with st.expander("💡 Need ideas? View sample interests"):
            st.markdown("""
            <div style='background: rgba(255, 255, 255, 0.05); padding: 10px; border-radius: 8px;'>
                <p style='margin: 5px 0; color: #e8e8e8;'><b>🎨 Culture:</b> museums, art galleries, history, architecture</p>
                <p style='margin: 5px 0; color: #e8e8e8;'><b>🍕 Food:</b> local cuisine, street food, fine dining, food tours</p>
                <p style='margin: 5px 0; color: #e8e8e8;'><b>🏃 Adventure:</b> hiking, water sports, extreme sports, trekking</p>
                <p style='margin: 5px 0; color: #e8e8e8;'><b>🛍️ Shopping:</b> markets, malls, boutiques, souvenirs</p>
                <p style='margin: 5px 0; color: #e8e8e8;'><b>🌿 Nature:</b> parks, beaches, mountains, wildlife</p>
                <p style='margin: 5px 0; color: #e8e8e8;'><b>🎭 Entertainment:</b> theater, nightlife, concerts, festivals</p>
            </div>
            """, unsafe_allow_html=True)
        
        submitted = st.form_submit_button("🚀 Generate Itinerary", use_container_width=True, type="primary")
    
    # Process form submission and display results OUTSIDE the form
    if submitted:
        # Clear quick selection after submission
        st.session_state.quick_city = ""
        st.session_state.quick_interests = ""
        
        if city and interests:
            with st.spinner("🤖 AI is crafting your perfect itinerary..."):
                # Progress bar simulation
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                try:
                    status_text.text("🔍 Analyzing your preferences...")
                    progress_bar.progress(25)
                    time.sleep(0.5)
                    
                    planner = TravelPlanner()
                    planner.set_city(city)
                    
                    status_text.text("🌍 Researching destination...")
                    progress_bar.progress(50)
                    time.sleep(0.5)
                    
                    planner.set_interests(interests)
                    
                    status_text.text("✨ Generating personalized itinerary...")
                    progress_bar.progress(75)
                    
                    itinerary = planner.create_itineary()
                    
                    status_text.text("✅ Finalizing your travel plan...")
                    progress_bar.progress(100)
                    time.sleep(0.3)
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
                    # Store in session state
                    st.session_state.current_itinerary = itinerary
                    st.session_state.current_city = city
                    st.session_state.current_interests = interests
                    
                    st.success("✅ Itinerary Generated Successfully!")
                    st.balloons()  # Celebration animation
                    
                    # Log the activity
                    ist = pytz.timezone('Asia/Kolkata')
                    current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")
                    if 'logs' not in st.session_state:
                        st.session_state.logs = []
                    st.session_state.logs.append({
                        'timestamp': current_time,
                        'action': 'Itinerary Generated',
                        'city': city,
                        'interests': interests,
                        'status': 'Success'
                    })
                    
                except Exception as e:
                    progress_bar.empty()
                    status_text.empty()
                    st.error(f"❌ Error: {str(e)}")
                    
                    # Log the error
                    ist = pytz.timezone('Asia/Kolkata')
                    current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")
                    if 'logs' not in st.session_state:
                        st.session_state.logs = []
                    st.session_state.logs.append({
                        'timestamp': current_time,
                        'action': 'Itinerary Generation Failed',
                        'city': city,
                        'interests': interests,
                        'status': 'Error',
                        'error': str(e)
                    })
        else:
            st.warning("⚠️ Please fill in both City and Interests to proceed")
    
    # Display itinerary if it exists in session state (OUTSIDE the form)
    if 'current_itinerary' in st.session_state and st.session_state.current_itinerary:
        st.markdown("---")
        st.markdown("### 📄 Your Personalized Itinerary By RatneshAI")
        st.markdown(f"""
        <div class="info-card">
            {st.session_state.current_itinerary}
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons - all in one line
        col_dl, col_spacer, col_rating = st.columns([2, 0.5, 2])
        
        with col_dl:
            # Download button
            st.download_button(
                label="📥 Download Itinerary as TXT",
                data=f"AI Travel Itinerary for {st.session_state.current_city}\n\nCity: {st.session_state.current_city}\nInterests: {st.session_state.current_interests}\n\n{st.session_state.current_itinerary}",
                file_name=f"itinerary_{st.session_state.current_city.lower().replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True,
                key="download_itinerary"
            )
        
        with col_spacer:
            st.empty()
        
        with col_rating:
            # Rating section with text and buttons together
            rate_col1, rate_col2, rate_col3 = st.columns([2, 0.6, 0.6])
            
            with rate_col1:
                st.markdown("<p style='margin-top: 8px; color: #FFD700; font-weight: bold; text-align: right;'>Rate this itinerary:</p>", unsafe_allow_html=True)
            
            with rate_col2:
                if st.button("👍", use_container_width=True, key="thumbs_up", help="Helpful"):
                    st.session_state.feedback = "positive"
                    st.success("Thanks! 😊")
            
            with rate_col3:
                if st.button("👎", use_container_width=True, key="thumbs_down", help="Not Helpful"):
                    st.session_state.feedback = "negative"
                    st.info("We'll improve! 🙏")



# Tab 2: About
with tab2:
    st.markdown("## 📖 About This Project")
    
    st.markdown("""
    <div class="info-box">
        <h3 style="margin-top: 0; color: #00d4ff;">🧠 AI Travel Planner - Agentic GenAI Application</h3>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #e8e8e8;">
            An AI-powered travel planning system that generates <b>personalized end-to-end travel itineraries</b> 
            (destinations, schedules, activities, budgets) using LLM reasoning, deployed as a cloud-native, 
            containerized application with production-grade monitoring and logging.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Architecture Diagram
    st.markdown("### 🏗️ System Architecture")
    try:
        st.image(os.path.join(ABOUT_DIAGRAM_DIR, "Picture1.png"), use_container_width=True, caption="Agentic AI Travel Planner Architecture")
    except Exception:
        st.info("Architecture diagram placeholder.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Project Objectives")
        st.markdown("""
        <div class="info-card">
            <ul style="line-height: 2; color: #e8e8e8;">
                <li><b>Personalized AI Itineraries:</b> Custom travel plans based on user preferences</li>
                <li><b>Budget-Aware Planning:</b> Cost-effective recommendations</li>
                <li><b>Fast LLM Inference:</b> Using Groq for ultra-low latency</li>
                <li><b>Production-Grade Logging:</b> Full ELK Stack observability</li>
                <li><b>Cloud-Native Architecture:</b> Kubernetes + Docker deployment</li>
                <li><b>Scalable Design:</b> Modular agent-based architecture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🌟 Key Highlights")
        st.markdown("""
        <div class="info-card">
            <ul style="line-height: 2; color: #e8e8e8;">
                <li><b>Agentic AI Workflows:</b> LangChain-powered reasoning</li>
                <li><b>Real-Time Generation:</b> Instant itinerary creation</li>
                <li><b>Interactive UI:</b> User-friendly Streamlit interface</li>
                <li><b>LLMOps Ready:</b> Complete monitoring pipeline</li>
                <li><b>DevOps Integration:</b> CI/CD ready architecture</li>
                <li><b>Recruiter-Friendly:</b> Production-grade portfolio project</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    

    # Resume Points (Expander)
    st.markdown("<h3 style='color: #2ecc71;'>🧠 Project Points</h3>", unsafe_allow_html=True)
    with st.expander("👉 Click to view Key Achievements & Bullets", expanded=False):
        st.markdown("""
<div class="success-box">
<h4 style="color: #00d4ff; margin-top: 0;">AI Travel Planner | GenAI, LLMOps, Kubernetes</h4>
<ul style="line-height: 1.8; color: #e8e8e8;">
<li>Built an agentic AI travel planner using <b>LangChain</b> and <b>Groq LLM</b> to generate personalized, multi-day itineraries based on user preferences and budget.</li>
<li>Designed a cloud-native architecture with <b>Docker</b> and <b>Kubernetes (Minikube)</b> for scalable deployment.</li>
<li>Implemented <b>LLMOps observability</b> using ELK Stack (Filebeat, Logstash, Elasticsearch, Kibana) for real-time monitoring and log analytics.</li>
<li>Developed an interactive <b>Streamlit UI</b> for real-time user interaction and itinerary visualization.</li>
<li>Applied <b>prompt engineering</b> and structured reasoning workflows to ensure coherent, context-aware travel planning.</li>
</ul>
</div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🏆 Project Positioning")
    st.markdown("""
    <div class="success-box">
        <p style="font-size: 1.1rem; margin: 0; color: #e8e8e8;">
            <b>Designed and deployed an Agentic AI Travel Planner</b> using LangChain and Groq LLM, 
            containerized with Docker, orchestrated via Kubernetes (Minikube), and monitored using 
            a full ELK-based LLMOps observability stack on GCP.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Tab 3: Tech Stack
with tab3:
    st.markdown("## 🛠️ Technology Stack & Infrastructure")
    


    st.markdown("### 🔧 Tech Stack Deep Dive")
    
    # 1. AI/GenAI
    with st.expander("🧠 1. AI / GenAI Layer (Groq & LangChain)", expanded=True):
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #00d4ff;">⚡ Groq (LLM – Free Tier)</h4>
            <ul style="color: #e8e8e8;">
                <li>Used as the Large Language Model for itinerary generation.</li>
                <li>Handles: Destination planning, Day-wise schedule creation, Budget-aware recommendations.</li>
                <li>Chosen for ultra-fast inference and cost efficiency.</li>
            </ul>
            <h4 style="color: #00d4ff;">🔗 LangChain</h4>
            <ul style="color: #e8e8e8;">
                <li>Acts as the GenAI orchestration framework.</li>
                <li>Responsible for: Prompt templates, Agent-style reasoning, Context chaining.</li>
                <li>Enables agentic travel planning workflows.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 2. Frontend
    with st.expander("🎨 2. Frontend Layer (Streamlit)", expanded=False):
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #00d4ff;">Streamlit</h4>
            <ul style="color: #e8e8e8;">
                <li>Used to build the interactive web UI.</li>
                <li>Features: User input forms, Real-time itinerary display, Clean responsive interface.</li>
                <li>Enables rapid prototyping + demo-ready UI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    # 3. Cloud
    with st.expander("☁️ 3. Cloud & Infrastructure (GCP)", expanded=False):
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #00d4ff;">GCP Virtual Machine</h4>
            <ul style="color: #e8e8e8;">
                <li>Hosts the complete application stack.</li>
                <li>Provides: Compute resources, Network access, Persistent runtime environment.</li>
                <li>Acts as the base infra for Kubernetes + Docker.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 4. Containerization
    with st.expander("🐳 4. Containerization & Orchestration", expanded=False):
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #00d4ff;">Docker</h4>
            <ul style="color: #e8e8e8;">
                <li>Containerizes: Streamlit frontend, LangChain backend.</li>
                <li>Ensures: Environment consistency, Easy deployment, Portability.</li>
            </ul>
            <h4 style="color: #00d4ff;">Minikube</h4>
            <ul style="color: #e8e8e8;">
                <li>Runs a local Kubernetes cluster inside the GCP VM.</li>
                <li>Used to simulate production-like K8s behavior (Pod lifecycle, Service exposure).</li>
            </ul>
            <h4 style="color: #00d4ff;">kubectl</h4>
            <ul style="color: #e8e8e8;">
                <li>CLI tool to deploy pods, expose services, and debug containers.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 5. Source Control
    with st.expander("🔁 5. Source Control (GitHub)", expanded=False):
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #00d4ff;">GitHub</h4>
            <ul style="color: #e8e8e8;">
                <li>Acts as SCM (Source Code Management).</li>
                <li>Used for: Version control, Collaboration, CI/CD readiness.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 6. Logging
    with st.expander("📊 6. Logging & Observability (ELK Stack)", expanded=False):
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #00d4ff;">Filebeat</h4>
            <ul style="color: #e8e8e8;">
                <li>Runs as a log collector; reads logs from Kubernetes pods.</li>
            </ul>
            <h4 style="color: #00d4ff;">Logstash</h4>
            <ul style="color: #e8e8e8;">
                <li>Processes incoming logs: Cleans raw data, Adds metadata.</li>
            </ul>
            <h4 style="color: #00d4ff;">Elasticsearch</h4>
            <ul style="color: #e8e8e8;">
                <li>Stores logs in searchable indexed format for fast querying.</li>
            </ul>
            <h4 style="color: #00d4ff;">Kibana</h4>
            <ul style="color: #e8e8e8;">
                <li>Visualization & dashboard layer (Error trends, Daily log counts).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🔗 End-to-End Flow")
    st.markdown("""
    <div class="info-card">
        <pre style="background: rgba(40, 44, 52, 1); color: #abb2bf; padding: 20px; border-radius: 8px; font-size: 14px; border: 1px solid #3e4451;">
User → Streamlit UI
     → LangChain Agent
     → Groq LLM
     → AI Travel Plan

App Logs
→ Filebeat
→ Logstash
→ Elasticsearch
→ Kibana Dashboard
        </pre>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Tech Stack Summary")
    st.markdown("""
    <div class="success-box">
        <ul style="columns: 2; -webkit-columns: 2; -moz-columns: 2; color: #e8e8e8;">
            <li><b>AI / GenAI:</b> Groq LLM, LangChain</li>
            <li><b>Frontend:</b> Streamlit</li>
            <li><b>Cloud:</b> Google Cloud VM</li>
            <li><b>DevOps:</b> Docker, Kubernetes (Minikube), kubectl</li>
            <li><b>Observability:</b> ELK Stack (Filebeat, Logstash, Elasticsearch, Kibana)</li>
            <li><b>Version Control:</b> GitHub</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Tab 4: HLD & LLD
with tab4:
    st.markdown("## 🏗️ High-Level (HLD) & Low-Level Design (LLD)")

    st.markdown("### 🆚 HLD vs LLD Comparison")
    st.markdown("""
    <div class="info-card">
    <table style="width:100%; color: #e8e8e8; border-collapse: collapse;">
      <tr style="border-bottom: 2px solid #555; text-align: left;">
        <th style="padding: 10px; color: #00d4ff;">Aspect</th>
        <th style="padding: 10px; color: #00d4ff;">HLD (High-Level Design)</th>
        <th style="padding: 10px; color: #00d4ff;">LLD (Low-Level Design)</th>
      </tr>
      <tr style="border-bottom: 1px solid #444;">
        <td style="padding: 8px;"><b>Focus</b></td>
        <td style="padding: 8px;">System architecture & components</td>
        <td style="padding: 8px;">Implementation details</td>
      </tr>
      <tr style="border-bottom: 1px solid #444;">
        <td style="padding: 8px;"><b>Audience</b></td>
        <td style="padding: 8px;">Architects, Interviewers, Stakeholders</td>
        <td style="padding: 8px;">Developers, DevOps, ML Engineers</td>
      </tr>
      <tr style="border-bottom: 1px solid #444;">
        <td style="padding: 8px;"><b>Tech Depth</b></td>
        <td style="padding: 8px;">What & Why</td>
        <td style="padding: 8px;">How</td>
      </tr>
      <tr>
        <td style="padding: 8px;"><b>Example</b></td>
        <td style="padding: 8px;">LangChain Agent calls Groq LLM</td>
        <td style="padding: 8px;">Prompt templates, Chain configs</td>
      </tr>
    </table>
    </div>
    """, unsafe_allow_html=True)

    # HLD Section
    st.markdown("### 🧠 High-Level Design (HLD)")
    st.info("🎯 Objective: Design a production-ready Agentic AI Travel Planner that generates personalized/budget-aware itineraries using Groq LLM reasoning.")
    
    # HLD Diagram
    col1, col2 = st.columns([1.5, 1])
    with col1:

        try:
            st.image(os.path.join(HLD_LLD_DIR, "Picture1.png"), use_container_width=True, caption="HLD Architecture Diagram")
        except:
            st.warning("HLD Diagram Placeholder")
    
    with col2:
        with st.expander("👉 HLD Component Breakdown", expanded=True):
            st.markdown("""
            <div class="info-card">
            <h4 style="color: #667eea;">1️⃣ User Interface Layer</h4>
            <ul><li>Streamlit Web App: Accepts destination, dates, budget. Displays itineraries.</li></ul>
            <h4 style="color: #667eea;">2️⃣ AI / GenAI Layer</h4>
            <ul><li>LangChain: Orchestrates prompts.</li><li>Groq LLM: Ultra-low latency generation.</li></ul>
            <h4 style="color: #667eea;">3️⃣ Application Layer</h4>
            <ul><li>Planner Logic, Budget Optimization.</li></ul>
            <h4 style="color: #667eea;">4️⃣ Infrastructure</h4>
            <ul><li>Docker, K8s (Minikube), GCP VM.</li></ul>
            <h4 style="color: #667eea;">5️⃣ Observability</h4>
            <ul><li>ELK Stack (Filebeat, Logstash, Elasticsearch, Kibana).</li></ul>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # LLD Section
    st.markdown("### 🔍 Low-Level Design (LLD)")
    
    with st.expander("👉 LLD Implementation Details", expanded=True):
        st.markdown("""
        <div class="info-card">
        <h4 style="color: #667eea;">1️⃣ Frontend (Streamlit)</h4>
        <ul><li>app.py: Input forms, Session State, API calls.</li></ul>
        <h4 style="color: #667eea;">2️⃣ Configuration & Chain</h4>
        <ul><li>config.py: API keys, Model params.</li><li>itinerary_chain.py: PromptTemplate, SequentialChain.</li></ul>
        <h4 style="color: #667eea;">3️⃣ Core Logic (planner.py)</h4>
        <ul><li>Combines user inputs + LangChain outputs -> Structured Itinerary.</li></ul>
        <h4 style="color: #667eea;">4️⃣ Deployment (K8s/Docker)</h4>
        <ul><li>Dockerfile: Base Python image.</li><li>deployment.yaml: Pods, Services, Limits.</li></ul>
        <h4 style="color: #667eea;">5️⃣ Logging Flow</h4>
        <ul><li>App -> Filebeat -> Logstash -> Elasticsearch -> Kibana.</li></ul>
        </div>
        """, unsafe_allow_html=True)
    
    # LLD Diagram
    try:
        st.image(os.path.join(HLD_LLD_DIR, "Picture3.png"), use_container_width=True, caption="Detailed LLD Flow Diagram")
    except:
        pass

    st.markdown("### 🔁 End-to-End Execution Flow")
    st.markdown("""
    <div class="success-box">
    <b>User Input</b> → Streamlit UI → Planner Controller → LangChain → Groq LLM → <b>Structured Plan</b> → UI Rendering<br>
    <br>
    <b>Logs (Parallel Flow):</b> App → Filebeat → Logstash → Elasticsearch → Kibana
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎤 Perfect Summary")
    st.markdown("""
    <div class="info-box">
    This system follows a layered HLD-driven GenAI architecture, where Streamlit handles user interaction, 
    LangChain orchestrates agentic LLM reasoning using Groq, Docker and Kubernetes enable scalable deployment, 
    and an ELK-based LLMOps pipeline ensures full observability and monitoring.
    </div>
    """, unsafe_allow_html=True)

# Tab 5: Architecture
with tab5:
    st.markdown("## 📐 System Architecture")
    
    st.info("🧠 One-Line Summary: This system follows a layered GenAI architecture, combining LangChain-based agentic reasoning, Dockerized microservices, Kubernetes orchestration, and a full ELK observability stack, deployed on a GCP VM for production-grade AI operations.")
    
    # Workflow Diagram
    col1, col2 = st.columns([2, 1])
    with col1:
        try:
            st.image(os.path.join(DIAGRAMS_DIR, "AI+travel+planner+Workflow.png"), use_container_width=True, caption="Detailed Architecture Workflow")
        except:
            st.warning("Architecture Diagram Placeholder")
    with col2:
         st.markdown("### 🏗️ Architecture Layers")
         st.markdown("""
         <div class="info-card">
         <ul style="color: #e8e8e8;">
         <li><b style="color: #667eea;">Blue:</b> Development Layer</li>
         <li><b style="color: #f1c40f;">Yellow:</b> Containerization</li>
         <li><b style="color: #9b59b6;">Purple:</b> Version Control</li>
         <li><b style="color: #2ecc71;">Green:</b> Build/Deploy</li>
         </ul>
         </div>
         """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("### 🛠️ Step-by-Step Implementation")
    
    with st.expander("🟦 1. DEVELOPMENT LAYER", expanded=True):
        st.markdown("""
        <div class="info-card">
        <h4 style="color: #667eea;">Step 1: Project & API Setup</h4>
        <ul><li>Initialize structure, Configure Groq API, Environment variables.</li></ul>
        <h4 style="color: #667eea;">Step 2: Configuration Code</h4>
        <ul><li>Centralized config for Model params (temp, tokens), Prompts.</li></ul>
        <h4 style="color: #667eea;">Step 3: Itinerary Chain Code (LangChain)</h4>
        <ul><li>Destination understanding, Day-wise itinerary, Budget-aware planning.</li></ul>
        <h4 style="color: #667eea;">Step 4: Travel Planner Core Logic</h4>
        <ul><li>Combines User inputs + LangChain chains + LLM responses.</li></ul>
        <h4 style="color: #667eea;">Step 5: Application Code (Streamlit)</h4>
        <ul><li>Builds frontend UI, Handles Input forms & API calls.</li></ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🟨 2. CONTAINERIZATION & DEPLOYMENT LAYER", expanded=False):
        st.markdown("""
        <div class="info-card">
        <h4 style="color: #f1c40f;">Step 6: Dockerfile</h4>
        <ul><li>Packages app into image. Ensures environment consistency.</li></ul>
        <h4 style="color: #f1c40f;">Step 7: Kubernetes Deployment</h4>
        <ul><li>Defines Pods, Services, Resource limits. Orchestration via Minikube.</li></ul>
        <h4 style="color: #f1c40f;">Step 8-11: ELK Stack Deployment</h4>
        <ul>
            <li><b>Filebeat:</b> Collects logs from containers.</li>
            <li><b>Logstash:</b> Processes, cleans, tags logs.</li>
            <li><b>Elasticsearch:</b> Stores logs (searchable).</li>
            <li><b>Kibana:</b> Visualizes logs (Dashboards).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🟪 3. VERSION CONTROL & CLOUD SETUP", expanded=False):
        st.markdown("""
        <div class="info-card">
        <h4 style="color: #9b59b6;">Step 12: Code Versioning (GitHub)</h4>
        <ul><li>SCM for history, collaboration, CI/CD.</li></ul>
        <h4 style="color: #9b59b6;">Step 13: GCP VM Setup</h4>
        <ul><li>Google Cloud VM with Docker, Minikube, kubectl.</li></ul>
        <h4 style="color: #9b59b6;">Step 14: Integrate GitHub with VM</h4>
        <ul><li>Pull code to VM for automated build.</li></ul>
        </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🟩 4. BUILD, DEPLOY & MONITOR", expanded=False):
        st.markdown("""
        <div class="info-card">
        <h4 style="color: #2ecc71;">Step 15: Build & Deploy on Kubernetes</h4>
        <ul><li>Build Docker image, Deploy to Minikube cluster as pods.</li></ul>
        <h4 style="color: #2ecc71;">Step 16: ELK Stack Setup</h4>
        <ul><li>Filebeat -> Logstash -> Elasticsearch. Centralized logging.</li></ul>
        <h4 style="color: #2ecc71;">Step 17: Monitoring with Kibana</h4>
        <ul><li>View dashboards (Errors, Latency, User activity).</li></ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔁 End-to-End Flow Summary")
    st.markdown("""
    <div class="success-box">
    <b>User Flow:</b> User → Streamlit UI → LangChain Agent → Groq LLM → Travel Itinerary<br>
    <br>
    <b>Logging Flow:</b> Logs → Filebeat → Logstash → Elasticsearch → Kibana Dashboards
    </div>
    """, unsafe_allow_html=True)

# Tab 6: System Logs
with tab6:
    st.markdown("## � System Logs & Activity Monitor")
    
    # Initialize logs if not exists
    if 'logs' not in st.session_state:
        st.session_state.logs = []
        # Add Startup Log
        ist_now = pytz.timezone('Asia/Kolkata')
        st.session_state.logs.append({
            'timestamp': datetime.now(ist_now).strftime("%Y-%m-%d %H:%M:%S IST"),
            'status': 'Success',
            'action': 'System Startup: Application Initialized',
            'city': 'System',
            'interests': 'N/A'
        })
    
    # 1. Metrics & Refresh
    # Calculate stats
    total_logs = len(st.session_state.logs)
    success_count = sum(1 for log in st.session_state.logs if log['status'] == 'Success')
    error_count = sum(1 for log in st.session_state.logs if log['status'] == 'Error')
    
    col_refresh, col_spacer = st.columns([1, 4])
    with col_refresh:
        if st.button("🔄 Refresh Logs", use_container_width=True):
             st.rerun()

    # Premium Metrics Cards
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
        <div style='background: rgba(40, 116, 240, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2874f0; text-align: center;'>
            <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>TOTAL LOGS</h4>
            <p style='color: #2874f0; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{total_logs}</p>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div style='background: rgba(46, 204, 113, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2ecc71; text-align: center;'>
            <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>SUCCESS</h4>
            <p style='color: #2ecc71; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{success_count}</p>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        err_color = "#e74c3c" if error_count > 0 else "#95a5a6"
        st.markdown(f"""
        <div style='background: rgba(231, 76, 60, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid {err_color}; text-align: center;'>
            <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>ERRORS</h4>
            <p style='color: {err_color}; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{error_count}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 2. Filters & Actions
    col_filter1, col_filter2 = st.columns([3, 1])
    with col_filter1:
        status_filter = st.multiselect(
            "� Filter Logs by Status", 
            ["Success", "Error"], 
            default=["Success", "Error"]
        )
    with col_filter2:
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        # Prepare text for download
        log_text = "\n".join([f"[{l['timestamp']}] [{l['status']}] {l['action']} | City: {l.get('city','')} | Error: {l.get('error','')}" for l in st.session_state.logs])
        st.download_button(
            label="📥 Download Logs",
            data=log_text,
            file_name=f"system_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

    # Filter Logic
    filtered_logs = [log for log in st.session_state.logs if log['status'] in status_filter]
    
    # 3. Log Feed
    st.markdown("### 📜 Activity Log Feed")
    log_container = st.container(height=500, border=True)
    
    with log_container:
        if filtered_logs:
            for idx, log in enumerate(reversed(filtered_logs)):
                status_icon = "✅" if log['status'] == 'Success' else "❌"
                status_color = "#11998e" if log['status'] == 'Success' else "#e74c3c"
                
                st.markdown(f"""
                <div class="log-entry" style="border-left: 4px solid {status_color}; background: rgba(20, 30, 48, 0.6); padding: 12px; margin-bottom: 8px; border-radius: 6px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-family: 'Courier New', monospace; font-size: 0.85rem; color: #f1c40f;">🕐 {log['timestamp']}</span>
                        <span style="background: {status_color}; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">
                            {status_icon} {log['status']}
                        </span>
                    </div>
                    <div style="margin-top: 8px; font-size: 0.95rem; color: #e8e8e8;">
                        <span style="color: #667eea; font-weight: bold;">Action:</span> {log['action']}
                    </div>
                    <div style="margin-top: 4px; font-size: 0.9rem; color: #bdc3c7;">
                         <span style="color: #667eea;">City:</span> {log.get('city', 'N/A')} &nbsp;|&nbsp; 
                         <span style="color: #667eea;">Interests:</span> {log.get('interests', 'N/A')}
                    </div>
                    {f"<div style='margin-top: 4px; color: #e74c3c; font-weight: bold;'>⚠️ Error: {log.get('error', '')}</div>" if log['status'] == 'Error' else ''}
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander(f"📄 View Raw Details"):
                    st.json(log)
        else:
            if st.session_state.logs:
                st.info("No logs match your filter criteria.")
            else:
                 st.markdown("""
                 <div class="info-card" style="text-align: center; padding: 40px;">
                    <h3 style="color: #999;">📭 No logs available</h3>
                    <p style="color: #666;">Generate an itinerary in the Demo tab to see logs here</p>
                 </div>
                 """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ System Information")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #667eea;">🖥️ Application Details</h4>
            <ul>
                <li><b>App Name:</b> AI Travel Planner </li>
                <li><b>Version:</b> 1.0.0</li>
                <li><b>Framework:</b> Streamlit</li>
                <li><b>Python Version:</b> 3.11.2</li>
                <li><b>LLM Provider:</b> Groq</li>
                <li><b>Model:</b> llama-3.3-70b-versatile</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #667eea;">📊 Monitoring Stack</h4>
            <ul>
                <li><b>Log Collection:</b> Filebeat</li>
                <li><b>Log Processing:</b> Logstash</li>
                <li><b>Log Storage:</b> Elasticsearch</li>
                <li><b>Visualization:</b> Kibana</li>
                <li><b>Containerization:</b> Docker</li>
                <li><b>Orchestration:</b> Kubernetes (Minikube)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### 🖼️ Log Architecture & Data Flow")
    
    # Add ELK Stack Diagrams (Grid Layout)
    try:
        dc1, dc2 = st.columns(2)
        
        with dc1:
            st.markdown("#### 1. 🔄 Data Flow")
            st.image(os.path.join(DIAGRAMS_DIR, "ELK_Flow.jpg"), width=450, caption="ELK Stack Data Flow")
            
            st.markdown("#### 3. 🚀 Deployment")
            st.image(os.path.join(DIAGRAMS_DIR, "ELK_Deployment.jpg"), width=450, caption="Production Deployment Architecture")
            
            st.markdown("#### 5. 📑 Vertical Stack")
            st.image(os.path.join(DIAGRAMS_DIR, "ELK_Vertical.png"), width=450, caption="ELK Stack Layers")

        with dc2:
            st.markdown("#### 2. 🧱 Components")
            st.image(os.path.join(DIAGRAMS_DIR, "ELK_Components.png"), width=450, caption="ELK Components Breakdown")

            st.markdown("#### 4. ☸️ Kubernetes Logic")
            st.image(os.path.join(DIAGRAMS_DIR, "ELK_Kubernetes.png"), width=450, caption="Kubernetes & ELK Integration")
            
    except:
        st.caption("Diagrams not available")

# Footer
st.markdown("---")

# Footer container
st.markdown("""
<div style='text-align: center; padding: 20px 20px 10px 20px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 10px; border-top: 2px solid #2874f0;'>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>✈️ AI Travel Planner Dashboard</p>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>Built with ❤️ by Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer) | 4+ Years Experience</p>
    <p style='font-size: 0.9rem; color: #e8e8e8; margin-bottom: 5px;'>Powered by LangChain, Groq, Docker, Kubernetes, ELK Stack, and Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Social links using Streamlit columns (inside the visual footer area)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col2:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://github.com/Ratnesh-181998" target="_blank" style="text-decoration: none; color: #2874f0; font-size: 1.1rem; font-weight: 600;">🔗 GitHub</a></p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="mailto:rattudacsit2021gate@gmail.com" style="text-decoration: none; color: #26a65b; font-size: 1.1rem; font-weight: 600;">📧 Email</a></p>', unsafe_allow_html=True)

with col4:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://www.linkedin.com/in/ratneshkumar1998/" target="_blank" style="text-decoration: none; color: #0077b5; font-size: 1.1rem; font-weight: 600;">💼 LinkedIn</a></p>', unsafe_allow_html=True)

# Close the visual footer
st.markdown("""
<div style='height: 10px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 0 0 10px 10px; border-bottom: 2px solid #2874f0; margin-top: -10px;'></div>
""", unsafe_allow_html=True)

