from screen_capture import grab_screen
from detector import SnapDetector
from overlay import Overlay

def main():
    detector = SnapDetector()
    overlay = Overlay()

    print("Monitoring gameplay for cheat-like snap movements. Press ESC to quit.")
    while True:
        frame = grab_screen()
        snap, speed = detector.detect(frame)
        status = [f"Aim Speed: {int(speed)} px/s"]
        if snap:
            status.append("⚠️ Snap Detected!")
        else:
            status.append("Status: Normal")
        overlay.update(frame, status)

if __name__ == "__main__":
    main()
