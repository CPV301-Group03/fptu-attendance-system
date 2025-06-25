import cv2
import os
import numpy as np
import time
from src.utils import log_attendance_once_per_day
from src.preprocessing import preprocess_face_image 

# Biến toàn cục để lưu thời gian phát hiện khuôn mặt
detection_timers = {}

# Hàm huấn luyện LBPH Model
def train_face_recognizer(data_dir, log_func=None):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    label_map = {}
    faces = []
    labels = []
    label_id = 0

    subfolders = ["images", "images_with_glasses", "images_with_mask"]
    for folder in subfolders:
        folder_path = os.path.join(data_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        for person_folder in os.listdir(folder_path):
            person_path = os.path.join(folder_path, person_folder)
            if not os.path.isdir(person_path):
                continue

            for file in os.listdir(person_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    img_path = os.path.join(person_path, file)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        faces.append(img)
                        labels.append(label_id)

            label_map[label_id] = person_folder
            label_id += 1

    # Kiểm tra đủ dữ liệu hay không
    if len(faces) < 2:
        if log_func:
            log_func("[WARN] Not enough training data. At least 2 face images from at least 1 person required.")
        return None, None

    recognizer.train(faces, np.array(labels))
    return recognizer, label_map

# Hàm nhận diện khuôn mặt trong từng frame
def recognize_faces_in_frame(frame, recognizer, label_map, log_func, th, enable_optional_preprocess=False):
    global detection_timers
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    current_time = time.time()

    for (x, y, w, h) in faces:
        roi_color = frame[y:y+h, x:x+w]

        # Nếu Training có preprocessing → Realtime cũng phải preprocess
        if enable_optional_preprocess:
            roi_processed = preprocess_face_image(roi_color)
        else:
            roi_processed = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)

        try:
            label_id, confidence = recognizer.predict(roi_processed)
        except:
            continue

        name = label_map.get(label_id, "Unknown")

        # Áp dụng threshold từ GUI
        if confidence > th:
            name = "Unknown"

        # Countdown 2s logic
        if name != "Unknown":
            if name not in detection_timers:
                detection_timers[name] = current_time
            elif current_time - detection_timers[name] >= 2:
                log_attendance_once_per_day(name, log_func)
                del detection_timers[name]
        else:
            # Nếu Unknown → xóa timer nếu có
            if name in detection_timers:
                del detection_timers[name]

        # Vẽ Bounding box + Name + Confidence
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        text = f"{name} ({int(confidence)})" if name != "Unknown" else "Unknown"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # Hiển thị countdown
        if name != "Unknown" and name in detection_timers:
            time_elapsed = current_time - detection_timers[name]
            countdown = max(0, 2 - time_elapsed)
            countdown_text = f"Countdown: {countdown:.1f}s"
            cv2.putText(frame, countdown_text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame
