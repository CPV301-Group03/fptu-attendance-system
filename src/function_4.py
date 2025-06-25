# src/function_4.py
import cv2
import os
import numpy as np
import time
from datetime import datetime
from utils import log_attendance_once_per_day


# Huấn luyện từ cả 3 thư mục ảnh
def train_face_recognizer(data_dir="data/preprocessed_image"):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    label_map = {}
    faces = []
    labels = []
    label_id = 0

    for subfolder in ["images", "images_with_glasses", "images_with_mask"]:
        folder_path = os.path.join(data_dir, subfolder)
        if not os.path.isdir(folder_path):
            continue

        for person in os.listdir(folder_path):
            person_path = os.path.join(folder_path, person)
            if not os.path.isdir(person_path):
                continue

            label_map[label_id] = person

            for file in os.listdir(person_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    img_path = os.path.join(person_path, file)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        faces.append(img)
                        labels.append(label_id)

            label_id += 1

    recognizer.train(faces, np.array(labels))
    return recognizer, label_map


# Biến toàn cục để theo dõi thời gian nhận diện
detection_timers = {}

# Nhận diện từ frame — không pop GUI mới, dùng GUI chính
def recognize_faces_in_frame(frame, recognizer, label_map, log_func):
    global detection_timers

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    current_time = time.time()
    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        label_id, confidence = recognizer.predict(roi)
        name = label_map.get(label_id, "Unknown")

        # Kiểm tra độ chính xác
        if name != "Unknown" and confidence < 100:
            prev_time = detection_timers.get(name, None)

            if prev_time is None:
                detection_timers[name] = current_time
                time_left = 2
            else:
                elapsed = current_time - prev_time
                time_left = max(0, round(2 - elapsed, 1))
                if elapsed >= 2:
                    log_attendance_once_per_day(name, log_func)

        else:
            time_left = float('inf')
            detection_timers[name] = current_time  # reset nếu Unknown hoặc confidence cao

        # Vẽ khung mặt và tên
        color = (0, 255, 0) if confidence < 100 else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, f"{name} ({int(confidence)})", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        cv2.putText(frame, f"Time: {time_left}s", (x, y + h + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame

