# Module quản lý logic điểm danh và dữ liệu sinh viên
# Người phụ trách: [Tên Thành Viên 6]

import csv
from datetime import datetime
from . import config

def load_student_info():
    """
    Tải thông tin sinh viên từ file CSV vào một dictionary.

    Returns:
        Một dictionary với key là MSSV và value là Họ Tên.
    """
    # TODO: Viết logic để đọc file config.STUDENT_INFO_PATH.
    # Dùng thư viện 'csv' hoặc 'pandas' để đọc và chuyển thành dictionary.

    # Placeholder: Trả về dictionary rỗng
    return {}

def log_attendance(student_id, student_name):
    """
    Ghi lại thông tin điểm danh của sinh viên vào file CSV.
    """
    # TODO: Viết logic để:
    # 1. Lấy ngày và giờ hiện tại.
    # 2. Mở file config.ATTENDANCE_LOG_PATH ở chế độ 'a' (append).
    # 3. Dùng csv.writer để ghi một dòng mới chứa: MSSV, Họ Tên, Ngày, Giờ.
    # Lưu ý: Kiểm tra xem file có tồn tại chưa để ghi header nếu cần.
    print(f"TODO: Log attendance for {student_name} ({student_id})")
    pass