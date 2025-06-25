from datetime import datetime
import os
import re


# Log vào file csv
def log_attendance_once_per_day(name, log_func):
    today = datetime.now().strftime("%Y-%m-%d")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"attendance_{today}.csv")

    # Nếu file đã tồn tại → đọc để kiểm tra đã ghi tên chưa
    already_logged = False
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logged_names = [line.strip().split(",")[0] for line in f.readlines()]
            already_logged = name in logged_names

    # Nếu chưa có trong log hôm nay thì ghi
    if not already_logged:
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            f.write(f"{name},{now_str}\n")
        log_func(f"[✓] {name} đã điểm danh lúc {now_str}")



def is_valid_folder_name(folder_name, log_func=None):
    """
    Kiểm tra định dạng folder theo chuẩn: MSSV_FullName_Class
    - MSSV: Bắt đầu bằng SE|AI|SS + 2 số < 21 + 4 số tiếp theo
    - FullName: Viết hoa từng chữ, không dấu cách
    - Class: Ví dụ SE2101, AI1907, SS2103
    """

    parts = folder_name.split("_")
    if len(parts) < 3:
        log_func("[WARN] Invalid folder name format. Please follow: MSSV_FullName_Class")
        return False

    mssv, full_name, class_name = parts

    # Check MSSV
    if not re.match(r"^(SE|AI|SS)\d{6}$", mssv):
        log_func(f"[WARN] {mssv} is invalid MSSV format. Please type again.")
        return False

    year = int(mssv[2:4])
    if year >= 21:
        log_func(f"[WARN] {year} is invalid student's year. Please type again.")
        return False

    # Check FullName: Từng phần phải viết hoa chữ cái đầu
    if not full_name.isalpha() or not full_name[0].isupper():
        log_func("[WARN] Invalid FullName format. Please type again.")
        return False

    # Check Class name: Ví dụ AI1907, SE2101, SS2103
    if not re.match(r"^(SE|AI|SS)\d{4}$", class_name):
        log_func("[WARN] Invalid Class name format. Please type again.")
        return False

    return True
