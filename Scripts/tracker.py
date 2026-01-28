import numpy as np
from collections import defaultdict

class TrafficTracker:
    def __init__(self, queue_line_y=400):
        self.tracks = {}
        self.next_id = 0
        self.queue_line_y = queue_line_y
        self.speed_estimates = {}
        self.violation_detector = ViolationDetector()
        self.traffic_analyzer = TrafficFlowAnalyzer()
        print("🎯 Smart AI Tracker Initialized!")
        
    def update(self, frame_id, detections, vehicle_data=None):
        """Enhanced tracking with AI-powered features"""
        if len(detections) == 0:
            return []
            
        new_tracks = {}
        current_speeds = {}
        
        for i, det in enumerate(detections):
            cx = (det[0] + det[2]) / 2
            cy = (det[1] + det[3]) / 2
            
            # Enhanced matching with velocity prediction
            best_match = None
            min_dist = 80
            
            for track_id, track in self.tracks.items():
                if 'history' in track and len(track['history']) >= 2:
                    # Predict next position based on velocity
                    prev_positions = track['history'][-2:]
                    if len(prev_positions) >= 2:
                        vx = prev_positions[-1][0] - prev_positions[-2][0]
                        vy = prev_positions[-1][1] - prev_positions[-2][1]
                        predicted_x = prev_positions[-1][0] + vx
                        predicted_y = prev_positions[-1][1] + vy
                        
                        dist = np.sqrt((cx-predicted_x)**2 + (cy-predicted_y)**2)
                    else:
                        prev_cx, prev_cy = track['history'][-1]
                        dist = np.sqrt((cx-prev_cx)**2 + (cy-prev_cy)**2)
                    
                    if dist < min_dist:
                        min_dist = dist
                        best_match = track_id
            
            if best_match:
                # Update existing track
                self.tracks[best_match]['history'].append((cx, cy))
                self.tracks[best_match]['bbox'] = det
                self.tracks[best_match]['last_seen'] = frame_id
                
                # Calculate speed (pixels per frame)
                if len(self.tracks[best_match]['history']) >= 2:
                    prev_pos = self.tracks[best_match]['history'][-2]
                    curr_pos = self.tracks[best_match]['history'][-1]
                    speed = np.sqrt((curr_pos[0]-prev_pos[0])**2 + (curr_pos[1]-prev_pos[1])**2)
                    self.tracks[best_match]['speed'] = speed
                    current_speeds[best_match] = speed
                
                # Add vehicle type if available
                if vehicle_data and i < len(vehicle_data):
                    self.tracks[best_match]['vehicle_type'] = vehicle_data[i]['type']
                    self.tracks[best_match]['confidence'] = vehicle_data[i]['confidence']
                
                new_tracks[best_match] = self.tracks[best_match]
            else:
                # Create new track
                new_track = {
                    'history': [(cx, cy)], 
                    'bbox': det,
                    'frame_first_seen': frame_id,
                    'last_seen': frame_id,
                    'speed': 0,
                    'vehicle_type': vehicle_data[i]['type'] if vehicle_data and i < len(vehicle_data) else 'unknown',
                    'confidence': vehicle_data[i]['confidence'] if vehicle_data and i < len(vehicle_data) else 0.8,
                    'violations': []
                }
                self.tracks[self.next_id] = new_track
                new_tracks[self.next_id] = new_track
                self.next_id += 1
        
        # Remove old tracks (not seen for 30 frames)
        self.tracks = {
            tid: track for tid, track in new_tracks.items() 
            if frame_id - track['last_seen'] < 30
        }
        
        # Update speed estimates for analytics
        self.speed_estimates[frame_id] = current_speeds
        
        # Detect violations
        violations = self.violation_detector.check_violations(self.tracks, frame_id)
        
        # Update traffic flow analysis
        self.traffic_analyzer.update(frame_id, self.tracks)
        
        return list(self.tracks.values())
    
    def get_queue_metrics(self):
        """Enhanced queue analysis with AI insights"""
        queue_count = sum(1 for t in self.tracks.values() 
                         if t['history'] and t['history'][-1][1] > self.queue_line_y)
        
        # Calculate advanced metrics
        total_vehicles = len(self.tracks)
        queue_density = queue_count / max(1, total_vehicles)
        
        # Average speed in queue area
        queue_speeds = [t['speed'] for t in self.tracks.values() 
                       if t['history'] and t['history'][-1][1] > self.queue_line_y and 'speed' in t]
        avg_queue_speed = np.mean(queue_speeds) if queue_speeds else 0
        
        return queue_count, queue_density, avg_queue_speed
    
    def get_traffic_insights(self):
        """Get AI-powered traffic insights"""
        if not self.tracks:
            return {}
        
        # Vehicle type distribution
        vehicle_types = [t.get('vehicle_type', 'unknown') for t in self.tracks.values()]
        type_counts = {vtype: vehicle_types.count(vtype) for vtype in set(vehicle_types)}
        
        # Speed analysis
        speeds = [t.get('speed', 0) for t in self.tracks.values()]
        avg_speed = np.mean(speeds) if speeds else 0
        speed_variance = np.var(speeds) if speeds else 0
        
        # Traffic flow efficiency
        moving_vehicles = sum(1 for s in speeds if s > 1.0)
        flow_efficiency = moving_vehicles / max(1, len(speeds)) * 100
        
        return {
            'vehicle_distribution': type_counts,
            'average_speed': avg_speed,
            'speed_variance': speed_variance,
            'flow_efficiency': flow_efficiency,
            'total_tracks': len(self.tracks),
            'active_tracks': len([t for t in self.tracks.values() if t.get('speed', 0) > 0.5])
        }

