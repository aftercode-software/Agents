# Presupuesto PREAR

## 1. Resumen ejecutivo

Presentamos una propuesta para el desarrollo de una aplicación web interna a medida para PREAR, orientada a digitalizar y ordenar la operación del taller, centralizar la información productiva y construir una base confiable para el análisis de costos, eficiencia y rentabilidad.

La solución propuesta contempla la gestión integral de obras con su despiece, órdenes de trabajo, materiales, stock operativo, pedidos de compra, costos y KPIs, dentro de una única plataforma web de uso interno. El objetivo es que PREAR pueda profesionalizar la trazabilidad del taller, medir con mayor precisión el costo real de cada trabajo y contar con información útil para comparar producción interna contra alternativas externas.

## 2. Objetivo del sistema

El objetivo del sistema es transformar el proceso actual del taller en una operación digital, trazable y medible, permitiendo registrar y gestionar el trabajo operativo diario, controlar el uso de materiales, dar seguimiento a compras internas y obtener indicadores concretos sobre productividad, costos e ingresos asociados a cada obra.

Además, la propuesta apunta a que el taller opere como una unidad con mayor independencia de gestión, con capacidad de visualizar sus propios costos y desempeño desde un entorno centralizado.

## 3. Problema a resolver

Hoy parte del seguimiento del taller depende de información dispersa entre planillas, registros manuales y criterios operativos no unificados. Esto dificulta conocer con precisión:

- el costo real de cada orden de trabajo
- el consumo de materiales e insumos
- la disponibilidad de stock operativo
- el estado de pedidos de compra
- la productividad y eficiencia del taller por período

También limita la capacidad de comparar costos internos con proveedores externos y de tomar decisiones sobre rentabilidad, planificación y uso de recursos en base a datos confiables.

## 4. Alcance funcional

La propuesta contempla una primera versión funcional del sistema enfocada en la operatoria interna del taller de PREAR. El alcance incluye autenticación, gestión de usuarios por roles, gestión de obras con su despiece, órdenes de trabajo, catálogo propio de insumos, stock operativo básico, pedidos de compra, costos, reportes operativos y dashboard de KPIs.

Dentro de esta etapa también se incluye la posibilidad de generar documentos PDF integrados al flujo de órdenes de trabajo y pedidos de compra, para facilitar la circulación interna de información con otras áreas.

El alcance está pensado para resolver la necesidad principal de digitalización y control operativo, sin convertir esta primera versión en un sistema corporativo integral de inventario o compras para toda la empresa.

## 5. Módulos del sistema

- Autenticación y acceso interno.
- Gestión de usuarios y roles.
- Gestión de obras con despiece.
- Gestión de órdenes de trabajo.
- Catálogo de insumos y materiales.
- Stock operativo básico.
- Pedidos de compra.
- Costos y presupuestación interna.
- KPIs y dashboard operativo.

## 6. Roles y permisos

El sistema contempla al menos los siguientes perfiles:

- Administrador, con acceso total a usuarios, obras, órdenes de trabajo, materiales, stock, pedidos de compra, costos y KPIs.
- Operario o trabajador del taller, con acceso operativo a consulta y carga de información según permisos definidos.
- Compras, con acceso acotado al circuito de pedidos de compra y al ingreso o actualización de stock, según la definición final del proceso.

La lógica exacta de permisos podrá ajustarse durante el relevamiento detallado, manteniendo siempre una base clara de accesos por rol.

## 7. Integraciones con terceros

Dentro del alcance contemplado se consideran integraciones livianas o dependencias externas concretas:

- carga inicial o importación del catálogo de materiales desde el archivo actual de inventario
- uso de una planilla existente como apoyo para alta inicial de insumos, si aplica
- generación de archivos PDF para órdenes de trabajo y pedidos de compra

No se contemplan en esta instancia integraciones complejas con ERP, contabilidad, facturación u otros sistemas corporativos no relevados.

## 8. Arquitectura y enfoque técnico

La solución se plantea como una aplicación web interna con backend, base de datos propia y panel administrativo centralizado. Esto permitirá registrar la operación diaria del taller, persistir la información histórica, controlar materiales e insumos y construir reportes confiables sobre costos y productividad.

Se trabajará con una arquitectura orientada a crecimiento progresivo, de modo que PREAR pueda implementar primero una versión operativa y luego sumar nuevas capacidades sin rehacer la base del sistema.

## 9. Etapas de implementación

La implementación se organizará en etapas para reducir riesgos y validar el avance de manera ordenada:

1. Relevamiento funcional detallado y validación de reglas operativas.
2. Diseño de pantallas, estructura de navegación y experiencia interna de uso.
3. Desarrollo del núcleo operativo: usuarios, obras con despiece y órdenes de trabajo.
4. Desarrollo del catálogo de insumos, stock operativo y pedidos de compra.
5. Desarrollo de costos, PDFs y dashboard de KPIs.
6. Pruebas, ajustes finales y salida inicial a producción.

## 10. Entregables por fase

