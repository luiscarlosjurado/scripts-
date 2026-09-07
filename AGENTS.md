# AGENTS.md — Reglas del proyecto Saber 11 × IPM

## Contexto
Proyecto de Especialización en Analítica de Datos. Objetivo: analizar la relación entre el
IPM (DANE) y el desempeño en Saber 11 (ICFES) a nivel departamental, 2018-2024 (2020 excluido
por diseño). Fuentes: CSV por periodo ICFES en datos/raw/ (Examen_Saber_11_YYYYP_limpio.csv),
anexo departamental IPM en datos/ (anex-PMultidimensional-Departamental-2024.xlsx),
datos/variables_icfes.md y resumen_investigacion.md (raíz del repo) como referencia.

## Regla de oro: cero alucinación
1. Toda cifra (conteos, porcentajes, nombres de columnas, rangos, fechas) debe provenir de una
   ejecución real de código o comando en este repo. Si no se ejecutó, no se afirma.
2. Toda afirmación cuantitativa en bitácora, informes o chat cita su evidencia:
   (fuente: <script> | <artefacto en datos/output/reports/> | salida pegada).
3. Si un dato se desconoce: se ejecuta código para obtenerlo. Si no es posible, se escribe
   "SIN VERIFICAR" y el motivo. Nunca se rellena con plausibilidad.
4. Las cifras de resumen_investigacion.md o del documento del proyecto son EXPECTATIVAS de
   comparación, nunca resultados. Los resultados salen de NUESTROS datos.
5. Prohibido inventar datos de prueba que puedan confundirse con datos reales.

## Inmutabilidad y reproducibilidad
6. datos/raw/ es de solo lectura. Nunca se modifica, sobrescribe o borra.
7. Scripts deterministas: rutas relativas, semilla fija si hay muestreo, idempotentes
   (ejecutar dos veces => mismo resultado). Salidas a datos/processed/ o datos/output/.
8. Todo paso de limpieza reporta antes/después (filas y columnas) y guarda evidencia
   (CSV/JSON/MD de conteos) en datos/output/reports/.
9. Dependencias declaradas en requirements.txt. Sin rutas absolutas. Sin try/except silenciosos.

## Bitácora (memoria del proyecto)
10. Carpeta bitacora/: un archivo por sesión: SESION-<NNN>_<YYYY-MM-DD>_<slug>.md.
    Las entradas pasadas NUNCA se editan; se corrige añadiendo una nota fechada.
11. bitacora/INDEX.md se actualiza en cada sesión (tabla: ID | Fecha | Objetivo | Estado | Archivo).
12. Toda sesión de opencode: ABRE leyendo AGENTS.md + INDEX.md + última entrada;
    CIERRA escribiendo su entrada y actualizando INDEX antes de terminar.
13. Si una sesión se interrumpe, queda entrada con estado INTERRUMPIDA y pendiente claro.
14. Plantilla obligatoria de entrada:
    # SESION-NNN — fecha
    ## Objetivo
    ## Contexto leído (AGENTS.md, INDEX, entrada anterior)
    ## Acciones y comandos ejecutados
    ## Resultados reales (salidas pegadas y/o rutas de artefactos)
    ## Hallazgos
    ## Decisiones (con justificación)
    ## Pendientes / riesgos
    ## Próxima sesión sugerida
    ## Artefactos generados (rutas)

## Convenciones de datos
15. Periodos ICFES en formato YYYYP (P=semestre). Verificar empíricamente qué periodos existen;
    2020 excluido por diseño: si apareciera, NO se incorpora y se documenta.
16. Códigos DIVIPOLA como TEXTO (preservar ceros a la izquierda).
17. Encoding y separador de cada archivo se detectan y documentan en el inventario (no se asumen).
18. IPM: conservar solo las 33 unidades territoriales (32 deptos + Bogotá D.C.); descartar filas
    de total nacional, cabeceras, rural y regiones. Marcar 2021 con indicador por cambio de
    algoritmo del indicador de inasistencia (verificar y documentar).
19. Evento objetivo del modelo: puntaje de Matemáticas >= 51 (nivel 3 o 4), reconstruido desde el
    puntaje continuo con umbrales oficiales ICFES. No usar columnas de niveles reportadas sin
    verificar equivalencia.
20. Duplicados y faltantes: ningún tratamiento (borrar/imputar) sin decisión documentada en
    bitácora con conteos antes/después.

## Estilo de scripts Python
21. pandas + pathlib; función main() e if __name__ == "__main__"; docstring con: propósito,
    entradas, salidas, sesión de bitácora que lo origina.
22. Nomenclatura snake_case en español (coherente con el repo existente).
    Pipeline numerado por orden de ejecución: 01_inventario.py, 02_..., etc.
23. Cada script imprime un resumen final y guarda su artefacto principal.
> Nota: El script debe estar diseñado para ser convertido a un archivo de jupyter notebook utilizando jupytex eso significa que deberas crear titulos y pequeñas explicaciones en markdown del codigo generado en el script

## Flujo de sesión (opencode)
24. Leer contexto → confirmar objetivo → explorar/ejecutar ANTES de afirmar → guardar artefactos →
    escribir bitácora con salidas reales → actualizar INDEX → proponer commit
    (mensaje: "bitacora: sesion NNN - <resumen>"). El commit lo ejecuta el humano.

## Prohibiciones al agente
25. No resumir datasets de memoria ni desde el PDF: perfilarlos.
26. No asumir que una columna existe: verificarla por periodo (las columnas cambian entre años).
27. No operar destructivamente (rm, overwrite de raw, drop sin evidencia).
28. No cambiar alcance u objetivos del proyecto sin registrarlo como decisión en bitácora.
