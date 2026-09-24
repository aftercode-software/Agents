# Etrack Access - alcance funcional del MVP Senado

Actualización: 23/09/2026. Versión 0.2. Tipo: **Sistema complejo acotado** (reglas de presencia, concurrencia, permisos y alertas). Estado: borrador para validación.

Esta es la fuente canónica de alcance del piloto. Fuentes: **S1** = pedido del usuario del 23/09/2026; **S1a** = aclaraciones del mismo día (grupo por responsable y cantidad, sin nómina; ACK = lectura; cualquier operador solicita asistencia); **S2** = [propuesta piloto](</Users/matias/Downloads/Propuesta_Piloto_Senadores_3meses.docx.pdf>), especialmente página 3; **S3** = decisión actual de usar el stack tecnológico de MCD y desplegar la web a cargo del proveedor. «Confirmado» indica necesidad expresada por el usuario, no software ya entregado. Criterios añadidos para hacerla verificable llevan la marca **propuesto**.

## Límites comunes y permisos

Una sola sucursal Senado, máximo cinco compuertas configuradas, aplicación web responsive y dos roles: Operador y Administrador. Una compuerta es el contexto elegido para registrar movimientos; no implica control automático de hardware. Los movimientos se comparten entre puestos con persistencia central. El equipo proveedor construye y despliega frontend, backend y base; Senado accede por enlace web, sin instalar software. La operación online es la hipótesis técnica de este paquete; no se incluye cola ni sincronización offline.

| Acción | Operador | Administrador |
| --- | --- | --- |
| Elegir compuerta habilitada; registrar ingresos y egresos | Sí | Sí, si realiza tarea operativa; criterio propuesto |
| Ver y buscar movimientos del día y alertas | Sí | Sí |
| Solicitar asistencia | Sí, S1a | Por confirmar si también opera como usuario de puesto |
| Dar ACK de lectura | Propuesto: sí | Propuesto: sí |
| Buscar cualquier ingreso abierto y cerrarlo como excepción | Por confirmar | Sí, S1 |
| Métricas, exportación, configuración de compuertas y alertas | No | Sí |
| Gestionar cuentas y permisos | No | Pendiente D-09; como mínimo se requiere aprovisionamiento inicial |

**Modelo mínimo propuesto:** `Usuario` (rol/estado), `Compuerta` (nombre/estado), `Movimiento` (tipo individual/grupo, responsable o persona, cantidad, observaciones, ingreso y posible egreso, compuertas y actores), `Alerta` (tipo, origen, estado/lecturas), `CambioAuditado`. La identidad de integrantes de un grupo no se almacena, según S1a. Los campos definitivos y la zona horaria se validan con la institución.

## Funcionalidades y aceptación

### RF-01 - Acceso y roles

**Incluida, confirmada por S1/S2; prioridad alta.** El usuario autorizado entra con credenciales y accede según su rol. Se requieren cuentas de operador y administrador para la puesta en marcha. Quién crea, suspende y recupera cuentas está pendiente (D-09). **Aceptación propuesta:** una cuenta deshabilitada no opera; un operador no puede llamar acciones administrativas por API ni descargar datos aunque conozca la ruta; la sesión registra actor en cada movimiento.

### RF-02 - Compuertas y contexto activo

**Incluida, confirmada por S1; prioridad alta.** Administración crea/configura hasta cinco puntos de ingreso/egreso; operadores eligen uno activo. **Aceptación propuesta:** no se habilita un sexto punto; solo se puede operar desde uno activo; cada movimiento conserva la compuerta elegida, incluso si luego se renombra o deshabilita. Está pendiente política para desactivar la compuerta usada por un operador (D-09).

### RF-03 - Ingreso individual

**Incluida, S1/S2; prioridad alta.** Formulario con nombre, apellido, documento y observaciones opcionales, más hora/compuerta/operador automáticos. **Aceptación propuesta:** se guardan los datos con una respuesta inequívoca; no se acepta duplicado abierto según la regla de identificación que se apruebe; errores de validación o red no muestran «registrado». Formato documental, menores y casos sin documento pendientes (D-05).

### RF-04 - Ingreso y egreso de grupo

**Incluida, S1/S1a; prioridad alta.** Opción «Grupo», cantidad de personas, observación/motivo y persona responsable. Un único egreso cierra a todos bajo ese responsable; no hay lista de miembros ni salida parcial. **Aceptación propuesta:** cantidad entera positiva; al ingresar un grupo de N, presencia y entradas suman N; al cerrar, presencia resta N y se conserva N en historial. No se admite un segundo egreso. Límite de tamaño, responsable ausente y correcciones pendientes (D-04/D-05).

### RF-05 - Egreso y búsqueda de abiertos

**Incluida, S1; prioridad alta.** Operador identifica un movimiento abierto y marca salida usando su compuerta activa. Administración busca personas abiertas y puede cerrar ingresos antiguos. **Aceptación propuesta:** entrada y salida mantienen compuertas, fechas y actores propios; si dos usuarios intentan cerrar a la vez, solo una salida queda confirmada; la búsqueda del operador no expone datos fuera del circuito permitido. Alcance exacto de búsqueda/corrección del operador pendiente D-09.

