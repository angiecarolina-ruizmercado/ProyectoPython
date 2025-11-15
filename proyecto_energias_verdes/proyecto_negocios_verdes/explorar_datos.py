import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("🔍 EXPLORACIÓN DEL DATASET")

# Cargar datos
url = "https://raw.githubusercontent.com/natachasena2023-sys/bootcam_analisis/refs/heads/main/Listado_de_Negocios_Verdes_20251025.csv"
df = pd.read_csv(url)

st.write(f"**Filas:** {df.shape[0]}, **Columnas:** {df.shape[1]}")

# Mostrar TODAS las columnas
st.subheader("📋 COLUMNAS DISPONIBLES:")
for i, col in enumerate(df.columns, 1):
    st.write(f"{i}. **{col}**")

# Mostrar primeras filas
st.subheader("👀 PRIMERAS FILAS:")
st.dataframe(df.head(), width='stretch')