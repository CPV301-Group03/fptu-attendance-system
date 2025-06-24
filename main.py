import tkinter as tk
from tkinter import ttk
import threading
import cv2
from PIL import Image, ImageTk
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.function_1 import initialize_camera, release_camera, get_camera_frame
from src.function_2 import capture_images_from_camera
from src.function_3 import extract_and_save_faces
from src.function_4 import train_face_recognizer, recognize_faces_in_frame

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry("1500x1000")
        self.root.configure(bg="#f0f0f0")

        self.cap = initialize_camera()
        self.recognizer = None
        self.label_map = None
        self.is_recognition_active = False

        self.setup_gui()
        self.update_camera()

    def setup_gui(self):
        # Left Frame for controls and camera
        self.left_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Entry Section
        frame_entry = tk.Frame(self.left_frame, bg="#f0f0f0")
        frame_entry.pack(pady=10)

        tk.Label(frame_entry, text="Folder (MSSV_FullName_Class):", font=("Arial", 14), bg="#f0f0f0").pack(side=tk.LEFT)
        self.entry_name = tk.Entry(frame_entry, font=("Arial", 14), width=35)
        self.entry_name.pack(side=tk.LEFT, padx=10)

        tk.Label(frame_entry, text="Image's Type:", font=("Arial", 14), bg="#f0f0f0").pack(side=tk.LEFT)
        self.image_type_var = tk.StringVar(value="raw")
        type_menu = ttk.Combobox(frame_entry, textvariable=self.image_type_var,
                                 values=["raw", "glasses", "mask"], state="readonly", width=10)
        type_menu.pack(side=tk.LEFT)

        # Buttons Section
        frame_buttons = tk.Frame(self.left_frame, bg="#f0f0f0")
        frame_buttons.pack(pady=20)

        tk.Button(frame_buttons, text="2. Capture Images", font=("Arial", 14), width=30,
                  command=self.run_capture).pack(pady=10)

        tk.Button(frame_buttons, text="3. Preprocess Faces", font=("Arial", 14), width=30,
                  command=self.run_preprocess).pack(pady=10)

        tk.Button(frame_buttons, text="4. Run Attendance Recognition", font=("Arial", 14), width=30,
                  command=self.run_recognition_thread).pack(pady=10)

        # Camera Frame
        self.camera_label = tk.Label(self.left_frame, bg="black")
        self.camera_label.pack(pady=10)

        # Right Frame for Log
        self.right_frame = tk.Frame(self.root, bg="#e0e0e0", width=300)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.right_frame, text="Log Output", font=("Arial", 14, "bold"), bg="#e0e0e0").pack(pady=10)

        self.log_text = tk.Text(self.right_frame, font=("Courier", 10), height=45, state=tk.DISABLED, wrap=tk.WORD)
        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def update_camera(self):
        frame = get_camera_frame()
        if frame is not None:
            if self.is_recognition_active and self.recognizer and self.label_map:
                frame = recognize_faces_in_frame(frame, self.recognizer, self.label_map, self.log)
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = img.resize((800, 600))
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)
        self.root.after(10, self.update_camera)

    def run_capture(self):
        folder = self.entry_name.get()
        img_type = self.image_type_var.get()
        if not folder:
            self.log("[WARN] Please enter folder name.")
            return
        self.log(f"[INFO] Capturing images for {folder} ({img_type})")
        threading.Thread(target=self.capture_thread, args=(folder, img_type)).start()

    def capture_thread(self, folder, img_type):
        capture_images_from_camera(name_folder=folder, image_type=img_type, cap=self.cap)
        self.log("[✓] Capture completed.")

    def run_preprocess(self):
        self.log("[INFO] Preprocessing faces...")
        threading.Thread(target=self.preprocess_thread).start()

    def preprocess_thread(self):
        extract_and_save_faces()
        self.log("[✓] Preprocessing completed.")

    def run_recognition_thread(self):
        self.log("[INFO] Training model...")
        def task():
            self.recognizer, self.label_map = train_face_recognizer("data/preprocessed_image")
            self.is_recognition_active = True
            self.log("[✓] Training completed. Ready for recognition.")
        threading.Thread(target=task).start()

    def on_closing(self):
        release_camera()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
