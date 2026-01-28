from video_processor import extract_frames
from detector import VehicleDetector
from tracker import TrafficTracker
import numpy as np

print("🚦 FULL TRAFFIC PIPELINE - STEP 4")
print("=" * 50)

detector = VehicleDetector()
tracker = TrafficTracker()

frames = extract_frames("traffic.mp4")
metrics = []

print(f"\n📊 ANALYZING FIRST 20 FRAMES...\n")

for frame_id, frame in enumerate(frames[:20]):
    boxes = detector.detect(frame)
    tracks = tracker.update(frame_id, boxes)
    queue_len, density = tracker.get_queue_metrics()
    
    print(f"Frame {frame_id:2d}: {len(boxes)}→{len(tracks)} | Queue: {queue_len}")
    
    metrics.append({
        'frame': frame_id,
        'vehicles': len(boxes),
        'tracks': len(tracks),
        'queue': queue_len
    })

print("\n✅ STEP 4 COMPLETE!")
print(f"📈 Max queue: {max(m['queue'] for m in metrics)} vehicles")
print(f"🚗 Total unique tracks: {tracker.next_id}")
