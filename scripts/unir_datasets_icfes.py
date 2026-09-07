import os
import glob
import pandas as pd

def consolidar_archivos_icfes(carpeta_origen='.', extension='csv', separador=';', encoding='utf-8'):
    """
    Une todos los archivos de Saber 11 en un único DataFrame y lo exporta.
    """
    # 1. Buscar todos los archivos que coincidan con el patrón
    patron = os.path.join(carpeta_origen, f"Examen_Saber_11_*.{extension}")
    archivos = sorted(glob.glob(patron))
    
    if not archivos:
        print(f"⚠️ No se encontraron archivos con el patrón '{patron}'.")
        print("Revisa la extensión (.csv o .xlsx) o el nombre de los archivos.")
        return

    print(f"📦 Se encontraron {len(archivos)} archivos para consolidar:")
    for f in archivos:
        print(f"  - {os.path.basename(f)}")

    lista_dfs = []
    
    # 2. Leer cada archivo
    for archivo in archivos:
        nombre_archivo = os.path.basename(archivo)
        print(f"\n⏳ Procesando: {nombre_archivo} ...")
        
        try:
            if extension.lower() == 'csv':
                # low_memory=False evita advertencias de tipos mixtos en columnas grandes
                df = pd.read_csv(archivo, sep=separador, encoding=encoding, low_memory=False)
            else:
                df = pd.read_excel(archivo)
            
            # Estandarizar nombres de columnas (eliminar espacios y pasar a mayúsculas)
            df.columns = df.columns.str.strip().str.upper()
            
            # Opcional: Agregar una columna con el origen si no existe periodo
            # df['FUENTE_ARCHIVO'] = nombre_archivo
            
            print(f"   Filas: {df.shape[0]:,}, Columnas: {df.shape[1]}")
            lista_dfs.append(df)
            
        except Exception as e:
            print(f"❌ Error al leer {nombre_archivo}: {e}")
            print("💡 Sugerencia: Prueba cambiando el encoding='latin1' o el separador=','.")

    # 3. Concatenar todos los DataFrames
    print("\n🔄 Concatenando todos los períodos...")
    df_consolidado = pd.concat(lista_dfs, ignore_index=True, sort=False)
    
    print(f"\n✅ ¡CONSOLIDACIÓN EXITOSA!")
    print(f"📊 Total de registros consolidados: {df_consolidado.shape[0]:,}")
    print(f"📊 Total de columnas: {df_consolidado.shape[1]}")

    # 4. Guardar resultados
    # Guardar en CSV
    salida_csv = "Saber_11_Consolidado_Total.csv"
    print(f"\n💾 Guardando en CSV ({salida_csv})...")
    df_consolidado.to_csv(salida_csv, sep=';', index=False, encoding='utf-8-sig')
    
    # Guardar en Parquet (Recomendado para tu tesis)
    try:
        salida_parquet = "Saber_11_Consolidado_Total.parquet"
        print(f"💾 Guardando en Parquet ({salida_parquet})...")
        df_consolidado.to_parquet(salida_parquet, index=False, engine='pyarrow')
    except Exception as e:
        print(f"ℹ️ No se pudo exportar a Parquet (instala pyarrow con: pip install pyarrow): {e}")

    print("\n🎉 Proceso finalizado con éxito.")

if __name__ == "__main__":
    # AJUSTA ESTOS PARÁMETROS SEGÚN TUS ARCHIVOS:
    consolidar_archivos_icfes(
        carpeta_origen='.',     # '.' significa la carpeta actual donde estás parado en la terminal
        extension='csv',        # 'csv' o 'xlsx'
        separador=';',          # Los datos del ICFES suelen venir separados por ';' o ','
        encoding='utf-8'        # Si te sale error de decodificación, cambia a 'latin1' o 'utf-8-sig'
    )