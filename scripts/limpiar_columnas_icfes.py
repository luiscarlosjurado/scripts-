import csv
import sys
import os
import argparse


COLUMNAS_ELIMINAR = [
    # variables que solo existen en algonos archivos:
    "estu_pilopaga",
    "estu_generacione",
    "estu_etnia",
    "estu_tieneetnia",
    "estu_grupoetnia",
    "fami_numhermanos",
    "fami_posicionhermanos",
    "estu_comunidadcampesina",
    "estu_numhijos",
    "estu_horastrabnoremu",
    "estu_tiempocasaacole",
    "estu_desplazacolegio",
    #variables que no se necesitan para el analisis
    "cole_calendario",
    "cole_caracter",
    "cole_cod_dane_establecimiento",
    "cole_cod_dane_sede",
    "cole_codigo_icfes",
    "cole_genero",
    "estu_consecutivo",
    "estu_estudiante",
    "estu_tipodocumento",
    "cole_nombre_establecimiento",
    "cole_nombre_sede",
    "percentil_global",
    "percentil_matematicas",
    "percentil_c_naturales",
    "percentil_ingles",
    "percentil_lectura_critica",
    "percentil_sociales_ciudadanas",
    "desemp_c_naturales",
    "desemp_ingles",
    "desemp_lectura_critica",
    "desemp_matematicas",
    "desemp_sociales_ciudadanas",
    "estu_privado_libertad", 
]


def main():
    parser = argparse.ArgumentParser(
        description="Elimina columnas de un archivo TXT ICFES y guarda como CSV"
    )
    parser.add_argument(
        "entrada", 
        nargs="?",  # <-- Hace que el argumento sea opcional
        default="../datos/datos icfes/Examen_Saber_11_20242.txt",  # <-- Ruta por defecto
        help="Ruta del archivo TXT a procesar"
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        help="Carpeta de salida (default: misma carpeta del archivo origen)",
        default=None,
    )
    args = parser.parse_args()

    ruta_entrada = args.entrada
    if not os.path.isfile(ruta_entrada):
        sys.exit(f"Error: no existe el archivo: {ruta_entrada}")

    carpeta_salida = args.output_dir or os.path.dirname(ruta_entrada) or "."
    base = os.path.splitext(os.path.basename(ruta_entrada))[0]
    ruta_salida = os.path.join(carpeta_salida, f"{base}_limpio.csv")

    print(f"Entrada:  {ruta_entrada}")
    print(f"Salida:   {ruta_salida}")
    print(f"Eliminando {len(COLUMNAS_ELIMINAR)} columnas: {COLUMNAS_ELIMINAR or '(ninguna)'}")

    with open(ruta_entrada, encoding="utf-8-sig", newline="") as fin:
        lector = csv.reader(fin, delimiter=";")
        cabecera = next(lector)

        indices_conservar = []
        indices_eliminar = []
        no_encontradas = []

        for i, col in enumerate(cabecera):
            if col in COLUMNAS_ELIMINAR:
                indices_eliminar.append(i)
            else:
                indices_conservar.append(i)

        for col in COLUMNAS_ELIMINAR:
            if col not in cabecera:
                no_encontradas.append(col)

        if no_encontradas:
            print(f"Advertencia: estas columnas no existen en el archivo y se ignoran: {no_encontradas}")

        cabecera_nueva = [cabecera[i] for i in indices_conservar]

        with open(ruta_salida, "w", encoding="utf-8", newline="") as fout:
            escritor = csv.writer(fout, delimiter=";")
            escritor.writerow(cabecera_nueva)

            filas = 0
            fila_salida = [None] * len(indices_conservar)
            for fila in lector:
                for j, idx in enumerate(indices_conservar):
                    fila_salida[j] = fila[idx] if idx < len(fila) else ""
                escritor.writerow(fila_salida)
                filas += 1

    print(f"Listo. Filas procesadas: {filas:,}")
    print(f"Columnas originales: {len(cabecera)} -> finales: {len(cabecera_nueva)}")


if __name__ == "__main__":
    main()