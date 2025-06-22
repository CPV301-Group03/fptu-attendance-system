import cv2
import os
import face_recognition
import numpy as np

def extract_faces_from_video(video_path, output_dir, max_faces=50):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERROR] Không thể mở video: {video_path}")
        return

    count = 0
    frame_interval = 5
    frame_id = 0

    while count < max_faces:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] Hết video hoặc lỗi.")
            break

        if frame_id % frame_interval == 0:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = np.ascontiguousarray(rgb)
            if rgb.dtype != np.uint8:
                rgb = rgb.astype(np.uint8)
            print(f"[DEBUG] frame shape: {rgb.shape}, dtype: {rgb.dtype}")
            faces = face_recognition.face_locations(rgb)

            if len(faces) > 0:
                for i, (top, right, bottom, left) in enumerate(faces):
                    face_image = rgb[top:bottom, left:right]
                    if face_image.size == 0:
                        continue

                    face_bgr = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
                    save_path = os.path.join(output_dir, f"face_{count:03}.jpg")
                    cv2.imwrite(save_path, face_bgr)
                    print(f"[✓] Lưu khuôn mặt {count+1}: {save_path}")
                    count += 1


                    if count >= max_faces:
                        break

        frame_id += 1

    cap.release()
    print(f"[DONE] Đã trích xuất {count} khuôn mặt từ video.")

# Ví dụ cách chạy
if __name__ == "__main__":
    video_path = "data/videos/raw.mp4"
    output_dir = "data/SE194225_HuynhQuocViet_AI1907"
    extract_faces_from_video(video_path, output_dir)
