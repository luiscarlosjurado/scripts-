import pandas as pd

# Reemplaza 'tu_archivo.csv' por el nombre real de tu archivo
# Usamos sep=';' porque es el estándar en los archivos del ICFES
df = pd.read_csv('../icfes_2018_2025.csv', sep=';', nrows=5)

# Esto mostrará las 5 filas en la consola
print(df)