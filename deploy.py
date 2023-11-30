import streamlit as st
import pandas as pd
import numpy as np
from google.cloud import bigquery
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import warnings
import os

warnings.filterwarnings('ignore')

st.set_option('deprecation.showfileUploaderEncoding', False)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pf-henry-404414-784e39ca59ab.json"

tema_seleccionado = st.sidebar.selectbox("Selecciona un tema", ["Preguntas"])  # Agregué un sidebar para seleccionar el tema

if tema_seleccionado == "Preguntas":
    st.write("## Preguntas sobre Esperanza de Vida")

    # Lista de preguntas
    preguntas = [
        "¿Qué país tiene la esperanza de vida más alta para el 2040?",
        "¿Qué países tienen la esperanza de vida más baja en 2040?",
        "Cuáles son los cinco países con la mayor esperanza de vida en 2040?",
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
          
        # Mapa de scripts por pregunta
        scripts = {
            "¿Qué país tiene la esperanza de vida más alta para el 2040?": "Scripts/scripts_pregunta_1.py",
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
                