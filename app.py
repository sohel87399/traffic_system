#!/usr/bin/env python3
"""
NEXUS Traffic AI Command Center
Entry point for the application
"""

import sys
import os

# Add Scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Scripts'))

# Import and run the main dashboard
if __name__ == "__main__":
    import subprocess
    subprocess.run([
        "python", "-m", "streamlit", "run", 
        "Scripts/traffic_dashboard.py",
        "--server.headless=true",
        "--server.fileWatcherType=none",
        "--browser.gatherUsageStats=false"
    ])