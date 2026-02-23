import streamlit as st
import pandas as pd

st. set_page_config(page_title="Dashboard de Prediccion de Accidentes",layout="wide")

st.title("Dashboard de Prediccion de Accidentes")
st.markdown("Prediccion de Accidentes por Años, Rango de edad, Tipo de clima, estado del conductor y tipo de carretera.")

@st.cache_data 
def load_data():
    df = pd.read_csv("accident_prediction.csv")
    return df

df = load_data()
st.dataframe(df)