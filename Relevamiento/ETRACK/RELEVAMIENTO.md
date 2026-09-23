# Etrack Access relevamiento integral

Actualización: 22 de septiembre de 2026. Versión 0.4. Estado: análisis para validación; estimación condicionada con hojas por disciplina y traspaso preparado. No es una fecha de aprobación del alcance detallado.

## Conclusión

Etrack Access es un **Sistema complejo** de operación institucional con tres módulos incluidos en el alcance recibido: accesos de personas, movimientos de flota y búnker confidencial. Comparte administración, identidad y configuración de establecimientos, pero debe separar las operaciones y la visibilidad de cada módulo.

La dificultad principal no es administrar los aproximadamente 45 a 50 vehículos mencionados. Es mantener estados consistentes entre varios puestos, aplicar permisos por contexto, proteger información confidencial y reconstruir quién hizo o consultó cada operación. El nivel de aislamiento exigido para el búnker puede cambiar materialmente la arquitectura.

El usuario confirmó **desarrollo desde cero y web app exclusivamente online**. Se recomienda una estructura modular, con datos transaccionales y autorización centralizada. Esa estructura técnica permanece propuesta. La entrega por etapas conserva los tres módulos; no convierte flota o búnker en mejoras opcionales.

## Fuente y lectura del alcance

Fuente S1: [ETRACK Puntos de partida para el desarrollo](</Users/matias/Downloads/ETRACK_Puntos_de_partida_para_el_desarrollo_SIN_PRECIOS (1).docx>), ocho páginas revisadas. El usuario lo identifica como el alcance definido. Sus funcionalidades constituyen la base de este análisis; las alternativas técnicas y comerciales que el texto plantea como propuestas conservan ese carácter.

Fuente S2: respuestas del usuario en esta conversación del 21/09/2026: desarrollo desde cero, operación web con Internet y aislamiento del búnker a definir por la institución. S2 resuelve D-01 y D-02 y mantiene D-03 pendiente. El archivo original permanece intacto. La revisión de código anterior y su reutilización no forman parte de este proyecto; no se verificó una instalación en ejecución.

Fuente S3: instrucción del usuario del 22/09/2026 de aplicar el agente actualizado al proyecto existente, ampliar tareas por disciplina, conservar IDs/decisiones/valores y preparar traspaso sin presupuesto, Drive, commit ni push. Se leyeron desde disco AGENTS.md, la skill y las cinco referencias indicadas. No se modificaron las instrucciones de ningún agente.

Fuente S4, únicamente para antecedentes: [casos Aftercode](../skills/relevamiento/references/casos-aftercode.md), registro consolidado el 22/09/2026 y leído en esta actualización. Es una síntesis documental, no una nueva lectura de los PDF, planillas ni repositorios originales de MCD o AfterAccess.

Fuente S5: aclaración del usuario del 22/09/2026: mobile debe incluirse como web responsive para celulares. Se confirma adaptación de los flujos web y sus pruebas; no se agrega aplicación nativa.

Estados utilizados en el paquete:

- **Confirmado en alcance:** necesidad incluida en S1 y tomada como base por el usuario; no equivale a implementación verificada.
- **Observado:** evidencia obtenida en esta revisión documental o en una fuente técnica citada.
- **Supuesto:** condición provisional para comparar o dimensionar.
- **Propuesto:** especificación o solución recomendada pendiente de aceptación.
- **Pendiente:** decisión sin información suficiente.

La fuente única de requisitos es [FUNCIONALIDADES.md](FUNCIONALIDADES.md). Las decisiones técnicas están en [ARQUITECTURA.md](ARQUITECTURA.md) y el modelo económico de operación en [COSTOS_OPERATIVOS.md](COSTOS_OPERATIVOS.md).

## Objetivo y operación esperada

La institución necesita administrar sedes y puntos sin solicitar una configuración externa por cada alta, registrar movimientos con responsables individuales y consultar la situación actual y el historial según permisos. S1 menciona al Congreso y a una Cámara de Senadores como ejemplos; falta confirmar institución contratante, país y responsables de aprobación.

No se documenta cómo se opera actualmente, si hay planillas, sistemas separados o registros en papel. Tampoco hay mediciones de tiempos o errores. No corresponde atribuir ahorros ni mejoras porcentuales todavía.

