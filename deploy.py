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

    # Mapa de consultas por pregunta
   

    consultas = {
    "¿Qué país tiene la esperanza de vida más alta para el 2040?": 
        """
        SELECT Pais, Esperanza_vida_total
        FROM `pf-henry-404414.Notebooks.Preguntas_ML`
        WHERE Ano = 2040
        ORDER BY Esperanza_vida_total DESC
        LIMIT 1
        """
    ,

    "¿¿Qué países tienen la esperanza de vida más baja en 2040?": 
        """
        SELECT Pais, Esperanza_vida_total
        FROM `pf-henry-404414.Notebooks.Preguntas_ML`
        WHERE Ano = 2040
        ORDER BY Esperanza_vida_total DESC
        LIMIT 5
        """
    ,

    # Agrega consultas para otras preguntas aquí
}

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
   
