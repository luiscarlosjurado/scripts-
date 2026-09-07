import pandas as pd
import numpy as np
from pathlib import Path

def detectar_atipicos(archivo: Path) -> dict:
    # 1. Cargar archivo con manejo de codificación y separador
    try:
        # Primero intentamos con punto y coma (muy común en ICFES)
        df = pd.read_csv(archivo, sep=';', encoding='utf-8', low_memory=False)
    except:
        try:
            df = pd.read_csv(archivo, sep=';', encoding='latin-1', low_memory=False)
        except:
            try:
                # Si falla, intentamos con coma
                df = pd.read_csv(archivo, sep=',', encoding='utf-8', low_memory=False)
            except Exception as e:
                return {'archivo': archivo.name, 'error': f'Error al leer archivo: {e}'}

    # 2. Identificar columnas numéricas (especialmente puntajes)
    columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Si los números vinieron como texto, intentamos convertir columnas que digan 'PUNT_' o 'PERCENTIL_'
    for col in df.columns:
        if ('PUNT_' in col.upper() or 'PERCENTIL_' in col.upper()) and col not in columnas_numericas:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if col not in columnas_numericas:
                columnas_numericas.append(col)

    reporte_columnas = {}
    errores_logicos = 0
    total_atipicos_iqr = 0

    for col in columnas_numericas:
        serie = df[col].dropna()
        if len(serie) == 0:
            continue

        # --- A. REGLAS LÓGICAS DEL ICFES ---
        fuera_de_rango = 0
        if 'GLOBAL' in col.upper():
            # El puntaje global del Saber 11 va de 0 a 500
            fuera_de_rango = ((serie < 0) | (serie > 500)).sum()
        elif 'PUNT_' in col.upper():
            # Las áreas individuales van de 0 a 100
            fuera_de_rango = ((serie < 0) | (serie > 100)).sum()
        
        errores_logicos += fuera_de_rango

        # --- B. ATÍPICOS ESTADÍSTICOS (Método IQR) ---
        Q1 = serie.quantile(0.25)
        Q3 = serie.quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        mascara_atipicos = (serie < limite_inferior) | (serie > limite_superior)
        conteo_iqr = mascara_atipicos.sum()
        total_atipicos_iqr += conteo_iqr

        if conteo_iqr > 0 or fuera_de_rango > 0:
            reporte_columnas[col] = {
                'min': serie.min(),
                'max': serie.max(),
                'atipicos_iqr': conteo_iqr,
                'fuera_rango_logico': fuera_de_rango,
                'lim_inf': round(limite_inferior, 2),
                'lim_sup': round(limite_superior, 2)
            }

    return {
        'archivo': archivo.name,
        'total_filas': len(df),
        'columnas_analizadas': len(columnas_numericas),
        'errores_logicos': errores_logicos,
        'total_atipicos_iqr': total_atipicos_iqr,
        'detalle': reporte_columnas
    }

def main():
    # =========================================================================
    # AQUÍ PONES LA RUTA DE TU CARPETA (deja '.' si están donde corre el script)
    # =========================================================================
    directorio = Path('.') 
    
    archivos_csv = sorted(directorio.glob('*.csv'))

    if not archivos_csv:
        print("No se encontraron archivos CSV.")
        return

    print("=" * 100)
    print("ANÁLISIS DE DATOS ATÍPICOS (ICFES)")
    print("=" * 100)

    for archivo in archivos_csv:
        res = detectar_atipicos(archivo)

        if 'error' in res:
            print(f"\n[!] {res['archivo']}: {res['error']}")
            continue

        print(f"\nArchivo: {res['archivo']} (Filas: {res['total_filas']:,})")
        print(f"-> Errores Lógicos (Puntajes fuera de rango 0-100 o 0-500): {res['errores_logicos']}")
        print(f"-> Atípicos Estadísticos (IQR): {res['total_atipicos_iqr']}")

        if res['detalle']:
            print("\n  Detalle por columna:")
            print(f"  {'Columna':<30} {'Mín':>6} {'Máx':>6} {'Fuera Rango':>12} {'Atípicos IQR':>14} {'Rango Esperado IQR':>20}")
            print("  " + "-" * 92)
            for col, datos in res['detalle'].items():
                rango_str = f"[{datos['lim_inf']} a {datos['lim_sup']}]"
                print(f"  {col:<30} {datos['min']:>6.1f} {datos['max']:>6.1f} {datos['fuera_rango_logico']:>12} {datos['atipicos_iqr']:>14} {rango_str:>20}")
        else:
            print("  [OK] No se detectaron valores atípicos.")

        print("-" * 100)

if __name__ == '__main__':
    main()