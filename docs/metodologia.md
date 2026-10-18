# Metodología de investigación y análisis

## 1. Propósito

Este documento define los procedimientos previstos para analizar datos hídricos, climáticos y territoriales en áreas seleccionadas del Triángulo del Litio argentino.

La metodología prioriza la trazabilidad de las fuentes, la conservación de los datos originales, la reproducibilidad de los procedimientos y la interpretación prudente de los resultados.

Los procedimientos aquí descritos constituyen un plan de trabajo. Su aplicación y sus resultados se documentarán a medida que avance la investigación.

## 2. Enfoque general

La investigación tendrá un enfoque cuantitativo, temporal y geoespacial, complementado con información hidrogeológica, ambiental y social disponible públicamente.

Se utilizarán herramientas de Python para preparar, analizar y explorar los datos. La visualización interactiva será desarrollada por la autora mediante herramientas convencionales de programación y representación de datos, de acuerdo con las restricciones del concurso sobre inteligencia artificial generativa.

El análisis distinguirá entre observaciones, estimaciones, asociaciones estadísticas e hipótesis explicativas.

## 3. Delimitación del área de estudio

El área de investigación se limitará a sectores seleccionados de Jujuy, Salta y Catamarca.

La selección de las áreas considerará:

- Ubicación de salares y cuencas relevantes.
- Disponibilidad de datos hídricos y climáticos.
- Resolución espacial de las fuentes.
- Existencia de información hidrogeológica local.
- Disponibilidad de documentación ambiental y minera verificable.

Las áreas no se definirán exclusivamente por límites provinciales o por la ubicación de los proyectos mineros. Siempre que sea posible, se utilizarán límites de cuencas o unidades hidrogeológicas documentadas.

La delimitación final se registrará en `docs/fuentes.md` y se justificará antes de realizar comparaciones entre territorios.

## 4. Adquisición y registro de datos

Cada conjunto de datos se documentará antes de su utilización, incluyendo:

- Institución responsable y enlace.
- Nombre y versión del producto.
- Fecha de descarga.
- Cobertura temporal y espacial.
- Variables y unidades.
- Formato de archivo.
- Licencia o condiciones de uso.
- Limitaciones conocidas.

Los archivos originales se guardarán en `data/raw/`, organizados por fuente.

Los datos descargados no se modificarán directamente. La limpieza, conversión de unidades, agregación temporal y selección geográfica se realizarán sobre copias de trabajo.

## 5. Preparación y control de calidad

Antes del análisis se verificará:

1. Que los archivos puedan abrirse correctamente.
2. Que las variables seleccionadas estén presentes.
3. Que las fechas y coordenadas sean interpretables.
4. Que las unidades coincidan con la documentación de la fuente.
5. Que se identifiquen valores faltantes, duplicados y períodos incompletos.
6. Que se revisen valores atípicos sin eliminarlos automáticamente.
7. Que cualquier conversión o exclusión quede registrada.

Los datos faltantes no se reemplazarán por valores inventados. Si se requiere interpolación o algún otro tratamiento estadístico, se justificará y se documentará de manera explícita.

Las salidas procesadas se guardarán en `data/processed/`, mientras que los registros de procedencia y validación se conservarán en `data/metadata/`.

## 6. Análisis del almacenamiento terrestre de agua

Se evaluará el producto seleccionado de GRACE/GRACE-FO para estudiar la evolución de las anomalías del almacenamiento terrestre total de agua.

El análisis considerará:

- Cobertura temporal efectiva.
- Unidad de medida y período de referencia.
- Valores faltantes e incertidumbre.
- Resolución espacial efectiva.
- Comparabilidad entre las áreas seleccionadas.

Se examinará la evolución temporal y se describirán las variaciones observadas. Cualquier cálculo de tendencia deberá indicar el período utilizado, el método estadístico y las limitaciones correspondientes.

Los resultados se interpretarán como cambios regionales estimados del almacenamiento total de agua. No se presentarán como mediciones directas del nivel de un acuífero ni como estimaciones automáticas de agua disponible para consumo.

## 7. Análisis de precipitaciones

Se evaluará un producto mensual de CHIRPS, verificando la versión, la cobertura temporal y las unidades.

El análisis buscará:

- Describir la evolución de las precipitaciones.
- Identificar períodos relativamente secos o lluviosos.
- Examinar variaciones interanuales.
- Comparar las series de precipitación con las anomalías de almacenamiento de agua.

Cuando se utilicen acumulaciones mensuales, se verificará que las unidades representen correctamente la precipitación acumulada durante cada período.

La identificación de sequías o anomalías requerirá un criterio explícito y documentado, incluyendo el período de referencia utilizado.

## 8. Comparación temporal entre variables

La comparación entre almacenamiento de agua y precipitación se realizará únicamente sobre períodos compatibles y con una definición espacial documentada.

