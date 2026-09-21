# Alternativas y arquitectura

## Comparar desde las restricciones

Derivar las opciones de los requisitos, el sistema existente, la capacidad del equipo y el presupuesto operativo. Considerar reutilización, configuración de un producto existente, desarrollo a medida y combinaciones cuando sean viables.

Comparar dos o tres opciones si hay una elección material. Si una restricción elimina las demás, explicar por qué; no inventar alternativas para llenar una tabla.

Evaluar cada opción con los criterios que realmente cambian la decisión:

- Cobertura de requisitos y límites conocidos.
- Esfuerzo inicial, complejidad operativa y capacidad del equipo para mantenerla.
- Costo operativo inicial y bajo distintos patrones de uso.
- Integraciones, portabilidad de datos y dependencia del proveedor.
- Seguridad, aislamiento, disponibilidad y recuperación requeridos.
- Evolución, migraciones futuras y decisiones difíciles de revertir.

Recomendar una opción y expresar las desventajas aceptadas. No elegir un stack por popularidad, un proveedor por su plan gratuito ni una base de datos exclusivamente por cantidad de registros. Considerar consultas, transacciones, concurrencia, tamaño, consistencia y operación.

## Diseño suficiente para decidir

Describir los componentes necesarios, sus responsabilidades y el flujo de datos. Cubrir, cuando corresponda:

- Canales y clientes: web, móvil, escritorio o integración.
- Backend, tareas asíncronas e integraciones externas.
- Datos, archivos, autenticación y autorización.
- Despliegue, ambientes, secretos, observabilidad y respaldos.
- Propiedad de cuentas, responsable operativo y recuperación ante fallos.

Mantener la solución inicial proporcional al uso esperado. Introducir servicios separados, colas, cachés o múltiples regiones cuando un requisito o evidencia lo justifique. La separación de módulos no obliga a desplegar microservicios.

Investigar capacidades del proveedor antes de depender de ellas. Registrar cualquier prueba necesaria para cerrar una duda de viabilidad.

## Decisiones

Registrar decisiones materiales en `ARQUITECTURA.md` con un identificador, estado, contexto, alternativas, recomendación o decisión aceptada, consecuencias y fuentes. En proyectos grandes o con convenciones existentes, usar ADRs separados sin duplicar su contenido.

Una propuesta técnica permanece propuesta hasta que exista una decisión del usuario. Preservar decisiones previas y registrar cuál reemplaza a cuál cuando cambien.

## Evolución por señales

Explicar qué puede crecer: volumen de datos, concurrencia, organizaciones, ubicaciones, equipo o complejidad de negocio. Para cada cambio futuro relevante registrar:

| Señal observable | Cambio a evaluar | Costo o dificultad | Evidencia pendiente |
| --- | --- | --- | --- |
| Métrica o límite que afectaría al proyecto | Acción concreta y alternativa | Operación, migración y mantenimiento | Qué habría que medir o probar |

No fijar umbrales de usuarios sin conocer la carga. Si no hay mediciones, presentar el umbral como hipótesis de validación y proponer cómo obtenerlo.

Distinguir mejoras reversibles de decisiones que exigen una migración. Explicar cómo exportar datos o sustituir una dependencia crítica si esa portabilidad es relevante.

Cerrar con el enfoque recomendado para la primera versión, los cambios diferidos y las condiciones que harían reconsiderar la decisión.
