# Etrack Access alcance funcional

Actualización: 22 de septiembre de 2026. Versión 0.4. Tipo: **Sistema complejo**. Estado: estimación condicionada; desglose preparado, sin horas asignadas.

## Base y reglas de lectura

Objetivo: operar accesos de personas, flota y búnker en varios establecimientos y puntos, con credenciales individuales, autogestión institucional y trazabilidad.

Decisiones confirmadas por el usuario el 21/09/2026, fuente S2: desarrollo desde cero y web app exclusivamente online. No incluye funcionamiento offline ni reutilización de código anterior. La institución definirá el nivel de aislamiento del búnker.

Fuente S1: [documento aportado](</Users/matias/Downloads/ETRACK_Puntos_de_partida_para_el_desarrollo_SIN_PRECIOS (1).docx>). Las referencias § remiten a sus secciones. Contexto y pendientes D-01 a D-10: [RELEVAMIENTO.md](RELEVAMIENTO.md).

Fuente S3: solicitud del usuario del 22/09/2026 de completar historias, tareas por disciplina y evidencia para presupuestar, conservando decisiones y valores. El contexto del equipo se registra en D-11. Esta actualización no aprueba las propuestas funcionales anteriores ni genera una estimación de horas.

En los requisitos RF, **C** significa confirmado en el alcance recibido; **P** significa propuesta de ampliación o detalle que requiere acuerdo. Los criterios de aceptación son operacionalizaciones propuestas, incluso cuando el requisito es C. Las prioridades y etapas son una secuencia recomendada, no un recorte aprobado.

Fuente S5: aclaración del usuario del 22/09/2026: mobile está incluido como web responsive para celulares. Diseño, implementación y QA móvil web forman parte del alcance; aplicación nativa y tiendas permanecen excluidas.

## Requisitos incluidos

| ID | Requisito y actor | Fuente y estado | Criterio de aceptación propuesto | Etapa y dependencia |
| --- | --- | --- | --- | --- |
| RF-01 | Administrador autogestiona establecimientos, puntos y módulos | §1 y §3 · C | Crear un predio y punto sin intervención técnica; renombrar o desactivar sin perder movimientos históricos. | Base · D-09 |
| RF-02 | Usuario se autentica antes de seleccionar contexto | §2 y §10 · C | Sin sesión no se enumeran entornos; con sesión aparecen solo los asignados; un contexto único puede abrirse automáticamente. | Base |
| RF-03 | Administrador asigna funciones y permisos | §3 y §9 · C | Otorgar una función en una sede no habilita otra sede o módulo; combinar perfiles solo suma autorizaciones expresas. | Base · D-09 |
| RF-04 | Administrador revoca permisos | §3 y §7.1 · C | Una sesión abierta pierde la capacidad de efectuar nuevas operaciones protegidas al revocarse el permiso; se acuerda y mide el tiempo máximo. | Base · D-09 |
| RF-05 | Operador registra ingreso individual | §4 · C | Registro conserva documento, nombre, minoría de edad, destino de visita, motivo, contexto, hora y operador; obligatorios y excepciones acordados. | Accesos · D-05 |
| RF-06 | Operador consulta presencia y registra salida cruzada | §1.1 y §5 · C | Ingreso en A se cierra desde B autorizado; mantiene datos de entrada y salida; dos cierres simultáneos producen un único cierre válido. | Accesos · D-04 |
| RF-07 | Operador registra grupos | §4 · C | Con el protocolo elegido, se registra grupo y se concilian entradas/salidas sin cantidades negativas ni cierre incompleto inadvertido. | Accesos · D-05 |
| RF-08 | Operador genera alertas e incidencias | §6 · C | Elegir una categoría de S1, prioridad y observación; conservar módulo, punto, hora y autor; no revelar información a otros módulos. | Transversal · D-06 |
| RF-09 | Responsable recibe avisos de alertas | §6 · C, canal pendiente | La alerta llega por el canal acordado al responsable habilitado; un fallo de envío queda identificado y se aplica la contingencia definida. | Transversal · D-06 |
| RF-10 | Administrador y perfiles autorizados consultan tablero e historial | §1.1 y §1.2 · C | Presencia, flota y alertas concuerdan con movimientos; filtrar por sede, punto, fechas, persona o vehículo según módulo y permiso. | Reportes · D-08 |
| RF-11 | Administrador crea búnker sin acceso automático a contenido | §3 y §7.1 · C | Crear/configurar el entorno no permite listar, buscar ni leer sus registros; se exige permiso adicional incluso para administrador. | Búnker · D-03 y D-09 |
| RF-12 | Operador autorizado registra movimientos del búnker | §7 · C | Entradas, salidas, alertas e historial permanecen separados; cerrar solo por puntos permitidos según política acordada. | Búnker · D-03 |
| RF-13 | Auditor autorizado reconstruye consultas y cambios del búnker | §7 y §7.1 · C | Consulta, registro y modificación conservan actor, acción, objeto, fecha y resultado; el operador no puede borrar su rastro. | Búnker · D-03 y D-08 |
| RF-14 | Responsable gestiona unidades institucionales | §8 y §8.1 · C, mantenimiento de catálogo inferido | Registrar número interno, chapa y tipo; asignar alcance; soportar el conjunto inicial de 45 a 50 vehículos sin fijarlo como máximo. | Flota · carga inicial a definir |
| RF-15 | Operador de flota registra salida y retorno | §8 · C | Conservar conductor, acompañantes si corresponden, destino/comisión, motivo, kilómetros, puntos, fechas, horas y observaciones. | Flota · D-04 |
| RF-16 | Responsable consulta situación de flota | §8 y §8.1 · C | Una salida abierta muestra circulación/retorno pendiente; un retorno válido la cierra sin afectar accesos de personas ni búnker. | Flota · D-04 |
| RF-17 | Administrador o auditor consulta actividad general | §3 y §9 · C | Filtrar actividad dentro del alcance concedido; un auditor solo lectura no modifica operaciones ni hereda acceso al búnker. | Transversal · D-08 y D-09 |
| RF-18 | Equipo prepara y habilita la operación | §11 · C | Ejecutar pruebas, configurar usuarios y sedes, capacitar y documentar aceptación de producción e inicio de validación. | Puesta en marcha · D-10 |

## Especificaciones propuestas que requieren acuerdo

| ID | Propuesta | Verificación | Efecto sobre estimación |
| --- | --- | --- | --- |
| RP-01 | Una visita activa por identidad y circuito; reingreso crea otra visita | Intentos duplicados no abren presencias adicionales; reingreso tras cierre conserva el anterior. | Define normalización e identidad; no usar documento como clave global sin tipo/país. |
| RP-02 | Corregir con motivo y responsable, sin sobrescribir silenciosamente | Se conserva valor anterior, nuevo y autor; operaciones erróneas pueden anularse con rastro. | Agrega flujo de supervisión; acordar quién puede corregir. |
| RP-03 | Un viaje abierto por vehículo; kilometraje de retorno no menor al de salida | Dos salidas concurrentes no abren dos viajes; excepciones de odómetro requieren corrección autorizada. | Regla recomendada para RF-15. |
| RP-04 | Segundo factor y sesiones limitadas para búnker y funciones privilegiadas | Probar alta, recuperación, expiración y revocación; recuperación no debe evadir autorización especial. | S1 lo propone considerar; método y obligatoriedad pendientes. |
| RP-05 | Estados de alerta abierta, en atención y resuelta, con acuse | Cada transición conserva actor; notificación enviada no se considera atención. | Seguimiento adicional a la emisión de alertas; no confirmado. |
| RP-06 | Exportación CSV de reportes permitidos | Exportación coincide con filtro y permisos y queda auditada; neutralizar contenido interpretable como fórmula. | S1 confirma reportes, no formato ni descarga; aprobar por separado. |

