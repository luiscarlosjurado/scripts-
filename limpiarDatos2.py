import pandas as pd
import numpy as np

ARCHIVO_ORIGINAL = "Saber_11_Consolidado_Total.csv"  # <-- Verifica tu nombre exacto
ARCHIVO_LIMPIO = "icfes_limpio_2018_2024.csv"

print("⏳ Cargando dataset del ICFES (4.6M registros, puede tardar unos segundos)...")

# Intentamos primero con ';' (formato típico colombiano), si no con ','
try:
    df = pd.read_csv(ARCHIVO_ORIGINAL, sep=';', encoding='latin-1', low_memory=False)
    if df.shape[1] <= 1:
        df = pd.read_csv(ARCHIVO_ORIGINAL, sep=',', encoding='latin-1', low_memory=False)
except Exception:
    df = pd.read_csv(ARCHIVO_ORIGINAL, sep=',', encoding='latin-1', low_memory=False)

df.columns = df.columns.str.strip().str.lower()
total_inicial = len(df)
print(f"✔️ Dataset cargado con éxito. Registros iniciales: {total_inicial:,} | Columnas: {df.shape[1]}")

# ==========================================
# 1. DIAGNÓSTICO DE PUNTAJES
# ==========================================
print("\n🔍 REVISIÓN DE PUNTAJES:")
if 'punt_global' in df.columns:
    df['punt_global'] = pd.to_numeric(df['punt_global'].astype(str).str.replace(',', '.'), errors='coerce')
    nulos_global = df['punt_global'].isna().sum()
    ceros_global = (df['punt_global'] <= 0).sum()
    print(f"  • punt_global nulo/inválido : {nulos_global:,}")
    print(f"  • punt_global <= 0          : {ceros_global:,}")

# ==========================================
# 2. CONSOLIDACIÓN DEL DEPARTAMENTO (EN CASCADA)
# ==========================================
print("\n🔄 Rescatando y estandarizando la ubicación departamental...")

# Columna base
df['depto_analisis'] = np.nan

# Prioridad 1: Departamento del colegio
if 'cole_depto_ubicacion' in df.columns:
    df['depto_analisis'] = df['depto_analisis'].fillna(df['cole_depto_ubicacion'])

# Prioridad 2: Departamento de residencia del estudiante
if 'estu_depto_reside' in df.columns:
    df['depto_analisis'] = df['depto_analisis'].fillna(df['estu_depto_reside'])

# Prioridad 3: Departamento donde presentó la prueba
if 'estu_depto_presentacion' in df.columns:
    df['depto_analisis'] = df['depto_analisis'].fillna(df['estu_depto_presentacion'])

# Limpieza de texto para facilitar el cruce futuro con el DANE
df['depto_analisis'] = (df['depto_analisis']
                        .astype(str)
                        .str.upper()
                        .str.strip()
                        .str.replace('Á', 'A')
                        .str.replace('É', 'E')
                        .str.replace('Í', 'I')
                        .str.replace('Ó', 'O')
                        .str.replace('Ú', 'U')
                        .str.replace('BOGOTA D.C.', 'BOGOTA')
                        .str.replace('BOGOTÁ', 'BOGOTA')
                        .str.replace('BOGOTA D. C.', 'BOGOTA'))

# ==========================================
# 3. FILTRADO INTELIGENTE
# ==========================================
print("🧹 Aplicando filtros...")

# Filtro 1: Puntaje global válido y estrictamente mayor a 0
filtro_puntaje = (df['punt_global'] > 0) & (df['punt_global'].notna())

# Filtro 2: Que el departamento sea válido
filtro_depto = (~df['depto_analisis'].isin(['NAN', 'NONE', '', 'DESCONOCIDO', 'NULL']))

df_limpio = df[filtro_puntaje & filtro_depto].copy()

total_final = len(df_limpio)
eliminados = total_inicial - total_final
pct_eliminado = (eliminados / total_inicial) * 100

# ==========================================
# 4. REPORTE FINAL
# ==========================================
print("\n" + "="*50)
print("📊 RESUMEN DE LA DEPURACIÓN AJUSTADA")
print("="*50)
print(f"• Registros iniciales   : {total_inicial:,}")
print(f"• Registros conservados : {total_final:,}")
print(f"• Registros eliminados  : {eliminados:,} ({pct_eliminado:.2f}%)")
print("="*50)

# ==========================================
# 5. GUARDAR ARCHIVO LIMPIO
# ==========================================
print(f"\n💾 Guardando archivo limpio en: '{ARCHIVO_LIMPIO}' ...")
df_limpio.to_csv(ARCHIVO_LIMPIO, sep=';', index=False, encoding='utf-8')
print("✅ ¡Archivo limpio guardado con éxito!")