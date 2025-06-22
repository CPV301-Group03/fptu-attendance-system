# from PIL import Image
# path = "data/SE194225_HuynhQuocViet_AI1907/raw.jpg"
# from PIL import Image
# import numpy as np
# import face_recognition

# try:
#     pil_img = Image.open(img_path).convert("RGB")  # RGBA -> RGB
#     rgb = np.array(pil_img)

#     if rgb.dtype != np.uint8:
#         rgb = rgb.astype(np.uint8)  # Ensure correct dtype
# except Exception as e:
#     print(f"[ERROR] Could not process {img_name}: {e}")
#     continue