Como señal de éxito se propone demostrar que un ingreso registrado en un acceso puede cerrarse correctamente en otro autorizado, que un vehículo mantiene un único movimiento abierto y que ninguna consulta general expone datos del búnker. La institución deberá fijar objetivos de tiempo de atención, actualización y recuperación.

## Procesos que hay que resolver

**Preparación institucional.** Un administrador habilita establecimiento, módulo y puntos; crea usuarios y asigna funciones. Un permiso para configurar un entorno no debe conceder acceso a sus datos. Al desactivar un punto, hay que conservar el historial y resolver sus movimientos pendientes.

**Personas.** El operador inicia sesión, selecciona su contexto y registra el ingreso. Otro operador autorizado identifica la visita activa y registra la salida. El cierre debe afectar esa visita concreta y conservar ambos puntos y ambos operadores. Queda por decidir si el circuito compartido se limita al mismo predio o atraviesa establecimientos.

**Grupos.** El registro simplificado está incluido, sujeto al protocolo institucional. Hay dos variantes diferentes: responsable y cantidad, o nómina individual vinculada al grupo. La primera no permite saber qué integrantes específicos continúan dentro después de salidas parciales. La institución debe elegir el control requerido.

**Flota.** Se identifica unidad y conductor, se registra salida con destino, motivo y kilometraje y luego retorno con sus datos. El estado de circulación debe derivarse del movimiento abierto. No se presume geolocalización, mantenimiento ni gestión de combustible.

**Búnker.** Un perfil autorizado entra a un entorno restringido, registra movimientos y consulta únicamente información habilitada. Las consultas también se auditan. Se debe definir quién concede el primer permiso y quién puede otorgar permisos a terceros, para que el administrador general no pueda habilitarse a sí mismo sin control.

**Incidencias.** El operador registra una categoría y prioridad; el sistema dirige el aviso al responsable permitido para ese módulo y establecimiento. Emitir un aviso no demuestra que alguien lo haya recibido o atendido. El seguimiento y escalamiento requieren definición expresa.

## Complejidad y consecuencias

| Frente | Complejidad relativa | Motivo y trabajo que genera |
| --- | --- | --- |
| Establecimientos y puntos | Media | Autogestión, desactivación segura y conservación de referencias históricas. |
| Identidad y permisos | Alta | Combinación de institución, sede, módulo, punto, acción y perfil; revocación con sesiones abiertas. |
| Personas y salidas cruzadas | Alta | Concurrencia, búsqueda mínima compartida y prevención de cierres duplicados. |
| Grupos | Media o alta | Cambia según identificación individual, menores y egresos parciales. |
| Flota | Media | Reglas de movimientos, odómetro, unidades asignadas y retornos excepcionales. |
| Búnker | Alta | Separación de administración y lectura, auditoría de consultas y posibles credenciales e infraestructura independientes. |
| Alertas | Media o alta | Depende de canales externos, confirmación de recepción y cobertura fuera de horario. |
| Reportes y auditoría | Media o alta | Consultas históricas, retención y aplicación de la misma confidencialidad a listados y exportaciones. |
| Disponibilidad online | Media o alta | Manejo claro de desconexión, solicitudes inciertas, respaldo y recuperación. Offline y sincronización quedan excluidos por S2. |
| Carga inicial de datos | Pendiente de volumen | Definir quién carga sedes, usuarios y vehículos. Migración histórica no incluida sin solicitud adicional. |

Estas categorías son un juicio técnico cualitativo, no horas ni factores automáticos de precio.

## Decisiones prioritarias