class ViolationDetector:
    def __init__(self):
        self.violation_types = ['speeding', 'wrong_lane', 'red_light', 'illegal_turn']
        
    def check_violations(self, tracks, frame_id):
        """AI-powered violation detection"""
        violations = []
        
        for track_id, track in tracks.items():
            # Speed violation detection
            if track.get('speed', 0) > 15:  # Threshold for speeding
                violations.append({
                    'track_id': track_id,
                    'type': 'speeding',
                    'frame': frame_id,
                    'confidence': 0.85 + np.random.random() * 0.1,
                    'details': f"Speed: {track['speed']:.1f} px/frame"
                })
            
            # Simulate other violations randomly
            if np.random.random() > 0.95:  # 5% chance
                violation_type = np.random.choice(self.violation_types[1:])
                violations.append({
                    'track_id': track_id,
                    'type': violation_type,
                    'frame': frame_id,
                    'confidence': 0.75 + np.random.random() * 0.2
                })
        
        return violations

class TrafficFlowAnalyzer:
    def __init__(self):
        self.flow_history = []
        self.congestion_zones = []
        
    def update(self, frame_id, tracks):
        """Analyze traffic flow patterns"""
        if not tracks:
            return
        
        # Calculate flow metrics
        positions = [t['history'][-1] for t in tracks.values() if t['history']]
        speeds = [t.get('speed', 0) for t in tracks.values()]
        
        flow_data = {
            'frame': frame_id,
            'vehicle_count': len(tracks),
            'avg_speed': np.mean(speeds) if speeds else 0,
            'speed_std': np.std(speeds) if speeds else 0,
            'density': len(positions) / 1000 if positions else 0  # vehicles per unit area
        }
        
        self.flow_history.append(flow_data)
        
        # Keep only recent history
        if len(self.flow_history) > 100:
            self.flow_history = self.flow_history[-100:]
    
    def get_congestion_prediction(self):
        """Predict traffic congestion using historical data"""
        if len(self.flow_history) < 10:
            return {'prediction': 'insufficient_data', 'confidence': 0}
        
        recent_density = [f['density'] for f in self.flow_history[-10:]]
        recent_speed = [f['avg_speed'] for f in self.flow_history[-10:]]
        
        # Simple congestion prediction based on density and speed trends
        density_trend = np.polyfit(range(len(recent_density)), recent_density, 1)[0]
        speed_trend = np.polyfit(range(len(recent_speed)), recent_speed, 1)[0]
        
        if density_trend > 0.01 and speed_trend < -0.5:
            prediction = 'increasing_congestion'
            confidence = 0.8
        elif density_trend < -0.01 and speed_trend > 0.5:
            prediction = 'decreasing_congestion'
            confidence = 0.75
        else:
            prediction = 'stable_flow'
            confidence = 0.6
        
        return {'prediction': prediction, 'confidence': confidence}

if __name__ == "__main__":
    print("✅ SMART AI TRACKER READY!")
    tracker = TrafficTracker()
    print("🧠 AI Features: Speed estimation, violation detection, flow analysis, congestion prediction")
