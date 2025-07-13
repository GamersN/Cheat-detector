import cv2

class Overlay:
    def __init__(self):
        self.window_name = "FPS Snap Monitor"

    def update(self, frame, status=[]):
        h, w, _ = frame.shape
        overlay = frame.copy()
        cv2.circle(overlay, (w//2, h//2), 10, (0, 255, 0), 2)
        y0, dy = 30, 30
        for i, line in enumerate(status):
            y = y0 + i*dy
            color = (0, 0, 255) if "Snap" in line else (0, 255, 0)
            cv2.putText(overlay, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX,
                        1, color, 2, cv2.LINE_AA)
        cv2.imshow(self.window_name, overlay)
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            exit()