RP-07, variante de operación offline considerada en la versión 0.1, queda descartada por la decisión S2. No forma parte de la estimación.

## Datos y reglas de negocio

**Identidad y visita son entidades diferentes.** Una persona puede visitar repetidamente. El documento no debe funcionar como identificador de la visita. Propuesta de identificación: tipo, país emisor y número normalizado; si falta documento, aplicar el protocolo pendiente y un identificador interno, sin inventar números oficiales.

**Presencia y punto son conceptos diferentes.** El registro conserva punto de entrada y de salida; la consulta de presencia pertenece al circuito autorizado. Propuesta inicial: cierre cruzado dentro del mismo establecimiento. Los traslados y cierres entre establecimientos están pendientes; no se autorizan por el solo hecho de pertenecer a la misma institución.

**Grupos.** Definir responsable, tipo de grupo, cantidad de adultos y menores si el protocolo lo requiere, destino y reglas de salida. Si se admite salida parcial sin nómina, mostrar cantidades remanentes y evitar afirmar que se identifican todos los presentes. Un acompañante autorizado requiere una regla explícita; marcar “menor” no prueba autorización.

**Flota.** Unidad y viaje tienen identidad propia. “Dentro” requiere una ubicación o estado inicial confiable; la ausencia de una salida cargada no demuestra por sí sola presencia física. “Retorno pendiente” significa viaje abierto; “demorado” requeriría una hora esperada, no incluida expresamente. Traslados, retorno en otro predio y cambios de conductor deben acordarse.

**Alertas.** Conservar las once categorías de S1: médica, seguridad, código rojo, acceso restringido/denegado, persona o vehículo observado, menor sin acompañamiento autorizado, incidente vehicular, situación sospechosa, emergencia/incendio/evacuación, objeto/documentación extraviada y otra incidencia. Prioridades, destinatarios y contenido visible se acuerdan por módulo.

**Correcciones y desactivaciones.** No borrar catálogos referenciados. Si un punto se desactiva con operaciones abiertas, bloquear nuevas aperturas y derivar el cierre a un punto/supervisor autorizado según protocolo. Horas operativas online provenientes del servidor; registrar por separado fecha del hecho y fecha de carga cuando se regularice una contingencia.

## Matriz de permisos propuesta

La autorización combina usuario, institución, establecimiento, módulo, punto y acción. “Según asignación” siempre requiere una concesión explícita. Los nombres de perfiles provienen de S1; los límites de acción siguientes deben validarse.

| Perfil | Configuración | Personas | Flota | Búnker |
| --- | --- | --- | --- | --- |
| Administrador institucional | Sedes, puntos, módulos y usuarios | Consulta según alcance concedido | Consulta según alcance concedido | Configura; no lee por defecto. |
| Supervisor de accesos | Asignaciones solo si se delega | Consulta de sedes; corrección propuesta | Sin acceso automático | No visible. |
| Operador de acceso | Ninguna | Registra en puntos asignados; busca visita activa del circuito permitido | Sin acceso | No visible. |
| Operador de flota | Ninguna | Solo con otro permiso | Registra movimientos de unidades y puntos asignados | No visible. |
| Responsable de flota | Catálogo y asignaciones si se delega | Solo con otro permiso | Consulta y supervisa dentro de su alcance | No visible. |
| Informática | Configuración técnica delegada | Sin lectura implícita | Sin lectura implícita | Configuración y contenido separados. |
| Jefe de seguridad | Concesiones sensibles si se designa | Según asignación | Según asignación | Solo con autorización nominal. |
| Operador de búnker o colaborador autorizado | Ninguna salvo delegación | Según otro permiso | Según otro permiso | Opera dentro de su autorización. |
| Auditor | Ninguna | Lectura autorizada | Lectura autorizada | Lectura con autorización especial. |

La facultad de conceder permisos del búnker no debe permitir autoasignación irrestricta. Autoridad inicial, reemplazos y procedimiento de emergencia quedan pendientes en D-09.

## Requisitos no funcionales

| ID | Necesidad y estado | Criterio propuesto para acordar |
| --- | --- | --- |
| RNF-01 | Confidencialidad · C, S1 §7 y §9 | Probar denegación en pantallas, API, búsquedas, notificaciones, reportes y suscripciones; no enviar datos ocultos al navegador. |
| RNF-02 | Consistencia multipunto · derivado de RF-06 y RF-15 | Operaciones transaccionales e identificadores de reintento; duplicar una solicitud no duplica un ingreso, salida o viaje. |
| RNF-03 | Actualización en tiempo real · C, S1 §1.1 | Acordar segundos máximos y carga de prueba; mostrar pérdida de conexión y evitar presentar información vieja como actual. |
| RNF-04 | Revocación inmediata · C, S1 §3 y §7.1 | Comprobar sesión abierta, nueva petición y canal de actualización; revalidar permisos al reconectar y no operar sin conexión. |
| RNF-05 | Trazabilidad · C, S1 §3 y §7 | Auditoría protegida por permisos propios; consultas del búnker incluidas; retención y revisión pendientes. |
| RNF-06 | Continuidad y recuperación · P | Acordar tiempo de recuperación y pérdida tolerable; restaurar una copia y verificar datos y permisos antes de producción. |
| RNF-07 | Web responsive para escritorio y celulares · C, S5; matriz de compatibilidad pendiente | Todos los flujos incluidos deben poder completarse en navegador móvil y escritorio, con navegación táctil, formularios y tablas adaptados; validar tamaños y navegadores acordados. |
| RNF-08 | Protección de datos · P, política pendiente | Definir campos mínimos, años de conservación, accesos a copias y eliminación/anonimización autorizada según política institucional. |
| RNF-09 | Operación exclusivamente online · C, S2 | Sin conexión, bloquear nuevas operaciones y avisar del estado; ante respuesta perdida, consultar el resultado al reconectar antes de repetir. Sin cola local offline. |

## Casos de aceptación propuestos para validar

Los casos aplican al alcance acordado y a las variantes seleccionadas. Exportación, correcciones, reglas RP y recuperación propuesta conservan su estado pendiente; no se incluyen por aparecer en este listado.

1. Operador A registra entrada y operador B autorizado cierra; C sin permiso no obtiene esa visita ni por URL directa.
2. Dos puestos intentan cerrar simultáneamente; queda un cierre y el otro recibe el estado actualizado.
3. Una respuesta se pierde y se reenvía la operación; no aparece un segundo movimiento.
4. Un administrador configura búnker sin poder leerlo ni asignarse lectura sin la autoridad acordada.
5. Revocar a un usuario conectado bloquea nuevas operaciones y retira sus suscripciones.
6. Un filtro, contador o exportación general no incluye datos ni metadatos del búnker.
7. El grupo sale parcialmente según protocolo; cantidades y estado final concuerdan.
8. La flota rechaza viaje duplicado y resuelve kilometraje inconsistente por el circuito de corrección acordado.
9. Se desactiva un acceso conservando historial y resolviendo movimientos abiertos.
10. Se restaura el respaldo en un entorno de prueba y se verifica consistencia y autorización.
11. Si se corta Internet, no se confirma una operación sin respuesta del servidor; al reconectar se resuelve cualquier resultado incierto sin duplicarlo.

## Límites del alcance recibido

