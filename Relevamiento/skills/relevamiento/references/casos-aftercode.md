# Antecedentes internos de Aftercode

Registro de aprendizaje consolidado el 2026-09-22 a partir de los documentos analizados y las aclaraciones de Matías en esta conversación. No es una base estadística ni acredita horas medidas. Usar para preparar estimaciones internas; no copiar precios, dedicaciones ni información de un cliente a propuestas de otro.

Los archivos originales permanecen fuera de la skill. Sus nombres y localizadores identifican la evidencia, pero no garantizan disponibilidad en otro equipo. Si se necesita profundizar, pedir la fuente correspondiente; no afirmar que se volvió a leer. Una corrección explícita posterior del usuario prevalece sobre este registro.

## MCD — Mi Casa Decoraciones

**Naturaleza:** proyecto ejecutado; dedicación reportada aproximada, sin registro completo de horas.

**Fuentes:** `Presupuesto sistema central Mi Casa Decoraciones (1).pdf` aportado por el usuario, aclaraciones del equipo y estudio de Git de `MCD-Backend` / `MCD-Frontend`. El usuario confirmó que se entregó exactamente el MVP del presupuesto original.

### Alcance y dedicación

- MVP: clientes y consultas comerciales, presupuestos con productos/ambientes/medidas y reglas de cálculo, versiones interna/comercial, integración Tango según acceso y viabilidad, panel básico y usuarios/roles. La propuesta original conserva el detalle y las condiciones; este resumen no lo sustituye.
- Inicio reportado: 4 de junio; entrega aproximada: 1 de septiembre. El historial estudiado corresponde a 2026. El inicio del trabajo no se deduce del primer commit.
- Tres personas: frontend alrededor de 4 h/día; fullstack alrededor de 6 h/día; backend/infra/DevOps alrededor de 2 h/día.
- Hubo otros proyectos en paralelo y días/semanas de distinta intensidad. Las dedicaciones no son partes horarios ni prueban una jornada fija durante todo el período.
- Relevamiento, armado del harness y revisión de PR estaban dentro del tiempo de desarrollo y del precio. No sumarlos nuevamente.
- Primer mes después de la entrega: fixes de aproximadamente 10 h/semana, exclusivamente del fullstack. Mantenerlo separado del esfuerzo preentrega, sin multiplicarlo automáticamente por un mes convencional ni por tres personas. Desde el segundo mes se indicó mantenimiento cobrado por separado.

### Valores y límites

- Precio reportado: USD 3.900, en tres cuotas. Es precio de venta, no costo ni prueba de rentabilidad.
- Se reportaron tres pagos de USD 100 del plan de Codex, usado también en otros proyectos. La porción atribuible a MCD no está determinada.
- Retrospectiva de Matías: posiblemente cobrar alrededor de USD 5.000 y hacerlo con un desarrollador menos. Es un escenario de aprendizaje, no evidencia de que se habría entregado el mismo alcance/plazo con menos horas totales.
- No hay total de horas reales verificado ni distribución por funcionalidad. **780 horas no es un dato del caso:** proviene de una extrapolación de jornadas constantes que no refleja la variabilidad aclarada. No usarlo ni derivar de él una tarifa efectiva.

### Qué aportó Git

El estudio de primeras apariciones de `status=done` en la línea principal encontró, hasta el 1 de septiembre de 2026 inclusive, 67 entradas de backend y 90 de frontend. Son tareas heterogéneas del harness, no 157 funcionalidades comerciales comparables ni tiempos de implementación. Hubo agrupaciones de cierres, renumeraciones y código integrado con revisión/cierre aún pendientes.

Snapshots consultados: backend `c807176bb340e59af01e54660723c0e4663d0cba`; frontend `96976c9933b448a4cd90dacc406855faa36b5d1d`, ambos con cambios hasta el 18 de septiembre. Son cortes históricos, no afirmaciones sobre el estado actual de los repositorios. Matías recordó aproximadamente tres tareas backend por día; eso no valida una conversión tareas/día→horas.

