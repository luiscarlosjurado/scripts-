# 01 — Inventario IPM (SESION-002, solo perfilado)

## Hojas del anexo (dimensiones openpyxl, solo lectura)

Numero de hojas: **13** (SESION-001 reporto 13).

| hoja | dimension | filas_max | columnas_max |
|---|---|---|---|
| Índice | A1:G34 | 34 | 7 |
| IPM_Regiones | A1:AF40 | 40 | 32 |
| IPM_Departamentos | A1:AF55 | 55 | 32 |
| IPM_Variables_Región | A1:L162 | 162 | 12 |
| IPM_Variables_Departamento  | A1:W870 | 870 | 23 |
| IC_IPM | A1:AE1012 | 1012 | 31 |
| Intensidad_IPM | A1:AF54 | 54 | 32 |
| Incidencia_Ajustada_IPM | A1:AF54 | 54 | 32 |
| Contribuciones IA_IPM | A1:AF508 | 508 | 32 |
| IPM_Sexo | A1:O55 | 55 | 15 |
| IC_IPM_Sexo | A1:BS57 | 57 | 71 |
| IPM_Sexo Jefe | A1:O55 | 55 | 15 |
| IC_IPM_Sexo Jefe  | A1:BS57 | 57 | 71 |

## Hoja IPM_Departamentos: primeras 60 filas TAL CUAL (header=None)

Muestra: 54 filas x 22 columnas (la hoja trae 54 filas: se pidieron 60); hoja completa: 54 filas x 22 columnas. Campos unidos con '|' (vacio = celda vacia o NaN por celda combinada; los saltos de linea internos vienen de celdas Excel con ajuste de texto, p. ej. 'Centros poblados y rural disperso').

