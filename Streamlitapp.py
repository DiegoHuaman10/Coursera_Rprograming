import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#------------------------------------------------------------------
st.sidebar.title("**Programación Avanzada**")
names=st.sidebar.expander("**¿Quiénes somos?**")
names.write("Somos estudiantes del V ciclo de Ingeniería de la Universidad Peruano Cayetano Heredia (UPCH) que, como parte del producto final del curso “Programación Avanzada”, elaboramos una página web con el presente tema""")
names.write("**- Diego Manuel Huamán Abad**")
foto=Image.open("imagen.jpeg")
names.image(foto)
names.write("**- Nayeli Verenice Sobrado**")
foto=Image.open("hola.jpg")
names.image(foto)
names.write("**- Eyvind Francisco Herrera More**")
foto=Image.open("Eyvind.jpeg")
names.image(foto)
names.write("**- Solait Alejandra de la cruz**")
foto=Image.open("yo.jpg")
names.image(foto)
aim=st.sidebar.expander("**Objetivo**")
aim.write("Presentar el avance y estatus del Licenciamiento Institucional de las universidades peruanas, incluyendo la región y tipo de entidad.")

#------------------------------------------------------------------
st.header("**LICENCIAMIENTO INSTITUCIONAL**")
st.write("El Licenciamiento Institucional es un procedimiento obligatorio para todas las universidades del país; por esta razón, cada casa de estudios debe demostrar ante la SUNEDU que cumple con las Condiciones Básicas de Calidad (CBC) para poder brindar su servicio educativo. Como resultado de este proceso, ahora existe un sistema universitario más ordenado, y universidades con una mayor orientación hacia la mejora continua.")
INICIO=Image.open("licenciamiento.jpg")
st.image(INICIO, caption="Licenciamiento de Universidades en el Perú", use_column_width=True)
st.write("Mostrar al público qué instituciones del país son licenciadas por la SUNEDU es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, la infraestructura, además, garantiza la calidad académica y eficiencia en la formación del futuro profesional como la proyección laboral en beneficio del estudiante.")
CBC=Image.open("CBC.jpg")
st.image(CBC, use_column_width=True)

#Descripción de las condiciones básicas de calidad 
st.write("Descripción de las CBC: ")
tab01, tab02, tab03, tab04, tab05, tab06, tab07, tab08= st.tabs(["**Condición I**", "**Condición II**", "**Condición III**", "**Condición IV**", "**Condición V**", "**Condición VI**", "**Condición VII**", "**Condición VIII**"])
with tab01:
   st.write(" EXISTENCIA DE OBJETIVOS ACADEMICOS, GRADOS Y TITULOS A OTORGAR, Y PLANES DE ESTUDIO CORRESPONDIENTE.")
with tab02:
   st.write("un presupuesto financiado y sustentado, coherente c")
with tab03:
   st.write("Elpo de ambientes, su dimensión, el mobiliario y el equipamiento que utilizan es diferente.")
with tab04:
   st.write("La universambiente propicio para la creación de conocimiento.")
with tab05:
   st.write("El rol quepleto, en peducativos.")
with tab06:
   st.write("El periodo de")
with tab07:
   st.write("El periodo de")
with tab08:
   st.write("El periodo de")
   
   
#Ubicación de universidades por regiones
st.header("**Mapa de ubicación geográfica**")
st.write("En el siguiente mapa, se muestra las universidades Peruanas de acuerdo a su ubicación geográfica.")
url4='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/Ubicaci%C3%B3n.csv'
file4 = pd.read_csv(url4, sep= ',')
st.map(file4)

#----------------------------------------------------------------------
url="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional.csv"
filename="LicenciamientoInstitucional.csv"
df=pd.read_csv("LicenciamientoInstitucional.csv")

st.subheader("Información general del licenciamiento:")
tab1, tab2= st.tabs(["**Periodo de licenciamiento**", "**Tipo de gestión**"])
with tab1:
   st.write("El periodo de licenciamiento refiere al tiempo por el cual la universidad ha recibido el licenciamiento. El tiempo mínimo de licenciamiento es de 6 años, además, tambien hay periodos de 8 y 10 años. Se otorga la mayor cantidad de años a las universidades que impulsan proyectos de investigación, apoyan a sus docentes investigadores y buscan que un mayor número de estudiantes escriban artículos que puedan ser publicados en alguna revista.")
   df_pl= df.PERIODO_LICENCIAMIENTO.value_counts()
   st.bar_chart(df_pl)
