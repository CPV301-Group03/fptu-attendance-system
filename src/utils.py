# Chứa các hàm tiện ích dùng chung

import cv2

def draw_bounding_box(frame, location, name):
    """
    Vẽ một khung chữ nhật và tên lên khuôn mặt trên khung hình.
    Lưu ý: Hàm này chỉnh sửa trực tiếp trên 'frame'.

    Args:
        frame: Khung hình (ảnh) để vẽ lên.
        location: Tuple (top, right, bottom, left) của khuôn mặt.
        name: Tên (MSSV hoặc Họ Tên) để hiển thị.
    """
    # TODO: Viết logic để vẽ lên frame.
    # Gợi ý:
    # - Dùng cv2.rectangle() để vẽ khung.
    # - Dùng cv2.putText() để ghi tên.
    pass