```
|||||||||||||||||||||
|||||||||||||||||||||
Incidencia de Pobreza Multidimensional|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
Incidencia de Pobreza Multidimensional
Departamentos
2018-2024|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
Cifras en porcentaje|||||||||||||||||||||
Departamento|2018|||2019|||2020**|||2021***|||2022|||2023|||2024||
|Total|Cabeceras|Centros poblados 
y rural disperso|Total|Cabeceras|Centros poblados 
y rural disperso|Total|Cabeceras|Centros poblados 
y rural disperso|Total|Cabeceras|Centros poblados 
y rural disperso|Total|Cabeceras|Centros poblados 
y rural disperso|Total|Cabeceras|Centros poblados 
y rural disperso|Total|Cabeceras|Centros poblados 
y rural disperso
Antioquia|15.3|9.6|35.4|15.7|10.2|35.9|14.9|10.2|32.7|14.3|10.8|28|10.7|7|25.8|9.5|5.9|24.2|10.9|8.4|21.2
Atlántico|21.1|20|39.5|14.9|13.7|38|14.1|13.1|33.9|15.5|14.8|29.6|10.2|9.4|25|12|11.3|25.7|9.5|8.6|26.4
Bogotá D.C.|4.1|4.1|19.2|7.1|7.1|16.5|7.5|7.5|15.4|5.7|5.7|19.4|3.8|3.8|10.1|3.6|3.6|11.7|5.4|5.4|10.8
Bolívar|31.9|25.6|50.5|26.9|21.4|42.9|28.1|21.5|47.1|26.8|21.5|41.8|19.4|13.9|34.6|18.4|14.9|28|15.6|13.5|21.5
Boyacá|16.5|7.9|28.5|12.8|5|23.9|11.7|4.3|22.4|10.9|5.4|19.1|9.6|6.1|15.1|9.9|5.4|17|6.9|3.7|12.1
Caldas|13.8|10.1|24.6|14.3|10.4|25.8|14.5|8.7|32.8|11.5|8.7|20.4|10.5|7.8|19.5|7.4|4.8|16.3|9.2|6|20.3
Caquetá|26.9|20.5|38.6|25.7|19.2|37.7|26.1|18.4|40.5|23.1|15.9|36.6|19.6|16.4|25.6|17.2|11.3|28.6|13.9|8.6|24.2
Cauca|27.7|13.2|36.2|24|10.6|31.8|28.2|12.3|37.4|18.6|10.5|23.2|18.3|8.8|23.6|15.8|6.8|20.9|14|7.5|17.6
Cesar|31.7|26.5|47.6|25.5|20.5|40.7|27.2|20.7|46.8|25.3|20.8|39.1|19.1|14.2|34.1|17.7|13.2|30.9|13.4|10.7|21.3
Córdoba|34.4|21.1|49.2|34.7|23.2|47.2|31.8|21.8|42.6|26.9|14.1|40.6|26.9|16.5|38|21.4|12.6|30.6|25.7|13|38.9
Cundinamarca|10.5|6.8|20|12.3|9.4|20.5|11.4|9.4|17.1|9.4|8.1|13.3|7.3|6.3|10.4|7.6|7.8|7.1|7.4|6.8|9.4
Chocó|46.3|29.4|60.3|42.3|26.7|55.1|49|33.5|61.5|36|25.3|44.4|36.8|25.2|45.8|37.4|25.5|46.4|33.9|18.8|45.2
Huila|18|12.1|27|18.3|12.5|27.1|23.4|13.1|39|17.5|11.8|26.1|13.3|9|19.7|11.9|7.2|19.1|10.9|7.6|15.8
La Guajira|53.3|31.3|72.9|48.8|28.1|68.2|51.7|30.1|72.7|48.7|26.3|70.7|42.9|20.7|65|42.6|23.6|61.7|39.3|17.4|61.3
Magdalena|36.4|31.1|48.5|31.6|24.6|47.8|33.4|27.3|47|32.4|27.2|43.7|23|17.5|34.9|21.4|15.9|33|19.2|15|28.1
Meta|15.6|10.7|31.4|19.1|17.8|23.1|14.1|9.7|28.2|14.9|11.3|26.4|11.3|8.5|20.3|12.9|10.6|20.2|10.4|8|18.2
Nariño|33.1|22|41.7|23.2|18.4|26.9|27.3|15|36.8|22.1|13.4|28.9|17.6|12.7|21.4|16.6|11.6|20.5|18.1|10|24.5
Norte de Santander|29.5|25.9|43|24.2|19.3|42.8|26.1|20.8|46.2|24.7|19.7|44|18.5|13|39.8|20.5|16.4|36.2|15.2|8.5|41.1
Quindío|14.2|13.5|19|10.2|9.1|18|12.9|11.8|21|10.9|10|17.1|10|9.3|15.3|7.5|6.7|13.5|7.4|6.8|11.3
Risaralda|11.6|7|28|11.1|6.5|28.2|13.1|8.9|29.5|10.7|8|21.5|10|6.6|23.9|11.8|8.8|24|9.5|6.3|23
Santander|12.6|8.2|26.8|12.4|8.8|24.1|12.5|8.2|26.6|13.3|9.1|27.3|10.4|7.4|20.6|9.8|6.6|20.7|6.8|4.9|13.6
Sucre|41.7|32.8|56.8|33.3|25.4|46.6|38.1|29.5|52.2|30.3|23.7|41|26|19.8|36|23.1|15.9|34.6|21.8|12.4|36.4
Tolima|22.2|11.8|44.7|15.2|8.4|30|19|12.1|34|16.6|11|29|10.5|5.4|22|12.9|8|23.9|12.6|7.2|24.7
Valle del Cauca|14.1|12.5|23.2|10.8|9.3|19.4|11.1|8.9|24.1|8.6|6.9|18.6|9.7|8|19.4|7.2|5.8|15.8|6.2|4.6|15.9
Arauca|27.6|24.6|33.3|23.3|20.5|28.6|26.1|23.4|31.1|26.8|25.8|28.7|22.6|22.4|22.9|22.8|20.7|26.6|17.7|17.4|18.3
Casanare|19|14.5|29.6|18.3|15.1|26.2|19.6|14.3|32.8|19.5|16.4|27.3|13.3|10.7|20|15|12.5|21.4|11.3|9.1|17.1
Putumayo|24.1|17.5|30.8|25.4|22.1|28.7|27.8|22.6|33.2|22.8|16.5|29.4|20.8|14.7|27.2|13.2|10.5|16.1|11.8|8.8|15.1
San Andrés|8.5|8.5||8.2|8.2||11.9|11.9||7|7||8.8|8.8||5|5||6|6|
Amazonas|35.4|27.4|42.1|35.6|19.5|49.6|39|24.3|53.5|25.7|23|28.4|27.9|23.5|32.3|25.4|18.6|32.6|15.6|13.8|17.6
Guainía|60.6|44|72.6|67|39.9|87.7|65.9|43.1|84.5|57.3|45.7|67.1|46.5|39.9|52.2|52.1|46.4|57|49|40.1|56.9
Guaviare|31.4|22.8|42.1|30.9|26.5|36.7|34.6|27.5|43.8|31|24.2|40|26.9|21.7|33.7|30.6|18.5|46.5|21.3|17.5|26.3
Vaupés|68.5|27.4|82.9|66.5|25.4|80.1|65.6|26.8|81.3|52.7|22.3|64.8|47.1|15|59.7|55.7|16.6|70.9|37.4|16.2|45.5
Vichada|63.5|33.7|73|72.2|35.7|84|75.6|46.6|85.1|64.8|38.3|73.4|75.4|36.1|87.9|65.4|33.6|75.4|70.2|30|82.7
|||||||||||||||||||||
|||||||||||||||||||||
Fuente: DANE - Encuesta Nacional de Calidad de Vida.|||||||||||||||||||||
Datos expandidos con proyecciones de población, con base en los resultados del CNPV 2018.|||||||||||||||||||||
Nota: (**) Para el año 2020 el indicador de Inasistencia escolar integra información del SIMAT – C600 – ECV.|||||||||||||||||||||
Nota: (***) En 2021 el operativo de campo de la ENCV incorporó un registro fotográfico para obtener información sobre la cobertura de servicios públicos domiciliarios en zona rural, en particular, acceso a servicios de acueducto y energía eléctrica.|||||||||||||||||||||
Nota: Para el cálculo total nacional, total cabeceras y centros poblados y rural disperso no se tiene en cuenta la ruralidad de la Amazonía- Orinoquía.|||||||||||||||||||||
Actualizado el 22 de abril de 2025|||||||||||||||||||||
```

