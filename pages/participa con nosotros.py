import streamlit as st
from PIL import Image

st.title("Participa con nosotros para ser uno de los ganadores")

st.header("Consursa por un increible sticker que tenemos para tenemos para ti")
st.write("Solo tienes que ingresar en el siguiente código Qr o en el link que aparece a continuación y contestar unas pequeñas preguntas")
image = Image.open("Código QR para Concurso.png")

st.image(image, caption="https://forms.office.com/r/tJ57RUQPAL")

# Texto con hipervínculo
link_text = "[Enlace a Google](https://forms.office.com/r/tJ57RUQPAL)"

# Mostrar el hipervínculo utilizando st.markdown
st.markdown(link_text, unsafe_allow_html=True)

