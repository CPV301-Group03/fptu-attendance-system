# Module 4: Nhận dạng khuôn mặt
# Người phụ trách: [Tên Thành Viên 5]

import face_recognition
import pickle
import os
from . import config

def load_known_encodings():
    """
    Tải dữ liệu khuôn mặt đã biết từ file.

    Returns:
        Một dictionary chứa 2 list: "encodings" và "names".
    """
    # TODO: Viết logic để tải file model 'encodings.pkl'.
    # Sử dụng pickle.load().
    # Nếu file không tồn tại, hãy gọi hàm build_and_save_encodings() bên dưới.

    print("TODO: Load known encodings.")
    # Placeholder: Trả về dữ liệu rỗng để chương trình không lỗi
    return {"encodings": [], "names": []}

def build_and_save_encodings():
    """
    (Chạy một lần) Duyệt qua thư mục data/dataset, mã hóa tất cả khuôn mặt
    và lưu chúng vào file encodings.pkl.
    """
    # TODO: Viết logic để:
    # 1. Lặp qua các thư mục con trong config.DATASET_PATH.
    # 2. Với mỗi thư mục, lặp qua các file ảnh.
    # 3. Dùng face_recognition.load_image_file() và face_recognition.face_encodings().
    # 4. Lưu các encoding và tên (MSSV) tương ứng vào 2 list.
    # 5. Dùng pickle.dump() để lưu dictionary {"encodings": ..., "names": ...} vào file.
    pass

def recognize_face(face_encoding, known_data):
    """
    So sánh một encoding khuôn mặt với các encoding đã biết.

    Args:
        face_encoding: Encoding của khuôn mặt cần nhận dạng.
        known_data: Dictionary chứa "encodings" và "names" đã biết.
        
    Returns:
        MSSV (str) nếu nhận dạng được, ngược lại trả về "Unknown".
    """
    # TODO: Viết logic so sánh khuôn mặt.
    # Gợi ý:
    # 1. Dùng face_recognition.compare_faces() để có được một list các giá trị True/False.
    # 2. Nếu có True, tìm index của nó và lấy ra tên tương ứng từ known_data["names"].

    # Placeholder: Luôn trả về "Unknown"
    return "Unknown"