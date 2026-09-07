import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def cargar_y_limpiar_datos(directorio: Path) -> pd.DataFrame:
    archivos = list(directorio.glob('*.csv'))
    if not archivos:
        print("No se encontraron archivos CSV.")
        return pd.DataFrame()

    dfs = []
    print(f"Cargando {len(archivos)} archivo(s)...")

    for archivo in archivos:
        try:
            # Leer detectando codificación y separador común
            try:
                df = pd.read_csv(archivo, sep=';', encoding='utf-8', low_memory=False)
            except:
                df = pd.read_csv(archivo, sep=';', encoding='latin-1', low_memory=False)
        except Exception as e:
            print(f"Error leyendo {archivo.name}: {e}")
            continue

        # Estandarizar nombres de columnas a mayúsculas
        df.columns = df.columns.str.upper().str.strip()

        # 1. Identificar columna de Departamento
        col_depto = None
        for posible in ['COLE_DEPTO_UBICACION', 'ESTU_DEPTO_RESIDE', 'ESTU_DEPTO_PRESENTACION']:
            if posible in df.columns:
                col_depto = posible
                break

        # 2. Identificar columna de Periodo / Año
        col_periodo = 'PERIODO' if 'PERIODO' in df.columns else None

        # 3. Identificar Puntaje Global
        col_puntaje = 'PUNT_GLOBAL' if 'PUNT_GLOBAL' in df.columns else None

        if col_depto and col_puntaje:
            sub_df = pd.DataFrame()
            sub_df['DEPARTAMENTO'] = df[col_depto].astype(str).str.strip().str.upper()
            sub_df['PUNT_GLOBAL'] = pd.to_numeric(df[col_puntaje], errors='coerce')
            
            # Extraer año (los primeros 4 dígitos de PERIODO, ej: '20194' -> 2019)
            if col_periodo:
                sub_df['ANIO'] = df[col_periodo].astype(str).str[:4]
            else:
                # Si no hay columna PERIODO, intenta sacar el año del nombre del archivo
                sub_df['ANIO'] = ''.join(filter(str.isdigit, archivo.name))[:4]

            # Limpiar datos nulos o fuera del rango real del ICFES (0 a 500)
            sub_df = sub_df.dropna()
            sub_df = sub_df[(sub_df['PUNT_GLOBAL'] >= 0) & (sub_df['PUNT_GLOBAL'] <= 500)]
            
            dfs.append(sub_df)
            print(f" -> {archivo.name}: {len(sub_df):,} registros válidos.")

    if not dfs:
        return pd.DataFrame()

    return pd.concat(dfs, ignore_index=True)

def graficar_lineas(df_promedios, departamentos_a_mostrar=None):
    """Gráfico de líneas por año"""
    plt.figure(figsize=(14, 7))
    sns.set_theme(style="whitegrid")

    datos_grafico = df_promedios
    titulo_extra = "(Todos los departamentos)"

    # Si seleccionas algunos departamentos para no saturar la gráfica
    if departamentos_a_mostrar:
        datos_grafico = df_promedios[df_promedios['DEPARTAMENTO'].isin([d.upper() for d in departamentos_a_mostrar])]
        titulo_extra = f"({', '.join(departamentos_a_mostrar)})"

    ax = sns.lineplot(
        data=datos_grafico,
        x='ANIO',
        y='PUNT_GLOBAL',
        hue='DEPARTAMENTO',
        marker='o',
        linewidth=2.5
    )

    plt.title(f'Evolución del Puntaje Global Promedio por Departamento {titulo_extra}', fontsize=14, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Puntaje Global Promedio (0 - 500)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Departamento')
    plt.tight_layout()
    plt.show()

def graficar_mapa_calor(df_promedios):
    """Mapa de calor (Heatmap) ideal para ver TODOS los 33 departamentos sin desorden"""
    plt.figure(figsize=(12, 10))
    
    # Crear matriz pivote: Filas = Departamentos, Columnas = Años
    tabla_pivote = df_promedios.pivot(index='DEPARTAMENTO', columns='ANIO', values='PUNT_GLOBAL')

    sns.heatmap(tabla_pivote, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=.5, cbar_kws={'label': 'Puntaje Promedio'})
    plt.title('Puntaje Global Promedio por Departamento y Año (Mapa de Calor)', fontsize=14, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Departamento', fontsize=12)
    plt.tight_layout()
    plt.show()

def main():
    # =========================================================================
    # 1. RUTA DE TUS ARCHIVOS CSV
    # =========================================================================
    directorio = Path('.')  # Pon la ruta donde están tus archivos

    # Cargar y procesar
    df_total = cargar_y_limpiar_datos(directorio)

    if df_total.empty:
        print("No se pudieron procesar datos.")
        return

    # 2. Calcular promedio agrupado
    print("\nCalculando promedios...")
    promedios = df_total.groupby(['ANIO', 'DEPARTAMENTO'])['PUNT_GLOBAL'].mean().reset_index()
    promedios['PUNT_GLOBAL'] = promedios['PUNT_GLOBAL'].round(2)

    # Mostrar tabla resumen en consola
    print("\nPrimeras filas del resumen:")
    print(promedios.head(10))

    # =========================================================================
    # 3. GENERAR GRÁFICOS
    # =========================================================================
    
    # OPCIÓN A: Gráfico de líneas seleccionando departamentos específicos (ejemplo)
    deptos_filtro = ['BOGOTA', 'ANTIOQUIA', 'VALLE', 'ATLANTICO', 'SANTANDER', 'CHOCO']
    print(f"\nGenerando gráfico de líneas para: {deptos_filtro}...")
    graficar_lineas(promedios, departamentos_a_mostrar=deptos_filtro)

    # OPCIÓN B: Mapa de calor con TODOS los departamentos
    print("Generando mapa de calor general...")
    graficar_mapa_calor(promedios)

if __name__ == '__main__':
    main()