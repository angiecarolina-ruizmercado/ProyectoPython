import pandas as pd
import matplotlib.pyplot as plt
ruta = 'https://github.com/juliandariogiraldoocampo/temporal/raw/refs/heads/main/estado_zni.csv'
df = pd.read_csv(ruta)
df = df.dropna()
df['ENERGÍA ACTIVA'] = df['ENERGÍA ACTIVA'].str.replace(',' , '').astype(float).astype(int)
df['ENERGÍA REACTIVA'] = df['ENERGÍA REACTIVA'].str.replace(',' , '').astype(float).astype(int)
df['POTENCIA MÁXIMA'] = df['POTENCIA MÁXIMA'].str.replace(',' , '').astype(float)
lista_cambio = [['Á', 'A'],['É', 'E'],['Í', 'I'],['Ó', 'O'],['Ú', 'U']]
for i in range(5):
    df['MUNICIPIO'] = df['MUNICIPIO'].str.replace(lista_cambio[i][0],lista_cambio[i][1])
    df['DEPARTAMENTO'] = df['DEPARTAMENTO'].str.replace(lista_cambio[i][0],lista_cambio[i][1])
condicion = ~df['DEPARTAMENTO'].isin([
    'ARCHIPIELAGO DE SAN ANDRES',
    'ARCHIPIELAGO DE SAN ANDRES y PROVIDENCIA',
    'ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA'
])
df_colombia_continental = df[condicion]

categoria = ['DEPARTAMENTO', 'MUNICIPIO']
cols = ['ENERGÍA ACTIVA', 'ENERGÍA REACTIVA', 'POTENCIA MÁXIMA']
informe = df_colombia_continental.groupby(categoria)[cols].sum().reset_index()
df_pivote = df_colombia_continental.pivot_table(
    index = 'DEPARTAMENTO',
    columns = 'AÑO SERVICIO',
    values = ['ENERGÍA ACTIVA'],
    aggfunc = 'sum'
)
#Este código genera un gráfico estadístico
df_pivote.plot(kind='barh', figsize=(8,5))
plt.title('ENERGIA ACTIVA 2020 a 2025')
plt.xlabel('ENERGIA')
plt.tight_layout()
plt.show()