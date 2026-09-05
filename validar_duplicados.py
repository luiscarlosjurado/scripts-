import pandas as pd
from pathlib import Path
import sys

def verificar_duplicados(archivo: Path) -> dict:
    try:
        df = pd.read_csv(archivo, sep=';', dtype=str, low_memory=False, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(archivo, sep=';', dtype=str, low_memory=False, encoding='latin-1')
        except Exception as e:
            return {'archivo': archivo.name, 'error': f'Error de encoding: {e}'}
    except Exception as e:
        return {'archivo': archivo.name, 'error': f'Error al leer: {e}'}

    total = len(df)
    duplicados_mask = df.duplicated(keep=False)
    num_duplicadas = duplicados_mask.sum()
    num_unicas = total - num_duplicadas
    grupos_duplicados = df[duplicados_mask].drop_duplicates().shape[0] if num_duplicadas > 0 else 0

    resultado = {
        'archivo': archivo.name,
        'total': total,
        'unicas': num_unicas,
        'duplicadas': int(num_duplicadas),
        'grupos_duplicados': int(grupos_duplicados),
        'ejemplos': None
    }

    if num_duplicadas > 0:
        ejemplos = df[duplicados_mask].head(5)
        resultado['ejemplos'] = ejemplos.to_dict('records')

    return resultado

def main():
    directorio = Path('.')
    archivos_csv = sorted(directorio.glob('*.csv'))

    if not archivos_csv:
        print("No se encontraron archivos CSV en el directorio actual.")
        return

    print(f"{'Archivo':<45} {'Total':>8} {'Únicas':>8} {'Duplicadas':>12} {'Grupos dup':>12}")
    print("-" * 95)

    resumen_total = {'archivos': 0, 'total_filas': 0, 'total_duplicadas': 0, 'archivos_con_dup': 0}

    for archivo in archivos_csv:
        res = verificar_duplicados(archivo)

        if 'error' in res:
            print(f"{res['archivo']:<45} ERROR: {res['error']}")
            continue

        print(f"{res['archivo']:<45} {res['total']:>8} {res['unicas']:>8} {res['duplicadas']:>12} {res['grupos_duplicados']:>12}")

        if res['ejemplos']:
            print(f"  >>> Ejemplos de filas duplicadas (primeras 5):")
            for i, fila in enumerate(res['ejemplos'], 1):
                print(f"     {i}. {fila}")
            print()

        resumen_total['archivos'] += 1
        resumen_total['total_filas'] += res['total']
        resumen_total['total_duplicadas'] += res['duplicadas']
        if res['duplicadas'] > 0:
            resumen_total['archivos_con_dup'] += 1

    print("-" * 95)
    print(f"\nRESUMEN GENERAL:")
    print(f"  Archivos procesados: {resumen_total['archivos']}")
    print(f"  Total filas: {resumen_total['total_filas']:,}")
    print(f"  Total filas duplicadas: {resumen_total['total_duplicadas']:,}")
    print(f"  Archivos con duplicados: {resumen_total['archivos_con_dup']}")

if __name__ == '__main__':
    main()