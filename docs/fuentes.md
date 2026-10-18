# Inventario y evaluación de fuentes de datos

## 1. Propósito

Este documento registra las fuentes que se evaluarán para el proyecto **Agua, comunidades y actividad minera en el Triángulo del Litio argentino**.

El inventario permitirá conocer qué mide cada fuente, qué cobertura temporal y espacial ofrece, qué limitaciones presenta y para qué preguntas de investigación puede utilizarse.

La inclusión de una fuente en este documento no significa que sus datos hayan sido descargados, validados o incorporados al análisis.

## 2. Registro de fuentes

### Fuente 01. NASA GRACE y GRACE-FO — almacenamiento terrestre de agua

**Institución responsable:** NASA / Jet Propulsion Laboratory (JPL) / Physical Oceanography Distributed Active Archive Center (PO.DAAC).

**Producto de referencia:** JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height, Release 06.3, Version 04.

**Enlace del producto:**  
https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4

**Catálogo de la versión con filtro CRI:**  
https://data.nasa.gov/dataset/jpl-grace-and-grace-fo-mascon-ocean-ice-and-hydrology-equivalent-water-height-coastal-reso-30063

**Cobertura temporal declarada:** desde abril de 2002 hasta el presente. La fecha de la última observación disponible deberá comprobarse al descargar los datos.

**Frecuencia:** mensual.

**Formato de referencia:** NetCDF.

**Variable principal:** `lwe_thickness`.

**Unidad:** centímetros de espesor equivalente de agua para el producto JPL de referencia.

**Variables complementarias:** tiempo, latitud, longitud e incertidumbre, según el producto seleccionado.

**Qué representa:** anomalías del almacenamiento terrestre total de agua respecto de una referencia temporal. El almacenamiento total puede integrar contribuciones de agua subterránea, humedad del suelo, agua superficial, nieve y otros componentes según las condiciones del territorio.

**Utilidad para la investigación:** examinar la evolución temporal del almacenamiento terrestre de agua a escala regional y comparar sus variaciones con las precipitaciones.

**Limitaciones:**

- No mide directamente la profundidad del agua en pozos individuales.
- No identifica por sí sola la cantidad de agua dulce disponible para consumo humano.
- Su resolución espacial limita el análisis de salares pequeños y captaciones específicas.
- No permite atribuir directamente una variación a la actividad minera.
- La interpretación requiere consultar la documentación técnica, la incertidumbre y las características del producto utilizado.

**Criterio de selección:** se evaluará la utilización de la versión JPL con filtro CRI para el análisis terrestre, documentando la versión exacta, las correcciones y las limitaciones correspondientes. No se mezclarán productos diferentes sin justificar la comparabilidad.

**Estado:** fuente prioritaria identificada; descarga y validación pendientes.

### Fuente 02. CHIRPS — precipitaciones

**Institución responsable:** Climate Hazards Center, University of California, Santa Barbara.

**Portal oficial:**  
https://www.chc.ucsb.edu/data/chirps3

**Cobertura temporal declarada:** desde 1981 hasta fechas recientes, según la versión y el producto.

**Resolución espacial declarada para CHIRPS v3:** 0,05°.

**Variable de interés:** precipitación.

**Frecuencia prevista:** mensual, mediante el producto mensual correspondiente.

**Qué representa:** estimaciones de precipitación obtenidas a partir de información satelital y observaciones de estaciones meteorológicas.

**Utilidad para la investigación:** estudiar la distribución temporal de las precipitaciones, identificar períodos relativamente secos o lluviosos y explorar su relación con las variaciones del almacenamiento terrestre de agua.

**Limitaciones:**

- Es una estimación de precipitación, no una medición directa de la recarga de un acuífero.
- Las precipitaciones no explican por sí solas la dinámica del agua subterránea.
- La cobertura y la calidad de las observaciones pueden variar entre regiones y períodos.
- Debe verificarse si se utiliza un producto preliminar o final.
- No se combinarán versiones distintas sin documentar sus diferencias.

**Criterio de selección:** evaluar CHIRPS v3 mensual como fuente principal de precipitación. Antes del análisis se comprobarán la cobertura temporal, las unidades, los valores faltantes y la compatibilidad con el período disponible de GRACE/GRACE-FO.

**Estado:** fuente prioritaria identificada; descarga y validación pendientes.

### Fuente 03. SEGEMAR — información geológica y minera

**Institución:** Servicio Geológico Minero Argentino.

**Portal cartográfico de referencia:**  
https://cdgam.segemar.gob.ar/DataMappingTools/Litio-NOA/

**Variables de interés:** ubicación de salares, referencias geológicas y otra información territorial disponible en la herramienta.

**Utilidad para la investigación:** apoyar la identificación preliminar de áreas de interés y contextualizar la distribución geográfica de los salares.

**Limitaciones:**

- La información cartográfica no reemplaza la delimitación hidrogeológica de las cuencas.
- La presencia de un salar o de un proyecto no demuestra que exista un impacto hídrico.
- La actualidad, la escala y la disponibilidad para descarga de cada capa deberán verificarse.

**Estado:** fuente cartográfica candidata; capas y metadatos pendientes de revisión.

### Fuente 04. USGS — referencias geográficas sobre litio y salares

**Institución:** United States Geological Survey.