with tab2:
   df_gestion= df.TIPO_GESTION.value_counts()
   st.write("En el siguiente gráfico, se presenta una distribución de las universidades nacionales de acuerdo al tipo de gestión.")
   st.bar_chart(df_gestion)
   
   st.write("En relación a la gestión **privada**, se presenta la distribución del estado de licenciamiento, en donde se observa una igualdad (46 en ambos casos).")
   df_gpriv=df[df["TIPO_GESTION"]=="PRIVADO"]
   df_gp=df_gpriv.ESTADO_LICENCIAMIENTO.value_counts()
   st.bar_chart(df_gp)
   
   st.write("De la misma manera, se presenta la distribución del estado de licenciamiento para la gestión **pública**, donde 47 tienen la licencia otorgada, 2 denegada, 1 con informa de observaciones y 1 en ningún caso.")
   df_gpúb=df[df["TIPO_GESTION"]=="PÚBLICO"]
   df_gp=df_gpúb.ESTADO_LICENCIAMIENTO.value_counts()
   st.bar_chart(df_gp)
#------------------------------------------------------------------

st.subheader("**Información por búsqueda:**")
tab1, tab2= st.tabs(["**Por regiones**", "**Por Universidad**"])
with tab1:
   st.write("En la actualidad, en cada región del Perú, existe al menos una a más universidades públicas o privadas. Lo cual significa, que cada habitante tiene mayor acceso a la educación, así como también la oportunidad de estudiar más cerca a sus hogares.")
   text_imput=st.text_input("**Ingrese la región para conocer qué universidades se encuentran en el lugar indicado👇 (Escribir en MAYÚSCULAS)**",)
   df_region=df[df["DEPARTAMENTO"]==text_imput]
   df_region=df_region.drop(columns=["CODIGO_ENTIDAD","SIGLAS","FECHA_INICIO_LICENCIAMIENTO","FECHA_FIN_LICENCIAMIENTO","PERIODO_LICENCIAMIENTO","UBIGEO","LATITUD","LONGITUD","FECHA_CORTE"])
   
   st.write("Para la región",text_imput,",se presenta una distribución de las universidad por el **_tipo de gestión_**.")
   df_tg= df_region.TIPO_GESTION.value_counts()
   st.bar_chart(df_tg)
   
   st.write("Además, se presenta una distribución del **_estado de licencimianto_** de dichas universidades.")
   df_el= df_region.ESTADO_LICENCIAMIENTO.value_counts()
   st.bar_chart(df_el)
   
   st.write("Del mismo modo, se presenta tablas con las universidades pertenecientes a cada **_estado de licencimianto_**")
   st.write("**Licenciamiento otorgado**")
   df_lo=df_region[df_region["ESTADO_LICENCIAMIENTO"]=="LICENCIA OTORGADA"]
   st.dataframe(df_lo)
   st.write("**Licenciamiento denegada**")
   df_lo=df_region[df_region["ESTADO_LICENCIAMIENTO"]=="LICENCIA DENEGADA"]
   st.dataframe(df_lo)
   st.write("**Licenciamiento con observaciones**")
   df_lo=df_region[df_region["ESTADO_LICENCIAMIENTO"]=="LICENCIA CON INFORME DE OBSERVACIONES (IO) NOTIFICADO"]
   st.dataframe(df_lo)
   st.write("**Ninguno de los casos**")
   df_lo=df_region[df_region["ESTADO_LICENCIAMIENTO"]=="NINGUNO"]
   st.dataframe(df_lo)
   
with tab2:
   text_imput=st.text_input("**Ingrese las SIGLAS del nombre de la universidad de su interés 👇 (Escribir en MAYÚSCULAS)**",)
   df_univ=df[df["SIGLAS"]==text_imput]
   df_univ=df_univ.drop(columns=["CODIGO_ENTIDAD","FECHA_INICIO_LICENCIAMIENTO","FECHA_FIN_LICENCIAMIENTO","PERIODO_LICENCIAMIENTO","UBIGEO","LATITUD","LONGITUD","FECHA_CORTE"])
   st.dataframe(df_univ)
   
   
