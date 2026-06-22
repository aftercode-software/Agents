# Horas Hombre

## Cliente

PREAR

## Criterio de estimación

La estimación contempla el desarrollo de un sistema web interno a medida con lógica operativa, trazabilidad de órdenes de trabajo, manejo de materiales, stock, compras, costos y reportes. Se asume una ejecución acelerada por uso intensivo de IA para relevamiento, documentación, diseño funcional, scaffolding técnico, construcción de interfaces, generación de código repetitivo, testing asistido y documentación interna.

La estimación no responde a un proceso tradicional puro, sino a un flujo de trabajo optimizado por herramientas como Codex o Claude Code, con iteraciones más cortas y mayor velocidad en tareas de implementación y ajuste. Aun así, se reserva tiempo real para definición funcional, validación operativa y resolución de lógica de negocio específica.

## Supuestos de productividad con IA

- Uso de IA para acelerar el relevamiento, síntesis funcional y detección temprana de inconsistencias.
- Aceleración en armado de paneles, formularios, tablas, reportes y componentes reutilizables.
- Apoyo de IA en modelado inicial de base de datos, endpoints, validaciones y flujos CRUD.
- Ahorro parcial en QA técnico y correcciones menores por mayor velocidad de inspección y depuración.
- Se asume un feedback razonablemente ágil por parte del cliente para no abrir múltiples rondas extensas de retrabajo.
- Se asume una primera versión acotada a uso interno, sin integraciones enterprise complejas.

## Desglose por rol

### Relevamiento funcional

- Objetivo del rol: cerrar alcance, reglas operativas, permisos, estados y dependencias del negocio.
- Tareas principales: análisis del flujo actual, traducción del proceso a módulos de sistema, definición de reglas de stock, compras, costos y reportes.
- Horas estimadas: 12 h
- Comentarios o supuestos: incluye instancias de ajuste fino para no sobredimensionar el MVP.

### Project management

- Objetivo del rol: coordinar el proyecto, ordenar validaciones y asegurar continuidad entre etapas.
- Tareas principales: planificación, seguimiento, priorización, coordinación interna, reuniones de control y cierre.
- Horas estimadas: 14 h
- Comentarios o supuestos: distribuido a lo largo de todo el proyecto.

### UX/UI

- Objetivo del rol: diseñar una interfaz clara para una operación interna intensiva en carga y consulta de datos.
- Tareas principales: arquitectura de pantallas, definición de flujos, diseño de formularios, tablas, vistas operativas, dashboards y documentos imprimibles.
- Horas estimadas: 24 h
- Comentarios o supuestos: contempla una línea visual sólida y utilitaria, no branding avanzado.

### Frontend

- Objetivo del rol: implementar la aplicación web interna y sus pantallas operativas.
- Tareas principales: autenticación, vistas de obras, órdenes de trabajo, materiales, stock, compras, reportes, filtros, tablas, formularios, PDFs y dashboard.
- Horas estimadas: 52 h
- Comentarios o supuestos: incluye responsive funcional para desktop y uso complementario en pantallas menores, con prioridad operativa en escritorio.

### Backend

- Objetivo del rol: construir la lógica de negocio, persistencia y trazabilidad del sistema.
- Tareas principales: modelado de base de datos, API, usuarios y permisos, obras, OTs, materiales, movimientos de stock, pedidos de compra, cálculos de costos, KPIs y generación de documentos.
- Horas estimadas: 64 h
- Comentarios o supuestos: es el bloque más sensible del proyecto por la lógica operativa y de costos.

### QA

- Objetivo del rol: validar funcionamiento real del sistema y consistencia de los flujos internos.
- Tareas principales: pruebas funcionales, validación de permisos, verificación de cálculos, pruebas de PDFs, revisión de estados y controles de regresión.
- Horas estimadas: 20 h
- Comentarios o supuestos: contempla una ronda sólida de pruebas y ajustes antes de entrega.

### DevOps

- Objetivo del rol: preparar ambientes y salida inicial del sistema.
- Tareas principales: configuración de despliegue, entorno de base de datos, variables, backups básicos, dominios o accesos y puesta en producción inicial.
- Horas estimadas: 12 h
- Comentarios o supuestos: no contempla infraestructura enterprise compleja ni alta disponibilidad avanzada.

## Total estimado

198 horas

## Riesgos y variaciones posibles

- La estimación puede aumentar si el circuito de compras requiere aprobaciones más complejas que las hoy relevadas.
- Puede aumentar si PREAR necesita una trazabilidad de stock más profunda, con movimientos, ajustes, reingresos y auditoría detallada desde la primera versión.
- Puede aumentar si se exige sincronización constante y bidireccional con planillas externas en lugar de migración o carga controlada al sistema.
- Puede aumentar si el cálculo de costos incorpora reglas contables, indirectos o valorizaciones especiales no definidas aún.
- Puede aumentar si se requieren múltiples perfiles con matrices de permisos finas por acción.
- Puede reducirse parcialmente si el alcance de compras y stock se simplifica en la primera etapa.
- Puede variar según la calidad real de los datos iniciales y la claridad del inventario base.
