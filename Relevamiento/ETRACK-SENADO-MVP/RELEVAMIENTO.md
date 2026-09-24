# Etrack Access - MVP piloto Senado

Actualización: 23/09/2026. Versión de alcance: 0.2. Estado: borrador para validación; no constituye aprobación institucional ni constancia de implementación.

## Propósito y fuentes

Documentar el **MVP piloto de Etrack Access para Senado**, limitado al registro de ingresos y egresos de personas en una única sucursal durante tres meses. La señal de éxito propuesta es que los puestos autorizados compartan el mismo estado de presencia, puedan cerrar correctamente ingresos individuales y grupales, y que administración consulte y exporte registros verificables. No hay línea de base ni metas de tiempo o precisión acordadas.

Fuentes y prioridad:

1. **S1, alcance actual:** mensaje del usuario del 23/09/2026 que define dos roles, hasta cinco puntos, grupos, salida, panel diario, exportación, métricas y alertas. Es la fuente principal de alcance. La palabra «TBD» deja abiertas las reglas detalladas de alertas, aunque su presencia en la interfaz sí se solicita.
2. **S1a, aclaraciones actuales:** el usuario confirmó el 23/09/2026 que el grupo se registra con responsable y cantidad, sin nómina individual; ACK confirma lectura; cualquier operador puede solicitar asistencia.
3. **S2, propuesta del piloto:** [Propuesta_Piloto_Senadores_3meses.docx.pdf](</Users/matias/Downloads/Propuesta_Piloto_Senadores_3meses.docx.pdf>), páginas 2 a 5. Describe web sin instalación para la institución, campos individuales, acceso por credenciales, exportación reutilizable, cifrado HTTPS/TLS, respaldos, capacitación y soporte durante tres meses, propiedad institucional de los datos y opciones al finalizar. La aclaración actual del usuario establece que **el equipo proveedor desarrolla y despliega la web**; «sin instalación» significa que Senado accede por enlace y no instala software ni aporta servidores.
4. **S3, decisión tecnológica y operativa actual:** aclaración del usuario del 23/09/2026: usar el mismo stack de MCD-Frontend y MCD-Backend y asumir el despliegue de la web. El stack se verificó en los `package.json`, `Dockerfile` y configuración de producción de esos repositorios; los componentes exactos constan en [ARQUITECTURA.md](ARQUITECTURA.md).

El alcance canónico de este piloto está en [FUNCIONALIDADES.md](FUNCIONALIDADES.md). Las alternativas técnicas y el modelo operativo están en [ARQUITECTURA.md](ARQUITECTURA.md) y [COSTOS_OPERATIVOS.md](COSTOS_OPERATIVOS.md).

## Actores y circuito

| Actor | Trabajo confirmado | Límite por validar |
| --- | --- | --- |
| Operador | Selecciona una compuerta activa; registra entradas y salidas; consulta y busca los movimientos del día; ve alertas y puede solicitar asistencia. | Si puede buscar/cerrar ingresos de otros días. |
| Administrador | Incluye el circuito operativo y además configura compuertas y alertas, ve métricas, busca personas para cerrar ingresos y exporta datos. | Quién crea/revoca cuentas y quién autoriza correcciones excepcionales. |
| Responsable de grupo | Persona identificada en el registro que responde por el egreso conjunto. | Documento exigido y procedimiento si falta o cambia el responsable. |
| Institución | Define protocolo, datos, custodia, retención, aceptación y destino de información al terminar el piloto. | Responsable nominal y políticas concretas. |

**Inicio de turno.** El usuario autorizado ingresa a la web y selecciona una de hasta cinco compuertas habilitadas. La selección activa se aplica al siguiente movimiento. El máximo es de puntos configurables, no de personas ni usuarios simultáneos. No se integran molinetes, lectores ni hardware.

**Ingreso individual.** El operador registra nombre, apellido y documento según S2, con observaciones opcionales. La hora, compuerta y usuario se asocian automáticamente. Debe impedirse un segundo ingreso abierto de la misma persona bajo la política de identificación que apruebe la institución.

