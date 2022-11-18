import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

st.title("Licenciamiento Institucional")
st.subheader("Se presenta el avance y estatus del Licenciamiento Institucional de las Universidades peruanas. Incluye información de región y tipo de entidad.")
st.text(
        "Mostrar al público qué instituciones del país son licenciadas por la Superintendencia Nacional de Educación Superior (SUNEDU) es importante, ya que permite conocer cuáles cumplen con las condiciones básicas de calidad, como una buena infraestructura, además, garantiza la calidad académica y eficiencia de la formación de un futuro profesional como la proyección laboral en beneficio del estudiante."
)

#@st.experimental_memo
#def download_data():
# url = "https://www.datosabiertos.gob.pe/sites/default/files/Licenciamiento%20Institucional_7.csv"
# filename = 'Licenciamiento Institucional_7.csv'
# urllib.request.urlretrieve(url, filename)
#download_data()

file = pd.read_csv("LicenciamientoInstitucional_7.csv")
print(file)

text_input = st.text_input(
        "Sugerencias👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
)

        
       
