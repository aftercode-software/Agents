# Funcionalidades y tareas preparadas para estimar

## Del proceso al listado

Partir de las fuentes disponibles y del alcance acordado, no de una lista genérica de módulos. Para cada proceso, recorrer actor, disparador, pasos, reglas, datos, estados, resultado y excepciones materiales. Identificar las capacidades necesarias para completar ese recorrido.

- Conservar los IDs de requisitos existentes. Vincular cada funcionalidad con su fuente: documento/sección, código inspeccionado o declaración concreta del usuario.
- Separar necesidad confirmada de solución propuesta. Un requisito deducido para completar un flujo debe figurar como supuesto o propuesto hasta validarlo; no incluirlo silenciosamente en la primera versión.
- Usar historias de usuario cuando ayuden: “Como [actor], quiero [capacidad] para [resultado]”. No forzar ese formato para infraestructura, migraciones o tareas técnicas.
- Dividir módulos amplios en resultados verificables. “Gestión de usuarios” no es una unidad estimable si mezcla altas, edición, permisos e invitaciones; relevar cuáles se necesitan, sin agregar todas por defecto.
- Desglosar una funcionalidad cuando mezcle responsabilidades, dependencias, incertidumbres o criterios de aceptación distintos. Detenerse cuando cada tarea tenga un resultado comprobable y un frente claro; no convertir el relevamiento en una lista de archivos o funciones de código.

Mantener una funcionalidad de negocio como agrupador cuando se divide en tareas. Usar IDs hijos estables, por ejemplo `RF-03-T01`, y conservar el enlace al requisito. No estimar a la vez el agrupador y sus tareas. Cuando una funcionalidad sea pequeña, una sola fila puede ser la unidad estimable.

## Información por funcionalidad

Registrar en `FUNCIONALIDADES.md`, o en conversación si ese es el formato solicitado:

- ID, módulo y nombre; actor/necesidad o historia de usuario.
- Fuente y estado del alcance: confirmado, observado, supuesto, propuesto o pendiente. Lo observado en código no implica que deba reconstruirse.
- Prioridad, etapa inicial/futura/excluida, inclusión acordada y límites.
- Comportamiento esperado, reglas y excepciones relevantes.
- Criterios de aceptación observables: resultado, validaciones, permisos y errores cuando correspondan. Si se proponen criterios aún no acordados, identificarlos como propuestos.
- Tareas necesarias y reutilización prevista, con dependencias y decisiones que afectan su estimación.

Para cada unidad estimable, indicar ID/padre, resultado verificable, frente y motivo, complejidad y motivo, incertidumbre y motivo, dependencias y estado para estimar (listo, condicionado o bloqueado). Heredar fuente, etapa y estado del padre salvo diferencias explícitas. Distinguir la aceptación técnica de la tarea del resultado de negocio de la funcionalidad.

Una tabla resumen puede usar: `ID | Funcionalidad/tarea | Frente y motivo | Complejidad y motivo | Incertidumbre/pendiente | Dependencias | Estado para estimar`. Poner criterios y fuentes en fichas breves cuando una tabla extensa perjudique la lectura. No omitirlos por simplificar la presentación.

Cuando el desglose vaya a alimentar horas y costos, aplicar [estimabilidad.md](estimabilidad.md): tipo de trabajo, tamaño observable, superficie web/mobile, reutilización comprobada, cobertura de entrega y contexto del equipo. Estas evidencias permiten estimar después; no requieren asignar horas durante el relevamiento.

## Frontend, backend o ambas

Clasificar el **trabajo requerido**, no todas las capas por las que pasa una funcionalidad. Basarse en la arquitectura acordada y, para sistemas existentes, en evidencia de lo que ya está implementado. Sin acceso al repositorio o contrato de una API, indicar que la clasificación es provisional y qué hay que verificar.

