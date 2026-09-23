# Etrack Access costos operativos preliminares

Actualización documental: 22 de septiembre de 2026. Versión 0.4. Consulta de tarifas conservada: 21 de septiembre de 2026; sin nueva consulta ni cambios numéricos en esta actualización. Moneda: USD. Estado: escenarios orientativos con subtotales conocidos; no constituyen cotización ni costo total cerrado.

## Lectura del costo

La infraestructura básica puede modelarse, pero el costo completo depende de aislamiento del búnker, recuperación, notificaciones y soporte. El usuario confirmó desarrollo nuevo y operación web exclusivamente online el 21/09/2026, fuente S2. No se incluye costo de desarrollo offline. No se ha elegido proveedor ni contratado recursos. La gratuidad de dos meses de validación mencionada en S1 es una condición comercial propuesta, no ausencia de costos.

Se separan construcción, operación y precio comercial. Este archivo cubre operación y enumera trabajos únicos. Las horas, honorarios, margen y precio al cliente corresponden a presupuestos. Alcance: [FUNCIONALIDADES.md](FUNCIONALIDADES.md). Alternativas técnicas: [ARQUITECTURA.md](ARQUITECTURA.md).

## Datos conocidos y escenarios de consumo

S1 indica aproximadamente 45 a 50 vehículos. Los ejemplos de cuatro, seis o diez accesos no fijan un número contratado. No informa usuarios simultáneos, visitas diarias, historial ni tasa de consultas.

Los siguientes valores son **supuestos para sensibilidad**, no previsiones ni límites prometidos. “Visita” es un ciclo de entrada/salida; grupos contados solo por cantidad pueden producir otro patrón de registros.

| Variable | Piloto ilustrativo | Uso institucional ilustrativo | Crecimiento ilustrativo |
| --- | --- | --- | --- |
| Sedes / puntos | 1 / 4 | 3 / 10 | 8 / 25 |
| Sesiones simultáneas | 8 | 25 | 60 |
| Visitas diarias | 300 | 1.500 | 5.000 |
| Viajes de flota diarios | 30 | 100 | 200 |
| Días activos por mes | 30 | 30 | 30 |
| Eventos de movimiento por mes | 19.800 | 96.000 | 312.000 |
| Transferencia mensual supuesta | 10 GB | 50 GB | 150 GB |

Fórmula de eventos: 2 × (visitas diarias + viajes diarios) × días activos. No incluye auditoría de consultas, incidencias ni reintentos. No hay un volumen de búnker confirmado; si sus visitas no están contenidas en el supuesto, deben agregarse por separado.

Para ilustrar acumulación, usando 2 KB decimales por evento persistido incluyendo índices, un año generaría 0,48 GB, 2,30 GB o 7,49 GB respectivamente. Es una hipótesis que debe medirse. No incluye personas, sesiones, consultas auditadas, archivos, logs, copias ni espacio de trabajo. En el búnker, muchas consultas pueden generar más datos de auditoría que de movimientos.

Modelo a completar: almacenamiento retenido = histórico inicial + eventos mensuales × tamaño medido × meses retenidos + auditoría + otras tablas. El espacio de respaldos se calcula aparte. Con borrado o archivo por retención, la acumulación cambia.

## Tarifas verificadas de referencia

Se utiliza Render para construir un ejemplo coherente de aplicación más base en una misma plataforma. No supone que cumpla la residencia exigida por la institución. Región de referencia a evaluar: Virginia; selección pendiente de política y mediciones de latencia.

| Componente Render | Unidad | Tarifa publicada |
| --- | --- | --- |
| Workspace Pro | Mensual por workspace | USD 25 |
| Servicio web 1c-2g | Mensual por instancia | USD 25 |
| Servicio web 0.5c-512mb | Mensual por instancia | USD 7 |
| PostgreSQL 0.5c-1g | Mensual por instancia | USD 19 |
| PostgreSQL 0.1c-256mb | Mensual por instancia | USD 6 |
| Almacenamiento PostgreSQL | GB provisionado por mes | USD 0,30 |

