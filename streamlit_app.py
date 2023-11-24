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
    # You can replace the image URL with the Looker logo or any other image you prefer
    st.image('https://www.canva.com/design/DAF1Bz0MA6A/h-w-AQFct8WEPEeWncyz0Q/view?utm_content=DAF1Bz0MA6A&utm_campaign=designshare&utm_medium=link&utm_source=editor', width=150)
st.markdown('---')

# Replace this with your Looker dashboard URL
looker_url = 'https://lookerstudio.google.com/s/uwgvVUM6nrM'

def toLooker():
    webbrowser.open_new_tab(looker_url)

container1 = st.container()

with container1:
    cola, colb, colc = st.columns([2, 4, 2])

with colb:
    # Embed Looker dashboard using iframe
    components.iframe(looker_url, width=768, height=603, scrolling=True)

with cola:
    st.button(label='Open in Looker', on_click=toLooker)