import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#------------------------------------------------------------------
st.sidebar.title("**Programación Avanzada**")
names=st.sidebar.expander("**¿Quiénes somos?**")
names.write("Somos estudiantes del V ciclo de Ingeniería de la Universidad Peruano Cayetano Heredia (UPCH) que, como parte del producto final del curso “Programación Avanzada”, elaboramos una página web con el presente tema""")
names.write("**- Diego Manuel Huamán Abad**")
foto=Image.open("foto.jpg")
names.image(foto)
names.write("**- Nayeli Verenice Sobrado**")
foto=Image.open("foto.jpg")
names.image(foto)
names.write("**- Eyvind Francisco Herrera More**")
foto=Image.open("foto.jpg")
names.image(foto)
names.write("**- Solait Alejandra de la cruz**")
foto=Image.open("foto.jpg")
names.image(foto)
aim=st.sidebar.expander("**Objetivo**")
aim.write("Crear una página interactiva para presentar el avance y estatus del Licenciamiento Institucional de las Universidades peruanas incluyendo información de región y tipo de entidad.")

#------------------------------------------------------------------
st.title("Licenciamiento Institucional")
st.write("El Licenciamiento Institucional es un procedimiento obligatorio para todas las universidades del país, a través del cual cada casa de estudios debe demostrar ante la SUNEDU que cumple con las Condiciones Básicas de Calidad (CBC) para poder brindar el servicio educativo. Como resultado de este proceso, ahora existe un sistema universitario más ordenado, y universidades con una mayor orientación hacia la mejora continua.")
INICIO=Image.open("licenciamiento.jpg")
st.image(INICIO, caption="Licenciamiento de Universidades en el Perú", use_column_width=True)
st.write("Mostrar al público qué instituciones del país son licenciadas por la SUNEDU es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además, garantiza la calidad académica y eficiencia en la formación del futuro profesional como la proyección laboral en beneficio del estudiante.")
CBC=Image.open("CBC.jpg")
st.image(CBC, use_column_width=True)

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

#------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["**Periodo de licenciamiento**", "**Tipo de gestión**", "**Buscar por regiones**"])

with tab1:
   st.write("El periodo de licenciamiento refiere a...")
   url ="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional_7_2.csv"
   file = pd.read_csv(url, sep= ',')
   st.line_chart(data=file, x='NOMBRE', y='PERIODO_LICENCIAMIENTO')

with tab2:
   st.write("Actualmente existen ....")

with tab3:
   st.write("Actualmente existen ....")
   url2='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/universidades_por_regiones.csv'
   file2 = pd.read_csv(url2, sep= ',')
   st.line_chart(data=file2, x='NOMBRE', y='DEPARTAMENTO')



 
  
