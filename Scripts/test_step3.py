from video_processor import extract_frames
from detector import VehicleDetector

print("🚦 STEP 3: DETECTION TEST")
frames = extract_frames("traffic.mp4")
detector = VehicleDetector()

# Test first 10 frames
for i, frame in enumerate(frames[:10]):
    boxes = detector.detect(frame)
    print(f"Frame {i+1}: {len(boxes)} vehicles detected")

print("✅ DETECTION WORKING!")
