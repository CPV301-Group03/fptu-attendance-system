# Module 1: Lấy luồng video
# Người phụ trách: [Tên Thành Viên 2]

import cv2
from . import config

def get_video_stream():
    """
    Tạo và trả về đối tượng VideoCapture dựa trên cấu hình.
    Sẽ kết nối với webcam hoặc stream RTSP.

    Returns:
        Đối tượng cv2.VideoCapture hoặc None nếu kết nối thất bại.
    """
    # TODO: Viết logic để kiểm tra cờ config.USE_WEBCAM.
    # Nếu True, sử dụng cv2.VideoCapture(config.WEBCAM_ID).
    # Nếu False, sử dụng cv2.VideoCapture(config.RTSP_URL).
    # Đừng quên kiểm tra cap.isOpened() và in ra thông báo lỗi nếu cần.

    print("TODO: Connecting to camera...")
    cap = None  # Đây là placeholder

    # Placeholder: Trả về webcam mặc định
    cap = cv2.VideoCapture(config.WEBCAM_ID)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    return cap