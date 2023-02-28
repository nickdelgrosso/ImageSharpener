import streamlit as st
import numpy as np
import cv2
from skimage.filters import unsharp_mask

st.title("Image Sharpener Tool")
st.sidebar.title("Settings")
sharpen_radius = st.sidebar.slider('Sharpen Radius', 0, 10, 0)
sharpen_amount = st.sidebar.slider('Sharpen Amount', 0, 10, 0)

tab1, tab2, tab3 = st.tabs(["Get Image", "Original Image", "Processd Image"])

with tab1:
    image_io_from_cam = st.camera_input("Webcam")
    image_io_from_file = st.file_uploader("Upload Image File")
    image_io = image_io_from_file or image_io_from_cam


with tab2:
    if image_io is not None:
        image_bytes = image_io.getvalue()
        image_buffer = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_buffer, cv2.IMREAD_COLOR)
        image = image[..., [2, 1, 0]]
    
        st.image(image)

with tab3:
    if image_io is not None:
        sharpened = unsharp_mask(image, radius=sharpen_radius, amount=sharpen_amount)
        st.image(sharpened)