**Ingreso grupal.** Al marcar «Grupo», se pide cantidad total de personas, responsable y observación o motivo. Se propone un único movimiento grupal que suma esa cantidad al aforo. El grupo sale completo en una sola operación atribuida al responsable; el usuario confirmó que no habrá nómina de integrantes. La gestión de excepciones y el máximo permitido por grupo siguen pendientes.

**Egreso.** Se localiza un ingreso abierto y se cierra con la compuerta activa del usuario que registra la salida. El cierre conserva compuerta y operador de entrada y de salida, y no modifica datos históricos. El administrador puede localizar ingresos abiertos fuera del listado diario para resolver personas que no salieron. Un segundo cierre concurrente debe ser rechazado y mostrado claramente.

**Consulta y administración.** Todos los usuarios ven movimientos de ingreso y egreso del día con búsqueda. Administración ve además presencia actual, entradas de hoy, ingresos aún abiertos de días anteriores y series semanales; puede exportar registros a un archivo Excel reutilizable. Conectar directamente con Google Sheets sería otra variante, no necesaria para satisfacer «Excel o Sheet» si se acepta XLSX.

**Alertas.** El umbral de tiempo dentro y la solicitud de asistencia deben generar avisos visibles para todos los operadores y administradores conectados. Cualquier operador puede pedir asistencia. El usuario definió «ACK» como confirmación de lectura; falta decidir si esa lectura es individual o compartida, quién cierra la alerta, prioridad, repetición, caducidad y tratamiento durante desconexión. El módulo se mantiene en el alcance objetivo, **condicionado** a esas reglas.

## Reglas transversales propuestas

- Usar la zona horaria oficial elegida para la sucursal en los cortes de día y semana; guardar marcas temporales inequívocas. «Hoy» se refiere al día de ingreso o egreso según cada métrica, mientras «dentro» incluye ingresos de fechas anteriores.
- Contar personas, no filas: un ingreso grupal por 8 añade 8 a «entraron» y a «dentro» hasta su egreso conjunto. Conservar aparte cantidad de movimientos. Una discrepancia de cantidad se corrige con una operación auditada, cuyo permiso y protocolo deben aprobarse.
- Aplicar permisos en el servicio y en exportaciones, además de ocultar controles en la interfaz. Registrar actor, fecha, compuerta y resultado de cada operación y cambio administrativo.
- Mostrar estado de conexión y resultado cierto de cada escritura. La propuesta de arquitectura es operación web online; ante fallo de red no se afirma que el movimiento quedó registrado.
- No borrar compuertas ni usuarios históricos de manera que se pierda la trazabilidad; desactivarlos. Resolver antes de desactivar una compuerta seleccionada o con movimientos abiertos.

Son criterios de diseño **propuestos**, salvo lo expresamente indicado en S1 o S2. No son funcionalidades ocultas ya aprobadas.

## Alcance y exclusiones

Incluido en el objetivo del MVP: una sucursal Senado; web responsive; dos roles; hasta cinco compuertas; ingresos y salidas individuales y grupales; panel diario; administración, métricas, exportación y alertas en interfaz según reglas a cerrar. S2 agrega preparación de usuarios, capacitación y soporte durante el piloto, y aclara que ese soporte no incluye nuevas funcionalidades; duración y responsabilidad de ese trabajo deben planificarse por separado de la construcción.

Excluidos de este paquete: controles físicos, geolocalización, aplicación nativa, sincronización offline, nómina individual del grupo, egresos parciales, avisos externos por correo/SMS/WhatsApp, integración directa con Google Sheets, migración histórica y contratación posterior al piloto. Si cualquiera resulta imprescindible, actualizar el alcance por ID antes de estimar.

La propuesta S2 menciona «implementación inmediata» desde un enlace web. Para cumplir el alcance actual, el equipo proveedor debe construir, desplegar y verificar una solución multiusuario antes de habilitarla. Senado utiliza el enlace en sus dispositivos; no instala la aplicación ni administra el servidor. Deben acordarse hitos de desarrollo, pruebas y aceptación antes de prometer una fecha de habilitación. Los tres meses se cuentan desde la habilitación de acceso según S2, no desde este relevamiento.

## Decisiones que cambian el alcance

