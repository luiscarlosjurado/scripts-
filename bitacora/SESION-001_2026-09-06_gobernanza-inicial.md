# SESION-001 — 2026-09-06

## Objetivo
Gobernanza inicial del repositorio: inspección real del repo (árbol, tamaños, datos/raw/,
scripts/), creación de AGENTS.md, estructura de carpetas (datos/processed/,
datos/output/reports/, informes/), requirements.txt mínimo, ajuste de .gitignore y apertura
de la bitácora (INDEX.md + esta entrada). Regla de sesión: NO ejecutar los scripts existentes
ni cargar los CSV completos al contexto; nada de datos/raw/ se modifica.

## Contexto leído (AGENTS.md, INDEX, entrada anterior)
- AGENTS.md existía pero estaba VACÍO (0 bytes) al inicio de la sesión (fuente: `ls -la`).
- bitacora/INDEX.md existía pero estaba VACÍO (0 bytes). No hay entradas anteriores: esta es
  la SESION-001.
- Leídos: README.md (1 línea: repo de scripts de limpieza), resumen_investigacion.md (raíz),
  datos/variables_icfes.md, y los 10 scripts de scripts/ (lectura rápida, sin ejecutarlos).

## Acciones y comandos ejecutados
```
ls -la; git status --short; git log --oneline -5
find . -not -path './.git*' -not -path './venv*' -not -path './env*' | sort
ls -lh datos/raw/ datos/ scripts/ bitacora/
wc -l datos/raw/*.csv
head -n 2 datos/raw/Examen_Saber_11_20182_limpio.csv | cut -c1-600   (idem 20242)
file datos/raw/*.csv datos/anex-PMultidimensional-Departamental-2024.xlsx
head -n 1 <cada CSV> | tr ';' '\n' | wc -l   (conteo de columnas por archivo)
diff de cabecera de cada CSV vs 20182
unzip -l / unzip -p .../xl/workbook.xml   (hojas del xlsx, sin abrirlo con pandas)
python3 csv.reader sobre 20211 (verificación líneas vs registros)
head -n 30 / tail -n +30 scripts/*.py   (lectura rápida de propósito)
verificación de paquetes en venv/, env/ y python3 del sistema (importlib.util.find_spec)
mkdir -p datos/processed datos/output/reports informes + touch .gitkeep
escritura de: AGENTS.md, requirements.txt, .gitignore (edición), bitacora/INDEX.md, esta entrada
```

## Resultados reales (salidas pegadas y/o rutas de artefactos)

### Árbol del repo (excluidos .git/, venv/, env/)
```
.
./AGENTS.md
./bitacora
./bitacora/INDEX.md
./datos
./datos/anex-PMultidimensional-Departamental-2024.xlsx
./datos/raw
./datos/raw/Examen_Saber_11_20182_limpio.csv
./datos/raw/Examen_Saber_11_20191_limpio.csv
./datos/raw/Examen_Saber_11_20192_limpio.csv
./datos/raw/Examen_Saber_11_20211_limpio.csv
./datos/raw/Examen_Saber_11_20212_limpio.csv
./datos/raw/Examen_Saber_11_20221_limpio.csv
./datos/raw/Examen_Saber_11_20222_limpio.csv
./datos/raw/Examen_Saber_11_20231_limpio.csv
./datos/raw/Examen_Saber_11_20232_limpio.csv
./datos/raw/Examen_Saber_11_20241_limpio.csv
./datos/raw/Examen_Saber_11_20242_limpio.csv
./datos/raw/.gitkeep
./datos/variables_icfes.md
./README.md
./resumen_investigacion.md
./scripts
./scripts/atipicos2.py
./scripts/atipicos.py
./scripts/limpiar_columnas_icfes.py
./scripts/limpiarDatos2.py
./scripts/limpiarDatos.py
./scripts/limpiraDatos.py
./scripts/pronedios_anio_dp.py
./scripts/unir_datasets_icfes.py
./scripts/validar_duplicados.py
./scripts/verdatas.py
```

