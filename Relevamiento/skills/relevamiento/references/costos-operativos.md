# Costos operativos y escenarios

## Tres cuentas separadas

1. **Construcción:** esfuerzo de desarrollo, migración y puesta en marcha. Identificar los trabajos necesarios; el presupuestador estima sus horas.
2. **Operación:** infraestructura, servicios, licencias y mantenimiento recurrente.
3. **Precio comercial:** importe, margen y condiciones que decide Aftercode. No deducirlos automáticamente de los costos.

Distinguir costos únicos, mensuales, anuales y variables por consumo. Identificar quién paga cada concepto y evitar sumarlo dos veces como gasto del cliente y de Aftercode.

## Modelo de consumo

Antes de calcular, identificar los impulsores de uso: usuarios activos y concurrentes, operaciones, almacenamiento acumulado, transferencia, mensajes, duración de trabajos, tokens o dispositivos según el caso.

Definir escenarios de inicio, uso esperado y crecimiento solo si aportan información. Registrar las cantidades aportadas por el usuario; las restantes son supuestos para sensibilidad, no previsiones confirmadas. No usar “10 veces más usuarios” como sustituto automático de diez veces todo el consumo.

Para cada servicio registrar:

- Proveedor, producto, plan y región cuando cambie la tarifa.
- Moneda, fecha de consulta, URL oficial y dato verificado.
- Cargo base, unidad de cobro, cantidad incluida, excedentes y escalones.
- Restricciones relevantes: uso comercial, disponibilidad, retención, cuotas o límites del plan.
- Cantidad del escenario, fórmula, subtotal y exclusiones.
- Estado del precio y del consumo: verificado, aportado o pendiente.

## Investigación de precios

Consultar páginas oficiales y, cuando sea necesario, calculadoras y documentación de facturación. Mantener los precios fuera de las instrucciones permanentes del agente.

No asumir que un plan gratuito cubre producción. Comprobar sus condiciones. Tampoco trasladar tarifas, márgenes o costos de otro cliente o plantilla.

Si no hay acceso web o la cotización es privada, usar variables o precios aportados, indicando su origen. No presentar un total cerrado si faltan componentes: mostrar **subtotal de rubros conocidos** y listar los pendientes.

## Cálculo verificable

Para una tarifa simple:

`costo mensual = cargo base + max(0, consumo - consumo incluido) × tarifa de excedente`

Esta expresión solo aplica cuando el proveedor factura así. Para bloques, escalones, mínimos, asientos o compromisos anuales, usar la regla real. Verificar unidades y conversiones; no confundir precio por mil operaciones con precio por operación.

- Prorratear costos anuales solo como equivalente mensual y mostrar también el desembolso real.
- Calcular almacenamiento y retención acumulados, y tráfico saliente, cuando sean relevantes.
- Si hay IA, separar entradas, salidas, caché y herramientas según el servicio.
- Incluir los ambientes y servicios necesarios: producción, pruebas, backups, logs, dominio, correo, mensajes y otros rubros aplicables.
- Mantener mantenimiento y soporte como rubros identificados; no asignar horas ni tarifa sin una fuente o un supuesto explícito.
- Aclarar tratamiento de impuestos y conversión de moneda. No sumar monedas distintas sin tipo de cambio, fuente y fecha.
- No confundir un descuento inicial o créditos promocionales con costo recurrente sostenible.
- Reconciliar filas, subtotales y escenarios con una calculadora o código para cálculos no triviales. Mostrar la fórmula y el criterio de redondeo.

## Entrega

Usar una tabla por componente con escenario, fórmula y fuente. Explicar qué conceptos dominan el costo y qué cambios de consumo o plan alteran la conclusión.

Un límite presupuestario sirve para comparar opciones. Si ninguna satisface requisitos y límite, explicar el conflicto y presentar ajustes de alcance o servicio; no reducir requisitos silenciosamente.

No contratar, redimensionar ni eliminar recursos al analizar costos. Una propuesta de optimización es una recomendación hasta que se autorice su ejecución.
