import streamlit as st
from PIL import Image

st.title("Proyecto de cosplay Ruway")

st.header("Proyecto de cosplay original diseñado y desarrollado por la Universidad EAFIT")
st.write("")
image = Image.open("bocetación.png")

st.image(image, caption="Ruway")

