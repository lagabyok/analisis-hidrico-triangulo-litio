# Agua, comunidades y actividad minera en el Triángulo del Litio argentino

**Investigación geoespacial y temporal con datos abiertos para explorar la evolución de los recursos hídricos en Jujuy, Salta y Catamarca.**

## 1. Descripción del proyecto

Este proyecto propone investigar la evolución temporal y espacial de variables hídricas y climáticas en áreas seleccionadas vinculadas a los salares y a la actividad minera de litio en las provincias argentinas de Jujuy, Salta y Catamarca.

Mediante el análisis de datos abiertos, se buscará identificar tendencias en el almacenamiento terrestre de agua, estudiar las variaciones de las precipitaciones y explorar posibles señales de estrés hídrico. También se investigará qué información hidrogeológica, ambiental y minera se encuentra disponible para evaluar posibles relaciones entre los cambios observados y las actividades desarrolladas en cada territorio.

El proyecto tendrá como resultado una **visualización interactiva desarrollada en Python**, diseñada para que las personas usuarias puedan explorar los datos, seleccionar períodos, comparar áreas y examinar las variables disponibles, lo que facilita la identificación de patrones, tendencias y diferencias. De este modo, se busca promover una exploración flexible y dinámica de la información.

La investigación parte de una prioridad socioambiental: contribuir a la protección del agua, las comunidades que dependen de ella y los ecosistemas de la Puna.

No se presupone que la actividad minera sea la causa de las variaciones hídricas ni se descartan posibles impactos. El objetivo es analizar la evidencia disponible, reconocer las limitaciones de los datos y determinar qué información adicional se necesita para evaluar cada situación con rigor científico.

## 2. Fundamentación y relevancia socioambiental

En las regiones áridas y de altura, el agua es fundamental para el consumo humano, la ganadería, la agricultura, las actividades productivas y el mantenimiento de los ecosistemas. Comprender su disponibilidad requiere considerar las precipitaciones, las características geológicas e hidrogeológicas, los procesos de recarga, la evaporación y las extracciones.

La expansión de la actividad minera de litio en los salares plantea interrogantes sobre la disponibilidad y la dinámica del agua. Sin embargo, estos interrogantes no pueden resolverse únicamente mediante datos de producción minera o información satelital regional.

Es necesario contrastar diferentes fuentes, escalas y tipos de evidencia, incluyendo mediciones locales de aguas subterráneas, registros de extracción, estudios hidrogeológicos, monitoreos ambientales y documentación sobre los usos del agua por parte de las comunidades.

La dimensión social también es central. Las preocupaciones comunitarias, los derechos de acceso al agua y los medios de vida locales deben considerarse junto con la evidencia ambiental y científica.

Por esta razón, el proyecto distinguirá entre los resultados de los análisis cuantitativos, los antecedentes documentales, las preocupaciones expresadas por las comunidades y las hipótesis que requieran investigación adicional.

## 3. Objetivo general

Desarrollar una herramienta interactiva de exploración y análisis geoespacial y temporal de datos hídricos y climáticos de áreas seleccionadas del Triángulo del Litio argentino, para identificar tendencias, examinar posibles señales de estrés hídrico y facilitar la evaluación de las preguntas ambientales y sociales que requieren mayor evidencia.

## 4. Objetivos específicos

1. Analizar la evolución temporal de las anomalías del almacenamiento terrestre de agua a partir de datos satelitales.
2. Examinar las variaciones de las precipitaciones y explorar su relación temporal con los cambios del almacenamiento de agua.
3. Delimitar áreas de estudio a partir de criterios hidrogeológicos, geográficos y de disponibilidad de información.
4. Comparar tendencias entre las áreas seleccionadas, considerando la resolución y las limitaciones de las fuentes.
5. Relevar datos locales sobre niveles piezométricos, extracciones, calidad del agua y monitoreo ambiental, cuando estén disponibles.
6. Investigar qué evidencia permitiría evaluar posibles relaciones entre la actividad minera y las variaciones hídricas.
7. Identificar vacíos de información relevantes para la protección de las comunidades y los ecosistemas.
8. Diseñar una experiencia interactiva que permita explorar los datos de manera autónoma, transparente y reproducible.

## 5. Preguntas de investigación

**Evolución del almacenamiento de agua**

¿Cómo cambió el almacenamiento terrestre de agua durante el período cubierto por las fuentes disponibles? ¿Se identifican tendencias, anomalías o períodos de recuperación?

**Relación con las precipitaciones**

