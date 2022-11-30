import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.sidebar.title("**Programación Avanzada**")
expander=st.sidebar.expander("**¿Quiénes somos?**")
expander.write("Somos estudiantes del V ciclo de Ingeniería de la Universidad Peruano Cayetano Heredia (UPCH) que, como parte del producto final del curso “Programación Avanzada”, elaboramos una página web con el presente tema")
expander.write("**Diego Huamán Abad**")
expander.Image.open("foto.png")
expander.write("**Nayeli Verenice Sobrado**")
expander.write("**Eyvind Herrera More**")
expander.write("**Solait Alejandra de la cruz**")
expander=st.sidebar.expander("**Objetivo**")
expander.write("Crear una página interactiva para presentar el avance y estatus del Licenciamiento Institucional de las Universidades peruanas incluyendo información de región y tipo de entidad.")


#st.sidebar.multiselect("**Por ubicación geográfica**",["AMAZONAS","ÁNCASH","APURIMAC","AREQUIPA","AYACUCHO","CAJAMARCA","CALLAO","CUSCO","HUANCAVELICA","HUANUCO","ICA","JUNIN","LA LIBERTAD","LAMBAYEQUE","LIMA","LORETO","MADRE DE DIOS","MOQUEGUA","PASCO","PIURA","PUNO","SAN MARTIN","TACNA","TUMBES","UCAYALI"])
#st.sidebar.multiselect("**Por el tipo de gestión**",["PRIVADAS","NACIONALES"])

st.title("Licenciamiento Institucional")
image=Image.open("licenciamiento.jpg")
st.image(image, caption="Licenciamiento de Universidades en el Perú", use_column_width=True)

st.write("**Introducción**")
st.write("Mostrar al público qué instituciones del país son licenciadas por la Superintendencia Nacional de Educación Superior (SUNEDU) es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además,  garantiza la calidad académica y eficiencia en la formación del futuro profesional como la proyección laboral en beneficio del estudiante")

#Ubicación de universidades por regiones
st.write("En el siguiente mapa, se muestra las universidades Peruanas de acuerdo a su ubicación geográfica")
url4='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/Ubicaci%C3%B3n.csv'
file4 = pd.read_csv(url4, sep= ',')
st.map(file4)

url="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional_7_2.csv"
filename="LicenciamientoInstitucional_7_2.csv"
df=pd.read_csv("LicenciamientoInstitucional_7_2.csv")
st.write("**Datos generales**")
st.dataframe(df)


           
           
  
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

#frfnejkbnrjf
k=df.loc[df.loc[:,'PERIODO_LICENCIAMIENTO']>0]
print(k)


 
  
