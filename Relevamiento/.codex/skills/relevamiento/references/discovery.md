# Descubrimiento y alcance

## Partir del trabajo real

Identificar el objetivo, quién decide, quién opera y quién recibe el resultado. Entender cómo se resuelve hoy el problema, dónde falla y qué evidencia existe: ejemplos, documentos, entrevistas, datos o código.

Preguntar por una situación concreta reciente antes de sugerir funcionalidades: qué ocurrió, qué hizo cada actor, qué información faltó y qué consecuencia tuvo. Evitar preguntas que induzcan a validar la solución preferida del agente.

Acordar una señal observable de éxito. Si el usuario no tiene una medición actual, registrarla como pendiente; no inventar una línea de base ni objetivos numéricos.

## Completar lo que cambia el proyecto

Seleccionar los ejes pertinentes:

| Eje | Información que buscar |
| --- | --- |
| Procesos | Inicio, actores, pasos, estados, aprobaciones, excepciones, cierre y tareas manuales. |
| Datos | Origen, campos, relaciones, calidad, volumen, retención, importación y exportación. |
| Usuarios | Roles, permisos, organizaciones o sedes, separación de datos y responsables. |
| Integraciones | Sistema exacto, documentación, API disponible, autenticación, límites y acceso de prueba. |
| Uso | Dispositivos, conectividad, concurrencia, frecuencia, picos, ubicaciones e idiomas. |
| Operación | Disponibilidad requerida, soporte, respaldos, recuperación y quién administra el servicio. |
| Restricciones | Presupuesto, fecha, contratos, stack existente, conocimientos del equipo y propiedad de cuentas/datos. |

Relevar requisitos no funcionales que afecten una decisión. “Rápido”, “seguro” o “escalable” necesitan contexto y criterios verificables, no cifras asignadas por el agente.

Cuando haya operación offline, investigar qué acciones deben funcionar, cuánto tiempo, en qué dispositivos y qué ocurre si dos operadores modifican el mismo dato. Aclarar sincronización, duplicados, conflictos y protección del almacenamiento local antes de comprometer el alcance.

## Alcance trazable

Asignar identificadores estables a requisitos que deban seguirse entre documentos, por ejemplo `RF-01` y `RNF-01`. Para cada requisito relevante registrar:

- Necesidad y fuente.
- Actor, comportamiento esperado y excepciones materiales.
- Criterio de aceptación verificable.
- Prioridad y etapa: alcance inicial, evolución o excluido.
- Estado: confirmado, observado, supuesto, propuesto o pendiente.
- Dependencias y preguntas que podrían cambiarlo.

Ajustar la formalidad al caso: una web pequeña puede usar una tabla corta. No agregar módulos solo porque sean habituales en otros proyectos.

## Supuestos y validaciones

Para cada incertidumbre importante, explicar qué estamos suponiendo, qué evidencia hay, qué decisión depende de ella y cómo comprobarla con el menor esfuerzo útil. Priorizar por consecuencia de equivocarse y falta de evidencia; no fabricar puntajes ni probabilidades.

Distinguir una hipótesis de producto de una incertidumbre técnica. Una entrevista puede aclarar una necesidad; una prueba de API puede demostrar compatibilidad; ninguna sustituye a la otra.

Separar imprescindible para la primera versión de mejoras posteriores. Registrar el motivo de la división y las dependencias reales. No incluir prestaciones futuras en el presupuesto inicial por el solo hecho de preparar la arquitectura para ellas.

## Sistemas existentes

Relevar qué funciona, qué se reutiliza, qué se modifica y qué requeriría migración. Contrastar documentación con rutas de ejecución, datos e integraciones pertinentes. No concluir que una función no existe solo porque falta en un documento.

Proponer una migración o reescritura únicamente si el problema y sus costos la justifican. Documentar continuidad operativa, compatibilidad, migración de datos y reversibilidad cuando sean parte del alcance.
