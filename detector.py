import time
import numpy as np

class SnapDetector:
    def __init__(self, snap_threshold=100, speed_threshold=1800):
        self.last_position = None
        self.last_time = None
        self.snap_threshold = snap_threshold
        self.speed_threshold = speed_threshold

    def detect(self, frame):
        h, w, _ = frame.shape
        current = (w // 2, h // 2)
        current_time = time.time()

        if self.last_position and self.last_time:
            dx = current[0] - self.last_position[0]
            dy = current[1] - self.last_position[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5
            dt = current_time - self.last_time
            speed = distance / dt if dt > 0 else 0

            self.last_position = current
            self.last_time = current_time

            if distance > self.snap_threshold or speed > self.speed_threshold:
                return True, speed
            else:
                return False, speed

        self.last_position = current
        self.last_time = current_time
        return False, 0