- Documento funcional consolidado con alcance, reglas principales y supuestos.
- Propuesta de pantallas y estructura operativa del sistema.
- Módulo operativo base para usuarios, obras con despiece y órdenes de trabajo.
- Módulo de materiales, stock operativo y pedidos de compra.
- Módulo de costos y KPIs con información consolidada.
- Generación de PDF para órdenes de trabajo y pedidos de compra.
- Versión inicial lista para uso interno.

## 11. Supuestos, dependencias y riesgos

- PREAR deberá designar un responsable funcional para validar alcance, reglas de negocio y prioridades.
- El archivo actual de inventario deberá estar disponible y en condiciones razonables para ser utilizado como base inicial.
- Las reglas de costeo de mano de obra, valorización de materiales y criterios de análisis deberán ser definidas o validadas por PREAR.
- El circuito de compras puede requerir ajustes finos si aparecen validaciones, estados o aprobaciones no relevadas en esta etapa.
- La estimación y los plazos podrían variar si se requiere una trazabilidad de stock más profunda desde la primera versión o sincronizaciones constantes con planillas externas.

## 12. Soporte y mantenimiento

La presente propuesta contempla la entrega de una primera versión funcional del sistema y la corrección de desvíos o errores propios del desarrollo dentro de una etapa razonable de estabilización posterior a la salida inicial.

De manera opcional, PREAR podrá contratar luego un esquema de soporte y mantenimiento evolutivo para:

- atención de incidencias operativas
- ajustes menores posteriores a la implementación
- mejoras progresivas sobre módulos existentes
- incorporación de nuevas funcionalidades

Como esquema base, se propone un soporte mensual mínimo, opcional y recomendado, de USD 150 por mes.

Adicionalmente, PREAR podrá optar por un esquema de soporte preferencial y crecimiento, en cuyo caso el alcance mensual podrá definirse en conjunto según necesidad operativa, volumen de acompañamiento y mejoras evolutivas a incorporar.

## 13. Plazos estimados

La duración estimada del proyecto es de aproximadamente 8 a 10 semanas, considerando relevamiento, validaciones, desarrollo, pruebas y puesta en marcha inicial.

Este plazo podrá ajustarse levemente según:

- velocidad de validación por parte de PREAR
- claridad de las reglas de costeo y compras
- calidad del inventario base y de la información inicial
- eventuales ampliaciones de alcance durante el proceso

## 14. Inversión

La inversión total del proyecto es de USD 3.600.

El valor podrá abonarse en pesos argentinos tomando como referencia el valor del dólar oficial tipo vendedor del día de cada pago.

La propuesta puede facturarse.

De manera adicional, la operación del sistema contemplará un costo mensual estimado de infraestructura y servidor de entre USD 20 y USD 30, según la configuración final del entorno.

## 15. Forma de pago

Se propone una modalidad de 3 cuotas mensuales iguales sobre el monto total acordado:

- 1 cuota de USD 1.200 al inicio del proyecto
- 1 cuota de USD 1.200 durante el segundo mes de trabajo
- 1 cuota de USD 1.200 contra cierre de la etapa principal y entrega operativa inicial

En caso de abonarse en pesos argentinos, cada cuota se calculará al valor del dólar oficial tipo vendedor del día de pago correspondiente.

## 16. Consideraciones y exclusiones

- La propuesta está orientada al uso interno del taller de PREAR.
- El alcance contempla un stock operativo del taller y no un sistema corporativo integral de inventario para toda la empresa.
- No incluye integración con ERP, contabilidad, facturación ni sistemas externos no relevados.
- No incluye circuitos avanzados de aprobación multinivel para compras, salvo que se definan expresamente como ampliación.
- No incluye app mobile nativa.
- No incluye migraciones históricas complejas ni saneamiento integral de datos heredados.
- No incluye funcionalidades evolutivas no priorizadas en esta primera etapa.
- No incluye dentro del valor de desarrollo el costo mensual de infraestructura, servidor o servicios externos necesarios para operar el sistema.
- No incluye dentro del valor base el soporte mensual posterior a la salida en producción.

Como plan de crecimiento opcional, PREAR podrá evaluar en una segunda fase:

- trazabilidad ampliada de movimientos de stock
- reingreso formal de materiales con historial detallado
- permisos más granulares por módulo o acción
- circuito de compras más robusto con aprobaciones y conciliación interna
- reportes avanzados de rentabilidad por obra, tipo de trabajo o período
- integraciones futuras con otros sistemas o áreas

## 17. Próximos pasos

Para avanzar con el proyecto, proponemos:

- aprobar formalmente el alcance de esta propuesta
- confirmar el esquema de pago en 3 cuotas
- definir modalidad de facturación y datos administrativos necesarios
- definir configuración inicial de infraestructura según ambiente de despliegue
- evaluar si PREAR desea contratar desde el inicio el soporte mensual recomendado
- realizar kickoff funcional para bajar reglas detalladas de operación, costos, stock y compras
- iniciar diseño y desarrollo de la primera versión del sistema
