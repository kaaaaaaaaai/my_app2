import streamlit as st
from PIL import Image
import cv2

def oil_painting(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (21, 21), 0)
    img_gray = cv2.medianBlur(img_gray, 15)
    img_gray = cv2.bilateralFilter(img_gray, 15, 75, 75)
    img_gray = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img = cv2.bitwise_and(img, img, mask=img_gray)
    img = Image.fromarray(img)
    return img

st.set_title("Oil Painting App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(oil_painting(image), caption='Oil Painting', use_column_width=True)