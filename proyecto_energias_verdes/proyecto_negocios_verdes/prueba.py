import streamlit as st
import pandas as pd
import plotly.express as px

print("✅ Streamlit version:", st.__version__)
print("✅ Pandas version:", pd.__version__)
print("✅ Plotly version:", px.__version__)

# Crear un dataframe de prueba
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})

print("✅ DataFrame creado exitosamente:")
print(df)

print("🎉 ¡Todas las librerías están instaladas correctamente!")