¿Qué relación temporal existe entre las precipitaciones y las variaciones del almacenamiento de agua? ¿Se observan períodos de coincidencia o posibles retrasos entre ambas variables?

**Diferencias territoriales**

¿Qué diferencias presentan las áreas seleccionadas? ¿Cómo deben interpretarse considerando las características de cada cuenca y la resolución de los datos?

**Actividad minera**

¿Qué información verificable existe sobre la ubicación y las etapas de los proyectos, los volúmenes de extracción de agua y los monitoreos ambientales? ¿Qué posibilidades y limitaciones existen para contrastar esos registros con los cambios hídricos?

**Comunidades y ecosistemas**

¿Qué información documentada existe sobre los usos locales del agua, las preocupaciones comunitarias y los ecosistemas dependientes de los recursos hídricos? ¿Qué aspectos requieren mayor monitoreo?

## 6. Alcance geográfico y temporal

El estudio se limitará a áreas seleccionadas de las provincias argentinas de Jujuy, Salta y Catamarca, en el sector correspondiente al Triángulo del Litio. La delimitación definitiva del área de estudio se establecerá considerando la ubicación de los salares y sus cuencas hidrográficas, la localización de los proyectos mineros y la disponibilidad y resolución espacial de los datos. Para ello, se priorizarán las características hidrográficas e hidrogeológicas del territorio, dado que la distribución de las cuencas y los sistemas de agua subterránea no necesariamente coincide con las divisiones políticas entre provincias.

El período de análisis se definirá una vez verificadas la cobertura temporal, la calidad, la continuidad y la comparabilidad de las fuentes de información disponibles.

El análisis se circunscribirá al territorio argentino y no incluirá áreas de Chile ni de Bolivia, aunque algunos sistemas hidrográficos e hidrogeológicos del área de estudio puedan extenderse más allá de las fronteras nacionales. Esta delimitación se considerará al interpretar los resultados, reconociendo que los procesos hídricos pueden estar vinculados con territorios que exceden el área analizada.


## 7. Fuentes de datos abiertas previstas

### NASA GRACE y GRACE-FO

Datos satelitales que permiten estudiar anomalías del almacenamiento terrestre total de agua a escala regional.

Fuente: https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4

### CHIRPS

Estimaciones históricas de precipitaciones que permiten analizar su distribución temporal y espacial.

Fuente: https://www.chc.ucsb.edu/data/chirps

### Fuentes hidrogeológicas y ambientales

Se buscarán datos publicados por organismos científicos, universidades y organismos públicos argentinos, incluyendo mediciones piezométricas, estudios de acuíferos, información sobre calidad del agua y monitoreos ambientales.

### Registros de actividad minera

Se relevarán fuentes oficiales sobre proyectos, etapas de desarrollo, evaluaciones de impacto ambiental y volúmenes de extracción, siempre que los datos estén publicados y puedan verificarse.

Como referencias geográficas iniciales se consultarán el Servicio Geológico Minero Argentino (SEGEMAR) y el Servicio Geológico de Estados Unidos (USGS).

- SEGEMAR: https://cdgam.segemar.gob.ar/DataMappingTools/Litio-NOA/
- USGS: https://www.usgs.gov/data/lithium-occurrences-and-processing-facilities-argentina-and-salars-lithium-triangle-central

### Documentación social y comunitaria

Se considerarán informes públicos, investigaciones académicas y documentación de organismos de derechos humanos relacionada con los usos del agua, las preocupaciones territoriales y la participación comunitaria.

Cada fuente utilizada deberá registrarse con su institución responsable, enlace, fecha de consulta, período, cobertura espacial, variables, unidades y limitaciones.

## 8. Metodología

El trabajo se organizará en las siguientes etapas:

1. **Documentación:** identificación, clasificación y evaluación de las fuentes disponibles.
2. **Delimitación:** selección justificada de las áreas de estudio.
3. **Adquisición:** descarga de datos abiertos y registro de sus metadatos.
4. **Validación:** revisión de formatos, unidades, cobertura temporal, valores faltantes y consistencia.
5. **Preparación:** generación de copias de trabajo, conservando los datos originales sin modificaciones.
6. **Análisis temporal:** cálculo y examen de tendencias, anomalías y variaciones de las variables seleccionadas.
7. **Análisis comparativo:** exploración de las relaciones entre almacenamiento de agua y precipitaciones, considerando posibles desfases temporales.
8. **Contextualización:** incorporación de información hidrogeológica, ambiental, minera y social cuando sea verificable.
9. **Evaluación de incertidumbre:** identificación de limitaciones, explicaciones alternativas y vacíos de información.
10. **Exploración interactiva:** desarrollo y evaluación de una aplicación que permita examinar los datos mediante filtros y controles seleccionados por la persona usuaria.
11. **Documentación de resultados:** presentación de hallazgos, limitaciones y preguntas que requieren estudios adicionales.

