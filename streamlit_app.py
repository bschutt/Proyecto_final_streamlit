import streamlit as st
import streamlit.components.v1 as components
import webbrowser

st.set_page_config(
    page_title="Looker",
    page_icon="🔍",
    layout="wide",
)

coln, colm = st.columns([4, 1])
with coln:
    st.header("📊 Looker Dashboards")
with colm:
    # Puedes reemplazar la URL de la imagen con el logo de Looker o cualquier otra imagen que prefieras
    st.image('Dark Blue Simple Dark Tech and Gaming Bio-Link Website.png', width=150)
st.markdown('---')

# Reemplaza esto con tu URL de Looker
looker_url = 'https://lookerstudio.google.com/reporting/2c58e29c-4ccc-43aa-a8ed-d55c4a12a9a1'

def toLooker():
    webbrowser.open_new_tab(looker_url)

container1 = st.container()

with container1:
    cola, colb, colc = st.columns([2, 4, 2])

with colb:
    # Agrega el atributo sandbox al iframe
    components.iframe(looker_url, width=768, height=603, scrolling=True, sandbox="allow-same-origin allow-scripts allow-popups")

with cola:
    st.button(label='Abrir en Looker', on_click=toLooker)
