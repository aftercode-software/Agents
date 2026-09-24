# Etrack Access - operación preliminar del piloto Senado

Actualización: 23/09/2026. Versión 0.2. Moneda de referencia: USD. Estado: **escenario ilustrativo, sin proveedor ni cuentas aprobadas**. Tarifas consultadas en fuentes oficiales el 23/09/2026; verificar antes de contratar. Alcance: [FUNCIONALIDADES.md](FUNCIONALIDADES.md); stack y despliegue: [ARQUITECTURA.md](ARQUITECTURA.md).

## Datos conocidos y vacíos

El piloto propuesto dura **tres meses desde la habilitación de acceso**, con uso gratuito para la institución según [propuesta, página 2](</Users/matias/Downloads/Propuesta_Piloto_Senadores_3meses.docx.pdf>). El usuario confirmó que **el equipo proveedor debe desplegar y operar la web**, además de la API y la base. Senado accede por enlace sin instalar software ni aportar servidores. La gratuidad comercial no elimina gasto de alojamiento, respaldo, soporte o preparación. Se conoce una sucursal y hasta cinco compuertas. No se informaron usuarios concurrentes, movimientos diarios, tamaño de grupos, transferencia, retención, latencia, RPO/RTO ni titularidad final de las cuentas.

El consumo crece por movimientos y consultas, no solo por número de compuertas. Si hay `i` ingresos individuales, `g` ingresos grupales y cantidades `n1...ng`, personas ingresadas = `i + suma(n)`, mientras movimientos de entrada = `i + g`. Cada salida agrega una operación/auditoría; las lecturas de panel y alertas generan tráfico adicional. Hasta medir uso, no se puede certificar capacidad ni calcular almacenamiento acumulado.

## Referencia de nube administrada

Ejemplo con Render para **web React/Vite servida por Nginx, API NestJS y PostgreSQL**, cada uno desplegado, más ambiente pequeño de pruebas. Es una **hipótesis de configuración**, no selección del proveedor ni garantía de rendimiento. Los contenedores serían servicios separados; este cuadro no supone ejecutar el archivo Compose de MCD en Render. Se usa workspace Pro para ilustrar operación de equipo y ventana de recuperación de 7 días de su Postgres pagado; la política institucional puede exigir otro nivel o proveedor. [Precios oficiales](https://render.com/pricing), [planes de cómputo](https://render.com/docs/compute-plans), [recuperación PostgreSQL](https://render.com/docs/postgresql-backups).

| Rubro supuesto | Cantidad × tarifa publicada | Subtotal mensual USD |
| --- | ---: | ---: |
| Workspace Pro | 1 × 25 | 25,00 |
| Web/Nginx producción 0.5c-512mb | 1 × 7 | 7,00 |
| API NestJS producción 1c-2g | 1 × 25 | 25,00 |
| PostgreSQL producción 0.5c-1g | 1 × 19 | 19,00 |
| Disco PostgreSQL producción | 10 GB × 0,30 | 3,00 |
| Web/Nginx pruebas 0.5c-512mb | 1 × 7 | 7,00 |
| API NestJS pruebas 0.5c-512mb | 1 × 7 | 7,00 |
| PostgreSQL pruebas 0.1c-256mb | 1 × 6 | 6,00 |
| Disco PostgreSQL pruebas | 10 GB × 0,30 | 3,00 |
| **Subtotal fijo ilustrativo** | Suma anterior | **102,00** |

Los 10 GB por base y tamaños de máquina son supuestos; pruebas no usan datos personales reales. Si 10 GB mensuales de salida están dentro de los 25 GB incluidos en Pro, el subtotal ilustrativo permanece en USD 102. Con 50 GB salientes, se añaden `(50 - 25) × 0,15 = USD 3,75`, para **USD 105,75/mes**. El cargo de transferencia se calcula a nivel workspace, no por cada servicio. [Tarifas y transferencia de Render](https://render.com/pricing).

Tres meses completos con el subtotal fijo de USD 102 representan **USD 306** de infraestructura de este ejemplo, antes de consumos y rubros faltantes. La facturación real puede prorratear servicios por tiempo y el desarrollo/ensayo puede consumir recursos antes de iniciar el piloto. Una cuenta compartida con otros proyectos requiere criterio de asignación; no se carga automáticamente todo el workspace a Senado ni se lo omite del costo bruto.

**Límite material:** [Render publica regiones](https://render.com/docs/regions) en EE. UU., Alemania y Singapur, no en Paraguay. La institución debe aceptar la ubicación y transferencia de datos antes de elegirlo. Si requiere residencia local o custodia propia, este subtotal deja de ser representativo.

## Rubros sin importe cerrado

| Rubro | Cómo se calculará | Responsable/decisión pendiente |
| --- | --- | --- |
| Copia independiente y retención mayor | GB almacenados × tarifa + operaciones de copia/restauración | D-08: política y titular. El PITR del proveedor no reemplaza una copia independiente si se exige. |
| Dominio y terminación TLS | Precio anual y renovación de dominio, más costo de borde si corresponde | Titularidad a acordar; configuración y operación a cargo del proveedor. |
| Correo de acceso/recuperación | Plan + envíos si se adopta | Método de identidad D-09. |
| Monitoreo y logs de web/API/base | Volumen, retención y plan | Equipo proveedor y política de datos acordada. |
| Mayor capacidad o alta disponibilidad | Instancias, base, réplica, red y ensayo | Solo tras carga medida y RPO/RTO acordados. |
| Soporte de tres meses | Cobertura horaria, personas, incidencias incluidas y tarifa acordada | S2 promete soporte, pero no indica dedicación; no se inventa monto. |
| Exportación/entrega final y eliminación | Trabajo de preparación, validación y cierre | S2 condiciona eliminación a recepción y obligaciones aplicables; definir procedimiento. |
| Equipos y conectividad del puesto | Terminales/enlace existentes o compras necesarias | S2 presupone uso de dispositivos web; confirmar disponibilidad institucional. |
| Comunicaciones externas de alertas | Mensajes × tarifa del canal | **Fuera del MVP actual**; solo si se amplía alcance. |

No se incluyen impuesto, comisiones bancarias ni conversión a guaraníes; su tratamiento comercial está pendiente. No se incluyen horas de construcción, margen, precio de venta ni contratación posterior al piloto. Las tarifas de nube de **web, API y base** son gastos operativos distintos del trabajo de despliegue `TR-05` y soporte `TR-07`, ambos a cargo del equipo proveedor durante el piloto según el alcance acordado.

## Sensibilidad y cierre

El costo base aumenta si la prueba de cinco puntos concurrentes exige más CPU, memoria, conexiones o menor demora en alertas; también si la institución pide alta disponibilidad, más retención o alojamiento en otra jurisdicción. El rango de USD 102 a USD 105,75 muestra únicamente sensibilidad a transferencia manteniendo máquinas iguales; **no valida su capacidad**.

Para cerrar el costo: (1) confirmar ubicación y titularidad de cuentas; (2) obtener volumen diario, simultaneidad y tamaño de grupos; (3) acordar retención, RPO/RTO y soporte; (4) ejecutar una prueba representativa y seleccionar proveedor; (5) recalcular infraestructura, consumos y rubros pendientes. Hasta entonces comunicar «subtotal ilustrativo de infraestructura», no costo total del piloto.
