# Casos de evaluación de relevamiento

Ejecutar cada caso con la skill `relevamiento` en un contexto independiente, sin adelantar al evaluador los criterios de revisión. Responder en conversación; no escribir en Drive ni modificar proyectos reales. Estas pruebas usan datos ficticios y no validan precios de proveedores ni integraciones en producción.

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

## Evidencia a conservar al repetir la evaluación

Registrar la versión o commit de la skill, el pedido exacto, la respuesta y las desviaciones observadas. Separar validación estructural, evaluación del comportamiento y pruebas de herramientas externas. Una revisión del Markdown por sí sola no demuestra el comportamiento del agente.
