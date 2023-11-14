import streamlit as st
from PIL import Image

st.title("Proyecto de cosplay Ruway")

st.header("Este proyecto desarrollado para")
st.write("")
image = Image.open("imagen 1.jpg")

st.image(image, caption="Interfaces multimodales")