### Tamaños en datos/raw/ (fuente: `ls -lh datos/raw/`, total 1.8G)
```
291M Examen_Saber_11_20182_limpio.csv
 18M Examen_Saber_11_20191_limpio.csv
292M Examen_Saber_11_20192_limpio.csv
 15M Examen_Saber_11_20211_limpio.csv
288M Examen_Saber_11_20212_limpio.csv
 19M Examen_Saber_11_20221_limpio.csv
284M Examen_Saber_11_20222_limpio.csv
 20M Examen_Saber_11_20231_limpio.csv
289M Examen_Saber_11_20232_limpio.csv
 21M Examen_Saber_11_20241_limpio.csv
282M Examen_Saber_11_20242_limpio.csv
```

### Líneas por CSV (fuente: `wc -l datos/raw/*.csv`; INCLUYE 1 línea de cabecera por archivo)
```
 609137 Examen_Saber_11_20182_limpio.csv
  66105 Examen_Saber_11_20191_limpio.csv
 614790 Examen_Saber_11_20192_limpio.csv
  58709 Examen_Saber_11_20211_limpio.csv
 606031 Examen_Saber_11_20212_limpio.csv
  73796 Examen_Saber_11_20221_limpio.csv
 589184 Examen_Saber_11_20222_limpio.csv
  77556 Examen_Saber_11_20231_limpio.csv
 602094 Examen_Saber_11_20232_limpio.csv
  84073 Examen_Saber_11_20241_limpio.csv
 592437 Examen_Saber_11_20242_limpio.csv
3973912 total
```
Verificación líneas vs registros CSV reales (fuente: `python3` con `csv.reader`, stdlib):
```
datos/raw/Examen_Saber_11_20211_limpio.csv: registros csv (incl. cabecera) = 58709
```
=> en el archivo más pequeño, registros == líneas (sin saltos de línea embebidos). Para los
otros 10 archivos queda PENDIENTE verificarlo en el inventario formal (01_inventario.py).

### Formato detectado (fuente: `file datos/raw/*.csv`, `head -n 1 | tr ';' '\n' | wc -l`)
- Los 11 CSV: `Unicode text, UTF-8 text, with very long lines (1198), with CRLF line terminators`.
- Separador observado en cabecera y primera fila: `;` (punto y coma).
- Los 11 archivos tienen 59 columnas en la cabecera y la cabecera es IDÉNTICA entre sí
  (comparación literal vs 20182, salida: 11× "IDENTICA").
- Primeras columnas observadas: `periodo;cole_area_ubicacion;cole_bilingue;cole_cod_depto_ubicacion;...`
  Últimas: `...;punt_c_naturales;punt_global;punt_ingles;punt_lectura_critica;punt_matematicas;punt_sociales_ciudadanas`.
- Periodos presentes (nombres de archivo): 20182, 20191, 20192, 20211, 20212, 20221, 20222,
  20231, 20232, 20241, 20242. NO existe ningún archivo 2020* (coherente con la exclusión por
  diseño, regla 15). Tampoco existe 20181.

### Anexo IPM (fuente: `unzip -l` y `xl/workbook.xml`; NO se abrió con pandas: openpyxl no instalado)
- `datos/anex-PMultidimensional-Departamental-2024.xlsx`: `Microsoft Excel 2007+`, 387K.
- 13 hojas: "Índice", "IPM_Regiones", "IPM_Departamentos", "IPM_Variables_Región",
  "IPM_Variables_Departamento ", "IC_IPM", "Intensidad_IPM", "Incidencia_Ajustada_IPM",
  "Contribuciones IA_IPM", "IPM_Sexo", "IC_IPM_Sexo", "IPM_Sexo Jefe", "IC_IPM_Sexo Jefe ".
- Contenido de las hojas: SIN VERIFICAR (motivo: requiere openpyxl/pandas, aún no instalados).

