import streamlit as st
import pandas as pd
import numpy as np
from google.cloud import bigquery
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import os

st.set_option('deprecation.showfileUploaderEncoding', False)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "modelos_machine_learning/pf-henry-404414-784e39ca59ab.json"

# Lista de temas
temas = ["Dashboards KPI'S-Looker Studio", "Modelo de Machine Learning", "Preguntas", "Acerca de Nosotros"]

# Barra lateral con botones para cada tema
tema_seleccionado = st.sidebar.radio("Selecciona un tema", temas)

# Página principal
st.title("Presentación Proyecto Final Henry")

# Mostrar contenido según el tema seleccionado
if tema_seleccionado == "Dashboards KPI'S-Looker Studio":
    # Función para mostrar gráfica con título en negrita y centrado
    def mostrar_grafica(titulo, url):
        st.write(f"**{titulo}**")
        st.markdown(f'<div style="text-align: center;"><iframe width="900" height="750" src="{url}" frameborder="0" style="border:0" allowfullscreen></iframe></div>', unsafe_allow_html=True)

    # Página principal
    st.markdown("<h2>Dashboards KPI'S-Looker Studio</h2>", unsafe_allow_html=True)  # Título más pequeño
    # Mostrar las gráficas con títulos en negrita y centrados
    mostrar_grafica("", "https://lookerstudio.google.com/embed/reporting/2c58e29c-4ccc-43aa-a8ed-d55c4a12a9a1/page/p_zalhmmsqbd")

elif tema_seleccionado == "Modelo de Machine Learning":
    st.write("Modelo de Machine Learning")
    # Agrega aquí el contenido para el Tema 2

elif tema_seleccionado == "Preguntas":
    st.write("## Preguntas sobre Esperanza de Vida")

    # Pregunta 1
    st.write("1. ¿Qué país tiene la esperanza de vida más alta para el 2040?")
    # Configura tu credencial de Google Cloud
    client = bigquery.Client.from_service_account_json('pf-henry-404414-784e39ca59ab.json')

    query_1 = """
        SELECT Pais, Esperanza_vida_total
        FROM `pf-henry-404414.Notebooks.Query_1`
        ORDER BY Esperanza_vida_total DESC
        LIMIT 1
    """
    result_1 = client.query(query_1).result()

    # Mostrar los resultados en Streamlit
    st.write("## Pregunta 1: ¿Qué país tiene la esperanza de vida más alta para el 2040?")

    for row in result_1:
        st.write(f"Respuesta: {row['Pais']} tiene la esperanza de vida más alta para el 2040 con {row['Esperanza_vida_total']} años.")

    # Pregunta 2
    st.write("2. ¿Qué países tienen la esperanza de vida más baja en 2040?")
    # Agrega aquí las consultas y visualizaciones para las otras preguntas

# El resto del código permanece sin cambios
    # Pregunta 3
    st.write("3. ¿Cuáles son los cinco países con la mayor esperanza de vida en 2040?")

    # Pregunta 4
    st.write("4. ¿Cuál es la relación entre las emisiones de CO2 y la esperanza de vida?")

    # Pregunta 5
    st.write("5. ¿Cómo afecta el nivel de educación obligatoria en años a la esperanza de vida?")

    # Pregunta 6
    st.write("6. ¿Cómo ha cambiado la esperanza de vida global en las últimas dos décadas?")

    # Pregunta 7
    st.write("7. ¿Cómo afecta el gasto gubernamental en salud al aumento de la esperanza de vida?")

    # Pregunta 8
    st.write("8. ¿Existe una correlación entre la estabilidad política y la esperanza de vida?")

    # Pregunta 9
    st.write("9. ¿Cuál es la relación entre el acceso al agua potable  y la esperanza de vida?")

    # Pregunta 10
    st.write("10. ¿Cómo influye el índice GINI en la esperanza de vida?")

    # Pregunta 11
    st.write("11. ¿Cómo afecta el nivel de educación obligatoria en años a la tasa de mortalidad en un país?")

    # Pregunta 12
    st.write("12. ¿Cómo afecta el PIB per cápita a la prevalencia de desnutrición en la población?")

    # Pregunta 13
    st.write("13. ¿Existe una relación entre las emisiones de CO2 y la tasa de mortalidad por enfermedades cardiovasculares, cáncer y diabetes?")

    # Pregunta 14
    st.write("14. ¿Hay diferencias significativas en la tasa de mortalidad entre la población rural y urbana?")

    # Pregunta 15
    st.write("15. ¿Cómo afecta la población urbana al acceso al agua potable?")

elif tema_seleccionado == "Acerca de Nosotros":

    st.write("## Acerca de Nosotros")
    
    # Agrega el contenido para el Tema 3
    st.write("Somos una consultora de datos llamada LatAm-Data Consulting encargada de realizar proyectos de data science sobre cualquier ámbito o sector que las empresas públicas o privadas deseen desarrollar con el fin de brindar herramientas para que tomen las mejores decisiones empresariales o corporativas basadas en datos (data-driven), estas decisiones contribuirán aumentar la eficiencia en todos los procesos con los que cuente la empresa (predicciones y pronóstico, medición de rendimientos, identificar oportunidades de negocio, análisis de competencia, reducción de riesgos, experiencia al cliente e innovación).")
    
    st.write("Para el presente proyecto, el propósito es trabajar en colaboración con entidades gubernamentales para mejorar la calidad de vida de las personas, aumentar los niveles de esperanza de vida y fomentar la salud y el bienestar a nivel global. Esto se realizará mediante un proyecto de data science completo en donde se involucren procesos de data engineering, data analytics y machine learning; basados principalmente en un dataset del Banco Mundial y otras fuentes de interés que proporcionen datos de calidad con el fin de realizar un ciclo de vida de dato completo y llegar a la resolución de los objetivos planteados.")
    
    st.write("## Equipo de Trabajo")
    st.write("Contamos con un excelente equipo de profesionales con amplios conocimientos en el campo de análisis de datos.")
    
    # Agrega la información del equipo
    st.write("* Brenda Schutt, (Data Analytics, Data Scientist)")
    st.write("* Mara Laudonia (Data Analytics, Data Scientist)")
    st.write("* Haider Infante Rey, (Data Engineer, Data Scientist)")
    
    # Agrega la imagen del equipo
    st.image("imagenes/01team.png", caption="Equipo de Trabajo")

else:
    st.write("Selecciona un tema para ver contenido específico.")

# Fin del código