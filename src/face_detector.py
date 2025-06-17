# Module 3: Phát hiện khuôn mặt
# Người phụ trách: [Tên Thành Viên 4]

import cv2  # hoặc face_recognition

def detect_single_face(frame):
    """
    Phát hiện một khuôn mặt duy nhất trong khung hình.

    Args:
        frame: Khung hình đầu vào (đã hoặc chưa tiền xử lý).

    Returns:
        Một tuple chứa tọa độ (top, right, bottom, left) của khuôn mặt.
        Trả về None nếu không tìm thấy khuôn mặt nào.
    """
    # TODO: Viết logic phát hiện khuôn mặt.
    # Gợi ý:
    # - Dùng thư viện face_recognition:
    #   face_locations = face_recognition.face_locations(rgb_frame)
    #   Nhớ chuyển đổi BGR (OpenCV) sang RGB (face_recognition).
    # - Hoặc dùng Haar Cascade của OpenCV.
    # Chỉ trả về khuôn mặt đầu tiên tìm thấy trong list.

    # Placeholder: Không phát hiện gì cả
    return None