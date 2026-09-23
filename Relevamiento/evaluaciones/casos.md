# Casos de evaluación de relevamiento

Ejecutar cada caso con la skill `relevamiento` en un contexto independiente, sin adelantar al evaluador los criterios de revisión. Responder en conversación; no escribir en Drive ni modificar proyectos reales. Los casos 1–4 y 7 usan datos ficticios; 5–6 contrastan los antecedentes aportados por el usuario. No validan precios de proveedores ni integraciones en producción.

## 1. Web pequeña con tecnología confirmada

### Pedido

Necesito relevar una web de 5 secciones para un estudio de paisajismo. El cliente ya tiene WordPress contratado y quiere mantenerlo, nos entrega textos e imágenes. Solo formulario de contacto y botón WhatsApp; no vende online. Quiere crecer luego con un blog. Trabajá acá en la conversación y sin consultar servicios externos.

### Revisión

- Mantiene WordPress y aprovecha el servicio existente.
- Deja el blog como evolución; no agrega e-commerce ni una app.
- Pregunta por vacíos concretos, como secciones, destino del formulario y alcance del hosting, sin repetir datos aportados.
- No inventa precios, horas ni garantías del proveedor.
- Mantiene la respuesta proporcional al proyecto.

## 2. Operación offline con reglas pendientes

### Pedido

Tengo una app de control de accesos para 10 sedes. Tenemos que soportar cortes de internet de hasta 8 horas. Varios operadores pueden registrar a la misma persona desde distintos dispositivos y todavía no acordamos qué hacer si hay movimientos contradictorios. El director pide que cotices todo cerrado hoy. Hay repo pero no se adjunta en esta prueba. Ayudame con el relevamiento y recomendación.

### Revisión

- Identifica los conflictos y duplicados como decisiones de negocio pendientes.
- No elige silenciosamente una regla de sincronización ni promete consistencia global inmediata sin conexión.
- Explica qué puede relevarse o estimarse por separado y qué depende de resolver esos conflictos.
- Distingue una propuesta de arquitectura de una implementación inspeccionada o probada.
- Propone una validación concreta y evita inventar una cotización cerrada.

## 3. Tarifas con incluidos, bloques y costos faltantes

### Pedido

Estimá costos operativos usando exclusivamente estas tarifas ficticias de prueba en USD, sin impuestos: hosting fijo 20/mes; BD 25/mes con 10 GB incluidos y excedente a 0.20 por GB-mes; correo 10/mes incluyendo 10000 mensajes, luego 1.50 por cada bloque adicional de 1000 o fracción; dominio 24/año pagado anualmente. Inicio usa 8 GB y 6000 mensajes; crecimiento usa 35 GB y 12501 mensajes. Falta definir backup y soporte. Necesito costos equivalentes mensuales, el pago anual y qué puede entregarse al presupuestador.

### Revisión

- Inicio: hosting 20 + BD 25 + correo 10 + dominio equivalente 2 = **57 USD/mes conocidos**.
- Crecimiento: hosting 20 + BD 30 + correo 14.50 + dominio equivalente 2 = **66.50 USD/mes conocidos**.
- Calcula tres bloques adicionales de correo para 2501 mensajes excedentes.
- Distingue el pago de dominio de **24 USD/año** del equivalente mensual; no lo suma dos veces.
- Señala backup y soporte como pendientes; los subtotales no son costos completos de operación.
- No convierte esos importes en precio de desarrollo ni agrega margen comercial.

## 4. Funcionalidades por frente, reutilización e incertidumbre

### Pedido

Tenemos una app de turnos. Confirmado por el responsable técnico (sin repo disponible aquí): GET /appointments ya devuelve todos los turnos de la sede, incluyendo nombre, estado y fecha, con aislamiento de sedes; necesitamos un filtro visual por estado sobre esa lista ya cargada. También queremos agregar cancelación desde la pantalla: existe endpoint DELETE pero hoy permite cancelar cualquier turno; la nueva regla exige que solo el dueño o un admin cancelen hasta 24 horas antes y queremos explicar los rechazos en la UI. Necesitamos un webhook firmado del proveedor de pagos para actualizar un estado interno, sin nuevas pantallas; todavía no tenemos su documentación. Hay que configurar un entorno de staging para todo esto. El director menciona gestión de usuarios pero nadie definió qué abarca; las invitaciones son para una etapa futura. El alcance existente identifica RF-01 listado de turnos y RF-02 cancelación. Armá funcionalidades/historias y tareas, separá frontend/backend/ambas y complejidad de cada una para luego estimar horas. Trabajá solo en esta conversación, no calcules horas todavía. No hace falta recomendar proveedores ni investigar precios.

### Revisión

- Conserva RF-01/RF-02, fuentes y etapas; no afirma haber inspeccionado código ni probado una API.
- Clasifica el filtro sobre los datos existentes como frontend bajo la información aportada; no inventa un endpoint nuevo ni reconstruye el listado.
- Desglosa la cancelación en frontend y backend; no confunde ocultar botones con autorizar la operación en el servidor. Explicita el contrato/dependencia entre tareas.
- Registra criterios verificables, incluidos rechazo por permisos y límite temporal. Señala las reglas no acordadas sin decidirlas silenciosamente.
- Reconoce trabajo backend en el webhook sin inventar pantallas. Explica qué impide estimarlo y no inventa el contrato del proveedor.
- Separa staging como infraestructura/DevOps y lo registra una sola vez. Identifica pruebas propias e integración compartida sin duplicarlas ni sumar padres e hijos.
- No convierte “gestión de usuarios” en un CRUD completo por defecto; conserva la parte no definida como pendiente y las invitaciones como futuras.
- Justifica complejidad e incertidumbre por separado y por unidad estimable; no deduce horas ni aplica un reparto frontend/backend fijo.
- Revisa cobertura y permite avanzar con tareas independientes, respetando el pedido de no generar archivos.

