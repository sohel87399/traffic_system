#!/usr/bin/env python3
"""
NEXUS Traffic AI Command Center
Entry point for the application
"""

import sys
import os

# Add Scripts directory to path
scripts_path = os.path.join(os.path.dirname(__file__), 'Scripts')
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)

# Import and run the main dashboard directly
try:
    # Import the dashboard module
    import traffic_dashboard
    
    # The dashboard will run automatically when imported
    # since it contains the streamlit code
    
except ImportError as e:
    import streamlit as st
    st.error(f"Error importing traffic_dashboard: {e}")
    st.info("Please ensure all required files are present in the Scripts directory.")
except Exception as e:
    import streamlit as st
    st.error(f"Application error: {e}")
    st.info("Please check the application logs for more details.")