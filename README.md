<div align="center">
  <h1>Face Recognition Attendance System</h1>
  <h3>Project for CPV301 - Computer Vision</h3>
  <p><strong>FPT University HCMC - Group 3</strong></p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Language">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>


---

## 📝 Overview

This repository is for **Group 6** in the **CPV301 (Computer Vision)** course at FPT University HCMC. It contains the source code and related materials for our final project. The project's goal is to build a simple attendance system that uses a computer's webcam to detect and recognize student faces, logging their check-in times automatically.

## ✨ Key Features

- ✅ **Real-time Video Streaming:** Captures live video feed from the laptop's webcam.
- ✅ **Face Detection:** Identifies and locates human faces within each video frame.
- ✅ **Face Recognition:** Compares a detected face against a pre-registered student database to determine identity.
- ✅ **Attendance Logging:** Records the Student ID, Full Name, and timestamp of a successful recognition into a `CSV` file.

## 🛠️ Tech Stack

*   **Language:** Python 3
*   **Computer Vision & Image Processing:** OpenCV, Dlib, `face_recognition`
*   **Numerical Computing:** NumPy
*   **Data Handling:** Pandas

## 🚀 Installation and Usage

Follow these steps to get the project running on your local machine.

1.  **Clone the Repository:**
    ```bash
    git clone <YOUR-REPOSITORY-URL>
    cd <PROJECT-DIRECTORY-NAME>
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Required Libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare the Dataset:**
    *   Add images of each student to the `data/dataset/` directory.
    *   Each student must have their own sub-directory named in the format `StudentID_FullNameWithoutSpaces` (e.g., `data/dataset/SE123456_NguyenVanA`).
    *   Place several clear portrait photos of the student inside their respective folder.

5.  **Run the Application:**
    ```bash
    python main.py
    ```
    The program will automatically build the face encodings file (`models/encodings.pkl`) on its first run if it doesn't exist.

## 📂 Project Structure

```
fptu-attendance-system
├── data/
│   ├── dataset/        # Contains registered student images
│   └── logs/           # Contains attendance log files
├── docs/               # Contains reports and presentation slides
├── models/             # Stores trained models (e.g., encodings.pkl)
├── notebooks/          # Jupyter notebooks for experimentation
├── src/                # All source code
│   ├── config.py
│   ├── streaming.py
│   ├── image_processor.py
│   ├── face_detector.py
│   ├── face_recognizer.py
│   ├── attendance_manager.py
│   └── utils.py
├── .gitignore
├── main.py             # Main script to run the application
├── requirements.txt
└── README.md
```

## 👥 Team Members & Roles

| Name                  | Role                         | Team         |
| --------------------- | ---------------------------- | ------------ |
| **Lê Nguyễn Gia Hưng** | **Overall Leader**           | -            |
| **Hoàng Phạm Gia Bảo** | **Coding Team Lead**         | Coding       |
| Ngô Hoài Nam          | Member                       | Coding       |
| Huỳnh Quốc Việt       | Member                       | Coding       |
| Võ Tấn Phát           | Member                       | Coding       |
| **Trương Phước Sang** | **Presentation Team Lead**   | Presentation |
| Dương Nguyên Bình     | Member                       | Presentation |

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
