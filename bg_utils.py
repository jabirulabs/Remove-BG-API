import cv2
import numpy as np
from rembg import remove
from PIL import Image, ImageEnhance
from io import BytesIO

# -------- STEP 1: ENHANCE IMAGE --------
def enhance_image_bytes(image_bytes: bytes) -> bytes:
    image = Image.open(BytesIO(image_bytes))

    # 1. Increase sharpness
    image = ImageEnhance.Sharpness(image).enhance(1.0)

    # 2. Increase contrast
    image = ImageEnhance.Contrast(image).enhance(1.0)

    # 3. Increase brightness
    image = ImageEnhance.Brightness(image).enhance(1.0)

    buf = BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()

# -------- STEP 2: REMOVE BACKGROUND --------
def remove_background_bytes(image_bytes: bytes) -> bytes:
    return remove(image_bytes)

# -------- STEP 3: COMPLETE PIPELINE --------
def process_image_bytes(image_bytes: bytes) -> bytes:
    enhanced = enhance_image_bytes(image_bytes)
    final = remove_background_bytes(enhanced)
    return final
