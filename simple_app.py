import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="NEXUS Traffic AI System",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark theme colors
bg_primary = "#0f172a"
bg_secondary = "#1e293b"
bg_card = "#1e293b"
text_primary = "#f1f5f9"
text_secondary = "#cbd5e1"
text_muted = "#94a3b8"
border_color = "#334155"
accent_primary = "#667eea"
accent_secondary = "#764ba2"

# Custom CSS for dark theme
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    
    .stApp {{
        background: {bg_primary} !important;
        color: {text_primary} !important;
        font-family: 'Inter', sans-serif !important;
    }}
    
    .main-header {{
        background: linear-gradient(135deg, {accent_primary} 0%, {accent_secondary} 100%);
        padding: 40px 48px;
        border-radius: 20px;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 40px;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
    }}
    
    .metric-card {{
        background: {bg_card} !important;
        padding: 32px 36px;
        border-radius: 20px;
        color: {text_primary} !important;
        text-align: center;
        margin: 20px 0;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid {border_color};
    }}
    
    h1, h2, h3, p, div, span {{
        color: {text_primary} !important;
        font-family: 'Inter', sans-serif !important;
    }}
    
    .stMetric {{
        background: {bg_card} !important;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid {border_color};
    }}
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<div class="main-header"><h1>🚦 NEXUS Traffic AI System</h1><p>Enterprise-Grade Traffic Monitoring & Control Platform</p></div>', unsafe_allow_html=True)

# System Status
st.markdown("## System Status Overview")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("AI Processing", "ONLINE", delta="94.7% accuracy")
with col2:
    st.metric("Traffic Control", "ACTIVE", delta="23% improvement")
with col3:
    st.metric("Data Processing", "RUNNING", delta="1.2K fps")
with col4:
    st.metric("System Status", "OPERATIONAL", delta="99.9% uptime")

# Sidebar
st.sidebar.markdown("## System Control Panel")
st.sidebar.success("● All Systems Operational")

st.sidebar.markdown("### Processing Configuration")
ai_mode = st.sidebar.selectbox("Detection Mode", 
    ["Standard Detection", "Enhanced Analysis", "Real-time Processing"])

st.sidebar.markdown("### Traffic Management")
st.sidebar.checkbox("Adaptive Signal Control", value=True)
st.sidebar.checkbox("Violation Detection", value=True)
st.sidebar.checkbox("Congestion Analysis", value=True)

# Demo data
st.markdown("## Live Traffic Analytics")

# Generate sample data
dates = pd.date_range(start=datetime.now() - timedelta(hours=24), end=datetime.now(), freq='H')
traffic_data = pd.DataFrame({
    'Time': dates,
    'Vehicle Count': np.random.randint(50, 200, len(dates)),
    'Congestion Level': np.random.randint(20, 80, len(dates)),
    'Average Speed': np.random.randint(25, 65, len(dates))
})

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Traffic Volume (24h)")
    st.line_chart(traffic_data.set_index('Time')['Vehicle Count'])

with col2:
    st.subheader("Congestion Levels")
    st.area_chart(traffic_data.set_index('Time')['Congestion Level'])

# Data table
st.subheader("Real-time Traffic Data")
st.dataframe(traffic_data.tail(10), use_container_width=True)

# File upload
st.markdown("## Video Analysis")
uploaded_file = st.file_uploader("Upload Traffic Video", type=['mp4'])

if uploaded_file:
    st.success("Video uploaded successfully! Processing...")
    st.info("🎯 AI Analysis Results:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Vehicles Detected", "47", delta="+12")
    with col2:
        st.metric("Violations Found", "3", delta="-2")
    with col3:
        st.metric("Processing Time", "2.3s", delta="-0.5s")

# Footer
st.markdown("---")
st.markdown("### NEXUS Traffic AI System v2.1")
st.markdown("*Enterprise-Grade Traffic Monitoring & Control Platform | Powered by Advanced AI Analytics*")