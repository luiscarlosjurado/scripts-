### 1. Objetivos del Proyecto

**Objetivo General:**
Analizar la relación entre el Índice de Pobreza Multidimensional (IPM) y el desempeño académico en la educación media de los departamentos de Colombia durante el periodo 2018-2024, integrando información oficial del DANE y del ICFES.

**Objetivos Específicos:**
1. **Describir** el comportamiento del IPM (sus 5 dimensiones y 15 indicadores) y de los resultados de las pruebas Saber 11 a nivel departamental mediante estadística descriptiva y análisis exploratorio.
2. **Estimar** la magnitud y asociación entre el IPM y el desempeño académico mediante modelos econométricos de datos de panel con efectos fijos (controlando la heterogeneidad de cada territorio y los choques anuales).
3. **Diseñar** un modelo probabilístico de respuesta binaria (aprendizaje automático) que estime la probabilidad de que un estudiante alcance un desempeño "satisfactorio" en función de la pobreza de su departamento.
4. **Validar** este modelo predictivo para asegurar su precisión y utilizarlo para simular escenarios futuros.

---

### 2. Producto que se desea obtener (¿Qué se va a hacer?)

El proyecto no solo busca hacer un diagnóstico, sino crear una **herramienta analítica y predictiva**. Los productos y resultados tangibles son:

*   **Un Diagnóstico Territorial Evidenciado:** Un mapa claro de cómo la pobreza estructural (vivienda, salud, trabajo, educación del hogar) está reproduciendo las brechas educativas en los departamentos de Colombia, identificando cuáles regiones logran "resiliencia académica" a pesar de su pobreza.
*   **Un Modelo Predictivo de Machine Learning:** Un algoritmo (regresión logística supervisada) capaz de calcular la probabilidad exacta de que un estudiante obtenga un puntaje satisfactorio (Nivel 3 o 4, es decir, 51 puntos o más en Matemáticas) basándose en el IPM de su territorio y otras variables administrativas.
*   **Simulación de Escenarios (Hoja de Ruta):** El modelo permitirá predecir qué pasaría con el rendimiento académico si se aplicaran políticas públicas que logren reducir el IPM en 1, 3 o 5 puntos porcentuales, o si los departamentos más pobres convergieran hacia la mediana nacional.
*   **Recomendaciones de Política Pública:** Sugerencias basadas en datos reales (no en supuestos) para que el Estado diseñe intervenciones focalizadas que mitiguen las barreras estructurales y promuevan la igualdad de oportunidades.

---

### 3. Cómo se quiere demostrar o evaluar (Metodología y Validación)

El proyecto utiliza un **enfoque cuantitativo, correlacional y predictivo**, trabajando con un panel de datos de los 32 departamentos más Bogotá D.C. entre 2018 y 2024 (excluyendo el año 2020 por las alteraciones atípicas de la pandemia). 

La demostración y evaluación se divide en las siguientes fases técnicas:

**A. Modelado Econométrico (Para demostrar la asociación histórica):**
*   Se usan **modelos de panel con efectos fijos**. Esto demuestra la relación aislando factores que no cambian en el tiempo (como la geografía o cultura de un departamento) y eventos que afectan a todos por igual (como la inflación nacional).
*   Se evalúa la asociación contemporánea (pobreza del mismo año) y rezagada (cómo la pobreza del año anterior afecta el resultado actual).
*   Se aplican pruebas estadísticas de robustez (Hausman, Wooldridge, Pesaran) para demostrar que los hallazgos son sólidos y no producto del azar.

**B. Entrenamiento y Validación del Modelo de Machine Learning (Para demostrar que puede predecir):**
Para demostrar que el modelo realmente funciona y no solo "memoriza" los datos pasados, se utiliza una estricta evaluación **fuera de muestra (out-of-sample)**:
1.  **Entrenamiento:** El modelo "aprende" con los datos de las cohortes de estudiantes de los años **2018, 2019, 2021 y 2022**.
2.  **Prueba a ciegas (Validación):** El modelo se enfrenta a datos que **nunca antes había visto**: las cohortes de **2023 y 2024**. Si el modelo acierta en estos años, se demuestra su capacidad predictiva real.

**C. Métricas de Evaluación del Modelo:**
El éxito del modelo probabilístico se medirá mediante:
*   **Bondad de ajuste:** Pseudo-R² de McFadden y criterios AIC/BIC.
*   **Calibración:** Prueba de Hosmer-Lemeshow (para asegurar que las probabilidades predichas coincidan con la realidad).
*   **Capacidad Discriminante:** Curva ROC y el Área Bajo la Curva (AUC), Matriz de Confusión, Sensibilidad y Especificidad (para medir qué tan bien distingue el modelo entre un estudiante que logrará el nivel satisfactorio y el que no).
*   **Validación Cruzada Espacial:** Se entrenará dejando un departamento fuera en cada iteración para asegurar que el modelo funcione bien en cualquier territorio del país, no solo en los más poblados.
