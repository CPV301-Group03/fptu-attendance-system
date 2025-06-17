# Module 2: Xử lý khung hình và tiền xử lý
# Người phụ trách: [Tên Thành Viên 3]

import cv2

def preprocess_frame(frame):
    """
    Thực hiện các bước tiền xử lý trên một khung hình.

    Args:
        frame: Khung hình gốc từ camera (định dạng BGR).
        
    Returns:
        Khung hình đã được xử lý (ví dụ: ảnh xám đã cân bằng sáng).
    """
    # TODO: Viết logic tiền xử lý ảnh.
    # Gợi ý các bước:
    # 1. Chuyển ảnh sang grayscale: cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 2. Cân bằng sáng: cv2.equalizeHist(gray_frame)
    # 3. Lọc nhiễu (tùy chọn): cv2.GaussianBlur(...)
    # Trả về khung hình đã được xử lý cuối cùng.

    # Placeholder: Trả về khung hình gốc mà không xử lý gì
    return frame