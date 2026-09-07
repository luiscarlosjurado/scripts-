# Variables ICFES 2018-2025 (Unión de 16 archivos)

## Resumen
- **Total columnas en CSV unificado:** 94
- **Columnas presentes en TODOS los 16 archivos:** 82
- **Columnas parciales (solo en algunos archivos):** 12
- **Registros totales:** 5,304,758

---

## Variables presentes en TODOS los archivos (82)

### Periodo (1)
- `periodo`

### Colegio (17)
- `cole_area_ubicacion`
- `cole_bilingue`
- `cole_calendario`
- `cole_caracter`
- `cole_cod_dane_establecimiento`
- `cole_cod_dane_sede`
- `cole_cod_depto_ubicacion`
- `cole_cod_mcpio_ubicacion`
- `cole_codigo_icfes`
- `cole_depto_ubicacion`
- `cole_genero`
- `cole_jornada`
- `cole_mcpio_ubicacion`
- `cole_naturaleza`
- `cole_nombre_establecimiento`
- `cole_nombre_sede`
- `cole_sede_principal`

### Desempeño (5)
- `desemp_c_naturales`
- `desemp_ingles`
- `desemp_lectura_critica`
- `desemp_matematicas`
- `desemp_sociales_ciudadanas`

### Estudiante (27)
- `estu_consecutivo`
- `estu_estudiante`
- `estu_tipodocumento`
- `estu_agregado`
- `estu_cod_depto_presentacion`
- `estu_cod_mcpio_presentacion`
- `estu_cod_reside_depto`
- `estu_cod_reside_mcpio`
- `estu_dedicacioninternet`
- `estu_dedicacionlecturadiaria`
- `estu_depto_presentacion`
- `estu_depto_reside`
- `estu_discapacidad`
- `estu_fechanacimiento`
- `estu_genero`
- `estu_grado`
- `estu_horassemanatrabaja`
- `estu_inse_individual`
- `estu_mcpio_presentacion`
- `estu_mcpio_reside`
- `estu_nacionalidad`
- `estu_nse_establecimiento`
- `estu_nse_individual`
- `estu_pais_reside`
- `estu_privado_libertad`
- `estu_repite`
- `estu_tiporemuneracion`

### Familia (20)
- `fami_comecarnepescadohuevo`
- `fami_comecerealfrutoslegumbre`
- `fami_comelechederivados`
- `fami_cuartoshogar`
- `fami_educacionmadre`
- `fami_educacionpadre`
- `fami_estratovivienda`
- `fami_numlibros`
- `fami_personashogar`
- `fami_situacioneconomica`
- `fami_tieneautomovil`
- `fami_tienecomputador`
- `fami_tieneconsolavideojuegos`
- `fami_tienehornomicroogas`
- `fami_tieneinternet`
- `fami_tienelavadora`
- `fami_tienemotocicleta`
- `fami_tieneserviciotv`
- `fami_trabajolabormadre`
- `fami_trabajolaborpadre`

### Percentiles (6)
- `percentil_global`
- `percentil_c_naturales`
- `percentil_ingles`
- `percentil_lectura_critica`
- `percentil_matematicas`
- `percentil_sociales_ciudadanas`

### Puntajes (6)
- `punt_global`
- `punt_c_naturales`
- `punt_ingles`
- `punt_lectura_critica`
- `punt_matematicas`
- `punt_sociales_ciudadanas`

---

## Variables que existen solo en algunos archivos (12)

| Variable | Archivos donde existe | Cantidad |
|---|---|---|
| `estu_pilopaga` | Solo **2018-1** | 1 |
| `estu_generacione` | 2018-2, 2019-1, 2019-2, 2020-1, 2020-2, 2021-2 | 6 |
| `estu_etnia` | Todos excepto **2020-2** | 15 |
| `estu_tieneetnia` | Todos excepto **2023-2** | 15 |
| `estu_grupoetnia` | 2023-2, 2024-1, 2024-2, 2025-1, 2025-2 | 5 |
| `fami_numhermanos` | Solo **2025-2** | 1 |
| `fami_posicionhermanos` | Solo **2025-2** | 1 |
| `estu_comunidadcampesina` | Solo **2025-2** | 1 |
| `estu_numhijos` | Solo **2025-2** | 1 |
| `estu_horastrabnoremu` | Solo **2025-2** | 1 |
| `estu_tiempocasaacole` | Solo **2025-2** | 1 |
| `estu_desplazacolegio` | Solo **2025-2** | 1 |

---

## Cómo ver las variables con pandas

```python
import pandas as pd

# Ver SOLO variables sin cargar 3.4 GB (instantáneo)
cols = pd.read_csv("icfes_2018_2025.csv", sep=";", nrows=0).columns.tolist()
print(len(cols))   # 94
print(cols)

# Cargar completo (requiere ~10 GB RAM)
df = pd.read_csv("icfes_2018_2025.csv", sep=";", low_memory=False)
df.info()
df.head()
```

---

## Script para generar matriz variable × archivo

```python
import glob, os
import pandas as pd

archivos = sorted(glob.glob("datos/datos icfes/Examen_Saber_11_*.txt"))
sets = {os.path.basename(a): set(pd.read_csv(a, sep=";", nrows=0).columns) for a in archivos}
todas = sorted(set().union(*sets.values()))
matriz = pd.DataFrame({n: pd.Series([c in s for c in todas], index=todas) for n, s in sets.items()})
comunes = matriz.all(axis=1)
print(f"Comunes a los 16: {comunes.sum()}")
print(matriz.loc[~comunes])
```

---

*Generado automáticamente — fuente: análisis de cabeceras de los 16 archivos TXT originales*