| ID | Decisión y estado | Consecuencia | Validación mínima y responsable propuesto |
| --- | --- | --- | --- |
| D-01 | Confirmado: desarrollo desde cero | Estimar construcción nueva; sin ahorro atribuido a reutilización | Resuelto por usuario en S2. |
| D-02 | Confirmado: web app exclusivamente online | Sin registro offline, cola local de sincronización ni servidor local para continuidad | Resuelto por usuario en S2; operaciones define su contingencia manual fuera de la app. |
| D-03 | Frente a quién se protege el búnker | Separación lógica, servicios separados o custodia institucional | Seguridad e informática definen quién puede administrar aplicación, servidores, base y claves. |
| D-04 | Sedes conectadas y salidas entre predios | Reglas de presencia y permisos de búsqueda | Validar ejemplos de entrada A/salida B y traslado entre sedes. |
| D-05 | Grupos, menores y falta de documento | Campos, identificación y cierre parcial | Seguridad aporta una ficha real anonimizada y protocolo. |
| D-06 | Destinatarios y canales de alertas | Integraciones, costos y operación de guardia | Matriz categoría × módulo × sede × destinatario, con canal y contingencia. |
| D-07 | Disponibilidad, pérdida tolerable y ubicación de datos | Hosting, redundancia, backups y recuperación | Informática confirma país, residencia exigida, tiempo máximo de caída y pérdida tolerada. |
| D-08 | Uso y retención | Tamaño, rendimiento y costo acumulado | Cantidad de sedes, puestos, usuarios simultáneos, visitas diarias, consultas y años conservados. |
| D-09 | Gobierno de permisos y correcciones | Evitar autoasignación y cambios sin responsable | Designar concedentes, supervisores y responsable de auditoría. |
| D-10 | Piloto, soporte y aceptación | Inicio de validación y responsabilidad recurrente | Confirmar sedes/módulos del piloto, cobertura de soporte y quién acepta cada hito. |
| D-11 | Equipo, stack y proceso de entrega pendientes | Calibración de esfuerzo, reparto por disciplinas y duración calendario | Aftercode indica stack, experiencia, roles/disponibilidad, herramientas existentes y cobertura de revisión/QA. No inferirlos del equipo de MCD. |

D-01 y D-02 quedan cerradas. La institución debe definir D-03. Las restantes decisiones permiten avanzar con supuestos explícitos, pero deben resolverse antes de comprometer el comportamiento afectado.

## Tensiones detectadas y propuesta de resolución

1. S1 limita al operador a sus accesos, pero exige cerrar visitas iniciadas en otros. Propuesta: permiso acotado de búsqueda de visitas activas dentro del circuito autorizado, sin conceder historial general.
2. S1 describe inicialmente administrador y operador, pero luego incorpora supervisión, auditoría, informática y responsables. Propuesta: funciones combinables con alcance explícito, evitando resolver todo con dos roles rígidos.
3. La matriz muestra acceso del jefe de seguridad al búnker y el texto exige autorización expresa para todos. Propuesta: también el jefe recibe una asignación nominal y revocable.
4. “Base lógica separada” no define protección frente a administradores de infraestructura. D-03 debe cerrar el modelo de amenaza antes de aprobar el diseño del búnker.
5. “Tiempo real” y “revocación inmediata” necesitan un límite medible. Sin conexión no se registran nuevas operaciones ni se presenta información almacenada como actual. Al reconectar se revalidan sesión, permisos y estado.
6. Las categorías de alertas no equivalen a sistemas adicionales. “Vehículo observado” no confirma una lista automática de vigilancia; “evacuación” no confirma un módulo de conteo o rescate.

## Secuencia propuesta de trabajo

| Etapa | Resultado revisable | Condición de cierre |
| --- | --- | --- |
| 0 Definición | Reglas críticas y decisión institucional de confidencialidad sobre una web nueva online | D-03 resuelta o variantes de estimación explícitas; D-01 y D-02 ya confirmadas. |
| 1 Base común | Institución, sedes, puntos, usuarios y autorización | Pruebas de permisos, desactivación y revocación satisfactorias. |
| 2 Accesos | Personas, grupos, presencia, salida cruzada e incidencias | Casos concurrentes y protocolo de grupos aprobados. |
| 3 Flota | Catálogo, salida, retorno y consulta operativa | Consistencia de movimientos y kilometraje verificada. |
| 4 Búnker | Circuito restringido, auditoría de lectura y autenticación reforzada acordada | Revisión de aislamiento y gobierno de permisos. Su diseño comienza en etapa 0. |
| 5 Preparación y piloto | Reportes integrados, recuperación probada, capacitación y producción | Aceptación operativa y fecha efectiva de inicio documentadas. |

El orden expresa dependencias; no determina un calendario ni obliga a esperar hasta el final para validar pantallas. S1 plantea dos meses de validación desde producción, no dos meses de desarrollo. La gratuidad para el cliente no elimina infraestructura ni soporte. Su modalidad comercial sigue pendiente.

## Estado para presupuestar

