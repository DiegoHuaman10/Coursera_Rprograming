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
   st.write("**EXISTENCIA DE OBJETIVOS ACADEMICOS, GRADOS Y TITULOS A OTORGAR, Y PLANES DE ESTUDIO CORRESPONDIENTE.**")
   st.write(" La acción educativa requiere metas claras para los diversos miembros de la comunidad universitaria.  Estos deben ser parte de los planes de estudio. Los programas educativos deben poner en claro los procedimientos administrativos y los requisitos previos que todos los estudiantes deben seguir desde su ingreso a la universidad  hasta su graduación. Por lo tanto, la universidad debe contemplar que sus programas tengan metas, que haya una jerarquía de metas institucionales y que guarden coherencia entre ellas.")
with tab02:
   st.write("**OFERTA EDUCATIVA A CREARSE COMPATIBLE CON LOS FINES PROPUESTOS EN LOS INSTRUMENTOS DE PLANEAMIENTO.**")
   st.write("Los servicios educativos necesitan recursos para financiar sus actividades.Las universidades deben contar con un presupuesto  financiado y sustentado con el plan operativo para los años siguientes.")
with tab03:
   st.write("**INFRAESTRUCTURA Y EQUIPAMIENTO ADECUADO AL CUMPLIMIENTO DE SUS FUNCIONES (AULAS, BIBLIOTECAS, LABORATORIOS, ENTRE OTROS).**")
   st.write("Los servicios educativos deben brindarse en un ambiente que cumpla con los requisitos mínimos de seguridad, capacidad y equipo necesario. La infraestructura de la universidad debe cumplir con la normatividad vigente. Aunque la educación ha sufrido grandes cambios debido a los avances tecnológicos,algunos servicios educativos han sido y serán proporcionados de forma  presencial. La universidad debe ser capaz de administrar todas sus instalaciones de acuerdo con la promoción de ventas.Para sus fines relacionados con los servicios de formación que prestan y sus antropometrías que determinarán el tipo de el tipo de ambientes el mobiliario y equipamiento  Los estudiantes universitarios deben tener un local de uso exclusivo  porque los lugares de educación básica  están diseñados para estudiantes de diferentes grupos de edad, por lo que tienen diferentes características de ambiente, equipamiento y mobiliario. También incluye requisitos previos que deben utilizarse para otras formas de educación superior.Realizar actividades de acuerdo a sus características de aprendizaje; por lo tanto, el tipo de ambiente, las dimensiones, el mobiliario y los equipos utilizados son diferentes.")
with tab04:
   st.write("**LÍNEAS DE INVESTIGACIÓN A SER DESARROLLADAS.**")
   st.write("Las universidades deben realizar actividades de investigación bajo la dirección de profesores y estudiantes, creando así un ambiente propicio para la creación de conocimiento.")
with tab05:
   st.write("**VERIFICACIÓN DE LA DISPONIBILIDAD DE PERSONAL DOCENTE CALIFICADO CON NO MENOS DE 25% DE DOCENTES A TIEMPO COMPLETO.**")
   st.write("El papel de los docentes en la mejora del aprendizaje es muy importante. Si bien esta interacción tiene lugar en el aula, también es importante fuera del aula, ya que permite que los estudiantes se absuelvan de  dudas o participen en las investigaciones. Para ello, las universidades deben contar con al menos un 25% de personal docente a tiempo completo, que es un porcentaje suficiente del total de programas de estudio.")
with tab06:
   st.write("**VERIFICACIÓN DE LOS SERVICIOS EDUCACIONALES COMPLEMENTARIOS BÁSICOS (SERVICIO MÉDICO, SOCIAL, PSICOPEDAGÓGICO, DEPORTIVO, ENTRE OTROS).**")
   st.write("La educación es un servicio constante y versátil. Este servicio forma parte de todo lo gestionado que complemente o facilite aspectos de la formación. De esta manera, las universidades deben ser capaces de proporcionar a los estudiantes ofertas de educación complementaria satisfactorias.")
with tab07:
   st.write("**EXISTENCIA DE MECANISMOS DE MEDIACIÓN E INSERCIÓN LABORAL (BOLSA DE TRABAJO U OTROS).**")
   st.write("Uno de los objetivos de las universidades modernas es preparar profesionales capaces de ingresar al mercado a trabajar. Con esta titulación, los estudiantes deberán ser capaces de realizar prácticas preprofesionales para facilitar su integración progresiva en el mercado laboral.")
with tab08:
   st.write("**CBC  COMPLEMENTARIA: TRANSPARENCIA DE UNIVERSIDADES.**")
   st.write("Cada universidad debe divulgar información sobre su oferta académica así como la calidad de sus servicios prestados. Su finalidad es facilitar la toma de decisiones a los alumnos y sus familias.")
   
st.write("**_______________________________________________________________________________________**") 
#Ubicación de universidades por regiones
st.subheader("Mapa de ubicación geográfica:")
st.write("En el siguiente mapa, se muestra las universidades Peruanas de acuerdo a su ubicación geográf:ica.")
url4='https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/Ubicaci%C3%B3n.csv'
file4 = pd.read_csv(url4, sep= ',')
st.map(file4)

#----------------------------------------------------------------------
url="https://raw.githubusercontent.com/DiegoHuaman10/Proyecto-Prograavanzada/main/LicenciamientoInstitucional.csv"
filename="LicenciamientoInstitucional.csv"
df=pd.read_csv("LicenciamientoInstitucional.csv")

st.write("**_______________________________________________________________________________________**") 
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
st.write("**_______________________________________________________________________________________**") 
st.subheader("**Información por búsqueda:**")
tab1, tab2= st.tabs(["**Por regiones**", "**Por universidad**"])
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
   
   
