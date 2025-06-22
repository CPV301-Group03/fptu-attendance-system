import os
import cv2
import numpy as np
import face_recognition
from PIL import Image

def load_known_faces(data_dir):
    known_encodings = []
    known_labels = []

    for person_folder in os.listdir(data_dir):
        person_path = os.path.join(data_dir, person_folder)
        if not os.path.isdir(person_path):
            continue

        label = person_folder

        for image_name in os.listdir(person_path):
            if not image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            image_path = os.path.join(person_path, image_name)
            try:
                # Mở ảnh bằng PIL → RGB → chuyển sang numpy
                pil_img = Image.open(image_path).convert("RGB")
                rgb = np.array(pil_img)

                if rgb.dtype != np.uint8:
                    rgb = rgb.astype(np.uint8)

                # Nhận diện khuôn mặt
                boxes = face_recognition.face_locations(rgb)
                if len(boxes) == 0:
                    print(f"[⚠] Không tìm thấy mặt trong: {image_name}")
                    continue

                encodings = face_recognition.face_encodings(rgb, boxes)
                known_encodings.extend(encodings)
                known_labels.extend([label] * len(encodings))

                print(f"[+] Đã load ảnh: {image_name}, số mặt: {len(encodings)}")

            except Exception as e:
                print(f"[ERROR] Không thể xử lý {image_name}: {e}")
    
    return known_encodings, known_labels

def recognize_faces(frame, known_encodings, known_labels):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    results = []

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_labels[best_match_index]

        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        results.append(((top, right, bottom, left), name))

    return results
