import cv2

# Global camera instance
cap = None

def initialize_camera():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)
    return cap

def get_camera_frame():
    global cap
    if cap is None or not cap.isOpened():
        return None
    ret, frame = cap.read()
    if not ret:
        return None
    return frame

def release_camera():
    global cap
    if cap is not None:
        cap.release()
        cap = None
