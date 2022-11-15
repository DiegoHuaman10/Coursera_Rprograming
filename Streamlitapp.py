import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

st.title("Licenciamiento Institucional")
st.subheader("Se presenta el avance y estatus del Licenciamiento Institucional de las Universidades peruanas. Incluye información de región y tipo de entidad.")
st.text("[Dar un contexto---alguién puede ir escribiendo esto bien referenciado]")

#@st.experimental_memo
#def download_data():
 # url = "https://www.datosabiertos.gob.pe/sites/default/files/Licenciamiento%20Institucional_7.csv"
 # filename = 'Licenciamiento Institucional_7.csv'
 # urllib.request.urlretrieve(url, filename)
#download_data()

file = pd.read_csv("Licenciamiento Institucional_7.csv")
print(file)
