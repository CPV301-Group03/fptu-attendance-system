from datetime import datetime

logged_names = set()

def log_attendance(name, output_file="attendance_log.csv"):
    if name == "Unknown" or name in logged_names:
        return
    logged_names.add(name)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_file, "a") as f:
        f.write(f"{name},{now}\n")
    print(f"[✓] {name} điểm danh lúc {now}")
