# src/function_2.py
import cv2
import os

def capture_images_from_camera(name_folder, image_type="raw", output_dir="data/raw_images", num_frames=20, cap=None):
    if cap is None or not cap.isOpened():
        print("[ERROR] Camera is not available.")
        return

    save_path = os.path.join(output_dir, image_type, name_folder)
    os.makedirs(save_path, exist_ok=True)

    count = 0
    while count < num_frames:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to capture frame.")
            continue

        img_name = f"{image_type}_{count:02}.jpg"
        cv2.imwrite(os.path.join(save_path, img_name), frame)
        print(f"[✓] Saved: {img_name}")
        count += 1
