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
aim.write("Crear una página interactiva para presentar el avance y estatus del Licenciamiento Institucional de las universidades peruanas, incluyendo la región y tipo de entidad.")

#------------------------------------------------------------------
st.title("Licenciamiento Institucional")
st.write("El Licenciamiento Institucional es un procedimiento obligatorio para todas las universidades del país; por esta razón, cada casa de estudios debe demostrar ante la SUNEDU que cumple con las Condiciones Básicas de Calidad (CBC) para poder brindar su servicio educativo. Como resultado de este proceso, ahora existe un sistema universitario más ordenado, y universidades con una mayor orientación hacia la mejora continua.")
INICIO=Image.open("licenciamiento.jpg")
st.image(INICIO, caption="Licenciamiento de Universidades en el Perú", use_column_width=True)
st.write("Mostrar al público qué instituciones del país son licenciadas por la SUNEDU es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además, garantiza la calidad académica y eficiencia en la formación del futuro profesional como la proyección laboral en beneficio del estudiante.")
CBC=Image.open("CBC.jpg")
st.image(CBC, use_column_width=True)

#Ubicación de universidades por regiones
st.write("En el siguiente mapa, se muestra las universidades Peruanas de acuerdo a su ubicación geográfica.")
url4='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/Ubicaci%C3%B3n.csv'
file4 = pd.read_csv(url4, sep= ',')
st.map(file4)

#----------------------------------------------------------------------
url="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional.csv"
filename="LicenciamientoInstitucional.csv"
df=pd.read_csv("LicenciamientoInstitucional.csv")

st.header("**INFORMACIÓN GENERAL DEL LICENCIAMIENTO**"):
tab1, tab2= st.tabs(["**Periodo de licenciamiento**", "**Tipo de gestión**"])
with tab1:
   st.write("El periodo de licenciamiento refiere al tiempo por el cual la universidad ha recibido el licenciamiento. El tiempo mínimo de licenciamiento es de 6 años, además, tambien hay periodos de 8 y 10 años. Se otorga la mayor cantidad de años a las universidades que impulsan proyectos de investigación, apoyan a sus docentes investigadores y buscan que un mayor número de estudiantes escriban artículos que puedan ser publicados en alguna revista.")
   df_pl= df.PERIODO_LICENCIAMIENTO.value_counts()
   st.bar_chart(df_pl)
with tab2:
   df_gestion= df.TIPO_GESTION.value_counts()
   st.write('En el siguiente gráfico, se presenta una distribución de las universidades nacionales de acuerdo al tipo de gestión')
   st.bar_chart(df_gestion)
   
df_gpriv=df[df["TIPO_GESTION"]=="PRIVADO"]
   df_gp=df_gpriv.ESTADO_LICENCIAMIENTO.value_counts()
   st.write('**Licenciamiento en la gestión privada:**')
   st.bar_chart(df_gp)
   
   df_gpúb=df[df["TIPO_GESTION"]=="PÚBLICO"]
   df_gp=df_gpúb.ESTADO_LICENCIAMIENTO.value_counts()
   st.write('**Licenciamiento en la gestión pública:**')
   st.bar_chart(df_gp)
#------------------------------------------------------------------

st.header("**INFORMACIÓN POR BÚSQUEDA**"):
tab1, tab2= st.tabs(["**Buscar por regiones**", "**Buscar por Universidad**"])
with tab1:
   st.write("En la actualidad, en cada región del Perú, existe al menos una a más universidades públicas o privadas. Lo cual significa, que cada habitante tiene mayor acceso a la educación, así como también la oportunidad de estudiar más cerca a sus hogares.")
   text_imput=st.text_input("**Ingrese la región para conocer qué universidades se encuentran en el lugar indicado👇 (Escribir en MAYÚSCULAS)**",)
   df_region=df[df["DEPARTAMENTO"]==text_imput]
   st.dataframe(df_region)
   
   df_tg= df_region.TIPO_GESTION.value_counts()
   st.write('**Distribución por el tipo de gestión:**')
   st.bar_chart(df_tg)
   
   df_el= df_region.ESTADO_LICENCIAMIENTO.value_counts()
   st.write('**Distribución por el estado de licenciamiento:**')
   st.bar_chart(df_el)
      
with tab2:
   text_imput=st.text_input("**Ingrese las SIGLAS del nombre de la universidad de su interés 👇 (Escribir en MAYÚSCULAS)**",)
   df_univ=df[df["SIGLAS"]==text_imput]
   st.dataframe(df_univ)
   
   