Por decisión expresa del usuario, quedan fuera la operación offline, sincronización de registros locales y ampliación del sistema anterior. Una caída de Internet interrumpe la operación de la web; la institución debe definir un procedimiento manual de contingencia. Esto no elimina pruebas de reintentos y errores de red.

S1 no confirma biometría, cámaras, lectura de patentes, molinetes, barreras, escáner documental, consulta a registros estatales, GPS, combustible, mantenimiento, reservas, facturación, aplicación nativa, publicación en tiendas, inicio de sesión institucional, mensajería externa específica ni migración histórica. No se incluyen automáticamente. Cualquier incorporación se registra como cambio o decisión posterior.

La solución multipredio de una institución no implica un producto SaaS para múltiples clientes con autosuscripción y cobro. El modelo puede conservar identidad institucional para facilitar evolución, sin presupuestar ese producto adicional.

No hay fases funcionales descartadas dentro de los tres módulos. Las variantes propuestas y las ampliaciones anteriores permanecen fuera del compromiso inicial hasta su decisión explícita.

## Cómo consumir el desglose para estimar

Los RF-01 a RF-18 anteriores son **agrupadores de negocio, no sumables**. Sus hijos RF-XX-TXX son unidades de trabajo. RP-01 a RP-06 conservan su estado propuesto; RP-07 continúa excluido. Los RNF son restricciones y criterios transversales: su cobertura se asigna más abajo, sin agregar otra bolsa de horas por cada RNF.

Inventario documental de esta versión: 53 hojas RF, 8 hojas de extensiones RP y 15 trabajos TR. Son 76 registros de trabajo, **no 76 prestaciones aprobadas ni unidades de tamaño equivalente**: incluyen variantes excluyentes, propuestas y pendientes. Por frente hay 30 registros web, 30 backend y 16 de otras disciplinas, contando también esas propuestas; no es una distribución de horas ni un total sumable sin filtrar inclusión.

Cada hijo hereda actor, fuente, estado del alcance y etapa del padre salvo indicación explícita. Todos los criterios de las tareas son **propuestos**. “Listo” significa que el trabajo puede estimarse con su tamaño y límites descritos; no significa implementado, aprobado para producción ni presupuestado. “Condicionado” admite una estimación con el supuesto identificado. “Bloqueado” requiere una decisión material antes de cerrar esa unidad; no bloquea las demás.

**Contexto común de esfuerzo.** La construcción funcional es nueva, sin reutilización del código anterior. En frontend se estima web responsive para escritorio y celulares, incluida por S5. Cada hoja web comprende su adaptación móvil y pruebas propias; no se trata como una segunda aplicación ni como trabajo gratuito. Cliente mobile nativo, tiendas y offline están excluidos, no registrados como horas cero. No hay contratos API existentes comprobados ni componentes reutilizables verificados. Librerías, autenticación administrada y patrones compartidos son opciones de implementación pendientes de D-11/ADR-02, no ahorro medido. El trabajo necesario de reglas, esquema y permisos sigue siendo backend aunque se use BaaS.

Cada hoja incluye implementación, pruebas propias y corrección de sus defectos antes de entrega; registra evidencia de su criterio técnico. Las pruebas de interfaz se cubren en la hoja web y las de reglas/persistencia en la hoja backend. La revisión independiente, integración de recorridos completos, validación de seguridad, carga, coordinación y puesta en marcha tienen propietarios TR únicos. No se suman porcentajes adicionales por estos conceptos.

**Tamaño observable:** cada fila nombra los flujos, entidades y variantes incluidos; no representa un conteo aprobado de pantallas o endpoints. Complejidad e incertidumbre se justifican por separado. La calibración de horas y calendario queda pendiente del equipo, no se deriva de estas etiquetas.

### RF-01 Administración de establecimientos y puntos

Historia: como administrador, quiero habilitar sedes, accesos y módulos para incorporar puestos sin intervención técnica. Tamaño: tres capacidades de configuración con estados activos/inactivos e historial referenciado. Prioridad: base previa a la operación.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-01-T01 | Formulario/listado de sedes: alta y cambio de nombre; errores y estado vacío visibles; no aparentar guardar si falla API | Frontend web: interacción de configuración | Baja: edición acotada | Baja: campos básicos explícitos | TR-03, TR-05; contrato RF-01-T02 | Listo |
| RF-01-T02 | Persistir y consultar sedes dentro de la institución; validar nombre y permiso; mantener identidad al renombrar | Backend: catálogo y aislamiento | Media: referencias históricas y autorización | Baja: jerarquía definida | RF-03-T04, TR-06 | Listo |
| RF-01-T03 | Crear/renombrar/desactivar punto; mostrar sus movimientos pendientes antes de confirmar desactivación | Frontend web: estados de acceso | Media: operaciones abiertas condicionan acción | Media: política de cierre D-09 | RF-01-T01, TR-05; contrato RF-01-T04 | Condicionado: derivación a supervisor propuesta |
| RF-01-T04 | Punto vinculado a sede; bloquear nuevas aperturas al desactivarlo, conservar historial y permitir cierre por circuito autorizado | Backend: integridad del catálogo | Media: desactivación concurrente y dependencias | Media: D-04 y D-09 | RF-01-T02, RF-03-T04, TR-06 | Condicionado: reglas de cierre |
| RF-01-T05 | Selección de módulos habilitados por sede; configuración del búnker sin mostrar su contenido | Frontend web: administración de habilitaciones | Media: separar configuración y operación | Media: metadatos visibles D-03 | TR-05; contrato RF-01-T06 | Condicionado: límites del búnker |
| RF-01-T06 | Guardar habilitación sede/módulo y asignación de puntos; rechazar operación en módulo no habilitado | Backend: configuración autoritativa | Media: relación de habilitación y permisos | Media: alcance de metadatos D-03 | RF-01-T02, RF-01-T04, RF-03-T04 | Condicionado: no incluye almacén restringido RF-11 |

### RF-02 Identidad y selección de entorno

Historia: como usuario, quiero iniciar sesión y ver solo mis entornos autorizados. Tamaño: autenticación y selección sede/módulo/punto, con contexto único y múltiple. Sin registro público ni SSO confirmado.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-02-T01 | Acceso con credenciales, salida de sesión y estado expirado; no enumerar entornos antes de autenticar; error sin revelar cuentas | Frontend web: ciclo de sesión | Media: navegación y estados protegidos | Media: método de identidad D-11 | TR-05; contrato RF-02-T02 | Condicionado: credenciales individuales |
| RF-02-T02 | Verificar credenciales, emitir y cerrar sesión, expirar y limitar intentos; negar token/sesión inválidos | Backend: autenticación y sesión | Media: controles de sesión | Media: proveedor, duración y recuperación D-09/D-11 | TR-02, TR-06, RF-03-T02 | Condicionado: no incluye MFA ni SSO |
| RF-02-T03 | Selector encadenado y acceso directo cuando hay un único contexto; cambiar contexto limpia datos del anterior | Frontend web: navegación autorizada | Media: contextos y permisos múltiples | Baja: secuencia en S1 | TR-05; contrato RF-02-T04 | Listo |
| RF-02-T04 | Consultar solo contextos vigentes; no confiar en IDs elegidos por cliente; búnker ausente sin concesión | Backend: proyección mínima de permisos | Media: combinación sede/módulo/punto | Media: metadatos sensibles D-03 | RF-03-T04, RF-01-T06 | Condicionado: política de ocultamiento |

### RF-03 Usuarios y asignaciones

