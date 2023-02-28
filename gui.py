# todos:
#   1. Make CLI version of tool: `python sharpen.py --radius 3 --amount 4 -o myimage.png`
#   2. Make Python API version of tool with OOP interface: `app.load_image('myimage.png'); app.sharpen(3, 4); app.save('newimage.png.')`
#   3. Let user choose a different backend (like scipy.ndimage) for doing the sharpening: https://scipy-lectures.org/advanced/image_processing/
#   4. Make Python wrapper functions for image processing and image loading (for other projects): `skimage_processing.sharpen(array, 3, 4)`
#   5. Release each tool seperately, with their own installation pathway (pip install imsharp, pip install imsharp-streamlit, pyinstaller imsharp-cli).

# improvements:
#   1. Separate dependencies into their own modules, where possible.
#   2. Separate UI layout from state management from processing steps
#   3. Separate pure functions from stateful modules.

# utils.py  
# app.py
# gui.py 

import streamlit as st
from app import App

app = App()

# Layout
st.title("Image Sharpener Tool")
st.sidebar.title("Settings")
app.sharpen_radius = st.sidebar.slider('Sharpen Radius', 0, 10, app.sharpen_radius)
app.sharpen_amount = st.sidebar.slider('Sharpen Amount', 0, 10, app.sharpen_amount)
tab1, tab2, tab3 = st.tabs(["Get Image", "Original Image", "Processed Image"])

with tab1:
    image_io_from_cam = st.camera_input("Webcam")
    image_io_from_file = st.file_uploader("Upload Image File")
    image_io = image_io_from_file or image_io_from_cam

with tab2:
    orig_image = st.empty()

with tab3:
    sharpened_image = st.empty()



# Processing/Actions

if image_io is not None:
    app.load_image(image_io.getvalue())
if app.image is not None:
    orig_image.image(app.image)

if app.sharpened_image is not None:
    sharpened_image.image(app.sharpened_image)
        