**Estimación condicionada por módulos.** Las hojas de administración, accesos online y flota permiten preparar una estimación de construcción nueva bajo las reglas propuestas. RF-01-T01/T02 y RF-02-T03 están listos por alcance funcional; sus horas aún requieren calibración por equipo. RF-07 está bloqueado para una cifra única hasta elegir variante; RF-09 para cerrar su integración hasta definir canal; RF-11 a RF-13 hasta resolver aislamiento y gobierno del búnker. No se estima desarrollo offline ni reutilización de código anterior. Las extensiones RP y estabilización TR-14 no se suman como compromiso aprobado.

El siguiente paso es validar D-03 con la institución y revisar los criterios de aceptación con operaciones, seguridad e informática. El agente de presupuestos podrá utilizar los cuatro archivos de esta carpeta sin reconstruir el alcance; horas, plazos y precio comercial pertenecen a esa etapa posterior.

## Contexto del equipo y evidencia de esfuerzo

Se conocen el alcance institucional, la decisión de construir desde cero y el canal online. No se informaron personas asignadas, disponibilidad efectiva, stack definitivo, experiencia con el proveedor, harness reusable ni proceso de revisión/QA para ETRACK. D-11 se pregunta en esta actualización; mientras no haya respuesta no se traslada el equipo de otro cliente.

La propuesta React/Next.js, API y PostgreSQL de ARQUITECTURA.md sigue siendo una opción técnica. No hay código previo del producto para descontar; usar componentes mantenidos o servicios administrados puede reducir implementación propia, pero exige evaluar configuración, reglas, pruebas y dependencia del proveedor. No se aplica descuento por IA ni productividad por cantidad de tareas.

El tamaño observable está en las hojas de FUNCIONALIDADES.md: flujos, variantes, estados, entidades y contratos, con frontend web separado de backend. UX, harness, diseño de contratos, revisión, QA, coordinación, DevOps y capacitación tienen responsables identificados. Una persona fullstack puede ejecutar ambos frentes; no genera una tercera categoría de horas sumable.

La duración calendario requiere capacidad y dependencias. Las esperas de decisiones institucionales afectan hitos, pero no se convierten automáticamente en horas trabajadas. No se promete un plazo a partir de un total histórico o del número de personas.

## Antecedentes de Aftercode y sus límites

### MCD como experiencia de entrega

Según S4, MCD fue ejecutado y el usuario reportó dedicaciones aproximadas: frontend alrededor de 4 h/día, fullstack alrededor de 6 h/día y backend/infra/DevOps alrededor de 2 h/día, con otros proyectos e intensidad variable. El periodo reportado va del 4 de junio a una entrega aproximada del 1 de septiembre de 2026. No son partes horarios ni permiten reconstruir un total real. No se calcula ni se utiliza el total extrapolado de 780 horas rechazado en S4.

Discovery, harness y revisión estaban cubiertos por el desarrollo de ese caso. Su utilidad para ETRACK es explicitar cobertura, no sumarlos como recargos automáticos. Los fixes del primer mes se reportaron en aproximadamente 10 h/semana del fullstack; permanecen separados de la entrega, sin multiplicarlos por semanas convencionales ni por todas las personas. Mantenimiento desde el segundo mes fue otro acuerdo.

MCD combina reglas comerciales y cálculos de presupuestos; ETRACK combina presencia multipunto, permisos y confidencialidad. Son útiles para comparar disciplina de entrega y riesgo de reglas interdependientes, no para igualar módulos, tareas del harness o velocidad. Precio de venta, pagos de herramientas compartidas y retrospectiva comercial de MCD permanecen en S4; no constituyen precios, costos o recursos asignados a ETRACK.

### AfterAccess como estimación histórica

Según S4, el alcance comparable de AfterAccess fue presupuestado pero no concretado. Su fuente de alcance seleccionada era `Propuesta Comercial - AfterAccess (2).pdf`, secciones 4–16; sus horas provenían de `Presupuestador base.xlsx`, hoja `Time sheet!B16:E29`, rotulada 29/07/2026. Estos son localizadores históricos conservados por S4, no rutas locales verificadas ni archivos abiertos en este turno.

Se conservan las horas agregadas del antecedente, **sin asignarlas a ETRACK ni repartirlas por funcionalidad**:

| Área del antecedente | Horas estimadas históricas |
| --- | ---: |
| Discovery y análisis funcional | 13 |
| Armado de harness | 26 |
| UX/UI | 4 |
| Frontend web | 80 |
| Mobile | 30 |
| Backend | 100 |
| QA | 12 |
| PM | 12 |
| DevOps | 8 |
| Total del antecedente | 285 |

