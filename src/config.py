# File cấu hình trung tâm cho dự án

# --- Cấu hình Nguồn Video ---
# Đặt USE_WEBCAM = True để dùng webcam laptop, False để dùng RTSP
USE_WEBCAM = True
WEBCAM_ID = 0  # ID của webcam, thường là 0

# URL cho IP Camera (chỉ dùng khi USE_WEBCAM = False)
RTSP_URL = "rtsp://your_username:your_password@your_ip_camera_address"

# --- Cấu hình Đường Dẫn ---
STUDENT_INFO_PATH = "data/student_info.csv"
ATTENDANCE_LOG_PATH = "data/logs/attendance.csv"
DATASET_PATH = "data/dataset"
ENCODINGS_PATH = "models/encodings.pkl"

# --- Cấu hình Nhận Dạng ---
RECOGNITION_TOLERANCE = 0.5  # Độ tương đồng, càng nhỏ càng khắt khe