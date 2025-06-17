# File chạy chính của chương trình
# Người phụ trách tích hợp: [Tên Team Leader]

import cv2
from src import streaming, image_processor, face_detector, face_recognizer, attendance_manager, utils

def main():
    print("Initializing system...")

    # --- Bước 1: Khởi tạo ---
    # Tải thông tin sinh viên và dữ liệu khuôn mặt đã biết
    student_info = attendance_manager.load_student_info()
    known_face_data = face_recognizer.load_known_encodings()

    # Kết nối camera
    cap = streaming.get_video_stream()
    if not cap:
        return

    print("System ready. Starting video loop...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting.")
            break
        
        # --- Bước 2: Tiền xử lý (Tùy chọn) ---
        # processed_frame = image_processor.preprocess_frame(frame)
        
        # --- Bước 3: Phát hiện khuôn mặt ---
        # Sử dụng frame gốc hoặc frame đã xử lý tùy vào hiệu quả
        face_location = face_detector.detect_single_face(frame)
        
        # --- Bước 4: Nhận dạng và Điểm danh ---
        if face_location:
            # TODO: Cần có code để trích xuất encoding từ face_location và frame
            # face_encoding = ... 
            
            # student_id = face_recognizer.recognize_face(face_encoding, known_face_data)
            student_id = "Unknown"  # Placeholder

            display_name = student_id
            if student_id != "Unknown":
                display_name = student_info.get(student_id, "Unknown Student")
                # TODO: Thêm logic để chỉ điểm danh một lần cho mỗi sinh viên
                # attendance_manager.log_attendance(student_id, display_name)

            # --- Bước 5: Hiển thị kết quả ---
            # Vẽ bounding box và tên lên frame gốc
            utils.draw_bounding_box(frame, face_location, display_name)

        cv2.imshow("FPT University Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Dọn dẹp
    cap.release()
    cv2.destroyAllWindows()
    print("System shut down.")

if __name__ == "__main__":
    main()