Los análisis se implementarán en Python. Las bibliotecas definitivas se seleccionarán según los formatos de las fuentes y las necesidades de exploración temporal y geoespacial.

## 9. Diseño de la exploración interactiva

La visualización será concebida como una herramienta de exploración de datos, no solamente como una presentación de resultados.

Se prevé incorporar las siguientes funcionalidades, sujetas a la disponibilidad y validación de las fuentes:

- **Selección geográfica:** elección de áreas de estudio claramente delimitadas y documentadas.
- **Filtros temporales:** selección de períodos de inicio y finalización.
- **Selección de variables:** exploración diferenciada de las variables hídricas y climáticas disponibles.
- **Comparación temporal:** examen de series y anomalías entre períodos o áreas compatibles.
- **Exploración de precipitaciones:** comparación con variables de almacenamiento utilizando períodos y escalas consistentes.
- **Consulta de fuentes:** acceso a la procedencia de los datos, sus unidades y sus limitaciones.
- **Contexto ambiental y minero:** consulta de registros documentados cuando su cobertura y calidad permitan incorporarlos.
- **Información metodológica:** explicación de qué representa cada variable y qué conclusiones no pueden obtenerse a partir de ella.

La implementación podrá utilizar herramientas de Python para aplicaciones interactivas y gráficos exploratorios. La selección final dependerá de las necesidades técnicas, la reproducibilidad y la posibilidad de ofrecer una experiencia clara para el público destinatario.

La interfaz deberá facilitar la lectura, evitar sobrecargas visuales, diferenciar variables y unidades, identificar datos faltantes y comunicar la incertidumbre sin inducir interpretaciones causales no demostradas.

## 10. Uso responsable de herramientas digitales e inteligencia artificial

El proyecto respetará las restricciones de las bases del concurso sobre inteligencia artificial generativa.

La selección de las variables, la interpretación de los resultados, las decisiones de diseño y la elaboración de la visualización final serán responsabilidad de la autora.

No se utilizarán herramientas de IA generativa para crear automáticamente los gráficos, mapas, diagramas, infografías o figuras finales, ni para sustituir el trabajo creativo que corresponde a la autora.

La programación, la exploración de datos y la representación visual se desarrollarán mediante herramientas convencionales de análisis y visualización en Python. Los resultados deberán poder vincularse con datos identificables, transformaciones documentadas y decisiones metodológicas explícitas.

Cualquier uso de herramientas digitales o asistencia que deba declararse según las bases se documentará con transparencia. Antes de la presentación se verificará que el procedimiento completo cumpla con las condiciones del concurso.

## 11. Criterios científicos y límites de interpretación

GRACE y GRACE-FO estiman anomalías del almacenamiento terrestre total de agua. No miden directamente la profundidad del agua en un pozo ni permiten separar por sí solos todos los componentes del almacenamiento.

Su resolución espacial limita la posibilidad de identificar cambios atribuibles a un salar pequeño, un proyecto minero o una captación individual. Por lo tanto, sus resultados se utilizarán como contexto regional y no como prueba directa de un impacto local.

Las precipitaciones son una variable importante, pero no explican por sí solas la dinámica del agua subterránea. La geología, la recarga, la evaporación, los intercambios entre unidades hidrogeológicas y las extracciones también pueden intervenir.

Una asociación estadística o coincidencia temporal entre actividad minera y variaciones hídricas no demuestra causalidad. Evaluar una posible relación requiere información local comparable, antecedentes hidrogeológicos, datos de extracción y consideración de otras explicaciones.

La ausencia de datos públicos no se interpretará como evidencia de ausencia de impacto.

Se distinguirá entre observaciones, estimaciones, asociaciones estadísticas, hipótesis y conclusiones respaldadas por evidencia suficiente.

## 12. Relevancia y utilidad potencial

La herramienta busca facilitar el acceso y la exploración de información hídrica y climática, hacer visibles sus limitaciones y ayudar a formular preguntas mejor fundamentadas.

Para las comunidades locales, podría contribuir a identificar cuestiones que requieren mayor investigación, sin reemplazar las mediciones locales, la participación comunitaria ni el conocimiento del territorio.

