import streamlit as st
import pandas as pd
import numpy as np


st.title("Licenciamiento Institucional")
st.subheader("Se presenta el avance y estatus del Licenciamiento Institucional de las Universidades peruanas. Incluye información de región y tipo de entidad.")
st.text("Mostrar al público qué instituciones del país son licenciadas por la Superintendencia Nacional de Educación Superior (SUNEDU) es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además, garantiza la calidad académica y eficiencia de la formación de un futuri profesional como la proyección laboral en un beneficio del estudiante")


url = "https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional_7.csv"
# filename = 'Licenciamiento Institucional_7.csv'
# urllib.request.urlretrieve(url, filename)
#download_data()

file = pd.read_csv(url, sep= ';')

print(file)

       