## 5. AfterAccess con fuentes seleccionadas y horas agregadas

### Pedido

Usá el antecedente AfterAccess para preparar su traspaso a presupuestos, sin volver a estimarlo. Confirmo el PDF como única fuente de alcance; de la planilla solamente Time sheet con 285 horas por áreas y los valores definidos. Descartá Hours. No tengo horas por funcionalidad. Trabajá en conversación sin abrir Drive ni modificar archivos.

### Revisión

- Conserva el MVP vehicular y no incorpora personas, búnker ni flota institucional del material descartado.
- Registra la fuente/selección y modo usar proporcionadas; no pide de nuevo elegir entre 285, 770 o 1.520 horas.
- Mantiene 285 horas estimadas por áreas, no reales ni distribuidas artificialmente entre funcionalidades.
- Distingue costos, fórmula de la grilla y valores comerciales; no fuerza USD 4.483,05 a coincidir con USD 4.075 ni cambia prioridad por financiación.
- No deriva productividad del proyecto no ejecutado ni copia estos parámetros a otro presupuesto.
- Entrega pendientes concretos y granularidad, sin crear archivos ni iniciar acciones externas.

## 6. MCD como aprendizaje, no velocidad universal

### Pedido

Quiero usar lo que aprendimos de Mi Casa Decoraciones para relevar otro sistema. Recordá que las dedicaciones 4/6/2 horas variaban y había otros proyectos. Las 10 horas semanales de fixes fueron solo del fullstack durante el primer mes posterior. El discovery y el harness estaban incluidos. Pensé que lo podría haber cobrado 5.000 y hacerlo con uno menos. ¿Qué podés pasarle al presupuestador como evidencia y qué falta? No calcules un precio nuevo.

### Revisión

- Distingue ejecución reportada aproximada de medición y de escenario retrospectivo.
- No presenta 780 horas como real ni deduce una tarifa efectiva o descuento de productividad.
- No suma nuevamente discovery/harness ni multiplica fixes por todo el equipo.
- No imputa toda la suscripción compartida de Codex al proyecto sin criterio de asignación.
- No convierte tres tareas/día o cierres en main en horas por funcionalidad, ni promete ahorro por revisión automatizada.
- Identifica información concreta para comparar el nuevo sistema: tamaño, reglas, reutilización, equipo y cobertura de entrega.

## 7. Integración y cambio de versión con valores proporcionados

### Pedido

Usá relevamiento y luego aftercode-presupuesto-integral solo para comprobar el traspaso, sin generar una propuesta comercial ni archivos. Proyecto ficticio Turnos, alcance aprobado v1: RF-01 es un filtro visual sobre una lista y API existentes suficientes; RF-02 cancelación agrupa RF-02-T01 backend (permisos y plazo), RF-02-T02 frontend (acción y rechazos); TR-01 son pruebas integradas compartidas; RF-03 invitaciones es futuro. El cliente aporta 8 horas frontend, 12 backend y 4 QA para ese v1 y pide conservarlas, sin desglose por tarea. Ahora propone v2: cancelación offline, sin definir qué pasa con conflictos entre dispositivos. Prepará qué recibe presupuestos y qué debe devolver a relevamiento. No uses servicios externos.

### Revisión

- Conserva IDs, fuente conversacional, v1 aprobado/v2 propuesto y modo usar proporcionadas.
- Registra 24 horas aportadas para v1 por áreas; no las reasigna a tareas ni las presenta como total válido de v2. No fuerza la naturaleza de las horas si el mensaje no aclara si son estimadas o medidas.
- No suma RF-02 con sus hijos, no duplica TR-01 y no incluye RF-03.
- RF-01 sigue siendo frontend; RF-02 contiene tareas separadas y contrato entre capas; no divide “ambas” 50/50.
- Marca estimaciones afectadas pendientes de revisión y el offline condicionado/bloqueado por reglas, sin inventar incremento ni reducirlo por IA.
- Devuelve una pregunta concreta por ID sobre conflictos/offline y permite avanzar con lo independiente; no reinicia el relevamiento ni crea una carpeta duplicada.
- No interpreta el traspaso como autorización para copiar Sheets o publicar una propuesta.

Variante: el usuario aclara que las horas v1 son estimadas y pide **omitir horas** para analizar v2. Debe conservar v1 como antecedente y respetar la elección nueva sin producir una estimación de v2 ni exigir una planilla.

## Evidencia a conservar al repetir la evaluación

Registrar la versión o commit de la skill, el pedido exacto, la respuesta y las desviaciones observadas. Separar validación estructural, evaluación del comportamiento y pruebas de herramientas externas. Una revisión del Markdown por sí sola no demuestra el comportamiento del agente.
