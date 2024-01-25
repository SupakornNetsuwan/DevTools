import streamlit as st
from PIL import Image
import os

env_BACKEND_URL = os.environ['BACKEND_URL']
   

st.title('Upload and Display Image with Username and ID with Backend Url = {}'.format(env_BACKEND_URL))

# User input
username = st.text_input("Enter your username")
id_number = st.text_input("Enter your ID number")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Finish button
if st.button('Finish'):
    if uploaded_file is not None:
        # Create a 2x1 table to display images
        col1, col2 = st.columns(2)
        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.write("Username:", username)
            st.write("ID Number:", id_number) 
        with col2:
            st.image(image, caption="Image 2")
            st.write("Username:", username)


    else:
        st.write("Please upload an image.")
