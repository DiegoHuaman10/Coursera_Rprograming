import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title("Programación Avanzada")
if st.sidebar.button("¿Quiénes somos?"):
    st.sidebar.write("Somos un grupo de estudiantes de V ciclo de Ingeniería de la Universidad Peruano Cayetano Heredia (UPCH) que ha elaborado como proyecto final del curso de “Programación Avanzada”  una página web con el tema “SUNEDU - Licenciamiento Institucional ”")
    st.sidebar.subheader("Diego  Manuel Huamán Abad")
    st.sidebar.subheader("Solait Alejandra De La Cruz Reyes")
    st.sidebar.subheader(" Neyeli Verenice Sobrado Vergara")
    st.sidebar.subheader("Eyvind Francisco Herrera More")

if st.sidebar.button("Objetivos"):
    st.sidebar.write("Buscamos crear una página interactiva y de fácil comprensión para nuestro usuario  con la Dataset de SUNEDU - Licenciamiento Institucional poniendo en práctica todo lo aprendido en el curso de Programación Avanzada.")


st.title("Licenciamiento Institucional")
st.write("**Se presenta el avance y estatus del Licenciamiento Institucional de las Universidades peruanas. Incluye información de región y tipo de entidad.**")
st.write("Mostrar al público qué instituciones del país son licenciadas por la Superintendencia Nacional de Educación Superior (SUNEDU) es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además,  garantiza la calidad académica y eficiencia en la formación del futuro profesional como la proyección laboral en beneficio del estudiante")

#Ubicación de universidades por regiones
st.write("En el siguiente mapa, se muestra las universidades Peruanas de acuerdo a su ubicación geográfica")
url4='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/Ubicaci%C3%B3n.csv'
file4 = pd.read_csv(url4, sep= ',')
st.map(file4)

st.write("**¿Cómo desea revisar la información?**")
st.selectbox("Por ubicación",("AMAZONAS","ÁNCASH","APURIMAC","AREQUIPA","AYACUCHO","CAJAMARCA","CALLAO","CUSCO","HUANCAVELICA","HUANUCO","ICA","JUNIN","LA LIBERTAD","LAMBAYEQUE","LIMA","LORETO","MADRE DE DIOS","MOQUEGUA","PASCO","PIURA","PUNO","SAN MARTIN","TACNA","TUMBES","UCAYALI"))
st.selectbox("Por el tipo de gestión",("PRIVADAS","NACIONALES"))

url="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional_7_2.csv"
filename="LicenciamientoInstitucional_7_2.csv"
df=pd.read_csv("LicenciamientoInstitucional_7_2.csv")
print df
st.subheader("**Características del Dataset**")
st.write(df.describe())
           
    
    
    
st.subheader("Periodo de Licenciamiento")
st.write("[Agregar texto]")
url ="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional_7_2.csv"
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


tab1, tab2 = st.tabs(["Universidades Privadas", "Universidades Nacionales"])
tab1.write("Aquí poner un seleccionador")
tab2.write("Aquí poner un seleccionador")