### RF-06 - Panel diario compartido

**Incluida, S1; prioridad alta.** Todos los usuarios autorizados ven ingresos y egresos del día de toda la sucursal, con búsqueda. **Aceptación propuesta:** lista y búsqueda reflejan movimientos de todas las compuertas, distinguen individual/grupo y estado, y actualizan la situación tras una operación desde otro puesto dentro de un tiempo acordado. Filtros y latencia objetivo pendientes D-06/D-07.

### RF-07 - Métricas administrativas

**Incluida, S1; prioridad alta.** Sección de administración con personas actualmente dentro, entradas del día, ingresos abiertos de días anteriores y evolución semanal. **Definiciones propuestas:** `dentro = suma de cantidades de movimientos abiertos`; `entraron hoy = suma de cantidades con ingreso en el día local`; `sin salida = movimientos abiertos ingresados antes de hoy`, separados por personas y registros; `ingresos semanales = suma de personas ingresadas por día de la semana local`. **Aceptación propuesta:** un grupo de N aporta N personas y un movimiento; un egreso posterior a medianoche no borra la entrada del día anterior. Zona horaria, inicio de semana y cortes pendientes D-06.

### RF-08 - Exportación administradora

**Incluida, S1/S2; prioridad alta.** Un administrador descarga datos en formato reutilizable. **Variante recomendada para el MVP:** archivo XLSX que se puede abrir en Excel o importar a Sheets; integración directa con una hoja externa queda fuera hasta D-10. **Aceptación propuesta:** el archivo contiene movimientos individuales y grupales, cantidad, responsable, fechas, compuertas, operadores y estado; respeta filtros/periodo acordados, permisos y tratamiento de datos personales. Columnas, anonimización y retención pendientes D-07/D-10.

### RF-09 - Alertas visibles y configuración

**Incluida como objetivo, reglas condicionadas; S1/S1a; prioridad alta.** Administración configura al menos el umbral X de permanencia y parámetros de alertas; la interfaz de operadores y administradores muestra alertas de exceso de tiempo y solicitudes de asistencia. Cualquier operador puede pedir asistencia. ACK significa **confirmación de lectura**. **Aceptación propuesta:** se genera una alerta para un ingreso que supera X estando abierto; su identificación, hora y estado aparecen a los usuarios conectados; un ACK registra quién y cuándo leyó; una asistencia solicitada se muestra a los demás usuarios conectados. Falta definir si ACK es individual o compartido, si se repite la alerta, cómo se cierra, si administración también solicita asistencia y qué ocurre fuera de sesión (D-02/D-03). No se asumen notificaciones externas.

## Hojas de trabajo estimables

Cada `RF-xx` anterior es **agrupador**, no se suma a sus tareas. Las filas `RF-xx-Txx` son unidades estimables; frente provisional porque la arquitectura no está aprobada. `Condicionado` significa que se puede estimar con supuestos expresos; `bloqueado` exige decisión para cifra única. Las pruebas propias de cada tarea se incluyen en su resultado; integración transversal está en `TR`.

