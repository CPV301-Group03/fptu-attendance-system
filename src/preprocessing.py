import cv2
import numpy as np

def preprocess_face_image(face_img):
    """
    Tiền xử lý ảnh khuôn mặt trước khi lưu vào preprocessed_image:
    - Chuyển grayscale
    - Resize 150x150
    - Histogram Equalization
    - Gaussian Blur
    - Sharpening
    """

    # Chuyển về grayscale
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

    # Resize về 150x150
    resized = cv2.resize(gray, (150, 150))

    # Histogram Equalization để tăng tương phản
    equalized = cv2.equalizeHist(resized)

    # Gaussian Blur (làm mịn nhẹ để giảm noise)
    blurred = cv2.GaussianBlur(equalized, (3, 3), 0)

    # Sharpening (Tăng độ nét)
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    sharpened = cv2.filter2D(blurred, -1, kernel)

    return sharpened