Para equipos científicos y organismos públicos, podría ofrecer un punto de partida para explorar tendencias regionales y detectar necesidades de monitoreo.

Para la gestión ambiental y la sociedad civil, podría facilitar la consulta de fuentes y la comprensión de un problema complejo, distinguiendo los datos disponibles de las interpretaciones que todavía necesitan evidencia adicional.

Estos usos potenciales no equivalen a una validación de impactos concretos ni a una evaluación definitiva de la sostenibilidad de un proyecto minero.

## 13. Organización del repositorio

```text
proyecto_agua_triangulo_litio/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── grace/
│   │   ├── chirps/
│   │   └── contexto_minero/
│   ├── processed/
│   └── metadata/
├── docs/
│   ├── marco_conceptual.md
│   ├── fuentes.md
│   ├── metodologia.md
│   └── criterios_de_evidencia.md
├── notebooks/
└── outputs/
    ├── graficos/
    ├── mapas/
    └── informes/
```

Los datos originales se conservarán sin modificaciones. Los archivos procesados deberán poder vincularse con sus fuentes y con los procedimientos utilizados para prepararlos.

Los archivos de gran tamaño no se incorporarán al repositorio sin evaluar previamente las condiciones de distribución y almacenamiento. Cuando corresponda, se documentarán los enlaces y los pasos necesarios para obtenerlos.

## 14. Resultados esperados

- Inventario documentado de fuentes hídricas, climáticas, hidrogeológicas y mineras.
- Delimitación justificada de las áreas de estudio.
- Series temporales validadas de las variables disponibles.
- Una herramienta interactiva de exploración de datos desarrollada en Python.
- Comparaciones temporales y espaciales sustentadas en fuentes identificables.
- Documentación metodológica reproducible.
- Identificación de tendencias, incertidumbres y vacíos de información.
- Informe final que diferencie los hallazgos respaldados de las hipótesis y preguntas abiertas.

Estos resultados son objetivos de trabajo. No representan hallazgos ya obtenidos ni anticipan conclusiones sobre la evolución del agua o la influencia de la actividad minera.

## 15. Principios de trabajo

- Priorizar la protección del agua, las comunidades y los ecosistemas.
- Trabajar con fuentes abiertas y documentar su procedencia.
- Preservar los archivos originales.
- Distinguir evidencia, hipótesis e interpretación.
- No atribuir causalidad sin evidencia suficiente.
- Reconocer la incertidumbre y las limitaciones de escala.
- Evitar que la ausencia de datos se interprete como ausencia de problemas.
- Favorecer la transparencia, la reproducibilidad y la comprensión pública.
- Respetar las condiciones de autoría y uso de herramientas establecidas por el concurso.

## 16. Referencias iniciales

1. NASA/JPL. GRACE y GRACE-FO, producto de anomalías del almacenamiento terrestre de agua. https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4
2. Climate Hazards Center. CHIRPS Precipitation Data. https://www.chc.ucsb.edu/data/chirps
3. Servicio Geológico Minero Argentino (SEGEMAR). Herramienta cartográfica sobre litio en el NOA. https://cdgam.segemar.gob.ar/DataMappingTools/Litio-NOA/
4. U.S. Geological Survey (USGS). Lithium occurrences and processing facilities, Argentina and salars of the Lithium Triangle, Central Andes. https://www.usgs.gov/data/lithium-occurrences-and-processing-facilities-argentina-and-salars-lithium-triangle-central
5. Naciones Unidas. Comité de Derechos Económicos, Sociales y Culturales. Observaciones sobre Argentina, documento E/C.12/ARG/CO/3. https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=QRsgmTKuCuMzIqAWy6Jj0jd2r%2Bf%2FHoqEs0EAuiXRFThNcflwLcFXtgX6%2BQx%2B0oA2EHiSJMmJuN055QdQmIVJNg%3D%3D

Las referencias se ampliarán y verificarán durante la etapa de documentación. La bibliografía definitiva incluirá únicamente las fuentes efectivamente consultadas y utilizadas.

## Estado del proyecto

**Fase 1 — Documentación, delimitación y diseño metodológico.**

Actualmente se está organizando la estructura del proyecto y el inventario inicial de fuentes. La delimitación geográfica definitiva, la validación de los datos, la implementación de la aplicación y el análisis de resultados son etapas pendientes.

No se han establecido conclusiones sobre la evolución del almacenamiento de agua ni sobre posibles efectos de la actividad minera.