Historia: como administrador autorizado, quiero crear usuarios y asignarles funciones acotadas. Tamaño: alta individual y asignaciones de acciones/contextos. No agregar importación masiva, invitaciones por correo o editor genérico de roles sin validación.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-03-T01 | Alta individual de usuario y resultado; validar campos y no exponer secretos en listados | Frontend web: administración de cuentas | Baja: alta acotada | Media: entrega inicial de credenciales D-09 | TR-05; contrato RF-03-T02 | Condicionado: alta sin envío externo |
| RF-03-T02 | Crear identidad única y vínculo institucional; credencial inicial por procedimiento acordado; rechazar duplicado y alta no autorizada | Backend: provisión de identidad | Media: identidad y secreto inicial | Media: proveedor y recuperación D-09/D-11 | TR-02, TR-06 | Condicionado: bootstrap inicial controlado |
| RF-03-T03 | Asignar funciones a sede/módulo/punto y mostrar alcance efectivo; no permitir autoconceder búnker sin autoridad | Frontend web: editor de asignaciones | Media: combinación de alcances | Alta: concedentes D-09 | TR-05; contrato RF-03-T04 | Condicionado: búnker separado RF-11 |
| RF-03-T04 | Política común de denegación por defecto y asignaciones; validar actor, acción y objeto; pruebas cruzadas entre perfiles y sedes | Backend: autorización central | Alta: políticas combinadas y elevación | Alta: gobierno D-09 y límite D-03 | TR-04, TR-06 | Condicionado: modelo explícito de permisos; D-03 en RF-11 |

La autorización común se construye aquí una sola vez. Las otras hojas backend implementan su uso y sus reglas de dominio, no vuelven a desarrollar el motor de permisos. La autenticación comprueba identidad; la autorización comprueba la acción. La dependencia entre ambas se resuelve con contratos y credenciales sintéticas, sin esperar dos implementaciones completas en círculo.

### RF-04 Revocación de acceso

Historia: como administrador, quiero retirar un permiso y que deje de habilitar operaciones incluso con una sesión abierta. Tamaño: revocación, invalidación en servidor y propagación a cliente/canales.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-04-T01 | Acción de revocar y aviso al usuario afectado; limpiar contexto y revalidar al reconectar | Frontend web: administración y sesión activa | Media: estado remoto cambiante | Media: tiempo máximo D-07/D-09 | RF-03-T03, RF-02-T01, TR-05; contrato RF-04-T02 | Condicionado: latencia acordada |
| RF-04-T02 | Revocar asignación y negar siguientes operaciones; invalidar autorización de canales abiertos y registrar evento | Backend: aplicación efectiva de revocación | Alta: sesiones, caché y canales | Media: estrategia de sesión y actualización | RF-02-T02, RF-03-T04, TR-06 | Condicionado: contrato de invalidación |

### RF-05 Ingreso de personas

Historia: como operador, quiero registrar a una persona y el motivo de su visita para conocer su presencia y responsable del registro. Tamaño: identidad, visita y evento de ingreso; menor/sin documento son variantes pendientes, no registros estatales externos.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-05-T01 | Formulario con los campos de S1; validaciones, menor y error de guardado; distinguir envío incierto de confirmado | Frontend web: captura operativa | Media: variantes y feedback de registro | Media: obligatorios/excepciones D-05 | TR-05; contrato RF-05-T02 | Condicionado: ficha definitiva |
| RF-05-T02 | Crear visita y entrada con hora/actor/punto de servidor; validar datos y permisos; reintento con mismo ID devuelve el mismo resultado | Backend: registro transaccional | Alta: consistencia, identidad y reintentos | Media: D-05 y RP-01 | RF-03-T04, RF-01-T04, TR-06 | Condicionado: unicidad de visita requiere RP-01; reintento no depende de esa regla |

### RF-06 Presencia y salida cruzada

Historia: como operador, quiero identificar una visita activa y cerrarla desde otro acceso autorizado sin acceder al historial general. Tamaño: búsqueda mínima de visita y cierre, con carrera entre dos puestos.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-06-T01 | Búsqueda de visita activa y estados vacíos/sin permiso; mostrar solo datos necesarios | Frontend web: identificación de salida | Media: búsqueda y mínima visibilidad | Media: circuito D-04 | TR-05; contrato RF-06-T02 | Condicionado: mismo predio propuesto |
| RF-06-T02 | Búsqueda acotada y paginada de visitas activas de puntos permitidos; negar historial general | Backend: consulta compartida segura | Alta: visibilidad cruzada sin ampliar acceso | Media: D-04 y tamaño D-08 | RF-05-T02, RF-03-T04 | Condicionado: circuito de búsqueda |
| RF-06-T03 | Confirmar cierre y representar “ya cerrada” si otro puesto se adelanta; conservar indicación de entrada y salida | Frontend web: resolución de concurrencia visible | Media: resultado cambiante | Media: criterio de cierre D-04 | RF-06-T01, TR-05; contrato RF-06-T04 | Condicionado: mismo predio propuesto |
| RF-06-T04 | Cerrar la visita una sola vez de forma atómica; conservar ambos puntos/actores y devolver conflicto recuperable al segundo cierre | Backend: transición de estado | Alta: cierres concurrentes | Media: D-04; tecnología transaccional | RF-06-T02, TR-06 | Condicionado: sin traslado interpredio aprobado |

### RF-07 Registro de grupos

Historia: como operador, quiero registrar una visita grupal según protocolo sin perder control de sus salidas. Tamaño pendiente: conteo de personas frente a nómina e identificación individual. El agrupador permanece **bloqueado para una cifra única** hasta D-05. Las dos parejas de tareas siguientes son alternativas excluyentes; no sumarlas ni considerarlas aprobadas.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-07-T01 | Variante G1: responsable, cantidades y cierre total/parcial; mostrar remanente y validar que no se retire más de lo presente | Frontend web: conteo grupal | Media: cantidades y estados parciales | Alta: protocolo D-05 | TR-05; contrato RF-07-T02 | Condicionado: solo si se elige G1 |
| RF-07-T02 | Variante G1: persistir grupo y movimientos de cantidades; impedir remanente negativo incluso con dos operadores | Backend: consistencia de conteos | Alta: salidas parciales concurrentes | Alta: D-05/D-04 | RF-03-T04, TR-06 | Condicionado: solo G1, sin nómina |
| RF-07-T03 | Variante G2: nómina y responsable; seleccionar integrantes que egresan y mostrar quién sigue dentro | Frontend web: selección individual | Alta: cantidad de filas y excepciones | Alta: datos de menores/sin documento D-05 | TR-05; contrato RF-07-T04 | Condicionado: solo si se elige G2 |
| RF-07-T04 | Variante G2: vincular integrantes a visita grupal y cerrar cada presencia una vez, manteniendo estado colectivo | Backend: grupo y presencias individuales | Alta: consistencia colectiva/individual | Alta: identidad y D-05/D-04 | RF-05-T02, RF-06-T04, TR-06 | Condicionado: G2 reutiliza mecanismos internos, no se cobran otra vez |

### RF-08 Registro de incidencias

Historia: como operador, quiero informar una incidencia con prioridad y contexto al área responsable. Tamaño: las once categorías ya relevadas; registro y consulta del resultado. El seguimiento por estados RP-05 es aparte.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-08-T01 | Captura de categoría, prioridad y observación; confirmación del registro diferenciada del envío de aviso | Frontend web: reporte de incidencia | Baja: formulario acotado | Media: prioridades D-06 | TR-05; contrato RF-08-T02 | Condicionado: catálogo inicial |
| RF-08-T02 | Registrar incidencia en su módulo/sede/punto y autor; validar categoría y proteger lectura | Backend: persistencia contextual | Media: separación entre módulos | Media: D-06; búnker D-03 | RF-03-T04, TR-06 | Condicionado: implementación restringida de búnker en RF-12 |

