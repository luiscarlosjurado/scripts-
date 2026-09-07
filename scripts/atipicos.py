import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo (ajusta el separador 'sep' según tu archivo: ',', '\t', ' ')
df = pd.read_csv('Saber_11_Consolidado_Total.csv', sep=';', encoding='utf-8', low_memory=False)

# Ver los primeros datos
#print(df.head())

# 1. Convertir a numérico (errors='coerce' convierte lo que no sea número en NaN)
df['PUNT_GLOBAL'] = pd.to_numeric(df['PUNT_GLOBAL'], errors='coerce')

# 2. Eliminar filas que tengan el puntaje vacío (opcional, pero recomendado)
df = df.dropna(subset=['PUNT_GLOBAL'])

# 3. Ahora sí definimos la columna y calculamos los cuartiles
columna = df['PUNT_GLOBAL']

Q1 = columna.quantile(0.25)
Q3 = columna.quantile(0.75)
IQR = Q3 - Q1

print(f"Primer Cuartil (Q1): {Q1}")
print(f"Tercer Cuartil (Q3): {Q3}")

IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Límite Inferior: {limite_inferior}")
print(f"Límite Superior: {limite_superior}")
print("-" * 30)

# 2. Filtrar los datos atípicos
atipicos_bajos = df[df['PUNT_GLOBAL'] < limite_inferior]
atipicos_altos = df[df['PUNT_GLOBAL'] > limite_superior]

# 3. Mostrar resultados
print(f"Cantidad de atípicos BAJOS (debajo de {limite_inferior}): {len(atipicos_bajos)}")
print(f"Cantidad de atípicos ALTOS (encima de {limite_superior}): {len(atipicos_altos)}")

# 4. Ver los ejemplos más extremos (los 10 mejores puntajes atípicos)
print("\nEjemplos de los puntajes más altos detectados como atípicos:")
print(atipicos_altos[['PUNT_GLOBAL']].sort_values(by='PUNT_GLOBAL', ascending=False).head(10))

IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR

# 2. Filtramos solo los que están por debajo de ese límite
atipicos_bajos = df[df['PUNT_GLOBAL'] < limite_inferior]

# 3. Ordenamos de menor a mayor para ver los casos más extremos
atipicos_bajos_ordenados = atipicos_bajos.sort_values(by='PUNT_GLOBAL', ascending=True)

# 4. Mostramos los resultados
print(f"--- Análisis de Atípicos Bajos (Menores a {limite_inferior}) ---")
print(f"Total encontrados: {len(atipicos_bajos_ordenados)}")
print("\nPrimeros 15 casos más bajos:")

# Mostramos solo las columnas que nos interesan (puedes agregar más si quieres)
# Por ejemplo: el puntaje global y el municipio
columnas_interes = ['PUNT_GLOBAL', 'ESTU_MCPIO_RESIDE'] 
print(atipicos_bajos_ordenados[columnas_interes].head(200))