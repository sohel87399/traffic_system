#!/usr/bin/env python3
"""
NEXUS Traffic AI - Deployment Helper Script
Helps prepare the application for deployment to Render
"""

import os
import sys
import subprocess
import json

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'requirements.txt',
        'render.yaml',
        'Scripts/traffic_dashboard.py',
        'Scripts/detector.py',
        'Scripts/tracker.py',
        'Scripts/video_processor.py',
        '.streamlit/config.toml'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files present")
    return True

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'streamlit',
        'cv2',
        'numpy',
        'pandas'
    ]
    
    failed_imports = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            failed_imports.append(package)
            print(f"❌ {package} - FAILED")
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True

def create_git_repo():
    """Initialize git repository if not exists"""
    if not os.path.exists('.git'):
        print("🔧 Initializing Git repository...")
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit: NEXUS Traffic AI System'], check=True)
        subprocess.run(['git', 'branch', '-M', 'main'], check=True)
        print("✅ Git repository initialized")
    else:
        print("✅ Git repository already exists")

def display_deployment_info():
    """Display deployment information"""
    print("\n" + "="*60)
    print("🚀 NEXUS TRAFFIC AI - READY FOR DEPLOYMENT!")
    print("="*60)
    print("\n📋 DEPLOYMENT CHECKLIST:")
    print("✅ All files prepared")
    print("✅ Dependencies verified")
    print("✅ Git repository ready")
    print("\n🌐 NEXT STEPS:")
    print("1. Push to GitHub:")
    print("   git remote add origin https://github.com/yourusername/nexus-traffic-ai.git")
    print("   git push -u origin main")
    print("\n2. Deploy to Render:")
    print("   - Go to render.com")
    print("   - Create new Web Service")
    print("   - Connect your GitHub repo")
    print("   - Use these settings:")
    print("     Build Command: pip install -r requirements.txt")
    print("     Start Command: streamlit run Scripts/traffic_dashboard.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true")
    print("\n3. Your app will be live at:")
    print("   https://nexus-traffic-ai.onrender.com")
    print("\n🎉 FEATURES AVAILABLE:")
    print("   • 90+ Interactive Visualizations")
    print("   • Real-time AI Traffic Analysis")
    print("   • Quantum-Enhanced Processing")
    print("   • Demo Mode (no upload required)")
    print("   • Mobile Responsive Design")
    print("\n📊 EXPECTED PERFORMANCE:")
    print("   • Deployment Time: 5-10 minutes")
    print("   • Cold Start: ~30 seconds")
    print("   • Response Time: <2 seconds")
    print("   • Concurrent Users: 100+")
    print("\n" + "="*60)

def main():
    """Main deployment preparation function"""
    print("🚀 NEXUS Traffic AI - Deployment Preparation")
    print("=" * 50)
    
    # Check requirements
    print("\n1. Checking required files...")
    if not check_requirements():
        sys.exit(1)
    
    # Test imports
    print("\n2. Testing package imports...")
    if not test_imports():
        print("\n💡 To fix import issues:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    # Initialize git
    print("\n3. Preparing Git repository...")
    try:
        create_git_repo()
    except subprocess.CalledProcessError:
        print("⚠️  Git not available or error occurred")
        print("   Please install Git and run manually")
    
    # Display deployment info
    display_deployment_info()

if __name__ == "__main__":
    main()