### scripts/ — 10 archivos, propósito inferido de lectura rápida (NO ejecutados, por regla de sesión)
| Script | Propósito inferido (lectura del código) |
|---|---|
| atipicos.py | Detección de atípicos por IQR sobre `PUNT_GLOBAL` de `Saber_11_Consolidado_Total.csv` (archivo NO presente en el repo); grafica con matplotlib/seaborn. |
| atipicos2.py | Función `detectar_atipicos(archivo)`: recorre los `*.csv` del directorio actual; reglas de rango ICFES (global 0-500, áreas 0-100) + IQR por columna numérica; imprime reporte. |
| limpiar_columnas_icfes.py | Elimina una lista fija de ~33 columnas (identificación de estudiante/colegio, percentiles, desemp_*, variables solo de algunos periodos) de un TXT ICFES y guarda `<nombre>_limpio.csv`; usa csv/argparse; ruta por defecto `../datos/datos icfes/Examen_Saber_11_20242.txt` (no existe en el repo). Probable origen de los CSV `*_limpio.csv` de datos/raw/. |
| limpiarDatos.py | Variante de limpieza del consolidado: columnas a mayúsculas, filtro `COLE_COD_DEPTO_UBICACION` no nulo; salida `Saber_11_Limpio_2018_2024.csv`. |
| limpiarDatos2.py | Variante 2: diagnóstico de puntajes (nulos/<=0), filtros, normaliza nombres a minúsculas; salida `icfes_limpio_2018_2024.csv` (sep=';', utf-8). |
| limpiraDatos.py | Variante 3: prueba múltiples combinaciones separador/encoding, filtro maestro (punt_global>0, áreas, depto); salida `icfes_limpio_2018_2024.csv` (sep=','). |
| pronedios_anio_dp.py | Promedios de `PUNT_GLOBAL` por año y departamento a partir de los `*.csv` de un directorio; gráficos de líneas con seaborn. |
| unir_datasets_icfes.py | Une `Examen_Saber_11_*.csv` en un solo DataFrame; exporta `Saber_11_Consolidado_Total.csv` (utf-8-sig) e intenta `.parquet` con pyarrow. |
| validar_duplicados.py | Verifica filas duplicadas exactas (y grupos/ejemplos) en los `*.csv` del directorio actual; imprime resumen. |
| verdatas.py | Vistazo rápido: lee `nrows=5` de `../icfes_2018_2025.csv` (archivo NO presente en el repo) y lo imprime. |

### Entorno Python (fuente: `importlib.util.find_spec` en cada intérprete)
```
== venv ==  {'pandas': False, 'numpy': False, 'matplotlib': False, 'seaborn': False, 'openpyxl': False, 'pyarrow': False}
== env ==   {'pandas': False, 'numpy': False, 'matplotlib': False, 'seaborn': False, 'openpyxl': False, 'pyarrow': False}
== sistema == {'pandas': False, 'numpy': False, 'matplotlib': False, 'seaborn': False, 'openpyxl': False, 'pyarrow': False}
python3 del sistema: 3.13.9 (main, Oct 14 2025, 00:00:00) [GCC 14.3.1 20250808 (Red Hat 14.3.1-3)]
```
Adicional: `env/.gitignore` contiene `*` (se autoignora); `git status` confirma que ni venv/
ni env/ ensucian el working tree.

## Hallazgos
1. datos/raw/ contiene 11 CSV `Examen_Saber_11_YYYYP_limpio.csv` (periodos 20182→20242, sin
   2020*, sin 20181), ~1.8 GB en total, UTF-8/CRLF, separador `;`, 59 columnas y cabeceras
   idénticas entre los 11 (fuente: salidas pegadas arriba).
2. El anexo IPM y variables_icfes.md NO están en datos/raw/ sino en datos/;
   resumen_investigacion.md está en la raíz (fuente: árbol del repo).
3. El xlsx del IPM tiene una hoja "IPM_Departamentos" (la relevante para la regla 18) y hojas
   de regiones/sexo/intensidad; su contenido sigue SIN VERIFICAR hasta instalar openpyxl.
4. datos/variables_icfes.md describe un consolidado de 16 archivos 2018-2025 con 94 columnas y
   5,304,758 registros: NO corresponde a lo que hay hoy en datos/raw/ (11 archivos, 59 columnas,
   3,973,912 líneas). Es documentación de referencia de un artefacto anterior/externo; por
   regla 4 y 26 de AGENTS.md no se usa como fuente de verdad.