| ID | Pregunta y estado | Efecto de la respuesta | Validación mínima |
| --- | --- | --- | --- |
| D-01 | **Resuelto por S1a:** grupo solo con responsable y cantidad, sin nómina individual. | Fija modelo de datos y egreso íntegro. | Validar formulario concreto; excepciones siguen en D-04. |
| D-02 | **Parcialmente resuelto por S1a:** ACK = lectura y cualquier operador pide asistencia. Pendiente si ACK es individual o compartido y quién cierra cada alerta. | Cambia estados, historial y pruebas de alertas. | Operaciones define flujo completo con un ejemplo. |
| D-03 | **Pendiente:** plazo X, repetición y fin de alerta de permanencia. | Cambia temporizador, frecuencia, volumen y cierre. | Definir política con caso de ingreso anterior a medianoche. |
| D-04 | **Pendiente:** ¿cómo se tratan salidas individuales/grupales excepcionales, error de cantidad o responsable ausente? | Cambia permisos de corrección y auditoría. | Aprobar protocolo operativo. |
| D-05 | **Pendiente:** formato de documento, datos mínimos, menores/sin documento y duplicados. | Cambia validaciones y riesgo de presencia incorrecta. | Revisar formulario institucional. |
| D-06 | **Pendiente:** zona horaria, comienzo de semana y definición exacta de cada métrica. | Cambia consultas, totales y alertas. | Contrastar ejemplos de cierre diario y semanal. |
| D-07 | **Pendiente:** cantidad de operadores, simultaneidad, volumen diario, retención y ubicación permitida de datos. | Cambia tamaño, proveedor, costos y pruebas de carga. | Informática y operaciones aportan cifras y política. |
| D-08 | **Parcialmente resuelto:** el equipo proveedor despliega y opera la web. Pendiente titularidad de cuentas, respaldo/recuperación, cobertura de soporte y procedimiento de exportación/eliminación final. | Cambia costos y operación, no quién despliega. | Acuerdo con informática y referente institucional. |
| D-09 | **Pendiente:** ¿quién da de alta/baja usuarios y quién puede cerrar un ingreso ajeno o antiguo? | Cambia permisos y pantallas administrativas. | Matriz de permisos firmada por operación. |
| D-10 | **Pendiente:** entrega XLSX suficiente o conexión directa a Sheets. | Una integración autenticada añade trabajo y obligaciones de acceso. | Confirmar formato y muestra de columnas. |

## Estado y traspaso documental

**Estimación condicionada.** Ingresos, salidas, compuertas, panel, métricas, grupos bajo S1a y XLSX pueden estimarse bajo los supuestos explícitos. Las excepciones de grupos (D-04) y reglas pendientes de alertas (D-02/D-03) requieren variantes o decisión previa para una cifra confiable. Los costos de operación son escenarios, no un precio comercial.

| Campo del contrato `relevamiento-presupuestos/v1` | Estado de este paquete |
| --- | --- |
| Proyecto / versión | Etrack Access Senado MVP, alcance 0.2 del 23/09/2026; sin aprobación detallada. |
| Alcance elegido | S1, S1a y S3; S2 define condiciones de la propuesta. [FUNCIONALIDADES.md](FUNCIONALIDADES.md) contiene IDs canónicos. |
| Horas | `pendiente de elección`; no se proporcionaron horas para el MVP. |
| Costos / precio | [COSTOS_OPERATIVOS.md](COSTOS_OPERATIVOS.md) modela operación. No hay precio comercial ni costo de construcción aportado. |
| Unidades | Hojas `RF-xx-Txx` y transversales `TR-xx`; padres `RF-xx` son agrupadores y no se suman. |
| Reutilización | El stack es el de MCD por decisión del usuario; compartir tecnología no implica reutilizar código ni descontar trabajo. |
| Pendientes | D-01 resuelto; D-02 y D-08 parciales; D-03 a D-07, D-09 y D-10 abiertos. |
| Próxima acción | Validar decisiones con la institución y luego solicitar estimación si el usuario lo pide. Este relevamiento no inicia el presupuesto. |

No se asigna plazo de construcción, horas ni ahorro por reutilización sin medirlos. La entrega a presupuestos deberá usar las rutas exactas de los cuatro archivos de esta carpeta.