Fuente: [tarifas oficiales de Render](https://render.com/pricing). Los tamaños son supuestos de partida para validar, no capacidad certificada para Etrack. Producción y pruebas se cuentan separadamente. No se propone cómputo gratuito para sostener la operación institucional.

Pro publica 25 GB de transferencia saliente incluidos y USD 0,15 por GB adicional. Fórmula usada: max(0, GB facturables agregados del workspace − 25) × 0,15. Es una cuota compartida; no multiplicarla por instancia. [Planes de Render](https://render.com/docs/new-workspace-plans) y [transferencia saliente](https://render.com/docs/outbound-bandwidth).

## Configuración base para comparación

Operación online confirmada. Supuestos técnicos: web y API servidas por una aplicación, tres módulos con aislamiento lógico y sin alta disponibilidad. Ambiente de pruebas pequeño y sin datos confidenciales reales. Dos bases con 10 GB provisionados cada una. No hay trabajador separado: las tareas diferidas se procesan inicialmente dentro del servicio con persistencia de trabajos.

| Rubro | Cálculo mensual | Subtotal USD |
| --- | --- | --- |
| Workspace | 1 × 25 | 25,00 |
| Aplicación de producción | 1 × 25 | 25,00 |
| Base de producción | 1 × 19 | 19,00 |
| Disco de producción | 10 × 0,30 | 3,00 |
| Aplicación de pruebas | 1 × 7 | 7,00 |
| Base de pruebas | 1 × 6 | 6,00 |
| Disco de pruebas | 10 × 0,30 | 3,00 |
| **Subtotal fijo conocido** | **Suma de los siete rubros** | **88,00** |

Con 10 GB de transferencia mensual supuesta, el subtotal continúa en USD 88,00. Con 50 GB, resulta USD 91,75. Con 150 GB, USD 106,75. Estos cambios solo muestran sensibilidad a transferencia manteniendo los mismos recursos; **no prueban que esa configuración soporte los tres escenarios de carga**. Si las pruebas exigen más memoria, CPU, disco o instancias, debe recalcularse.

Si el búnker necesita un servicio y una base adicionales con tamaños equivalentes a producción, sumar 25 + 19 + 3 = **USD 47,00/mes**: subtotal fijo USD 135,00 antes de otros rubros. Es solo una separación de componentes dentro del mismo workspace, no custodia independiente ni alta disponibilidad. Duplicar también su entorno de pruebas añade 7 + 6 + 3 = USD 16,00/mes. Un workspace independiente, claves administradas u otros controles se agregan según D-03.

## Alternativa administrada para datos e identidad

Supabase es una alternativa a evaluar si se aprovechan sus servicios administrados. Pro cuesta USD 25/mes, incluye USD 10 de créditos de cómputo y referencia Micro a aproximadamente USD 10/mes por proyecto; dos proyectos Micro implican aproximadamente 25 + 20 − 10 = **USD 35/mes**. Esto sustituiría la parte de datos pertinente, no se suma automáticamente al PostgreSQL de Render. Faltan hosting de la aplicación y demás rubros. [Planes](https://supabase.com/pricing) y [cómputo](https://supabase.com/docs/guides/platform/manage-your-usage/compute).

La facturación de cómputo es horaria, por lo que el importe exacto varía con las horas del ciclo. Pro incluye respaldos diarios con siete días de retención; recuperación a un instante tiene un adicional publicado desde aproximadamente USD 100/mes por proyecto para siete días, sujeto a requisitos de cómputo. [Respaldos Supabase](https://supabase.com/docs/guides/platform/backups). No se utiliza ese adicional para construir un total comparativo incompleto.

La comparación debe considerar recuperación, conexiones, ubicación, cuotas y operación conjunta. Un menor cargo base no decide la arquitectura del búnker.

## Rubros aún sin precio o consumo definido

| Rubro | Unidad o fórmula a completar | Frecuencia y responsable |
| --- | --- | --- |
| Dominio | Tarifa anual de dominio elegido; equivalente mensual = anual / 12 | Anual; titular y pagador a acordar. |
| Copias independientes | GB retenidos × tarifa + solicitudes + recuperación + proceso de copia | Mensual/consumo; operador designado. |
| Logs y monitoreo | Volumen ingerido, retención y alertas | Mensual; Aftercode o informática según acuerdo. |
| Correo transaccional | Plan y cantidad de envíos; dominio remitente | Mensual/consumo si se usa en recuperación o avisos. |
| SMS, WhatsApp u otros canales | Mensajes, destino y proveedor | Solo si D-06 los selecciona; no hay canal externo confirmado. |
| Identidad institucional o segundo factor comercial | Usuarios, conexiones o licencia | Según método; no presumir costo por usuario si el mecanismo elegido no lo tiene. |
| Alta disponibilidad y recuperación exigente | Réplicas, instancias, almacenamiento y red | Según RPO/RTO; no incluido en la base. |
| Puestos y conectividad | Equipos, UPS o enlace de Internet de respaldo si se requieren | Rubros institucionales separados; no incluyen servidor para modo offline. |
| Búnker con custodia separada | Cuentas, claves, redes, copias y soporte restringido | Según D-03; no cubierto por sumar una base solamente. |
| Soporte y mantenimiento | Cobertura × recursos/tarifa acordados | Mensual; no se asignan horas o precio en esta etapa. |
| Auditoría técnica externa | Alcance y cotización del servicio | Por hito o periódica si se exige. |
| Excedentes del proveedor | Transferencia, compilaciones, dominios u otras unidades facturables | Consumo real y planes definitivos. |

Los valores publicados se presentan antes de impuestos, percepciones, comisiones y conversión de moneda. No se fija tipo de cambio. Las cuotas compartidas con otros proyectos deben distribuirse por un criterio explícito; el ejemplo supone recursos destinados a Etrack y evita duplicar el workspace por servicio.

## Gastos únicos y periodo de validación

La configuración y carga inicial, capacitación, pruebas de seguridad, ensayo de recuperación y puesta en marcha son trabajo de construcción/preparación. La migración histórica no está incluida. Equipamiento de puestos sería una compra adicional si se requiere. No se convierten aquí en importes.

Si se adoptara la base ilustrativa durante dos meses completos, el **subtotal fijo de infraestructura sería USD 176,00**. No representa el costo del piloto: faltan preparación, infraestructura durante desarrollo, soporte, consumos y rubros pendientes. El costo de esos meses debe asignarse a Aftercode o a la institución según acuerdo; no contarlo dos veces.

Fórmula operativa final: subtotal de infraestructura seleccionada + consumos + copias + monitoreo + comunicaciones + licencias aplicables + soporte + impuestos/comisiones. El precio comercial puede tener otra estructura y no se deriva automáticamente de esta suma.

## Qué cambia la conclusión

Los impulsores principales son la exigencia de continuidad, la separación real del búnker, la retención de consultas auditadas y la cobertura de soporte. Cantidad de sedes y usuarios ayudan a dimensionar, pero no sustituyen medir operaciones simultáneas, consultas y tráfico de actualizaciones.

Para cerrar el modelo hacen falta D-03, D-06, D-07 y D-08, una prueba de carga y la selección de cuentas/región. D-01 y D-02 están resueltas por S2. Hasta entonces, comunicar **subtotales orientativos de infraestructura**, no un costo mensual total ni una promesa de capacidad.

## Relación con las tareas de construcción

El desglose versión 0.4 está en [FUNCIONALIDADES.md](FUNCIONALIDADES.md). TR-12 comprende el trabajo de configurar infraestructura, secretos y ambientes; TR-13, el de configurar y ensayar recuperación; TR-15, el despliegue de la versión validada. Las tarifas de servidores, almacenamiento y respaldos de este archivo son gastos operativos distintos de ese esfuerzo humano. Una tarifa mensual no permite deducir horas de DevOps.

RF-09 comprende el trabajo de integración del canal que se elija; los mensajes o suscripción del proveedor se registran aquí como operación. RF-18 comprende carga inicial, documentación/capacitación y aceptación operativa. TR-14 se reserva para estabilización posterior condicionada; su periodo y dedicación no se deducen de los dos meses de validación. El mantenimiento recurrente requiere otro acuerdo de cobertura, sin duplicar incidencias ya incluidas en estabilización.

Las suscripciones de herramientas del equipo, incluido Codex si se usa, no tienen importe ni asignación aportados para ETRACK. Cualquier costo bruto compartido y su criterio de asignación deben declararse antes de imputarlo al proyecto. No se copian pagos ni tarifas históricas de MCD/AfterAccess. Este apartado no agrega cargos, horas o precios a las cifras ya conservadas.

S5 confirma la web responsive para celulares. Su diseño, adaptación y QA se contemplan como esfuerzo de construcción en las hojas web y TR-03/TR-05/TR-08; no genera una partida de app nativa ni licencias de tiendas. Esta aclaración no recalcula consumos ni modifica los valores operativos existentes.
