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
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PARA DEPLOY/pf-henry-404414-784e39ca59ab.json"

# Configura tu credencial de Google Cloud
client = bigquery.Client.from_service_account_json(
    "Deploy_streamlit/pf-henry-404414-784e39ca59ab.json"
)

# Inicializar cliente BigQuery
client = bigquery.Client()

# Cargar datos desde BigQuery
query = """
SELECT *
FROM `pf-henry-404414.data_machine_learning.wb_data_machine_learning_bis`
WHERE year = 2040
"""
data_original = client.query(query).to_dataframe()
data = data_original.copy()

# Lista de temas
temas = ["Dashboards KPI'S-Looker Studio", "Modelo de Machine Learning", "Preguntas", "Acerca de Nosotros"]

# Barra lateral con botones para cada tema
tema_seleccionado = st.sidebar.radio("Selecciona un tema", temas)

if tema_seleccionado == "Preguntas":
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
        "¿Cómo afecta la población urbana al acceso al agua potable?"
    ]

    # Lista desplegable para seleccionar la pregunta
    pregunta_seleccionada = st.selectbox("Selecciona una pregunta", preguntas)

    # Mapa de consultas por pregunta
    consultas = {
        "¿Qué país tiene la esperanza de vida más alta para el 2040?": """
SELECT country, esperanza_vida_total
FROM `pf-henry-404414.data_machine_learning.wb_data_machine_learning_bis`
WHERE year = 2040
ORDER BY esperanza_vida_total DESC
LIMIT 1
""",
    }

    # Ejecutar consulta según la pregunta seleccionada
    if pregunta_seleccionada in consultas:
        result = client.query(consultas[pregunta_seleccionada]).result()

        # Mostrar los resultados en Streamlit
        st.write(f"## {pregunta_seleccionada}")

    for row in result:
        st.write(f"Respuesta: {row['country']} tiene la esperanza de vida de {row['esperanza_vida_total']} años")






def obtener_paises_con_menor_esperanza_vida(pregunta_seleccionada):
    # Lógica para obtener los países con la esperanza de vida más baja en 2040
    return []

# Ejecutar consulta según la pregunta seleccionada
if pregunta_seleccionada in consultas:
    result = client.query(consultas[pregunta_seleccionada]).result()

    # Mostrar los resultados en Streamlit
    st.write(f"## {pregunta_seleccionada}")

    for row in result:
        st.write(f"Respuesta: {row['Pais']} tiene la esperanza de vida más alta para el 2040 con {row['Esperanza_vida_total']} años.")