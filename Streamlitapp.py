import streamlit as st
import pandas as pd
import numpy as np


st.title("Licenciamiento Institucional")
st.subheader("Se presenta el avance y estatus del Licenciamiento Institucional de las Universidades peruanas. Incluye información de región y tipo de entidad.")
st.write("Mostrar al público qué instituciones del país son licenciadas por la Superintendencia Nacional de Educación Superior (SUNEDU) es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además,  garantiza la calidad académica y eficiencia en la formación del futuro profesional como la proyección laboral en beneficio del estudiante")

st.write("¿Cómo desea revisar la información?")
st.selectbox("Por ubicación",("AMAZONAS","ÁNCASH","APURIMAC","AREQUIPA","AYACUCHO","CAJAMARCA","CALLAO","CUSCO","HUANCAVELICA","HUANUCO","ICA","JUNIN","LA LIBERTAD","LAMBAYEQUE","LIMA","LORETO","MADRE DE DIOS","MOQUEGUA","PASCO","PIURA","PUNO","SAN MARTIN","TACNA","TUMBES","UCAYALI"))
st.selectbox("Por el tipo de gestión",("PRIVADAS","NACIONALES"))
url ="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional_7_2.csv"

st.subheader("Periodo de Licenciamiento")
st.write("[Agregar texto]")
file = pd.read_csv(url, sep= ',')
st.line_chart(data=file, x='NOMBRE', y='PERIODO_LICENCIAMIENTO')

#Universidades por regiones
st.subheader("Universidades por regiones")
st.write("[Agregar texto]")
url2='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/universidades_por_regiones.csv'
file2 = pd.read_csv(url2, sep= ',')
st.line_chart(data=file2, x='NOMBRE', y='DEPARTAMENTO')

# Estado de licenciamiento
st.subheader("Estado de Licenciamiento")
st.write("[Agregar texto]")
url3='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/estado%20de%20licenciamiento.csv'
file3 = pd.read_csv(url3, sep= ',')
st.line_chart(data=file3, x='NOMBRE', y='ESTADO_LICENCIAMIENTO')

#Ubicación de universidades por regiones
st.subheader("Ubicación de universidades por regiones")
st.write("[Agregar texto]")
url4='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/Ubicaci%C3%B3n.csv'
file4 = pd.read_csv(url4, sep= ',')
st.map(file4)

tab1, tab2 = st.tabs(["Universidades Privadas", "Universidades Nacionales"])
tab1.write("Aquí poner un seleccionador")
tab2.write("Aquí poner un seleccionador")