### RF-09 Notificación a responsables

Historia: como responsable autorizado, quiero recibir avisos de mi ámbito para actuar. Tamaño pendiente: canal interno o proveedor externo, destinatarios y resultado de entrega. **Bloqueado para cerrar canal/integración** por D-06; notificar no equivale a atender.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-09-T01 | Si se elige canal interno: bandeja/aviso visible solo a destinatarios autorizados, con desconexión y reconexión | Frontend web: recepción interna | Media: actualización y visibilidad | Alta: canal no seleccionado D-06 | TR-05; contrato RF-09-T02 | Condicionado: variante interna; si es solo externo no aplica |
| RF-09-T02 | Resolver destinatarios por módulo/sede; registrar trabajo de entrega, reintentos y fallos sin filtrar datos | Backend: enrutamiento y entrega | Alta: permisos y entrega asíncrona | Alta: canal, reintentos y guardia D-06 | RF-08-T02, RF-03-T04, TR-06 | Bloqueado: contrato del canal |

Si se elige un proveedor externo, concretar su configuración/integración como hijo de RF-09-T02 antes de asignar horas; no agregar indiscriminadamente correo, SMS y WhatsApp. Las credenciales de infraestructura se administran en TR-12; el adaptador de negocio pertenece a RF-09.

### RF-10 Tablero e historial

Historia: como administrador o consultor autorizado, quiero conocer presencia, incidencias y movimientos por filtros. Tamaño: tablero de situación y consulta histórica; no incluye constructor de reportes ni CSV sin RP-06.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-10-T01 | Tablero con presencia e incidencias y enlace al estado de flota; filtros autorizados y fecha de actualización | Frontend web: resumen operativo | Media: varias fuentes de datos | Media: indicadores finales D-08 | TR-05; contrato RF-10-T02 | Condicionado: indicadores de S1 |
| RF-10-T02 | Proyección de presencia e incidencias por alcance; actualización solo a suscriptores autorizados | Backend: consultas y actualización | Alta: consistencia y filtrado de eventos | Media: latencia/carga D-07/D-08 | RF-06-T02, RF-08-T02, RF-03-T04, RF-04-T02 | Condicionado: no duplica proyección de flota RF-16 |
| RF-10-T03 | Historial con filtros de fecha, punto y persona; paginación, vacío, error y lectura limitada por perfil | Frontend web: exploración histórica | Media: filtros combinados | Media: reportes requeridos D-08 | TR-05; contrato RF-10-T04 | Condicionado: flota se consume desde RF-16 |
| RF-10-T04 | Consulta histórica paginada de accesos con filtros permitidos; no incluir búnker ni exportaciones | Backend: consultas de historial | Media: índices y retención | Media: volumen y retención D-08 | RF-05-T02, RF-06-T04, RF-03-T04 | Condicionado: histórico de personas |

### RF-11 Configuración y concesión del búnker

Historia: como administrador, quiero habilitar el espacio confidencial sin adquirir permiso de lectura. Tamaño: configuración, permiso adicional y separación de datos/credenciales según L1/L2/L3. La implementación restringida queda **bloqueada por D-03 y D-09**; su definición está en TR-01, sin agregar una estimación global del búnker.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-11-T01 | Configurar espacio y mostrar permisos concedibles sin listar contenido ni permitir autoasignación no autorizada | Frontend web: separar configuración/lectura | Media: acciones privilegiadas | Alta: quién concede D-09 y qué se revela D-03 | RF-01-T05, RF-03-T03 | Bloqueado: política institucional |
| RF-11-T02 | Habilitar espacio, concesiones especiales y frontera de acceso; probar que administrador funcional no accede por defecto | Backend: frontera del dominio confidencial | Alta: privilegios y custodia | Alta: L1/L2/L3 cambian implementación | RF-03-T04, TR-06, D-03, D-09 | Bloqueado: elegir aislamiento antes de detallar recursos |

Si se requiere servicio/base/custodia independientes, las configuraciones de recursos se desglosan dentro de TR-12 tras D-03. No presupuestar L1, L2 y L3 juntos ni usar el subtotal de una segunda base como medida de esfuerzo de seguridad.

### RF-12 Operación del búnker

Historia: como operador autorizado, quiero registrar entradas, salidas e incidencias del entorno confidencial. Tamaño: circuito de registro y consulta con puntos de egreso específicos, sin búsqueda general compartida.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-12-T01 | Interfaz restringida de entrada/salida e incidencia; ningún dato llega a vistas generales; indicar puntos de salida permitidos | Frontend web: operación confidencial | Alta: visibilidad y circuito diferente | Alta: D-03 y campos/puntos | RF-11-T01, TR-05 | Bloqueado: política y contrato restringido |
| RF-12-T02 | Persistir movimientos e incidencias restringidos y cerrar solo por puntos permitidos; no reutilizar búsquedas generales de identidad | Backend: reglas y datos restringidos | Alta: separación y concurrencia | Alta: aislamiento D-03 | RF-11-T02, TR-06 | Bloqueado: frontera institucional |

Los patrones de formularios o transacciones pueden adaptarse del trabajo nuevo del proyecto; no se descuenta una reutilización previa inexistente. La instrumentación de lecturas se completa en RF-13, sin repetir el registro base TR-06.

### RF-13 Auditoría del búnker

Historia: como auditor especialmente autorizado, quiero reconstruir quién consultó o modificó información restringida. Tamaño: captura de consultas/cambios y visor de bitácora confidencial.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-13-T01 | Visor restringido con actor, acción, objeto, hora y resultado; solo lectura y filtros autorizados | Frontend web: lectura de bitácora | Media: filtros y acceso especial | Alta: permisos/retención D-03/D-08 | TR-05; contrato RF-13-T02 | Bloqueado: política de auditoría |
| RF-13-T02 | Instrumentar consultas y cambios del búnker; persistir/consultar rastro protegido según custodia acordada | Backend: auditoría de lectura y cambio | Alta: integridad y datos sensibles | Alta: protección frente a infraestructura | RF-11-T02, RF-12-T02, TR-06, D-03 | Bloqueado: garantías y retención |

### RF-14 Catálogo de flota

Historia: como responsable, quiero identificar las unidades y su alcance para registrar viajes de la flota institucional. Tamaño: catálogo inicial de aproximadamente 45 a 50 vehículos; no es máximo de capacidad.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-14-T01 | Alta/edición y búsqueda de unidad por número/chapa; errores, vacío y permisos; no incluir mantenimiento mecánico | Frontend web: catálogo de unidades | Baja: catálogo acotado | Media: edición/estado inicial inferidos | TR-05; contrato RF-14-T02 | Condicionado: validar gestión de catálogo |
| RF-14-T02 | Persistir unidades y asignaciones; validar identificadores y estado inicial confiable sin borrar historial | Backend: integridad de unidad | Media: unicidad y estado inicial | Media: carga inicial y unidades autorizadas | RF-03-T04, TR-06 | Condicionado: reglas de catálogo |

La carga real de los datos iniciales corresponde a RF-18-T01; construir el catálogo aquí no significa volver a cargarlo ni crear un importador masivo no solicitado.

### RF-15 Salida y retorno de vehículos

