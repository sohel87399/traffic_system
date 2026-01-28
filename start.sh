#!/bin/bash

# Make sure we're in the right directory
cd /opt/render/project/src

# Start the Streamlit application
streamlit run Scripts/traffic_dashboard.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.fileWatcherType=none \
    --browser.gatherUsageStats=false \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false