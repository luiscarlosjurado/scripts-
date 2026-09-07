# SESION-002 — 2026-09-07

## Objetivo
Entorno (instalar `requirements.txt` en `venv/`, fijar versiones con `==`) e inventario
formal de las dos fuentes: 11 CSV del ICFES en `datos/raw/` (perfilado por chunks de
250_000, un archivo a la vez) y anexo IPM
`datos/anex-PMultidimensional-Departamental-2024.xlsx` (solo perfilado, sin transformar).
Solo medir y describir: sin filtros, imputaciones ni tratamientos.

## Contexto leído (AGENTS.md, INDEX, entrada anterior)
- AGENTS.md vigente (reglas 1-28, incluida la nota jupytext de la regla 23).
- bitacora/INDEX.md: una fila (SESION-001 COMPLETADA).
- bitacora/SESION-001_2026-09-06_gobernanza-inicial.md completa: de ella salen la lista
  literal de 59 columnas (comparación literal B1), los tamaños/`wc -l`, las 13 hojas del
  xlsx y los pendientes que esta sesión resuelve (entorno, registros reales por periodo,
  formato DIVIPOLA, contenido del xlsx).
- resumen_investigacion.md y datos/variables_icfes.md re-leídos: NO contienen las cifras
  4.039.755 / 606.214 / 22 / 28.394 (`grep` en el repo: 0 coincidencias). Esas cifras son
  EXPECTATIVAS del documento vía consigna (regla 4), no resultados.

## Acciones y comandos ejecutados
```
venv/bin/pip install -r requirements.txt
venv/bin/pip freeze | grep -Ei '^(pandas|numpy|matplotlib|seaborn|openpyxl|pyarrow)=='
reescritura de requirements.txt con == (mismos 6 paquetes y comentarios)
venv/bin/pip install -r requirements.txt (verificacion: Requirement already satisfied x6)
venv/bin/python -c "import pandas,numpy,..." (verificacion de versiones)
escritura de scripts/01_inventario.py (nuevo; formato jupytext py:percent)
venv/bin/python -m py_compile scripts/01_inventario.py
venv/bin/python scripts/01_inventario.py   (3 ejecuciones: v1 deteccion IPM ingenua,
  v2 correccion 2020**/2021***, v3 final tras corregir fila-titulo y desfase anioxdominio;
  artefactos finales 100% de la v3; corridas idempotentes, mismo total ICFES en las 3)
sondas de solo lectura del xlsx para depurar deteccion (import del modulo, sin main)
extracciones compactas desde datos/output/reports/01_inventario_icfes.csv (evidencia citada)
git check-ignore datos/output/reports/01_inventario_icfes.csv
ls -l datos/raw/ (verificar intacto) ; rm -rf scripts/__pycache__
```

## Resultados reales (salidas pegadas y/o rutas de artefactos)

### TAREA A — freeze real (fuente: `venv/bin/pip freeze`)
```
matplotlib==3.11.1
numpy==2.5.3
openpyxl==3.1.5
pandas==3.0.5
pyarrow==25.0.1
seaborn==0.13.2
```
Verificación de import: `3.0.5 2.5.3 3.11.1 0.13.2 3.1.5 25.0.1`. `requirements.txt`
reescrito con esas versiones exactas (`==`); reinstalación confirma "Requirement already
satisfied" en los 6. Dependencias transitivas instaladas (no fijadas, fuera del alcance
de la decisión 2 de SESION-001): contourpy==1.3.3, cycler==0.12.1, et-xmlfile==2.0.0,
fonttools==4.64.0, kiwisolver==1.5.1, packaging==26.3, pillow==12.3.0, pyparsing==3.3.2,
python-dateutil==2.9.0.post0, six==1.17.0. pip del venv sigue en 24.2 (no se actualizó;
aviso de 26.2.1 ignorado a propósito).

