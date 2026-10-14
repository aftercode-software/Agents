# Drive y preservación de la plantilla

## Destino

1. Leer los identificadores en [clientes.md](clientes.md). Usar Google Drive para verificar Cuentas y localizar la carpeta del cliente entre sus descendientes. La búsqueda por nombre ayuda, pero comprobar los padres para evitar una cuenta homónima fuera de Cuentas. Continuar la paginación si la búsqueda no está completa.
2. Revisar los informes pertinentes en la carpeta del cliente y sus subcarpetas, identificando por el período del contenido el informe del mes anterior; la fecha de modificación o del nombre de carpeta no basta. No confundir un presupuesto con un informe de mantenimiento.
3. Obtener la fecha actual al ejecutar el trabajo, usando `America/Argentina/Mendoza` como zona de creación salvo indicación distinta del usuario. Crear o reutilizar `Cuentas/<cliente>/AAAA-MM-DD/`. Esta fecha no define el período del informe y no debe quedar fijada a la fecha de creación de la skill.
4. Titular el Google Doc `Informe mensual de mantenimiento — <Cliente> — <Mes Año>`, o conservar el nombre ya elegido por el usuario. Si hay un informe del mismo cliente y período, comprobar si es el trabajo actual, un borrador o una versión entregada. Reutilizar un borrador propio; si hay conflicto real, preguntar si se actualiza o se crea una nueva versión. Evitar duplicados al reintentar una creación incierta: primero buscar y leer el resultado.
5. Crear una copia nativa del documento de ejemplo en la carpeta fechada usando la acción de copia de Drive con `parent_folder`. No crear un documento vacío ni reconstruir la plantilla vía DOCX. El entregable es un Google Doc editable; `.doc` no implica usar Word antiguo ni producir además un PDF para el cliente.

## Forma y estructura observadas

La lectura inicial encontró una pestaña (`t.0`, «Tab 1»), tipografía **Poppins**, pesos 400 y 600 y tamaños explícitos de 10 pt para metadatos, 11 pt para texto y 13/15 pt en algunos títulos. Otros tamaños y propiedades son heredados: leer la referencia completa al ejecutar, sin rellenarlos por suposición.

- Apertura: «Informe Mensual – Mantenimiento Web», cliente, período y servicio; título con rol `HEADING_2` y metadatos destacados.
- «Cambios y mejoras realizadas este período», con trabajos agrupados, títulos de rol `HEADING_3` y listas explicativas.
- «Métricas de uso del sitio» y «Rendimiento general del sitio», con indicadores, observaciones y captura centrada.
- Comparativa de métricas: tabla nativa de cuatro columnas, **Indicador / Período anterior / Período actual / Variación**. Los textos de fechas del ejemplo deben reemplazarse por las bases reales.
- «Adquisición de usuarios y tráfico por canal», con canales, hallazgos y captura.
- «Páginas y contenidos con mayor movimiento», con tabla nativa de dos columnas, **Página / Título de pantalla** y **Visualizaciones**, captura y hallazgos.
- «Comparación con el comportamiento histórico» como cierre analítico.

La tabla comparativa inicial tiene bordes negros de 0,5 pt y padding de 5 pt; la de páginas tiene bordes gris verdoso de 0,75 pt, padding horizontal de 9 pt y vertical de 6 pt. Son firmas observadas, no reglas para uniformar todo el documento. Copiar la geometría y estilos del elemento pertinente; no rediseñar ni normalizar diferencias del ejemplo sin una necesidad concreta. Conservar márgenes, listas, estilos, encabezados, pies y elementos visuales que efectivamente existan. El número de filas, de trabajos y de capturas se adapta a los datos actuales.

Añadir **«Comparación de arreglos con el mes anterior»** después de los trabajos y **«Propuestas de mejora»** al cierre, reutilizando los estilos de títulos, párrafos y tablas del ejemplo. Son extensiones pedidas por el usuario, no motivo para cambiar el diseño. Si no hay mejoras justificadas, decirlo brevemente en vez de inventarlas.

## Adaptación y controles

- Leer la copia completa antes de su primera escritura. Si la skill de Google Docs está disponible, seguir su lectura confiable, preservación de plantilla y referencias de imágenes/QA. Resolver las pestañas, objetos, índices y revisión actuales antes de editar.
- Reemplazar todos los datos y capturas del ejemplo; una captura antigua no puede quedarse por su valor estético. Mantener posiciones y estilos útiles, pero eliminar o sustituir información de Nutriterra al trabajar con otro cliente. Las conclusiones del ejemplo tampoco se heredan para otro mes de Nutriterra.
- No copiar errores del ejemplo: el encabezado abarca hasta el 1 de septiembre, mientras el cuerpo dice agosto completo; otra comparación menciona abril y luego junio-julio. Reemplazar todos esos rótulos por períodos coherentes. Sus porcentajes, explicaciones de bots y afirmaciones de crecimiento no son evidencia del nuevo informe.
- Insertar las capturas aportadas en sus secciones mediante mecanismos disponibles del conector, conservando proporciones y legibilidad. Usar pies con fuente y período cuando aporten contexto. No subirlas a un servicio público para obtener una URL. Si no existe una vía de inserción accesible, informar el faltante y no representar la captura como una imagen insertada.
- Para valores de fecha o enlaces a recursos de Google, respetar los elementos nativos y estilos que requiera la skill de Google Docs vigente.
- Tras editar, volver a leer contenido, tablas, imágenes y estilos. Comprobar que no queden datos o capturas del ejemplo, encabezados huérfanos, tablas desbordadas o texto recortado. Cuando haya exportación y renderizado disponibles, revisar **todas** las páginas del PDF exportado; usarlo para QA sin añadirlo como entregable no solicitado. Si solo se verificó estructura, no afirmar equivalencia visual final.
- Verificar el padre del archivo y la carpeta fechada; devolver los enlaces reales del documento y, cuando sea útil, de su carpeta. Conservar los permisos existentes. No enviar correos ni cambiar compartición por guardar el informe.