5. Los scripts existentes son iteraciones exploratorias previas: varios apuntan a archivos que
   no están en el repo (`Saber_11_Consolidado_Total.csv`, `icfes_2018_2025.csv`,
   `../datos/datos icfes/*.txt`), trabajan sobre el directorio actual ('.'), usan
   `try/except` amplios (contra regla 9) y no siguen la convención main()/docstring (regla 21).
6. Ningún entorno (venv/, env/, sistema) tiene pandas instalado: no se puede perfilar ni el
   xlsx ni los CSV con pandas hasta instalar requirements.txt.
7. Lista EXACTA de las 59 columnas (fuente: `head -n 1 Examen_Saber_11_20182_limpio.csv | tr ';' '\n' | nl`,
   idéntica en los 11 archivos): periodo; cole_area_ubicacion, cole_bilingue,
   cole_cod_depto_ubicacion, cole_cod_mcpio_ubicacion, cole_depto_ubicacion, cole_jornada,
   cole_mcpio_ubicacion, cole_naturaleza, cole_sede_principal; estu_agregado,
   estu_cod_depto_presentacion, estu_cod_mcpio_presentacion, estu_cod_reside_depto,
   estu_cod_reside_mcpio, estu_dedicacioninternet, estu_dedicacionlecturadiaria,
   estu_depto_presentacion, estu_depto_reside, estu_discapacidad, estu_fechanacimiento,
   estu_genero, estu_grado, estu_horassemanatrabaja, estu_inse_individual,
   estu_mcpio_presentacion, estu_mcpio_reside, estu_nacionalidad, estu_nse_establecimiento,
   estu_nse_individual, estu_pais_reside, estu_repite, estu_tiporemuneracion;
   fami_comecarnepescadohuevo, fami_comecerealfrutoslegumbre, fami_comelechederivados,
   fami_cuartoshogar, fami_educacionmadre, fami_educacionpadre, fami_estratovivienda,
   fami_numlibros, fami_personashogar, fami_situacioneconomica, fami_tieneautomovil,
   fami_tienecomputador, fami_tieneconsolavideojuegos, fami_tienehornomicroogas,
   fami_tieneinternet, fami_tienelavadora, fami_tienemotocicleta, fami_tieneserviciotv,
   fami_trabajolabormadre, fami_trabajolaborpadre; punt_c_naturales, punt_global, punt_ingles,
   punt_lectura_critica, punt_matematicas, punt_sociales_ciudadanas.
   => NO existen columnas `desemp_*`, `percentil_*` ni de identificación personal
   (estu_consecutivo, nombres, códigos DANE), consistente con COLUMNAS_ELIMINAR de
   limpiar_columnas_icfes.py: los raw/ ya son el producto de esa limpieza.
8. git: HEAD en rama con 3 commits (3eea7c9 "Ignore venv folder", 3c949e3 "Add basic skeleton",
   2ab1a47 "subiendo escripts de python"); ya estaban trackeados AGENTS.md y bitacora/INDEX.md
   (vacíos), el xlsx y variables_icfes.md.

## Decisiones (con justificación)
1. **Ajuste de rutas en AGENTS.md (única desviación del texto entregado, autorizada por la
   consigna)**: el bloque original decía "Fuentes en datos/raw/: CSV..., anexos departamentales
   IPM (xlsx), variables_icfes.md y resumen_investigacion.md". La inspección demostró que el
   xlsx y variables_icfes.md están en datos/ y resumen_investigacion.md en la raíz. Se ajustó
   solo ese párrafo del Contexto; el resto del archivo es literal.
2. **requirements.txt con 6 paquetes y sin versiones fijadas** (pandas, numpy, matplotlib,
   seaborn, openpyxl, pyarrow): son los pedidos por la consigna y cada uno tiene justificación
   concreta (comentarios en el archivo). No se agregó nada "por si acaso" (p. ej. scikit-learn
   o statsmodels entrarán en una sesión futura cuando el plan de modelado lo exija y se
   documente). Las versiones se congelarán cuando el entorno quede validado.
