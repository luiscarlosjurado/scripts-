import numpy as np
import pandas as pd

# 1. Cargar el dataset consolidado
# Nota: Ajusta la ruta a tu archivo local
file_path = "Saber_11_Consolidado_Total.csv"
print("Cargando dataset... (esto puede tardar unos segundos por el tamaño)")

# low_memory=False ayuda a evitar advertencias de tipos mixtos en datasets grandes
df = pd.read_csv(file_path, sep=";", low_memory=False)

# Estandarizar nombres de columnas a mayúsculas para evitar errores tipográficos
df.columns = df.columns.str.upper()

filas_iniciales = len(df)
print(f"Total registros iniciales: {filas_iniciales:,}\n" + "=" * 50)

# -------------------------------------------------------------------------
# PASO 1: Población - Filtrar colegios con código de departamento no nulo
# -------------------------------------------------------------------------
# Delimita a la cohorte regular de educación media (excluye validantes/individuales)
filas_antes = len(df)
df = df[df["COLE_COD_DEPTO_UBICACION"].notna()].copy()
filas_eliminadas_poblacion = filas_antes - len(df)

print(
    f"1. Filtro Población Regular (COLE_COD_DEPTO_UBICACION != NULL):"
    f"\n   - Filas eliminadas: {filas_eliminadas_poblacion:,}"
    f"\n   - Filas restantes: {len(df):,}\n"
)

# -------------------------------------------------------------------------
# PASO 2: Outliers/Error - Filtrar PUNT_GLOBAL > 0
# -------------------------------------------------------------------------
# Asegurar que sea numérico por si venía como texto
df["PUNT_GLOBAL"] = pd.to_numeric(df["PUNT_GLOBAL"], errors="coerce")

filas_antes = len(df)
# Se eliminan puntajes iguales a 0 o que sean nulos
df = df[(df["PUNT_GLOBAL"].notna()) & (df["PUNT_GLOBAL"] > 0)].copy()
filas_eliminadas_ceros = filas_antes - len(df)

print(
    f"2. Filtro Exámenes Anulados / Error (PUNT_GLOBAL > 0):"
    f"\n   - Filas eliminadas: {filas_eliminadas_ceros:,}"
    f"\n   - Filas restantes: {len(df):,}\n"
)

# -------------------------------------------------------------------------
# PASO 3: Integridad - Filtrar PUNT_INGLES no nulo
# -------------------------------------------------------------------------
# Asegurar que sea numérico
df["PUNT_INGLES"] = pd.to_numeric(df["PUNT_INGLES"], errors="coerce")

filas_antes = len(df)
df = df[df["PUNT_INGLES"].notna()].copy()
filas_eliminadas_ingles = filas_antes - len(df)

print(
    f"3. Filtro Integridad de Puntajes (PUNT_INGLES != NULL):"
    f"\n   - Filas eliminadas: {filas_eliminadas_ingles:,}"
    f"\n   - Filas restantes: {len(df):,}\n"
)

# -------------------------------------------------------------------------
# PASO 4: Imputación - COLE_BILINGUE (NULL -> 'N')
# -------------------------------------------------------------------------
# Contamos cuántos nulos hay antes de imputar
nulos_bilingue_antes = (
    df["COLE_BILINGUE"].isna().sum() if "COLE_BILINGUE" in df.columns else 0
)

if "COLE_BILINGUE" in df.columns:
    df["COLE_BILINGUE"] = df["COLE_BILINGUE"].fillna("N")
    # Estandarizar valores por si existen minúsculas o espacios
    df["COLE_BILINGUE"] = df["COLE_BILINGUE"].astype(str).str.strip().str.upper()

print(
    f"4. Imputación de Bilingüismo (COLE_BILINGUE):"
    f"\n   - Valores imputados con 'N': {nulos_bilingue_antes:,}"
    f"\n   - Valores nulos residuales: {df['COLE_BILINGUE'].isna().sum():,}\n"
)

# -------------------------------------------------------------------------
# RESUMEN FINAL
# -------------------------------------------------------------------------
filas_finales = len(df)
total_eliminadas = filas_iniciales - filas_finales
pct_conservado = (filas_finales / filas_iniciales) * 100

print("=" * 50)
print(f"RESUMEN FINAL DEPURACIÓN:")
print(f"- Filas Iniciales:    {filas_iniciales:,}")
print(f"- Total Eliminadas:   {total_eliminadas:,}")
print(
    f"- Filas Finales:      {filas_finales:,} ({pct_conservado:.2f}% de los datos originales)"
)
print("=" * 50)

# -------------------------------------------------------------------------
# PASO 5: Exportar archivo limpio
# -------------------------------------------------------------------------
# Recomendación: Para 3.4M de filas, guardarlo en formato Parquet es 10x más rápido
# y ocupa hasta 80% menos espacio en disco que un CSV.

# Opción A: Guardar en Parquet (Recomendado para analítica)
# df.to_parquet("Saber_11_Limpio_2018_2024.parquet", index=False)

# Opción B: Guardar en CSV
print("Exportando dataset depurado...")
df.to_csv("Saber_11_Limpio_2018_2024.csv", index=False)
print("¡Archivo exportado exitosamente!")