### TAREA B1/C — tabla por archivo (fuente: `scripts/01_inventario.py` sobre
`datos/output/reports/01_inventario_icfes.csv`)
```
 periodo  visto  registros  cab59  depto_n  formato                  mcpio_n  dup  depto_nulo  gbl_cero  gbl_nulo  area_nula  bilingue_nulos
 20182  20182     609136  True       33  digitos_sin_ceros_izquierda     1113    0       53817         5         0       1446          138036
 20191  20191      66104  True       29  digitos_sin_ceros_izquierda      147    0       44762         0         0        116           48946
 20192  20192     614789  True       33  digitos_sin_ceros_izquierda     1113    0       60020         5         0       2894          149158
 20211  20211      58708  True       28  digitos_sin_ceros_izquierda      102    0       43126         0         0         97           45686
 20212  20212     606030  True       33  digitos_sin_ceros_izquierda     1114    0       64548         6         0       6220          157500
 20221  20221      73795  True       29  digitos_sin_ceros_izquierda      165    0       53746         0         0        184           58649
 20222  20222     589183  True       33  digitos_sin_ceros_izquierda     1114    0       45477         4         0       4697          143449
 20231  20231      77555  True       29  digitos_sin_ceros_izquierda      151    0       56903         2         0        177           62337
 20232  20232     602093  True       33  digitos_sin_ceros_izquierda     1116    0       39179         7         0       5890          143781
 20241  20241      84072  True       29  digitos_sin_ceros_izquierda      161    0       63442         2         0        150           84072
 20242  20242     592436  True       33  digitos_sin_ceros_izquierda     1118    0       35138         3         0       7158          143852
TOTAL_REGISTROS = 3973901
SUM_DIAG = depto_nulo=560158, global_cero=34, global_nulo=0, alguna_area_nula=29029
```
- Cabecera: `columnas_identicas_59=True` en los 11 (comparación literal contra la lista de
  SESION-001, mismo orden). `periodo`: 1 único por archivo, coincidente con el nombre.
- Duplicados exactos (md5, 8 bytes, set por archivo): **0 en los 11** (sin segunda pasada).
- Puntajes: 0 nulos y 0 no-numéricos en global/matemáticas/lectura/naturales/sociales en
  los 11; `punt_ingles` concentra TODOS los nulos de área (1446|116|2894|97|6220|184|
  4697|177|5890|150|7158 = 29.029 = `diag_alguna_area_nula`, verificado aritméticamente).
  Fuera de escala oficial: **0 en las 6 columnas × 11 archivos**.
  `punt_global` min|max por periodo: 20182 0|478; 20191 9|470; 20192 0|477; 20211 14|495;
  20212 0|500; 20221 **82**|500; 20222 0|500; 20231 0|478; 20232 0|500;
  20241 0|496; 20242 0|495. Áreas y global con max<=límite siempre. (Medias completas en
  `01_inventario_icfes.csv`.)
- `cole_cod_depto_ubicacion`: formato `digitos_sin_ceros_izquierda` en los 11 (p. ej.
  `11|13|...|5|...|8|...`: sin ceros a la izquierda; resuelve el pendiente de SESION-001).
  Códigos 20182 (33, referencia P2):
  `11|13|15|17|18|19|20|23|25|27|41|44|47|5|50|52|54|63|66|68|70|73|76|8|81|85|86|88|91|94|95|97|99`.
  P1 con menos: 20191/20221/20231/20241 faltan 88|91|97|99; 20211 falta además 27.
  `cole_cod_mcpio_ubicacion` nunique: P2 1113-1118, P1 102-165.
- Nulos: `cole_bilingue` es la columna con más nulos en TODOS los archivos (138036 en
  20182; **84072 = 100% en 20241**). En 20182 el bloque de 7 columnas `cole_*` + jornada/
  área/sede tiene exactamente 53.817 nulos (= `depto_nulo`: mismas filas sin info de
  colegio). Detalle completo por columna en `01_inventario.md` (795 líneas) y
  `01_inventario_icfes.csv`.