**Recurso:** Lithium occurrences and processing facilities, Argentina and salars of the Lithium Triangle, Central Andes.

**Enlace:**  
https://www.usgs.gov/data/lithium-occurrences-and-processing-facilities-argentina-and-salars-lithium-triangle-central

**Utilidad para la investigación:** utilizar como referencia complementaria para contextualizar la ubicación de salares y ocurrencias de litio.

**Limitaciones:**

- No se asumirá que el inventario representa el estado actual de todos los proyectos.
- La ubicación de una ocurrencia mineral no equivale a una explotación activa.
- No sustituye los registros oficiales de extracción de agua ni los monitoreos ambientales locales.

**Estado:** referencia complementaria identificada; actualización y cobertura por verificar.

### Fuente 05. Información hidrogeológica y ambiental local

**Fuentes por identificar:** organismos públicos argentinos, universidades, instituciones científicas, estudios hidrogeológicos e informes ambientales accesibles públicamente.

**Variables de interés, según disponibilidad:**

- Niveles piezométricos y evolución temporal.
- Caudales y características de las captaciones.
- Calidad del agua.
- Información sobre recarga y características de los acuíferos.
- Monitoreos de agua superficial y subterránea.
- Informes de impacto ambiental y datos de extracción publicados.

**Utilidad para la investigación:** complementar la perspectiva regional de los satélites con información local necesaria para estudiar posibles cambios en acuíferos y evaluar hipótesis relacionadas con la actividad minera.

**Limitaciones:** las mediciones pueden tener diferentes frecuencias, unidades, métodos, períodos y condiciones de acceso. Su comparabilidad deberá evaluarse antes de combinarlas.

**Estado:** búsqueda documental pendiente.

### Fuente 06. Documentación social y comunitaria

**Fuentes por identificar:** informes públicos, investigaciones académicas, documentación de organismos de derechos humanos y materiales comunitarios de acceso verificable.

**Temas de interés:** usos del agua, abastecimiento, medios de vida, preocupaciones territoriales, participación comunitaria y ecosistemas dependientes del agua.

**Utilidad para la investigación:** contextualizar la relevancia social del problema y documentar cuestiones que requieran estudios o monitoreos adicionales.

**Limitaciones:**

- Las fuentes deberán identificarse según su autoría, fecha, metodología y alcance.
- Los testimonios y las preocupaciones documentadas no se presentarán como mediciones instrumentales.
- Los datos satelitales tampoco se utilizarán para invalidar experiencias o preocupaciones locales.
- Se distinguirán los antecedentes documentales de las conclusiones que pueda respaldar el análisis cuantitativo.

**Estado:** búsqueda y clasificación pendientes.

## 3. Registro de validación

Cada fuente incorporada al análisis deberá contar con un registro que incluya:

| Campo | Descripción |
|---|---|
| ID | Identificador único de la fuente |
| Institución | Organismo responsable |
| Nombre | Nombre del conjunto de datos o documento |
| URL | Enlace de acceso |
| Versión | Versión exacta utilizada |
| Fecha de consulta | Día en que se consultó la fuente |
| Cobertura temporal | Primer y último período disponible |
| Cobertura espacial | Extensión geográfica |
| Variables | Campos utilizados |
| Unidades | Unidades originales y conversiones justificadas |
| Formato | CSV, NetCDF, GeoTIFF, PDF u otro |
| Licencia | Condiciones de uso y redistribución |
| Limitaciones | Incertidumbres y restricciones conocidas |
| Estado | Identificada, descargada, validada o descartada |

## 4. Criterios para aceptar una fuente

Antes de utilizar una fuente se comprobará que:

1. Su origen institucional o autoría pueda identificarse.
2. Exista documentación suficiente para comprender qué representa.
3. Sus unidades y su cobertura temporal sean conocidas.
4. Su cobertura geográfica sea pertinente para el área de estudio.
5. Sus limitaciones puedan documentarse.
6. Sus condiciones de acceso y uso sean compatibles con el proyecto.
7. Los datos puedan vincularse con un procedimiento reproducible.

Una fuente podrá conservarse como referencia contextual aunque no reúna las condiciones necesarias para el análisis cuantitativo.

## 5. Política de conservación de datos

Los archivos descargados se conservarán en `data/raw/` sin modificaciones.

Las transformaciones se realizarán sobre copias de trabajo que se guardarán en `data/processed/`. Los metadatos, las fechas de descarga y los procedimientos aplicados se documentarán de manera separada.

No se reemplazarán los datos faltantes por valores inventados. Cualquier filtrado, conversión de unidades, agregación temporal o selección geográfica deberá quedar documentado.

## 6. Criterio de interpretación

Ninguna fuente aislada se considerará suficiente para demostrar que la actividad minera causó una variación hídrica determinada.

La interpretación combinará, cuando sea posible, datos climáticos, información de almacenamiento de agua, mediciones hidrogeológicas locales, registros de extracción y documentación ambiental y social.

Se distinguirá entre lo que una fuente mide, lo que permite estimar y lo que no puede demostrar.

## 7. Estado del inventario

**Fase actual:** identificación y evaluación preliminar de fuentes.

Las fuentes incluidas son candidatas para el estudio. La selección definitiva dependerá de la validación de sus metadatos, la disponibilidad de datos utilizables y la correspondencia con las áreas de estudio.

Aún no se han producido resultados del análisis hídrico.
