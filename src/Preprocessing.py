import os
import cv2
from PIL import Image, ExifTags
import numpy as np

def auto_rotate_if_landscape(img):
    h, w = img.shape[:2]
    if w > h:   #ngang → dọc
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return img

# Xoay ảnh theo EXIF (nếu có)
def load_and_correct_orientation(image_path):
    img = Image.open(image_path)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == "Orientation":
                break
        exif = img._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation)
            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except:
        pass
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

# CLAHE + Gaussian Blur
def preprocess_color_image(img, clipLimit=1.5, tileSize=(8, 8), blur_kernel=(5, 5), sigmaX=0):
    b, g, r = cv2.split(img)
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileSize)
    b = clahe.apply(b)
    g = clahe.apply(g)
    r = clahe.apply(r)
    equalized = cv2.merge((b, g, r))
    blurred = cv2.GaussianBlur(equalized, blur_kernel, sigmaX)
    return blurred

# Duyệt tất cả ảnh trong folder gốc, xử lý và lưu giữ cấu trúc thư mục
def process_all_images(input_root, output_root):
    for root, dirs, files in os.walk(input_root):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(root, file)

                # Xác định đường dẫn và tạo đường dẫn output 
                rel_path = os.path.relpath(input_path, input_root)
                output_path = os.path.join(output_root, rel_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                try:
                    img = load_and_correct_orientation(input_path)
                    img = auto_rotate_if_landscape(img)  
                    processed = preprocess_color_image(img)
                    cv2.imwrite(output_path, processed)
                    print(f"Saved: {output_path}")
                except Exception as e:
                    print(f"Error: {input_path} - {e}")

# đường dẫn
input_root = r"D:\Study\Semester 4\CPV\raw"
output_root = r"D:\Study\Semester 4\CPV\processed"
process_all_images(input_root, output_root)