### TAREA B2/C — IPM (fuente: `datos/output/reports/01_inventario_ipm.md`)
- 13 hojas, dimensiones: Índice A1:G34; IPM_Regiones A1:AF40; IPM_Departamentos A1:AF55;
  IPM_Variables_Región A1:L162; IPM_Variables_Departamento A1:W870; IC_IPM A1:AE1012;
  Intensidad_IPM A1:AF54; Incidencia_Ajustada_IPM A1:AF54; Contribuciones IA_IPM A1:AF508;
  IPM_Sexo A1:O55; IC_IPM_Sexo A1:BS57; IPM_Sexo Jefe A1:O55; IC_IPM_Sexo Jefe A1:BS57.
  (Confirma las 13 de SESION-001, incluidos los espacios finales en dos nombres.)
- `IPM_Departamentos`: 54 filas × 22 columnas leídas; volcado TAL CUAL de las primeras 60
  (llegan las 54 existentes) en el reporte. Estructura: 12 filas de títulos/notas, fila 11
  (0-based) grupos de año `Departamento|2018|…|2024` (con `2020**` y `2021***` por notas),
  fila 12 sub-dominios Total|Cabeceras|Centros poblados y rural disperso, 33 filas de
  datos, 6 filas de fuente/notas.
- Años: **2018, 2019, 2020, 2021, 2022, 2023, 2024 completos** (hipótesis de la consigna
  CONFIRMADA). Columnas detectadas (22): `Departamento` + 7 años × (Total, Cabeceras,
  Centros poblados y rural disperso); cobertura 33/33 en Total y Cabeceras todos los años,
  **32/33 en rural todos los años (falta San Andrés: celdas vacías, isla sin rural)**.
- Unidades territoriales: **33, solo nombres** (lista en el reporte: 32 deptos + Bogotá
  D.C.). Cero filas de total nacional/cabeceras/rural/regiones EN ESTA HOJA (viven como
  columnas de dominio, no como filas). Columna código DIVIPOLA: **NO existe**.
- Notas textuales del DANE (transcripción exacta del volcado): `( ** ) Para el año 2020 el
  indicador de Inasistencia escolar integra información del SIMAT – C600 – ECV.` y
  `( ***) En 2021 el operativo de campo de la ENCV incorporó un registro fotográfico
  para ... acceso a servicios de acueducto y energía eléctrica [zona rural]`. Ver regla 18
  (marcar 2021): hay evidencia de cambio operativo 2021 en el propio anexo.
- Depuración honesta del script (3 versiones, todas idempotentes): v1 perdió 2020/2021 por
  regex exacta (`2020**`); v2 cayó en la fila-título combinada (celda con `\n` que contiene
  'Departamentos' + '2018-2024'); v3 exige ≥2 años distintos y alinea año×dominio. El total
  ICFES (3.973.901) fue idéntico en las 3 corridas.

### TAREA D — checkpoints (expectativas del documento, no resultados)
- Total medido 3.973.901 vs expectativa 4.039.755 → **diferencia exacta −65.854**.
  P1 existentes: 20191=66.104, 20211=58.708, 20221=73.795, 20231=77.555, 20241=84.072
  (rango 58.708–84.072). |−65.854| = 65.854 ∈ rango P1 → hipótesis "falta el periodo
  20181" PLAUSIBLE por magnitud (equivale a un P1 típico), pero NO concluyente: la
  evidencia interna no puede probar un archivo ausente y 65.854 no coincide con ningún P1
  medido. Diferencia declarada SIN explicar del todo.
- Cruce diagnóstico medido vs referencia documento (606.214 | 22 | 28.394), sin mapeo
  asumido: depto_nulo 560.158 (−46.056, −7,6%); global_cero 34 (+12); global_nulo 0;
  alguna_area_nula 29.029 (+635, +2,2%; es exactamente la suma de nulos de `punt_ingles`).
- `git check-ignore datos/output/reports/01_inventario_icfes.csv`: NO ignorado (queda
  versionable; el patrón `datos/output/*.csv` no alcanza a `reports/`).
- `datos/raw/` y el xlsx intactos (mtimes 2026-09-06, solo lecturas en esta sesión).

## Hallazgos
1. Los 11 CSV traen 3.973.901 registros reales (no 3.973.912 líneas: 11 cabeceras), 59
   columnas idénticas, 1 periodo por archivo, 0 duplicados exactos y 0 valores fuera de
   escala oficial en puntajes.