Historia: como operador de flota, quiero registrar salida y retorno para conocer responsable, destino y kilometraje del viaje. Tamaño: apertura/cierre, conductor, acompañantes y observaciones; cambios de conductor y retorno en otro predio no están resueltos.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-15-T01 | Captura de salida con unidad, conductor, destino, motivo, acompañantes y kilómetros; confirmación inequívoca | Frontend web: apertura de viaje | Media: validaciones y selección de unidad | Media: datos obligatorios y RP-03 | RF-14-T01, TR-05; contrato RF-15-T02 | Condicionado: reglas de viaje |
| RF-15-T02 | Abrir viaje con hora/punto/actor y reintento idempotente; validar unidad/permiso y viaje activo según RP-03 | Backend: apertura transaccional | Alta: exclusividad de movimiento | Media: RP-03 y D-04 | RF-14-T02, RF-03-T04, TR-06 | Condicionado: unicidad propuesta |
| RF-15-T03 | Seleccionar retorno pendiente, registrar kilómetros y observaciones; mostrar conflicto o datos inválidos sin cerrar localmente | Frontend web: cierre de viaje | Media: estado cambiante y odómetro | Media: excepciones RP-03/D-04 | TR-05; contratos RF-16-T02 y RF-15-T04 | Condicionado: sin corrección avanzada RP-02 |
| RF-15-T04 | Cerrar viaje una vez conservando salida/retorno; validar punto y kilómetros según RP-03 | Backend: retorno y consistencia | Alta: cierre concurrente y odómetro | Media: RP-03, retorno interpredio D-04 | RF-15-T02, TR-06 | Condicionado: circuito acordado |

### RF-16 Situación e historial de flota

Historia: como responsable de flota, quiero distinguir unidades presentes, en circulación y retornos pendientes. Tamaño: estado de flota e historial por unidad/punto/fecha, consumibles también desde RF-10.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-16-T01 | Listado de estado e historial filtrado de unidades; indicar datos incompletos y última actualización | Frontend web: consulta de flota | Media: estado e historial | Media: ubicación inicial y filtros D-04/D-08 | TR-05; contrato RF-16-T02 | Condicionado: no inventar “demorado” |
| RF-16-T02 | Proyectar presencia/circulación desde estado inicial y viajes; consultar historial paginado dentro de permisos | Backend: proyección y lectura de flota | Media: consistencia entre unidad y viaje | Media: estado inicial, D-04/D-08 | RF-14-T02, RF-15-T02, RF-15-T04, RF-03-T04 | Condicionado: contrato reutilizado por tablero general |

### RF-17 Actividad y auditoría general

Historia: como administrador o auditor autorizado, quiero consultar actividad de mi ámbito sin modificarla. Tamaño: búsqueda de eventos de administración y operación, excluyendo contenido del búnker.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-17-T01 | Visor de actividad con filtros y detalle permitido; sin acciones de edición para auditor | Frontend web: exploración de evidencia | Media: filtros y perfiles | Media: campos/retención D-08/D-09 | TR-05; contrato RF-17-T02 | Condicionado: alcance de consulta |
| RF-17-T02 | Consultar eventos generales paginados por permisos; separar contenido restringido y denegar mutaciones por auditor | Backend: lectura segura de auditoría | Media: autorización y consulta | Media: retención/volumen D-08 | TR-06, RF-03-T04 | Condicionado: no reconstruye capturador común |

### RF-18 Preparación operativa

Agrupador técnico/operativo, no una historia artificial. Fuente S1 §11. Tamaño pendiente: catálogo inicial de sedes/puntos/usuarios, flota inicial, perfiles a capacitar y sedes de piloto. La infraestructura está en TR-12 y el despliegue final en TR-15, no en estas hojas.

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RF-18-T01 | Validar y cargar configuración y datos iniciales acordados; institución verifica correspondencia de sedes, usuarios y unidades | Otro: preparación operativa/configuración | Media: calidad de datos y accesos iniciales | Media: volumen y responsable D-08/D-10 | RF-01, RF-03, RF-14; entorno TR-12 | Condicionado: sin migración ni importador masivo |
| RF-18-T02 | Guía operativa y capacitación por perfiles; participantes ejecutan flujo de prueba y contingencia online | Otro: documentación/capacitación | Media: varios perfiles y protocolos | Media: asistentes, modalidad y sedes D-10 | TR-08, RF-18-T01 | Condicionado: no asumir cantidad de jornadas |
| RF-18-T03 | Verificar aceptación de funciones/permisos, responsables y fecha efectiva de producción; separar inicio de validación | Otro: aceptación y lanzamiento operativo | Media: criterios institucionales | Alta: alcance de piloto y firma D-10 | RF-18-T02, TR-08, TR-09, TR-10, TR-13, TR-15 | Condicionado: no fija duración ni costo de piloto |

Una referencia a un padre como dependencia significa sus hojas aplicables completadas, nunca un importe adicional por ese padre.

### Propuestas RP y su efecto sobre las hojas

| ID preservado | Tratamiento de estimación | Responsabilidad y evidencia de aceptación |
| --- | --- | --- |
| RP-01 | Regla alternativa cubierta en RF-05-T01/T02 y RF-06; no hoja adicional | Backend controla duplicación de visita, web muestra resultado; elegir circuito e identidad. |
| RP-02 | Extensión propuesta, fuera de base hasta autorización | Hojas RP-02-T01/T02 siguientes; no confundir con corregir defectos del software. |
| RP-03 | Regla alternativa cubierta en RF-15; no hoja adicional | Backend controla exclusividad/odómetro; web representa validación y conflicto. |
| RP-04 | Extensión propuesta, fuera de base hasta autorización | Hojas RP-04-T01/T02; método y recuperación pendientes. |
| RP-05 | Extensión propuesta, fuera de base hasta autorización | Hojas RP-05-T01/T02; no convertir notificación en flujo de atención automáticamente. |
| RP-06 | Extensión propuesta, fuera de base hasta autorización | Hojas RP-06-T01/T02; no agregar formatos no solicitados. |
| RP-07 | Excluido por S2 | Sin hojas ni costo asignado de offline. |

| ID | Resultado y aceptación técnica propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| RP-02-T01 | Corrección/anulación con motivo y visualización del antes/después sin editar silenciosamente | Frontend web: supervisión | Media: diferencias y confirmación | Alta: acciones permitidas D-09 | RF-06, RF-15, TR-05 | Condicionado: propuesta no incluida |
| RP-02-T02 | Aplicar corrección autorizada conservando rastro y recalculando estado afectado sin romper visitas/viajes | Backend: consistencia de corrección | Alta: cambios retroactivos | Alta: reglas D-09 | RF-06-T04, RF-15-T04, TR-06 | Condicionado: propuesta no incluida |
| RP-04-T01 | Alta/desafío/recuperación de segundo factor y expiración; no ofrecer vía que evada autorización | Frontend web: autenticación reforzada | Media: distintos estados | Alta: método y perfiles D-03/D-09 | RF-02-T01, TR-05 | Condicionado: propuesta no incluida |
| RP-04-T02 | Configurar/verificar segundo factor y recuperación protegida; auditar éxitos y fallos sin secretos | Backend: control reforzado | Alta: recuperación y sesión | Alta: proveedor y política | RF-02-T02, TR-06 | Condicionado: propuesta no incluida |
| RP-05-T01 | Acusar atención y resolver alerta con estados e historial visibles a responsables | Frontend web: seguimiento | Media: transiciones | Alta: protocolo D-06 | RF-08, RF-09, TR-05 | Condicionado: propuesta no incluida |
| RP-05-T02 | Transiciones autorizadas de alerta y registro del responsable; rechazar carrera o transición inválida | Backend: ciclo de atención | Media: estados y concurrencia | Alta: protocolo D-06 | RF-08-T02, RF-03-T04, TR-06 | Condicionado: propuesta no incluida |
| RP-06-T01 | Solicitar y descargar CSV del filtro autorizado; estados vacío/error y alcance visible | Frontend web: exportación | Baja: una acción de formato definido | Media: tamaño y permiso D-08 | RF-10-T03, RF-16-T01, TR-05 | Condicionado: propuesta no incluida |
| RP-06-T02 | Generar CSV del filtro con permisos y neutralización de fórmulas; auditar sin mezclar búnker | Backend: generación de archivo | Media: datos sensibles y volumen | Media: límite síncrono/asincrónico D-08 | RF-10-T04, RF-16-T02, TR-06 | Condicionado: propuesta no incluida |

