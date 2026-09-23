# Entregables y traspaso a presupuestos

## Ubicación y estado

Usar la carpeta del proyecto o cliente indicada por el usuario. Si ya existe material, mantener esa carpeta como fuente; evitar duplicarlo entre Relevamiento y Presupuestos.

Si se solicita un relevamiento documentado sin ruta, crear una carpeta con el nombre del proyecto dentro del directorio de trabajo, informar la ruta y reutilizarla al continuar. Si no se conoce la identidad del proyecto, trabajar en conversación hasta poder identificarla. Si el usuario solo pide análisis en conversación o indica solo lectura, responder allí.

Antes de actualizar, leer los archivos existentes. Conservar información aprobada y contenido ajeno al cambio. No sobrescribir un presupuesto comercial existente al completar el relevamiento.

Los documentos deben indicar proyecto, fecha de actualización y estado. Identificar las fuentes junto a los hechos que respaldan, usando rutas o enlaces concretos. El borrador puede tener pendientes explícitos; no confundir un encabezado completo con una decisión resuelta.

## RELEVAMIENTO.md

Documento de contexto y descubrimiento:

- Problema, objetivo y señal de éxito.
- Usuarios, actores y proceso actual, con ejemplos y excepciones relevantes.
- Restricciones y evidencia disponible.
- Supuestos, contradicciones, pendientes y validaciones necesarias.
- Enlace al alcance canónico en `FUNCIONALIDADES.md`.
- Contexto del equipo, antecedentes y cifras aportadas con naturaleza, granularidad y límites de evidencia según [estimabilidad.md](estimabilidad.md). Separar la fuente de alcance de las fuentes de horas, costos y condiciones comerciales.
- Bloque de traspaso versionado según [traspaso-presupuestos.md](traspaso-presupuestos.md), al preparar la entrega a presupuestos. No crear otro archivo para repetirlo.

## FUNCIONALIDADES.md

Fuente del alcance que consume el agente de presupuestos:

- Cliente/proyecto y tipo: `Pagina web basica` o `Sistema complejo`; usar pendiente si faltan datos para clasificar.
- Objetivo y resumen del problema.
- Alcance incluido, exclusiones y evolución fuera del alcance inicial.
- Módulos y funcionalidades o historias de usuario con identificadores, fuentes y criterios de aceptación.
- Desglose en tareas estimables, frente de trabajo (frontend, backend, ambas, otro o por definir), justificación y dependencias.
- Complejidad preliminar e incertidumbre separadas, con motivos y validaciones pendientes.
- Factores que permiten estimar cada unidad: tipo/tamaño del trabajo, reutilización, superficie y cobertura de entrega, heredando contexto común sin duplicarlo.
- Trabajos transversales identificados una sola vez y revisión de cobertura del alcance.
- Roles, permisos, integraciones y requisitos no funcionales relevantes.
- Supuestos, dependencias y decisiones pendientes.

Mantener identificadores y estados de los requisitos. No copiar aquí toda la investigación técnica: enlazar la decisión que impone una dependencia. Una función propuesta no debe figurar como incluida y confirmada.

Aplicar [funcionalidades.md](funcionalidades.md) para el detalle y la clasificación. Conservar los IDs existentes al ampliar un relevamiento; no crear un backlog separado que compita con este documento.

## ARQUITECTURA.md

- Requisitos y restricciones que determinan la solución.
- Alternativas comparadas y enfoque recomendado.
- Componentes, datos, integraciones e infraestructura inicial.
- Decisiones con estado, razones, consecuencias y fuentes.
- Evolución por señales y pruebas de viabilidad pendientes.
- Enlace a los escenarios de operación.

Si una decisión bloqueante sigue abierta, documentar las alternativas; no presentar la arquitectura como aprobada.

## COSTOS_OPERATIVOS.md

- Escenarios y supuestos de consumo.
- Componentes, unidades, planes, fórmulas y subtotales.
- Costos únicos y recurrentes, moneda y tratamiento de impuestos.
- Fuentes de precios, fechas de consulta y límites relevantes.
- Totales o subtotales conocidos, rubros pendientes y sensibilidad al crecimiento.
- Responsable de pago/operación cuando esté definido.

Aplicar [costos-operativos.md](costos-operativos.md). No incluir márgenes de venta ni convertir este documento en una cotización.

## Tamaño del paquete

En un relevamiento completo, producir los cuatro archivos con contenido proporcional al proyecto. Para una consulta parcial, crear o actualizar solo lo solicitado. Mantener cada hecho en su documento canónico y enlazarlo desde los demás.

## Listo para estimar

Clasificar el traspaso y explicar el motivo:

- **Listo para estimar:** alcance inicial suficientemente definido, criterios verificables y dependencias conocidas.
- **Estimación condicionada:** supuestos explícitos permiten rangos o alternativas, con impacto identificado.
- **Bloqueado para estimación confiable:** falta una decisión que cambia materialmente la solución, por ejemplo una integración sin acceso o una regla offline no definida.

No exigir precisión absoluta para empezar a estimar. Identificar los bloqueos por módulo cuando el resto del alcance pueda avanzar.

Si el usuario pide continuar con presupuesto, usar `aftercode-presupuesto-integral` si está disponible y pasar el estado, versión/fecha del alcance, decisiones aceptadas y pendientes, junto con las rutas exactas de los documentos existentes. Si no se generaron documentos, entregar ese mismo contenido en la conversación, sin inventar rutas ni crear archivos por el solo hecho del traspaso. Si la skill de presupuestos no está disponible, entregar ese paquete para su uso posterior.

El presupuestador debe reutilizar el alcance y preguntar solo por vacíos o cambios materiales; conserva la responsabilidad sobre horas y condiciones comerciales. Los costos operativos se presentan aparte del precio de construcción, con las fuentes y supuestos que los sostienen.

Entregar el desglose por ID y frente, las dependencias, la complejidad justificada y las incertidumbres. Señalar qué filas son agrupadores y cuáles son unidades estimables para no sumar padres e hijos, ni repetir trabajos compartidos. La complejidad no equivale a horas: el presupuestador debe calibrar el esfuerzo según alcance, evidencia y equipo.

Aplicar el contrato [traspaso-presupuestos.md](traspaso-presupuestos.md) también al recibir preguntas de presupuestos. Conservar fuentes elegidas y modo de horas; un cambio de alcance puede dejar una estimación anterior pendiente de revisión, pero no autoriza a cambiar los valores aportados. Esta integración es documental y de instrucciones, no una ejecución automática entre agentes.
