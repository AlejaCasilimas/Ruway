import streamlit as st
from PIL import Image

st.title("Participa con nosotros para ser uno de los ganadores)

st.header("Comsursa por um increible sticker que tenemos para tenemos para ti")
st.write("Solo tienes que ingresar en el siguiente código Qr o en el link que aparece a cointinuación y contestar unas pequeñas preguntas")
image = Image.open("Código QR para comcurso.png")

st.image(image, caption="https://forms.office.com/r/tJ57RUQPAL")