3. **.gitignore**: se conservó lo existente (`datos/raw/*`, `!datos/raw/.gitkeep`, `venv/`) y se
   agregaron exactamente `datos/processed/*.csv`, `datos/processed/*.parquet` y
   `datos/output/*.csv`. NO se ignora datos/output/reports/ ni *.png (son la evidencia del
   proyecto, reglas 2 y 8). No se agregó regla para env/ porque env/.gitignore ya se
   autoignora (verificado con `git status`).
4. **.gitkeep**: se puso en datos/processed/, datos/output/reports/ e informes/ (quedan vacías
   tras la sesión). bitacora/ no lo necesita (ya tiene INDEX.md y esta entrada); datos/output/
   tampoco (contiene reports/).
5. **Cifras de tamaño**: se reporta "líneas (wc -l)" y no "registros", porque solo se verificó
   la equivalencia líneas==registros en 20211 (csv.reader). El conteo formal de registros por
   periodo es tarea de 01_inventario.py. Evita afirmar filas reales sin evidencia completa.
6. **No se ejecutó ningún script de scripts/ ni se modificó datos/raw/** (reglas de sesión y
   regla 6 de AGENTS.md). Los scripts se conservan como referencia histórica; el pipeline nuevo
   será numerado (01_inventario.py, ...) según reglas 21-23.

## Pendientes / riesgos
- Instalar requirements.txt en un entorno (venv/ o env/) y dejar constancia en bitácora.
- 01_inventario.py: conteo de registros por CSV (no solo líneas), verificación de encoding por
  archivo, lista exacta de las 59 columnas por periodo, rangos de `periodo`, perfil de
  faltantes/duplicados (sin tratamiento, regla 20), y lectura del xlsx IPM (hoja
  IPM_Departamentos: años disponibles, unidades territoriales, nota 2021 - regla 18).
- Reconstruir el umbral Matemáticas >= 51 (regla 19) SOLO desde `punt_matematicas`: verificado
  que en raw/ NO existen columnas `desemp_*` ni `percentil_*` (ver hallazgo 7), así que no hay
  niveles reportados que contrastar. Pendiente: obtener/documentar los umbrales oficiales ICFES
  por periodo (pueden cambiar entre años) antes de fijar el evento objetivo. Riesgo adicional:
  datos/variables_icfes.md documenta 94 columnas (incluidas desemp_/percentil_) de un
  consolidado que no corresponde a los raw/ actuales (59 columnas): no usarlo como fuente de
  verdad (reglas 4 y 26).
- Decidir tratamiento de DIVIPOLA como texto (regla 16): en la fila de muestra de 20182,
  `cole_cod_depto_ubicacion=11` y `cole_cod_mcpio_ubicacion=11001` (sin ceros a la izquierda a
  la vista); verificar si algún departamento usa códigos con cero inicial (p. ej. '05').
- Riesgo de rendimiento: CSV P2 de ~290 MB cada uno; el pipeline debe leer por columnas/
  agregaciones en una pasada, no cargar todo en memoria (variables_icfes.md menciona ~10 GB
  RAM para el consolidado antiguo).
- Los scripts viejos escriben salidas en el directorio actual y usan except amplios: no
  reutilizarlos sin adaptarlos a las reglas 7-9 y 21-23.

## Próxima sesión sugerida
SESION-002: instalar dependencias (`pip install -r requirements.txt` en el entorno elegido) y
crear/ejecutar `scripts/01_inventario.py` (compatible con jupytext: celdas markdown + código,
docstring con propósito/entradas/salidas/sesión, main(), rutas pathlib relativas) que genere
`datos/output/reports/01_inventario.md` (+ JSON/CSV de conteos) con: registros y columnas por
periodo, encoding/separador verificados, lista de columnas por archivo, valores únicos de
`periodo`, y perfil del xlsx IPM (hojas, años, unidades territoriales, detección de filas de
total nacional/cabeceras/rural/regiones).

## Artefactos generados (rutas)
- AGENTS.md (completado; antes vacío)
- requirements.txt (nuevo)
- .gitignore (editado: +3 patrones de artefactos pesados)
- datos/processed/.gitkeep, datos/output/reports/.gitkeep, informes/.gitkeep (nuevos)
- bitacora/INDEX.md (completado; antes vacío)
- bitacora/SESION-001_2026-09-06_gobernanza-inicial.md (este archivo)