## Aceptación común de la web responsive

RNF-07 aplica a todas las hojas frontend web del alcance elegido, incluidos administración, personas/grupos, flota y búnker. Sus criterios propuestos son:

- Completar los mismos flujos autorizados desde escritorio y navegador móvil, sin depender de hover ni ocultar acciones necesarias.
- Adaptar navegación, formularios, diálogos y listados al ancho disponible; evitar desbordes de página y conservar acceso a los datos cuando una tabla requiera desplazamiento propio.
- Mantener campos, mensajes de error y acciones utilizables con interacción táctil y teclado virtual, sin que este impida completar el formulario.
- Verificar envío, conflicto, pérdida de conexión y revalidación de permisos también en móvil, sin agregar modo offline.

La matriz de navegadores, tamaños y dispositivos concretos se acuerda durante TR-03/TR-08. Esa precisión pendiente no vuelve opcional la cobertura móvil. TR-03 diseña los patrones, TR-05 implementa la base común, cada hoja web adapta su flujo y TR-08 verifica recorridos integrados en ambas superficies. No se suma un segundo frontend ni se traslada la partida histórica de mobile nativo de AfterAccess.

## Trabajo compartido contado una sola vez

Los TR son hojas compartidas, no agrupadores de recargos. Su cobertura propuesta se refiere a la entrega de este alcance nuevo. Salvo TR-14, son trabajos de preparación/implementación/validación inicial; registrar su inclusión en la futura estimación y su responsable. El pedido S3 hace visible este trabajo, pero no aprueba nuevas prestaciones comerciales. RF-18 referencia las tareas técnicas de entrega sin duplicarlas.

| ID | Tipo, resultado y aceptación propuesta | Frente y motivo | Complejidad y motivo | Incertidumbre y motivo | Dependencias | Estimabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| TR-01 | Discovery restante: resolver matriz de decisiones, reglas y variantes con responsables; entregar cambios por ID y aceptación registrada | Otro: análisis funcional y arquitectura | Media: decisiones relacionadas | Alta: respuestas institucionales D-03 a D-10 | S1, S2, S5, versión 0.4 | Condicionado: estimar solo trabajo restante, no rehacer documentos terminados |
| TR-02 | Configuración de harness: estructura inicial, seguimiento por IDs, entornos reproducibles, verificaciones automáticas y datos sintéticos; un clon limpio ejecuta los checks iniciales | Otro: ingeniería de desarrollo/herramientas | Media: preparación compartida | Media: stack/herramientas D-11 | D-11/ADR-02 | Condicionado: no incluye las pruebas de negocio de cada hoja |
| TR-03 | Diseño: recorridos de operador/administración, estados vacío/error/sin permiso y patrones responsive de escritorio y celular; revisar navegación táctil, formularios y tablas de cada flujo distinto con operaciones | Otro: UX/UI | Media: rapidez operativa y permisos | Media: dispositivos, identidad visual y rondas D-10/D-11 | RF y decisiones funcionales aplicables | Condicionado: tamaño por flujos, no número inventado de pantallas |
| TR-04 | Definición de contratos compartidos: campos, errores, paginación, contexto e identificador de operación/evento; ejemplos web/backend consistentes | Otro: diseño de contratos técnicos | Media: coordinación entre dominios | Media: stack y reglas pendientes | ADR-02 y D pertinentes | Condicionado: definición; implementación pertenece a cada hoja, no estimar cada contrato otra vez |
| TR-05 | Implementación de base web: navegación, componentes comunes, feedback de solicitudes, conexión y revalidación de contexto; probar navegación y componentes responsive en escritorio/celular, sin datos de otro contexto | Frontend web: infraestructura de cliente compartida | Media: estado transversal | Media: dispositivos y sesión | TR-02, TR-03, TR-04; contratos RF-02/RF-04 | Condicionado: no duplica formularios ni login; mobile web incluido, sin cliente nativo |
| TR-06 | Implementación base backend: errores uniformes, eventos auditables, mecanismo de reintento idempotente y migraciones de esquema reproducibles; pruebas con una operación sintética | Backend: utilidades comunes | Media: consistencia y observabilidad | Media: persistencia/stack D-11 | TR-02, TR-04 | Condicionado: esquemas de negocio, capturas concretas y reglas están en sus hojas |
| TR-07 | Revisión: contrastar cambios y pruebas de hojas con criterios/contratos y registrar hallazgos/resolución; no dar por revisado solo por compilar | Otro: revisión técnica | Media: varios dominios y permisos | Media: revisores y política D-11 | Hojas implementadas | Condicionado: revisión una vez; fixes de código permanecen en la hoja responsable |
| TR-08 | QA integrado: ejecutar recorridos multiusuario, grupos elegidos, flota, cortes online y aceptación funcional en escritorio y navegador móvil, con interacción táctil y teclado virtual; guardar evidencia y volver a verificar incidencias | Otro: QA funcional/integración | Alta: combinaciones y concurrencia | Media: D-04/D-05/D-10 y variantes | Hojas aplicables, TR-07, entorno TR-12 | Condicionado: no repite pruebas unitarias; ejecución PV-01/PV-04 incluida aquí |
| TR-09 | Validación de seguridad: matriz de denegaciones, revocación y fugas en API/canales/reportes; registrar evidencia por perfil | Otro: QA de seguridad | Alta: fronteras y canales múltiples | Alta: aislamiento institucional D-03 | RF-03, RF-04, RF-11 a RF-13, TR-07 | Condicionado para base; aceptación del búnker bloqueada por D-03; no es auditoría externa certificada |
| TR-10 | Validación de carga: acordar escenario y ejecutar mezcla representativa de registros/consultas/actualizaciones; comparar latencias y errores contra umbrales | Otro: QA de rendimiento | Media: datos y escenarios reproducibles | Alta: concurrencia/volumen D-07/D-08 | Hojas operativas, entorno TR-12 | Condicionado: hipótesis de costos no son carga aprobada; cubre PV-05 |
| TR-11 | Coordinación: plan de dependencias, responsables, revisión de cambios de alcance y aceptación de hitos; mantener versiones y pendientes por ID | Otro: PM/coordinación | Media: institución y varias disciplinas | Media: disponibilidad y responsables D-10/D-11 | Plan funcional y decisiones institucionales | Condicionado: espera externa no son horas; no duplica análisis TR-01 ni revisión TR-07 |
| TR-12 | Configuración: preparar ambientes separados, secretos, acceso operativo, entrega reproducible y monitoreo; levantar versión de prueba y verificar salud | Otro: infraestructura/DevOps | Media, alta si custodia separada | Alta: región/proveedor/aislamiento D-03/D-07 | ADR-06, TR-02 | Condicionado: base administrada; frontera de búnker bloqueada; configurar recursos no incluye su factura mensual |
| TR-13 | Configurar respaldo y recuperación, restaurar en entorno aislado y verificar permisos/datos; registrar RPO/RTO obtenido frente a lo acordado | Otro: infraestructura/recuperación | Media, alta si custodia separada | Alta: pérdida/tiempo/retención D-03/D-07/D-08 | TR-12, datos de muestra y reglas de dominio | Condicionado: propuesta RNF-06; ejecución PV-06 una vez, sin sumar otro ensayo en QA |
| TR-14 | Definir y prestar estabilización posterior si se contrata: registrar incidentes del periodo y evidencia de cierre; distinguir defectos de ampliaciones | Otro: soporte de estabilización | Por definir: cobertura no acordada | Alta: periodo, disponibilidad y alcance D-10 | Aceptación RF-18-T03 y acuerdo específico | Bloqueado: no incluido en suma de construcción ni equiparado automáticamente a dos meses de dedicación |
| TR-15 | Despliegue final: publicar versión validada, comprobar salud/permisos y disponer rollback ensayado; registrar versión entregada y resultado | Otro: infraestructura/DevOps | Media: continuidad y reversión | Media: ventana y responsable D-07/D-10 | TR-12, TR-13, TR-08, TR-09, TR-10 | Condicionado: acción futura, no autorizada a ejecutar en este relevamiento |

