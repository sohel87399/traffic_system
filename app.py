#!/usr/bin/env python3
"""
NEXUS Traffic AI Command Center
Streamlit Cloud Compatible Version
"""

import streamlit as st
import sys
import os

# Add Scripts directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.join(current_dir, 'Scripts')
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

# Set page config
st.set_page_config(
    page_title="NEXUS Traffic AI System",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import the main dashboard
try:
    # Try to run the main dashboard
    exec(open(os.path.join(scripts_dir, 'traffic_dashboard.py')).read())
except Exception as e:
    # Fallback simple dashboard
    st.title("🚦 NEXUS Traffic AI System")
    st.error(f"Loading main dashboard... {str(e)}")
    
    # Simple fallback interface
    st.markdown("""
    ## 🌟 Professional Traffic Management System
    
    **Features:**
    - Real-time traffic analysis
    - AI-powered vehicle detection  
    - Professional dark theme interface
    - Interactive analytics dashboard
    
    **Status:** Initializing system components...
    """)
    
    if st.button("🔄 Reload System"):
        st.rerun()