## Respuestas B2 (con cifras de la lectura completa)

- anios detectados en el encabezado: ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
- fila de grupos de anio (0-based, header=None): 11
- filas de datos detectadas (sin titulos ni notas): 33
- lista de columnas detectadas (22):
  - [0] 'Departamento' (valores no nulos: 33)
  - [1] '2018 Total' (valores no nulos: 33)
  - [2] '2018 Cabeceras' (valores no nulos: 33)
  - [3] '2018 Centros poblados y rural disperso' (valores no nulos: 32)
  - [4] '2019 Total' (valores no nulos: 33)
  - [5] '2019 Cabeceras' (valores no nulos: 33)
  - [6] '2019 Centros poblados y rural disperso' (valores no nulos: 32)
  - [7] '2020 Total' (valores no nulos: 33)
  - [8] '2020 Cabeceras' (valores no nulos: 33)
  - [9] '2020 Centros poblados y rural disperso' (valores no nulos: 32)
  - [10] '2021 Total' (valores no nulos: 33)
  - [11] '2021 Cabeceras' (valores no nulos: 33)
  - [12] '2021 Centros poblados y rural disperso' (valores no nulos: 32)
  - [13] '2022 Total' (valores no nulos: 33)
  - [14] '2022 Cabeceras' (valores no nulos: 33)
  - [15] '2022 Centros poblados y rural disperso' (valores no nulos: 32)
  - [16] '2023 Total' (valores no nulos: 33)
  - [17] '2023 Cabeceras' (valores no nulos: 33)
  - [18] '2023 Centros poblados y rural disperso' (valores no nulos: 32)
  - [19] '2024 Total' (valores no nulos: 33)
  - [20] '2024 Cabeceras' (valores no nulos: 33)
  - [21] '2024 Centros poblados y rural disperso' (valores no nulos: 32)
- columna territorial usada (indice): 0
- columna de codigo DIVIPOLA: None
- codigos DIVIPOLA: NO se detecto columna de codigo (solo nombres).
- unidades territoriales unicas: 33
  - posible_departamento (33): ['Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bogotá D.C.', 'Bolívar', 'Boyacá', 'Caldas', 'Caquetá', 'Casanare', 'Cauca', 'Cesar', 'Chocó', 'Cundinamarca', 'Córdoba', 'Guainía', 'Guaviare', 'Huila', 'La Guajira', 'Magdalena', 'Meta', 'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío', 'Risaralda', 'San Andrés', 'Santander', 'Sucre', 'Tolima', 'Valle del Cauca', 'Vaupés', 'Vichada']
