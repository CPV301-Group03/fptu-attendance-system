import cv2
from face_detector import load_known_faces, recognize_faces
from attendance_manager import log_attendance

def run_attendance():
    print("[INFO] Loading known faces...")
    known_encodings, known_labels = load_known_faces("data")
    print(f"[INFO] Loaded {len(known_labels)} known faces.")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot open webcam.")
        return

    print("[INFO] Starting attendance. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break
        
        results = recognize_faces(frame, known_encodings, known_labels)

        for (top, right, bottom, left), name in results:
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            log_attendance(name)

        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_attendance()
