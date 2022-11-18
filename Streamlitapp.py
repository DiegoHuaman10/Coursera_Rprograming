import streamlit as st
import pandas as pd
import numpy as np


st.title("Licenciamiento Institucional")
st.subheader("Se presenta el avance y estatus del Licenciamiento Institucional de las Universidades peruanas. Incluye información de región y tipo de entidad.")
st.write("Mostrar al público qué instituciones del país son licenciadas por la Superintendencia Nacional de Educación Superior (SUNEDU) es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además, garantiza la calidad académica y eficiencia de la formación de un futuri profesional como la proyección laboral en un beneficio del estudiante")


url = "https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional_7_2.csv"

st.subheader("Periodo de Licenciamiento")
st.write("[Agregar texto]")
file = pd.read_csv(url, sep= ',')
st.line_chart(data=file, x='NOMBRE', y='PERIODO_LICENCIAMIENTO')


       
