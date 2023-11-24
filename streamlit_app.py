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
    st.image('https://www.canva.com/design/DAF1Bz0MA6A/h-w-AQFct8WEPEeWncyz0Q/view?utm_content=DAF1Bz0MA6A&utm_campaign=designshare&utm_medium=link&utm_source=editor', width=150)
st.markdown('---')

# Reemplaza esto con tu URL de Looker
looker_url = 'https://lookerstudio.google.com/u/0/reporting/2c58e29c-4ccc-43aa-a8ed-d55c4a12a9a1/page/p_zalhmmsqbd/edit'

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
