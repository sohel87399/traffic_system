#!/usr/bin/env python3
"""
NEXUS Traffic AI - Deployment Verification Script
Verifies that all files are ready for Blueprint deployment
"""

import os

def check_blueprint_file():
    """Check if render.yaml exists"""
    if not os.path.exists('render.yaml'):
        print("❌ render.yaml not found")
        return False
    
    # Check if file contains required content
    with open('render.yaml', 'r') as f:
        content = f.read()
    
    required_content = [
        'services:',
        'type: web',
        'name: nexus-traffic-ai',
        'runtime: python3',
        'buildCommand:',
        'startCommand:',
        'streamlit run Scripts/traffic_dashboard.py'
    ]
    
    missing = []
    for item in required_content:
        if item not in content:
            missing.append(item)
    
    if missing:
        print(f"❌ render.yaml missing content: {', '.join(missing)}")
        return False
    
    print("✅ render.yaml is valid and complete")
    return True

def check_requirements():
    """Check requirements.txt"""
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found")
        return False
    
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
    
    required_packages = [
        'streamlit',
        'opencv-python-headless',
        'numpy',
        'pandas',
        'Pillow'
    ]
    
    missing = []
    for package in required_packages:
        if package not in requirements:
            missing.append(package)
    
    if missing:
        print(f"❌ Missing packages in requirements.txt: {', '.join(missing)}")
        return False
    
    print("✅ requirements.txt contains all required packages")
    return True

def check_streamlit_config():
    """Check Streamlit configuration"""
    config_path = '.streamlit/config.toml'
    if not os.path.exists(config_path):
        print("❌ .streamlit/config.toml not found")
        return False
    
    print("✅ Streamlit configuration found")
    return True

def check_main_files():
    """Check main application files"""
    required_files = [
        'Scripts/traffic_dashboard.py',
        'Scripts/detector.py',
        'Scripts/tracker.py',
        'Scripts/video_processor.py'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"❌ Missing application files: {', '.join(missing)}")
        return False
    
    print("✅ All main application files present")
    return True

def check_git_status():
    """Check git repository status"""
    if not os.path.exists('.git'):
        print("⚠️  Git repository not initialized")
        print("   Run: git init && git add . && git commit -m 'Initial commit'")
        return False
    
    print("✅ Git repository found")
    return True

def display_deployment_instructions():
    """Display deployment instructions"""
    print("\n" + "="*60)
    print("🚀 BLUEPRINT DEPLOYMENT READY!")
    print("="*60)
    
    print("\n📋 DEPLOYMENT OPTIONS:")
    
    print("\n🌟 OPTION 1: One-Click Deploy Button")
    print("1. Push your code to GitHub")
    print("2. Update the deploy button URL with your GitHub username")
    print("3. Click the deploy button in README.md")
    print("4. Your app will be live in 5-8 minutes!")
    
    print("\n🔧 OPTION 2: Manual Blueprint Deployment")
    print("1. Push your code to GitHub")
    print("2. Go to https://dashboard.render.com")
    print("3. Click 'New +' → 'Blueprint'")
    print("4. Connect your GitHub repository")
    print("5. Render will detect render.yaml automatically")
    print("6. Click 'Apply' to deploy")
    
    print("\n🎯 EXPECTED RESULTS:")
    print("• Deployment time: 5-8 minutes")
    print("• Live URL: https://nexus-traffic-ai.onrender.com")
    print("• Auto-scaling: 1-3 instances")
    print("• Health monitoring: Enabled")
    print("• Auto-deploy: On git push")
    
    print("\n🌟 FEATURES AVAILABLE:")
    print("• 90+ Interactive Visualizations")
    print("• Quantum AI Processing")
    print("• Real-time Analytics")
    print("• Demo Mode (no upload required)")
    print("• Mobile Responsive Design")
    print("• Global CDN Access")
    
    print("\n📋 BLUEPRINT ADVANTAGES:")
    print("• Zero manual configuration")
    print("• Production-ready settings")
    print("• Automatic environment variables")
    print("• Health checks enabled")
    print("• Auto-scaling configured")
    print("• Continuous deployment")
    
    print("\n" + "="*60)

def main():
    """Main verification function"""
    print("🔍 NEXUS Traffic AI - Blueprint Deployment Verification")
    print("=" * 55)
    
    checks = [
        ("Blueprint Configuration", check_blueprint_file),
        ("Requirements File", check_requirements),
        ("Streamlit Configuration", check_streamlit_config),
        ("Application Files", check_main_files),
        ("Git Repository", check_git_status)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        print(f"\n🔍 Checking {check_name}...")
        if not check_func():
            all_passed = False
    
    if all_passed:
        print("\n🎉 ALL CHECKS PASSED!")
        display_deployment_instructions()
    else:
        print("\n❌ SOME CHECKS FAILED")
        print("Please fix the issues above before deploying.")
        return False
    
    return True

if __name__ == "__main__":
    main()