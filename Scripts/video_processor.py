import cv2
import os
import numpy as np

def extract_frames(video_path, skip_frames=3):
    if not os.path.exists(video_path):
        print(f"❌ Video not found: {video_path}")
        return []
    
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f"📹 Video: {os.path.basename(video_path)}")
    print(f"⏱️ FPS: {fps:.1f} | Total frames: {total_frames}")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        if frame_count % skip_frames == 0:
            frames.append(frame)
        frame_count += 1
        if frame_count % 100 == 0:
            print(f"⏳ Processed {frame_count}/{total_frames} frames")
    
    cap.release()
    print(f"✅ Extracted {len(frames)} frames")
    return frames

def save_sample_frame(frames, output_path="sample_frame.jpg"):
    if frames:
        cv2.imwrite(output_path, frames[0])
        print(f"🖼️ Saved sample: {output_path}")
    return output_path

if __name__ == "__main__":
    video_name = "traffic.mp4"
    frames = extract_frames(video_name)
    if frames:
        save_sample_frame(frames)
        print("🎉 VIDEO PROCESSING SUCCESS!")