| ID | Resultado verificable / frente | Complejidad / incertidumbre y motivo | Dependencia / estado |
| --- | --- | --- | --- |
| RF-01-T01 | Pantallas de acceso, sesión y rutas por rol / **frontend web** | Media / media: estados de sesión y errores; método de credenciales pendiente | Contrato de identidad; condicionado |
| RF-01-T02 | Credenciales, sesión, permisos de servidor y trazabilidad de actor / **backend** | Media / media: esquema de identidad y revocación pendiente | D-09, TR-02; condicionado |
| RF-01-T03 | Alta inicial de cuentas y eventual gestión administrativa / **por definir** | Por definir / alta: provisión técnica o autoservicio admin cambian frente y tamaño; separar interfaz y servicio cuando se resuelva | D-09; bloqueado para cifra única |
| RF-02-T01 | Pantalla de elección y visualización de compuerta activa / **frontend web** | Baja / baja: selector acotado | Contrato RF-02-T02; listo con supuesto online |
| RF-02-T02 | Modelo, límite de cinco y habilitación/deshabilitación / **backend** | Media / media: referencias históricas y cambio concurrente | TR-02, D-09; condicionado |
| RF-02-T03 | Panel administrativo de compuertas / **frontend web** | Baja / media: estados de desactivación pendientes | RF-02-T02; condicionado |
| RF-03-T01 | Formulario individual responsive y validaciones visibles / **frontend web** | Baja / media: reglas de documento sin confirmar | D-05, RF-02; condicionado |
| RF-03-T02 | Alta transaccional, duplicados y metadatos / **backend** | Media / media: criterio de identidad y concurrencia | D-05, TR-02; condicionado |
| RF-04-T01 | Opción grupo, cantidad, motivo y responsable / **frontend web** | Media / baja: variante simple confirmada | RF-03-T01; listo para el flujo normal; excepciones en D-04 |
| RF-04-T02 | Persistencia de cantidad y cierre íntegro del grupo / **backend** | Media / media: reglas de corrección excepcional | RF-03-T02, D-04; condicionado |
| RF-05-T01 | Búsqueda de abiertos y confirmación de salida con compuerta activa / **frontend web** | Media / media: alcance operador/admin | D-09, RF-02; condicionado |
| RF-05-T02 | Cierre único concurrente y búsqueda autorizada, incluidos antiguos / **backend** | Alta / media: carreras y permisos de consulta | RF-03/RF-04, D-09; condicionado |
| RF-06-T01 | Lista diaria, búsqueda y estados de actualización / **frontend web** | Media / media: refresco entre puestos | Contrato RF-06-T02; condicionado |
| RF-06-T02 | Consulta paginable del día y mecanismo de actualización / **backend** | Media / media: volumen/latencia sin medir | D-06/D-07; condicionado |
| RF-07-T01 | Panel de indicadores y serie semanal / **frontend web** | Media / baja: cuatro vistas acotadas | RF-07-T02; listo con definiciones propuestas |
| RF-07-T02 | Consultas de presencia, día, abiertos antiguos y semana contando personas / **backend** | Media / media: zona/cortes sin aprobar | D-06, RF-03/RF-04; condicionado |
| RF-08-T01 | Descarga XLSX y tratamiento de errores / **frontend web** | Baja / baja si se acepta archivo | RF-08-T02; listo bajo XLSX |
| RF-08-T02 | Extracción autorizada y generación de XLSX / **backend** | Media / media: volumen, columnas y retención | D-07/D-10; condicionado |
| RF-09-T01 | Configuración de umbral y reglas permitidas / **frontend web** | Media / alta: campos finales abiertos | D-02/D-03; bloqueado |
| RF-09-T02 | Cálculo persistente de permanencia y creación de alerta única / **backend** | Alta / alta: temporización, reinicios y repetición | D-02/D-03; bloqueado |
| RF-09-T03 | Solicitud de asistencia y bandeja visible a todos / **frontend web** | Media / media: disparador confirmado, estados pendientes | D-02; condicionado |
| RF-09-T04 | Persistencia, difusión, ACK de lectura y cierre / **backend** | Alta / alta: semántica por usuario, entrega concurrente | D-02/D-03; bloqueado |

### Trabajo compartido, contado una sola vez

| ID | Resultado / frente | Complejidad e incertidumbre | Estado |
| --- | --- | --- | --- |
| TR-01 | Confirmar protocolo, formulario, métricas, matriz de permisos y casos de alerta con institución / **análisis/UX** | Media / alta por decisiones D-02 a D-10 | Condicionado a disponibilidad institucional |
| TR-02 | Esquema, contratos, migraciones, autorización común y base de proyecto con NestJS/TypeORM/PostgreSQL / **arquitectura/backend** | Media / media; stack definido, reglas de identidad pendientes | Condicionado a D-05/D-09 |
| TR-03 | Sistema visual responsive y estados vacíos/error/espera compartidos con React/Vite / **UX/frontend web** | Media / baja; stack definido, diseño pendiente | Condicionado a revisión del diseño |
| TR-04 | Ensayos integrados de concurrencia, roles, grupos, métricas, alertas y exportación en escritorio/celular / **QA** | Alta / media; escenarios por definir | Condicionado a D-02/D-06/D-07 |
| TR-05 | Desplegar web, API y base; configurar ambientes, dominio/TLS, secretos, monitoreo, respaldo y restauración probada / **infraestructura/DevOps** | Media / alta; tarea del proveedor confirmada, RPO/RTO, ubicación y hosting pendientes | Condicionado a D-07/D-08 |
| TR-06 | Carga inicial de puntos y usuarios, capacitación breve, aceptación y entrega de procedimientos / **operación/documentación** | Media / media; cantidades y responsables pendientes | Condicionado a D-08/D-09 |
| TR-07 | Soporte del piloto y entrega/exportación final de datos / **operación** | Por definir / alta; tres meses están en S2 pero cobertura/retención sin definir | Bloqueado para dedicación única |

## Cobertura y límites de estimación

El trabajo es de construcción del MVP con el stack confirmado en [ARQUITECTURA.md](ARQUITECTURA.md). Usar las mismas tecnologías que MCD no acredita reutilización de código ni horas ahorradas. Superficie: web responsive en móvil, tableta y escritorio; no app nativa. Las hojas incluyen pruebas propias, y TR-04 cubre flujos integrados. TR-05 incluye el despliegue de la web, API y base a cargo del proveedor, una sola vez. TR-07 corresponde a operación durante el piloto, separada de construcción.

Para estimar una sola variante se deben cerrar D-02/D-03 (alertas), D-04 (excepciones de grupos), D-05 (identificación) y D-09 (cuentas/permisos). D-07/D-08 condicionan infraestructura y soporte. El resto puede recibir estimación condicionada explícita. No hay horas suministradas para este MVP.