2. Único puntaje con nulos: inglés (29.029; 100% del diagnóstico de áreas nulas).
   `punt_global` nunca es nulo; solo 34 ceros en total; 20221 destaca con min=82.
3. `cole_bilingue` es la columna con más nulos en todos los periodos (hasta 100% en
   20241): candidata a decisión de tratamiento en Fase 1, NO tratada aquí.
4. DIVIPOLA como texto sin ceros a la izquierda (verificado en datos, no asumido); los P1
   no cubren San Andrés/Amazonas/Vaupés/Vichada (y Chocó en 20211): coherente con
   calendarios P1 de menor cobertura, solo diagnóstico.
5. El anexo IPM trae 2018–2024 completos a nivel departamento × dominio, con notas
   metodológicas 2020 (inasistencia SIMAT-C600-ECV) y 2021 (registro fotográfico ECV
   rural): insumo directo para la regla 18. IPM 2020 existe en el anexo aunque el panel
   ICFES excluye 2020 por diseño.
6. Las cifras del documento no están en el repo: todo cruce es contra expectativas
   externas y queda así rotulado en `01_inventario.md`.

## Decisiones (con justificación)
1. `requirements.txt` fijado a las 6 versiones reales del freeze (decisión 2 SESION-001
   cumplida); transitivas sin fijar (fuera de alcance).
2. Lectura CSV con `dtype=str` + NA por defecto: nulos = campos vacíos; no-numéricos
   contados explícitamente vía `to_numeric(errors="coerce")` (0 en puntajes).
3. Duplicado = md5 de la fila con separador `\x1f` (evita colisiones por `;` en texto),
   primeros 8 bytes como entero, set por archivo. 0 duplicados → sin segunda pasada.
4. Detección IPM basada en evidencia del volcado (≥2 años distintos; fin de datos ante
   fila de notas; clasificación territorial por coincidencia exacta normalizada para no
   marcar 'Amazonas' como región). Iterada 3 veces hasta cubrir el layout real DANE.
5. `scripts/__pycache__/` eliminado; no se commitea.

## Pendientes / riesgos
- Fase 1 (futura sesión): decidir tratamiento de `cole_bilingue` (nulos masivos), bloque
  `cole_*` nulo (~35-64k por archivo), nulos de inglés y 34 ceros globales, con conteos
  antes/después (regla 20). Nada tratado en esta sesión.
- Umbrales oficiales ICFES por periodo para el evento Matemáticas ≥ 51 (pendiente
  SESION-001, sigue abierto; hoy solo se verificó escala 0-100 sin salidas de rango).
- Diferencia −65.854 vs documento sin explicación concluyente (hipótesis 20181 plausible).
- `punt_global` min=82 en 20221: atípico frente a otros periodos (min 0-14); solo
  diagnóstico, vigilar en limpieza.
- IPM: hojas de variables/IC/intensidad/incidencia/sexo aún SIN perfilar (fuera del
  alcance B2); regla 18 (indicador 2021) pendiente de implementar con las notas halladas.

## Próxima sesión sugerida
SESION-003: limpieza Fase 1 con decisiones documentadas (filtros depto/global/áreas,
`cole_bilingue`, DIVIPOLA como texto con validación contra los 33 + 4 faltantes en P1),
script `02_limpieza_icfes.py` numerado que reporte antes/después y guarde evidencia en
`datos/output/reports/` + procesados en `datos/processed/`.

## Artefactos generados (rutas)
- scripts/01_inventario.py (nuevo; jupytext py:percent; 3 versiones iteradas, final v3)
- requirements.txt (editado: 6 paquetes con ==)
- datos/output/reports/01_inventario.md (nuevo)
- datos/output/reports/01_inventario_icfes.csv (nuevo; versionable, no ignorado)
- datos/output/reports/01_inventario_ipm.md (nuevo)
- bitacora/SESION-002_2026-09-07_entorno-inventario.md (este archivo)
- bitacora/INDEX.md (editado: fila 002)