**Uso útil:** hacer visibles discovery, harness, revisión, coordinación y estabilización; vincular funcionalidades comerciales con tareas y evidencias de entrega. La posible automatización de revisión es una mejora a medir, no un descuento garantizado.

## AfterAccess — presupuesto no concretado

**Naturaleza:** estimación y propuesta comercial; no existe ejecución de este alcance que valide sus horas. No confundirlo con trabajo en la aplicación anterior ni con otras versiones presupuestadas.

### Selección de fuentes confirmada por el usuario

- Alcance, funcionalidades, exclusiones y condiciones comerciales: únicamente `Propuesta Comercial - AfterAccess (2).pdf` (secciones 4–16).
- Horas y valores de cálculo: `Presupuestador base.xlsx`, hoja **`Time sheet`**, rotulada 29 de julio de 2026. Conservarlos tal como fueron definidos, sin reestimar.
- Hoja **`Hours` excluida**: sus 60 tareas/1.520 horas corresponden a otro alcance y no se usan para completar este MVP ni para distribuir sus horas.
- No sustituir esta selección por cifras de versiones anteriores, por ejemplo 770 horas. La precedencia de fuentes está resuelta; no reabrirla sin nueva evidencia material.

### Alcance del PDF

Reconstrucción del control vehicular con app móvil, panel web, backend y PostgreSQL. Incluye usuarios/roles, sucursales, ingresos/egresos, patente, acompañantes, presentes/historial, operación offline, cola persistente/reintentos, sincronización e idempotencia, dashboards, auditoría/correcciones, estadísticas/reportes, infraestructura y envío a tiendas Android/iOS.

Excluye migración histórica, control de personas/edificios/empresas/proveedores/visitas, QR/OCR, hardware, pagos/facturación automática y alta pública de clientes. Preparar la arquitectura para crecer no incluye desarrollar esos módulos. No incorporar el búnker ni la gestión de flota institucional de la hoja descartada.

Plazo ofrecido: 8–10 semanas desde congelar alcance; termina con producto enviado a revisión, no con aprobación garantizada de las tiendas. Esto no demuestra capacidad de equipo ni ejecución de 285 horas en ese plazo.

### Horas estimadas por área

Fuente: `Time sheet!B16:E29`. Valor usado: USD 10/h para todas las áreas; no se establece como tarifa general de Aftercode.

| Área | Horas previstas |
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
| Total | 285 |

Son estimaciones agregadas, no horas por funcionalidad ni horas reales. No hay desglose aprobado que permita asignar, por ejemplo, una parte de las 100 horas de backend al offline o a autenticación. La cobertura de revisión de PR dentro de estas áreas no está explicitada; señalarla sin añadir horas al valor suministrado.

### Costos y precios, sin mezclarlos

Fuente de cálculo: `Time sheet!B31:E47`. Mano de obra: USD 2.850. Otros costos previstos: Codex 2 × USD 50 = USD 100; infraestructura USD 60; Apple USD 100; Android USD 25. Total adicional USD 285; costo previsto total USD 3.135. Conservar como supuestos históricos de la planilla, no tarifas vigentes verificadas ni gastos efectivamente realizados.

La fórmula de E47 es `(E43*(1+E45))*(1+E46)`: aplica 30% de recargo sobre costo y luego 10% rotulado prioridad, obteniendo USD 4.483,05. El rótulo “margen” no transforma el recargo en margen sobre ventas. No modificar la fórmula ni equiparar prioridad con financiación.

El PDF conserva valores comerciales propios: opción A USD 4.075 (contado USD 3.900); opción B USD 2.500 (contado USD 2.400). Operación USD 180/mes; en B además USD 20 por sucursal activa/mes; evolución opcional USD 15/h o 10 h por USD 150. Financiación extendida publicada: A USD 4.482; B USD 2.748. Son valores ofrecidos, no ingresos cobrados. No forzar igualdad con E47 ni corregir redondeos/condiciones sin pedido explícito.

**Uso útil:** separar costos/horas por área, trabajo compartido y compromisos operativos; mantener trazabilidad entre alcance y números. No usar las 285 horas, USD 10/h o recargos como parámetros automáticos de nuevos proyectos.