Se evaluarán:

- Coincidencias temporales entre variaciones.
- Diferencias entre períodos secos y húmedos.
- Posibles desfases temporales.
- Sensibilidad de los resultados al período seleccionado.
- Limitaciones derivadas de la diferencia de resolución entre fuentes.

Cualquier correlación se interpretará como una asociación estadística, no como demostración de causalidad.

La precipitación, la recarga, la evaporación, las características geológicas y las extracciones pueden intervenir en la dinámica hídrica. Las conclusiones deberán considerar estas explicaciones alternativas.

## 9. Incorporación de información hidrogeológica y minera

Se buscarán datos locales de niveles piezométricos, caudales, calidad del agua, extracción y monitoreo ambiental.

Para cada registro se verificará, cuando sea posible, la ubicación, el período, la unidad, el método de medición y la institución responsable.

La información minera se analizará considerando la etapa del proyecto y la fecha efectiva de los registros disponibles. No se asumirá que un proyecto anunciado se encuentra operativo ni que su ubicación demuestra una influencia sobre una cuenca determinada.

Las comparaciones se realizarán solamente cuando las fuentes sean compatibles y permitan una interpretación razonable.

Si no existen datos suficientes para evaluar una hipótesis, se documentará esa limitación sin concluir que el impacto está presente o ausente.

## 10. Diseño de la exploración interactiva

La aplicación se desarrollará en Python con una herramienta de visualización interactiva elegida según las necesidades del proyecto.

Se evaluará la incorporación de:

- Filtros de período.
- Selección de áreas de estudio.
- Selección de variables.
- Comparación de series temporales.
- Consulta de unidades, fuentes y limitaciones.
- Exploración de datos faltantes y cobertura disponible.
- Contextualización territorial mediante información geográfica validada.

Cada interacción deberá modificar de manera coherente la información presentada y permitir que la persona usuaria comprenda qué datos está examinando.

Los gráficos, mapas y demás componentes visuales finales serán elaborados y revisados por la autora, sin recurrir a generación automática mediante IA generativa. Se documentarán las decisiones de diseño y los procedimientos de programación pertinentes.

## 11. Evaluación de calidad e incertidumbre

La interpretación considerará:

- Incertidumbre de las estimaciones.
- Diferencias entre resoluciones espaciales.
- Cobertura temporal incompleta.
- Calidad y representatividad de las mediciones.
- Posibles sesgos y limitaciones de las fuentes.
- Disponibilidad desigual de información entre territorios.

Las conclusiones se limitarán a lo que permitan sostener los datos. Se distinguirán los resultados descriptivos de las inferencias estadísticas y de las hipótesis que requieran estudios adicionales.

## 12. Reproducibilidad

Para facilitar la reproducción del análisis:

- Se conservarán los datos originales.
- Se documentarán las versiones de las fuentes.
- Se registrarán las transformaciones aplicadas.
- Se mantendrán los procedimientos de análisis en archivos identificables.
- Se registrarán las dependencias de Python.
- Se explicarán los pasos necesarios para ejecutar el proyecto.
- Se conservará la procedencia de los datos que alimenten cada resultado.

La reproducibilidad estará condicionada por la disponibilidad de las fuentes, sus licencias y los requisitos técnicos de los archivos utilizados.

## 13. Uso de herramientas e inteligencia artificial

La investigación respetará las bases del concurso respecto del uso de IA generativa.

Las decisiones metodológicas, la interpretación científica, la selección de resultados y la elaboración de la visualización final serán responsabilidad de la autora.

No se utilizará IA generativa para crear automáticamente los gráficos, mapas, diagramas, infografías o figuras finales. La programación y la visualización se realizarán mediante herramientas convencionales de Python.

Los usos de asistencia digital que deban declararse se documentarán con transparencia, conforme a las bases.

## 14. Criterios para comunicar resultados

Los resultados se presentarán diferenciando:

- **Observación:** valor o patrón identificado en los datos.
- **Estimación:** resultado calculado por una fuente o un procedimiento estadístico.
- **Asociación:** relación observada entre variables.
- **Hipótesis:** explicación posible que requiere evaluación.
- **Conclusión:** interpretación respaldada por evidencia suficiente para el alcance del análisis.

La ausencia de evidencia suficiente se comunicará explícitamente. No se atribuirán efectos a la minería sin datos adecuados para evaluar la relación ni se descartarán impactos por la falta de registros.

## 15. Estado metodológico

**Estado actual:** planificación metodológica.

La selección definitiva de áreas, la descarga y validación de datos, el análisis estadístico y el desarrollo de la aplicación interactiva son etapas pendientes.

Las decisiones finales se actualizarán en este documento a medida que se verifiquen las fuentes y se implementen los procedimientos.