El harness nuevo de TR-02 prepara la forma de trabajar; no acredita que el producto esté implementado. El relevamiento documental ya realizado está completo para esta versión, pero sin horas medidas aportadas: no imputarlo retroactivamente ni asumir que fue gratuito. TR-01 comprende las validaciones restantes; su tratamiento comercial se definirá después.

TR-07 revisa; cada hoja corrige sus defectos; TR-08 vuelve a verificar la integración. Esas responsabilidades son diferentes y no deben convertirse en tres estimaciones del mismo arreglo. Si el futuro presupuestador usa un agregado que ya incluye revisión o QA, debe marcar los TR cubiertos por ese agregado y retirarlos de la suma separada.

La espera de respuestas, accesos o revisión institucional afecta calendario. Solo se registra como esfuerzo la preparación, seguimiento y trabajo efectivo correspondiente, sin convertir todo el tiempo de espera en horas de PM o desarrollo.

TR-12 prepara el entorno donde se prueba; TR-15 entrega la versión validada. Separarlos evita que QA dependa de un despliegue final que a su vez requiere QA. RF-18-T03 confirma la aceptación operativa, no vuelve a desplegar ni vuelve a ejecutar toda la batería de pruebas.

## Cobertura de requisitos y aceptación

| Restricción o resultado | Trabajo propietario | Validación compartida y límite |
| --- | --- | --- |
| RNF-01 Confidencialidad | RF-03-T04; uso del control en cada backend; frontera RF-11/RF-12 | TR-09/PV-02; web elimina visibilidad pero no sustituye control de servidor. |
| RNF-02 Consistencia multipunto | TR-06 mecanismo común; RF-05-T02, RF-06-T04, RF-07 variante, RF-15-T02/T04 reglas específicas | TR-08/PV-01; no cobrar un “módulo de concurrencia” adicional. |
| RNF-03 Actualización | RF-10-T02 y datos RF-16-T02; TR-05 consume estados de conexión | TR-10; protocolo/canal se define en TR-04, sin construir un tiempo real separado por pantalla. |
| RNF-04 Revocación | RF-04-T01/T02 y RF-03-T04 | TR-09/PV-03; no otra implementación en autenticación. |
| RNF-05 Trazabilidad | TR-06 base; eventos en hojas; RF-17 consulta general y RF-13 lectura restringida | TR-09; infraestructura de conservación en TR-12/TR-13, no duplicar visor con bitácora. |
| RNF-06 Recuperación propuesta | TR-13 y entorno TR-12 | PV-06 dentro de TR-13; pendiente acordar RPO/RTO. |
| RNF-07 Responsive web confirmado | TR-03 diseño escritorio/celular; TR-05 base y adaptación de cada hoja web | TR-08 verifica ambos; matriz de compatibilidad pendiente, sin duplicar frontend. |
| RNF-08 Protección de datos propuesta | TR-01 acuerda minimización/retención; hojas aplican campos/permisos; TR-12/TR-13 copias | Si se exige borrado/anonimización automatizados, falta una hoja específica y aprobación; no afirmar que esta versión los incluye o estima. |
| RNF-09 Online | TR-05 estados; TR-06 mecanismo y hojas backend resultados de operación | TR-08/PV-04; sin cola persistente offline. |
| Casos de aceptación 1 a 3 y 7 a 9 | Hojas de accesos/grupos/flota/configuración y RP aplicables | TR-08; variantes propuestas solo si se seleccionan. |
| Casos 4 a 6 | RF-03/RF-04/RF-11 a RF-13; RP-06 solo si se aprueba | TR-09. |
| Caso 10 | TR-13 | Restauración propuesta condicionada, no prueba realizada. |
| Caso 11 | TR-05 y hojas transaccionales | TR-08. |

## Estado resumido por agrupador

| Agrupador | Estado del conjunto para estimar | Qué permite avanzar o falta resolver |
| --- | --- | --- |
| RF-01 | Condicionado; T01/T02 listas por alcance | Desactivación, permisos y configuración de búnker requieren límites. |
| RF-02 | Condicionado; T03 lista por alcance | Método de identidad, recuperación y límite de metadatos. |
| RF-03/RF-04 | Condicionado | Concedentes y permisos efectivos; modelo de revocación. |
| RF-05/RF-06 | Condicionado | Ficha, identidad y circuito de salida cruzada. |
| RF-07 | Bloqueado para cifra única; variantes desglosadas | Elegir G1 o G2 y protocolo de menores/salidas. |
| RF-08 | Condicionado | Prioridades y campos; emisión separada de atención. |
| RF-09 | Bloqueado para integración; variante interna condicionada | Canal y responsables sin resolver. |
| RF-10/RF-16/RF-17 | Condicionado | Indicadores, filtros, retención y volumen. |
| RF-11/RF-12/RF-13 | Bloqueado | Definición institucional de aislamiento y gobierno del búnker. |
| RF-14/RF-15 | Condicionado | Catálogo inicial, unicidad, odómetro y retornos. |
| RF-18 | Condicionado | Tamaño del piloto, carga inicial, capacitación y autoridad de aceptación. |
| RP-01 a RP-06 | Propuestos; no sumables como alcance aprobado | Seleccionar reglas/extensiones y estimar únicamente hojas aplicables. |
| RNF-07 Mobile web responsive | Incluido y confirmado por S5 | Esfuerzo de adaptación y QA dentro de frontend web, UX y QA; compatibilidad concreta pendiente. |
| RP-07 y cliente mobile nativo | Excluidos | No asignar desarrollo offline/nativo por analogía con AfterAccess. |
| TR-01 a TR-13 | Condicionados, con límites indicados por tarea | Calibración por stack/equipo y definiciones institucionales; TR-09/TR-12 tienen parte búnker bloqueada. |
| TR-14 | Bloqueado; fuera de construcción base | Condiciones de estabilización/soporte sin definir. |
| TR-15 | Condicionado | Versión validada, ventana de publicación y rollback acordados. |

Esta matriz describe estimabilidad funcional. La calibración de esfuerzo de todas las hojas depende del contexto del equipo D-11; no cambia una tarea acotada a complejidad alta por desconocer quién la ejecutará. Se preservan todas las necesidades confirmadas sin presentar como cerradas las variantes abiertas.
