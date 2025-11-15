import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(
    page_title="Negocios Verdes Colombia",
    layout="wide",
    page_icon="🌱"
)

st.title("🌿 Dashboard - Negocios Verdes Colombia")

# Cargar datos
url = "https://raw.githubusercontent.com/natachasena2023-sys/bootcam_analisis/refs/heads/main/Listado_de_Negocios_Verdes_20251025.csv"
df = pd.read_csv(url)

# **CÓDIGO SEGURO - NO GENERARÁ ERRORES**
st.subheader("📊 Métricas Generales")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Negocios", len(df))

with col2:
    # Buscar columna de departamento de forma segura
    depto_cols = [col for col in df.columns if 'departamento' in col.lower()]
    if depto_cols:
        st.metric("Departamentos", df[depto_cols[0]].nunique())
    else:
        st.metric("Categorías Principales", df.iloc[:, 1].nunique())

with col3:
    # Buscar columna de municipio de forma segura
    muni_cols = [col for col in df.columns if 'municipio' in col.lower()]
    if muni_cols:
        st.metric("Municipios", df[muni_cols[0]].nunique())
    else:
        st.metric("Subcategorías", df.iloc[:, 2].nunique())

with col4:
    # Buscar columna de sector de forma segura
    sector_cols = [col for col in df.columns if 'sector' in col.lower()]
    if sector_cols:
        st.metric("Sectores", df[sector_cols[0]].nunique())
    else:
        st.metric("Tipos", df.iloc[:, 3].nunique())

# Mostrar información del dataset
st.subheader("🔍 Información del Dataset")
st.write(f"El dataset tiene **{len(df)}** negocios verdes y **{len(df.columns)}** columnas")

# Mostrar columnas disponibles
with st.expander("Ver columnas disponibles"):
    for col in df.columns:
        st.write(f"- `{col}`")

# Mostrar datos
st.subheader("📋 Listado de Negocios Verdes")
st.dataframe(df, width='stretch')

# Gráfico simple con la primera columna categórica
st.subheader("📈 Distribución")
for col in df.columns:
    if df[col].dtype == 'object' and df[col].nunique() < 20:
        fig = px.bar(df[col].value_counts(), 
                    title=f"Distribución de {col}",
                    labels={'value': 'Cantidad', 'index': col})
        st.plotly_chart(fig, width='stretch')
        break