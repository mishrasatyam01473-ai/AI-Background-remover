import streamlit as st 
import os
from PIL import Image
from rembg import remove


st.title("🖼️ AI Background Remover for All")

img_file = st.file_uploader("Upload an Image")

if img_file:
    img = Image.open(img_file)
    st.subheader("Original image")
    resized_img = img.resize((500,500))
    st.image(resized_img)
    if st.button("Remove background"):
        with st.spinner("Removing Background..... Please wait for few seconds."):
        output_img = remove(img)
        
        st.subheader("Background removed")
        showing_img = output_img.resize((500,500))
        st.image(showing_img)


