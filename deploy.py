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
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Deploy_streamlit/pf-henry-404414-784e39ca59ab.json"

# Lista de temas
temas = ["Dashboards KPI'S-Looker Studio", "Modelo de Machine Learning", "Preguntas", "Acerca de Nosotros"]

# Barra lateral con botones para cada tema
tema_seleccionado = st.sidebar.radio("Selecciona un tema", temas)

# Página principal
st.title("Presentación Proyecto Final Henry")

# Mostrar contenido según el tema seleccionado
if tema_seleccionado == "Dashboards KPI'S-Looker Studio":
    # ... (código existente)
  pass
elif tema_seleccionado == "Modelo de Machine Learning":
    st.write("Modelo de Machine Learning")
    # Agrega aquí el contenido para el Tema 2

elif tema_seleccionado == "Preguntas":
    st.write("## Preguntas sobre Esperanza de Vida")

    # Lista de preguntas
    preguntas = [
        "¿Qué país tiene la esperanza de vida más alta para el 2040?",
        "¿Qué países tienen la esperanza de vida más baja en 2040?",
        "¿Cuáles son los cinco países con la mayor esperanza de vida en 2040?",
        "¿Cuál es la relación entre las emisiones de CO2 y la esperanza de vida?",
        "¿Cómo afecta el nivel de educación obligatoria en años a la esperanza de vida?",
        "¿Cómo ha cambiado la esperanza de vida global en las últimas dos décadas?",
        "¿Cómo afecta el gasto gubernamental en salud al aumento de la esperanza de vida?",
        "¿Existe una correlación entre la estabilidad política y la esperanza de vida?",
        "¿Cuál es la relación entre el acceso al agua potable y la esperanza de vida?",
        "¿Cómo influye el índice GINI en la esperanza de vida?",
        "¿Cómo afecta el nivel de educación obligatoria en años a la tasa de mortalidad en un país?",
        "¿Cómo afecta el PIB per cápita a la prevalencia de desnutrición en la población?",
        "¿Existe una relación entre las emisiones de CO2 y la tasa de mortalidad por enfermedades cardiovasculares, cáncer y diabetes?",
        "¿Hay diferencias significativas en la tasa de mortalidad entre la población rural y urbana?",
        "¿Cómo afecta a la población urbana al acceso al agua potable?"
    ]
# Lista desplegable para seleccionar la pregunta
    pregunta_seleccionada = st.selectbox("Selecciona una pregunta", preguntas)

    if pregunta_seleccionada:
        st.write(f"Has seleccionado la pregunta: {pregunta_seleccionada}")

        # Configura tu credencial de Google Cloud
        client = bigquery.Client.from_service_account_json('pf-henry-404414-784e39ca59ab.json')

        # Mapa de scripts por pregunta
scripts = {
   "¿Qué país tiene la esperanza de vida más alta para el 2040?": "scripts/pregunta_1.py",
    # Importar la API de BigQuery
   
# Crear un cliente de BigQuery
    client = bigquery.Client.from_service_account_json('pf-henry-404414-784e39ca59ab.json')

# Consultar el archivo
query = """
SELECT *
FROM `pf-henry-404414.Noteboks.`
WHERE name = 'scripts/pregunta_1.py'
"""

# Ejecutar la consulta
job_config = bigquery.QueryJobConfig()
job_config.destination = "/tmp/pregunta_1.py"
job_config.write_disposition = bigquery.WriteDisposition().WRITE_TRUNCATE

job = client.query(query, job_config=job_config)
job.result()

# Abrir el archivo
with open("/tmp/scripts/pregunta_1.py", "r") as script_file:
    script_code = script_file.read()
    exec(script_code)

    # Agrega scripts para otras preguntas aquí
        }

        # Agregar un botón para ejecutar el script
if st.button("Consultar"):
    # Cargar el script correspondiente a la pregunta seleccionada
    script_path = scripts.get(pregunta_seleccionada, "")
    if script_path:
        # Ejecutar el script
        try:
            with open(script_path, "r") as script_file:
                script_code = script_file.read()
                exec(script_code)
        except Exception as e:
            st.write(f"Error al ejecutar el script: {e}")
    else:
        st.write("Script no encontrado.")

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