Naturaleza: estimación por área, no medición ni esfuerzo ejecutado. La cobertura de revisión de PR no quedó explícita en el antecedente y no se le agregan horas. El valor histórico USD 10/h, sus costos, recargos y precios comerciales permanecen como datos del caso en S4; no se usan como parámetros de ETRACK.

La hoja `Hours`, sus 60 tareas/1.520 horas y la versión anterior de 770 horas están descartadas como fuente de este antecedente por la selección documentada en S4. No completan celdas faltantes por similitud del nombre del proyecto. Se mantiene la distinción entre valores de cálculo y valores comerciales del PDF; no se fuerza su igualdad.

La similitud útil está en identidades, sucursales, entradas/salidas, historial, auditoría y preparación de entrega. Las diferencias son materiales: AfterAccess tenía cliente mobile, sincronización offline y envío a tiendas; ETRACK es web online e incorpora personas/grupos, flota institucional y búnker. **No corresponde restar 30 horas de mobile de 285 ni añadir una cantidad inventada para búnker.** Las horas de backend no están distribuidas y no permiten aislar el offline u otro módulo. No hay antecedente comparable de esfuerzo para la custodia del búnker.

## Fuentes numéricas elegidas por dimensión

| Dimensión | Fuente elegida para ETRACK | Naturaleza, granularidad y límite |
| --- | --- | --- |
| Alcance | S1 más S2, S3 y S5; FUNCIONALIDADES.md versión 0.4 | S1 define necesidades; S2 confirma desarrollo nuevo/online; S3 pide detalle; S5 confirma web responsive para celulares. |
| Horas del proyecto | No proporcionadas en el material actual de ETRACK | No hay total ni horas por área/ID. Ausencia de dato no significa cero ni habilita copiar 285 o repartir porcentajes. |
| Costos operativos | COSTOS_OPERATIVOS.md; tarifas consultadas el 21/09/2026 y escenarios propios | Subtotales orientativos, no precio comercial ni consumo medido. Se conservan cifras y supuestos; no se refrescaron tarifas el 22/09. |
| Costo de construcción | No proporcionado ni calculado | Sin tarifa, costo de equipo ni asignación de herramientas para este proyecto. |
| Precio comercial | No proporcionado ni calculado | S1 propone modalidades sin importes. No trasladar los precios ni financiación de MCD/AfterAccess. |
| Antecedentes de esfuerzo | S4 y localizadores históricos que cita | MCD: aproximaciones reportadas; AfterAccess: 285 horas estimadas por área. Comparación cualitativa, no base numérica aprobada para ETRACK. |

Se preservan los escenarios existentes: subtotal fijo de infraestructura USD 88/mes y sensibilidades USD 91,75 y USD 106,75; alternativa de componentes separados USD 135/mes, con agregado ilustrativo de pruebas USD 16/mes; base de dos meses USD 176. Su significado, fórmulas y exclusiones pertenecen a COSTOS_OPERATIVOS.md y no se suman entre sí ni se convierten en precio del piloto. El resto de tarifas de ese archivo permanece sin cambios.

## Traspaso a presupuestos

