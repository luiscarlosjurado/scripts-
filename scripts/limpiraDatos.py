import pandas as pd
import numpy as np

# ==========================================
# 1. CONFIGURACIÓN DE ARCHIVOS
# ==========================================
# Si el archivo está en la misma carpeta, solo pon el nombre. 
# Si no, pon la ruta completa (ej: "D:/Especializacion/.../archivo.csv")
ARCHIVO_ORIGINAL = "Saber_11_Consolidado_Total.csv"  # <-- Asegúrate de que el nombre coincida exactamente
ARCHIVO_LIMPIO = "icfes_limpio_2018_2024.csv"

print("⏳ Intentando cargar el dataset del ICFES...")

# Intentamos leer con diferentes separadores y codificaciones típicas de Colombia
df = None
configuraciones = [
    {'sep': ';', 'encoding': 'utf-8'},
    {'sep': ';', 'encoding': 'latin-1'},
    {'sep': ',', 'encoding': 'utf-8'},
    {'sep': ',', 'encoding': 'latin-1'},
    {'sep': '\t', 'encoding': 'latin-1'}
]

for conf in configuraciones:
    try:
        print(f"Probando lectura con separador: '{conf['sep']}' y codificación: '{conf['encoding']}'...")
        df = pd.read_csv(
            ARCHIVO_ORIGINAL, 
            sep=conf['sep'], 
            encoding=conf['encoding'], 
            low_memory=False,
            on_bad_lines='skip'  # Si hay una fila corrupta aislada, la salta en vez de tumbar el script
        )
        # Verificamos si detectó más de 5 columnas
        if df.shape[1] > 5:
            print(f"✔️ ¡Éxito! Dataset cargado correctamente.")
            break
    except Exception as e:
        continue

if df is None or df.shape[1] <= 1:
    raise ValueError("❌ No se pudo determinar el formato correcto del archivo. Revisa que el nombre y ruta sean correctos.")

total_registros_iniciales = len(df)
print(f"📊 Registros iniciales: {total_registros_iniciales:,} | Columnas detectadas: {df.shape[1]}")

# ==========================================
# 2. ESTANDARIZAR NOMBRES DE COLUMNAS
# ==========================================
# Quita espacios extra y pasa a minúsculas
df.columns = df.columns.str.strip().str.lower()

# ==========================================
# 3. VERIFICACIÓN Y CONVERSIÓN DE TIPOS
# ==========================================
cols_puntajes = [
    'punt_global', 
    'punt_c_naturales', 
    'punt_ingles', 
    'punt_lectura_critica', 
    'punt_matematicas', 
    'punt_sociales_ciudadanas'
]

for col in cols_puntajes:
    if col in df.columns:
        # Reemplazar comas por puntos por si vienen en formato decimal '245,5'
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace(',', '.')
        df[col] = pd.to_numeric(df[col], errors='coerce')
    else:
        print(f"⚠️ Aviso: La columna '{col}' no fue encontrada.")

# ==========================================
# 4. CRITERIOS DE EXCLUSIÓN (LIMPIEZA)
# ==========================================
print("\n🧹 Aplicando criterios de exclusión...")

# Condición 1: punt_global > 0 y no nulo
filtro_global = (df['punt_global'] > 0) & (df['punt_global'].notna())

# Condición 2: Ningún sub-puntaje puede ser 0 o nulo
filtro_areas = True
for col in cols_puntajes:
    if col in df.columns:
        filtro_areas = filtro_areas & (df[col] > 0) & (df[col].notna())

# Condición 3: Debe tener código de departamento
filtro_depto = df['cole_cod_depto_ubicacion'].notna() if 'cole_cod_depto_ubicacion' in df.columns else True

# Aplicar todos los filtros
filtro_maestro = filtro_global & filtro_areas & filtro_depto
df_limpio = df[filtro_maestro].copy()

total_registros_finales = len(df_limpio)
registros_eliminados = total_registros_iniciales - total_registros_finales
porcentaje_eliminado = (registros_eliminados / total_registros_iniciales) * 100

# ==========================================
# 5. REPORTE DE CALIDAD DE DATOS
# ==========================================
print("\n" + "="*50)
print("RESUMEN DE LA DEPURACIÓN DE DATOS")
print("="*50)
print(f"• Registros iniciales   : {total_registros_iniciales:,}")
print(f"• Registros conservados : {total_registros_finales:,}")
print(f"• Registros eliminados  : {registros_eliminados:,} ({porcentaje_eliminado:.2f}%)")
print("="*50)

# ==========================================
# 6. GUARDAR EL NUEVO ARCHIVO LIMPIO
# ==========================================
print(f"\n💾 Guardando archivo limpio en: '{ARCHIVO_LIMPIO}' ...")
# Lo guardamos con separador coma estándar y utf-8
df_limpio.to_csv(ARCHIVO_LIMPIO, sep=',', index=False, encoding='utf-8')
print("¡Proceso completado con éxito!")