| Frente | Cuándo corresponde |
| --- | --- |
| Frontend | Cambios solo en interfaz/cliente: presentación, interacción, navegación, accesibilidad, estado local o consumo de contratos existentes suficientes. |
| Backend | Cambios solo en servicios: API, reglas autoritativas, persistencia, permisos de servidor, procesos, integraciones o configuración server-side. |
| Ambas | Hay trabajo necesario en cliente y servidor. Explicar cada parte y separar las tareas frontend/backend y su contrato compartido cuando sea posible. |
| Otro: [disciplina] | Trabajo que no encaja en esas capas: UX/diseño, infraestructura/DevOps, migración operativa, QA transversal o documentación. Nombrar la disciplina; no esconderlo en backend. |
| Por definir | No hay evidencia suficiente para asignar el frente. Registrar la pregunta o comprobación que lo resuelve; no usar “ambas” como comodín. |

Una dependencia de backend no implica desarrollar backend. Por ejemplo, un filtro visual sobre datos ya cargados puede ser solo frontend; si requiere nueva búsqueda paginada de servidor, cambia el desglose. Un webhook sin nueva pantalla puede ser solo backend.

Ocultar un botón no implementa autorización: verificar qué control de servidor existe. Tampoco asumir backend nuevo para un formulario si un servicio o CMS ya cubre el envío; registrar la reutilización y el trabajo de configuración que realmente haga falta. Aplicar el mismo criterio a servicios gestionados/BaaS: reglas, esquema o funciones nuevas siguen siendo trabajo backend aunque no haya un servidor propio.

Si una funcionalidad mezcla frontend, backend y otras disciplinas, conservar “ambas” para sus capas e identificar además las tareas de las otras disciplinas. Las tareas transversales no desaparecen por usar esa etiqueta. No repartir automáticamente el esfuerzo 50/50.

## Complejidad e incertidumbre

Evaluar ambas por separado para cada unidad estimable, de forma relativa al proyecto y a las capacidades conocidas del equipo:

- **Complejidad baja:** comportamiento acotado, pocas reglas y un patrón conocido/reutilizable.
- **Complejidad media:** varias reglas, estados o dependencias conocidas que necesitan coordinación.
- **Complejidad alta:** interacción significativa entre reglas, concurrencia, sincronización, migración delicada o exigencias no funcionales que afectan el diseño.
- **Por definir:** falta información que impide incluso una clasificación preliminar. También se puede indicar una complejidad provisional bajo un supuesto explícito.

Justificar con factores del caso, no solo con la etiqueta o con la cantidad de pantallas. No convertir estos niveles en horas, story points, porcentajes ni multiplicadores automáticos; el presupuesto calibra el esfuerzo posteriormente.

Indicar incertidumbre baja, media o alta con la evidencia disponible, la duda concreta y su efecto. Una tarea puede ser simple con alta incertidumbre por una API desconocida, o compleja pero bien definida. Las dudas bloqueantes necesitan una validación o decisión específica; no resolverlas subiendo arbitrariamente la complejidad.

## Cobertura y esfuerzo compartido

Antes de cerrar, contrastar el listado contra cada proceso y requisito en alcance:

- ¿Cada necesidad confirmada tiene una funcionalidad/criterio asociado, o una exclusión o pendiente explícito?
- ¿El recorrido contempla estados vacíos, errores, permisos, datos e integraciones relevantes, además del camino feliz?
- ¿Hay preparación, pruebas, integración entre capas, despliegue o migración necesarios para entregar ese alcance? Señalarlos cuando apliquen, no agregarlos todos por costumbre.
- ¿Qué se reutiliza y qué se modifica? Lo existente no es trabajo nuevo; su validación o adaptación sí puede serlo.
- ¿Hay tareas duplicadas o dependencias circulares, y funciones futuras mezcladas con la primera versión?

Registrar los trabajos compartidos una sola vez (por ejemplo `TR-01`) y referenciarlos desde las funcionalidades que los necesitan. Diferenciar pruebas propias de una tarea de QA/integración transversal para evitar doble conteo. No sumar agrupadores, ni multiplicar infraestructura o configuración común por cada funcionalidad.

Cerrar con faltantes concretos y su impacto en la estimación, no con una promesa de exhaustividad. Si una decisión abierta impide descomponer una parte, conservar el agrupador como bloqueado con la validación necesaria; avanzar con las partes independientes. Actualizar clasificación y complejidad si cambia el alcance o la arquitectura, conservando la trazabilidad.