| Campo del contrato | Entrega |
| --- | --- |
| Contrato | `relevamiento-presupuestos/v1`, leído de la referencia nueva y aplicado en este bloque. |
| Proyecto y alcance | ETRACK Access, versión 0.4 del 22/09/2026. Necesidades S1 y decisiones S2 preservadas; responsive móvil web confirmado por S5. Tareas y criterios detallados propuestos; no equivalen a aprobación institucional ni implementación. Estado global: condicionado. |
| Fuentes | Alcance canónico: `/Users/matias/Aftercode/Agents/Relevamiento/ETRACK/FUNCIONALIDADES.md`. Contexto: `/Users/matias/Aftercode/Agents/Relevamiento/ETRACK/RELEVAMIENTO.md`. Arquitectura: `/Users/matias/Aftercode/Agents/Relevamiento/ETRACK/ARQUITECTURA.md`. Operación: `/Users/matias/Aftercode/Agents/Relevamiento/ETRACK/COSTOS_OPERATIVOS.md`. Documento fuente: `/Users/matias/Downloads/ETRACK_Puntos_de_partida_para_el_desarrollo_SIN_PRECIOS (1).docx`, secciones 1–13. Mensajes S2 del 21/09, S3 y S5 del 22/09 en esta conversación. Antecedentes únicamente: `/Users/matias/Aftercode/Agents/Relevamiento/skills/relevamiento/references/casos-aftercode.md`. Selección por dimensión en la tabla precedente. |
| Modo de horas | **pendiente de elección** para la etapa de presupuestos. Este turno prepara evidencia sin calcular horas. No interpretar “todavía no generar presupuesto” como una elección permanente de omitir horas; tampoco habilita calcularlas ahora. |
| Unidades | Hojas RF-XX-TXX y TR-01 a TR-13 más TR-15, según estado y variantes seleccionadas, en FUNCIONALIDADES.md. RF padres y RNF no sumables. RP propuestas fuera de compromiso; G1/G2 excluyentes; TR-14 posterior y bloqueado. Frontend web responsive de escritorio y celulares separado de backend; mobile nativo excluido. Adaptación y QA móvil incluidos en sus hojas y TR, sin duplicación. No existe desglose numérico por ID. |
| Base de esfuerzo | Tipo/tamaño, criterios técnicos y de negocio, complejidad, incertidumbre y dependencias en cada ficha/hoja; contexto compartido al inicio del desglose. Sin reutilización de código previo; patrones internos y librerías por validar. Equipo D-11 pendiente. MCD y AfterAccess solo como antecedentes con límites descritos. |
| Valores aportados | Horas/costo de construcción/precio de ETRACK no disponibles. Escenarios operativos existentes conservados con fecha y naturaleza. Horas históricas de AfterAccess mantienen agregados por área; MCD conserva aproximaciones, sin inventar total ni reparto. |
| Pendientes | RF-01-T01/T02 y RF-02-T03 listos por alcance; resto de base condicionado. RF-07 bloqueado para variante única, RF-09 para integración y RF-11 a RF-13 para aislamiento institucional. Detalle en matriz canónica; D-03 a D-11 permanecen abiertos donde no hay confirmación. |
| Cambios | Versión 0.3 → 0.4: S5 confirma responsive móvil; RNF-07, hojas web por herencia, TR-03/TR-05/TR-08 y traspaso actualizados sin horas nuevas. Se conserva el cambio 0.2 → 0.3: RF-01 a RF-18 conservados y desglosados; RP-01 a RP-07 preservados, sin aprobación tácita; RNF-01 a RNF-09 vinculados a responsables; TR-01 a TR-15 agregados como cobertura; D-11 añadido. Sin estimaciones de construcción anteriores disponibles que recalcular. Valores operativos sin cambios. |
| Próxima acción autorizada | Completar este traspaso documental y registrar decisiones que el usuario aporte. No iniciar presupuesto, crear HORAS_HOMBRE.md, publicar en Drive, hacer commit ni push. Cuando el usuario pida presupuestar, elegir modo de horas y resolver solo vacíos materiales por ID. |

Presupuestos debe reutilizar esta misma carpeta. Si recibe una decisión o una discrepancia, debe devolver el ID afectado y el efecto esperado para actualizar el alcance canónico, no crear un backlog paralelo. Las partes bloqueadas deben permanecer visibles; un subtotal de las hojas listas no es el total del proyecto.

## Cambios y verificación de esta actualización

Se conserva la versión de las decisiones aprobadas; la fecha 22/09 es la actualización documental. La superficie mobile incluida es navegador web responsive; no se agrega una app nativa ni reutilización del producto previo. RF-18 se desglosa como trabajo de preparación operativa; DevOps, QA y revisión tienen cobertura única en TR.

Se revisan cobertura de los 18 RF y 9 RNF, continuidad de los 7 RP, unicidad de hijos y referencias, exclusión de variantes no aprobadas y conservación de cifras previas. No se ejecutan pruebas del producto: todavía se está definiendo su trabajo. La validación estructural de los espejos y cuatro contratos del agente pasó en modo de lectura; no se editan sus instrucciones.

La versión 0.4 corrige la expresión ambigua “mobile excluido” de la entrega anterior: solo se excluye el cliente nativo. Responsive móvil es alcance confirmado; la adaptación y las pruebas deben contemplarse al estimar las hojas existentes. No hay horas de construcción calculadas que modificar ni cambios en cifras operativas.
