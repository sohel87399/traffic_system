#!/usr/bin/env python3
"""
Test script to verify deployment readiness
"""

def test_imports():
    """Test all required imports"""
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
        
        import cv2
        print("✅ OpenCV imported successfully")
        
        import numpy as np
        print("✅ NumPy imported successfully")
        
        import pandas as pd
        print("✅ Pandas imported successfully")
        
        from datetime import datetime
        print("✅ DateTime imported successfully")
        
        print("\n🎉 All core dependencies are working!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_app_structure():
    """Test if app structure is correct"""
    import os
    
    required_files = [
        'app.py',
        'requirements.txt',
        'Scripts/traffic_dashboard.py',
        'Scripts/detector.py',
        'Scripts/tracker.py',
        'Scripts/video_processor.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
        return True

if __name__ == "__main__":
    print("🧪 Testing deployment readiness...\n")
    
    imports_ok = test_imports()
    structure_ok = test_app_structure()
    
    if imports_ok and structure_ok:
        print("\n🚀 Deployment ready! Your app should work on Streamlit Cloud.")
    else:
        print("\n⚠️ Some issues found. Please fix before deploying.")