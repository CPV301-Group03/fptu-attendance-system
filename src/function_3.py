# src/function_3.py
import cv2
import os
import shutil
from preprocessing import preprocess_face_image

def extract_and_save_faces(raw_dir="data/raw_images", enable_optional=False, log_func=None):
    pre_dir = "data/preprocessed_gray_images" if enable_optional else "data/preprocessed_images"
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    type_to_folder = {
        "raw": "images",
        "glasses": "images_with_glasses",
        "mask": "images_with_mask"
    }

    for img_type in os.listdir(raw_dir):
        input_type_path = os.path.join(raw_dir, img_type)
        if not os.path.isdir(input_type_path):
            continue

        output_folder = type_to_folder.get(img_type)
        if not output_folder:
            continue

        for person_folder in os.listdir(input_type_path):
            person_path = os.path.join(input_type_path, person_folder)
            save_path = os.path.join(pre_dir, output_folder, person_folder)
            os.makedirs(save_path, exist_ok=True)

            for idx, img_name in enumerate(os.listdir(person_path)):
                img_path = os.path.join(person_path, img_name)
                img = cv2.imread(img_path)
                if img is None:
                    continue

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                for i, (x, y, w, h) in enumerate(faces):
                    face_crop = img[y:y+h, x:x+w]

                    if log_func:
                            log_func("[INFO] Preprocessing Images...")
                            
                    if enable_optional:
                        face_crop = preprocess_face_image(face_crop)

                    filename = f"{person_folder}({img_type})_{idx}_{i}.jpg"
                    cv2.imwrite(os.path.join(save_path, filename), face_crop)

        shutil.rmtree(input_type_path)

    if log_func:
        log_func("[✓] Preprocessing completed.")

