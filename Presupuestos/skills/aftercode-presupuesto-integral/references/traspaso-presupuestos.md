# Contrato de traspaso relevamiento → presupuestos (v1)

Guía compartida por ambos agentes. Define información y responsabilidades, no ejecuta un orquestador ni autoriza escrituras externas. Funciona con documentos existentes o en conversación; no exige JSON ni un quinto archivo por proyecto.

## Responsabilidades y fuentes

- Relevamiento mantiene necesidades, alcance, criterios de aceptación, desglose, factores de esfuerzo y pendientes. Presupuestos conserva la responsabilidad de calcular horas cuando se solicite y de redactar condiciones comerciales.
- `FUNCIONALIDADES.md` es el alcance canónico si existe. Reutilizar su carpeta y sus IDs; no copiarlo a otra carpeta de cliente ni regenerarlo perdiendo criterios o estados.
- Identificar fuentes **por dimensión**: alcance, horas, costos y precio comercial pueden provenir de documentos distintos. Registrar selección explícita del usuario, versiones y fuentes descartadas con su motivo. Un archivo descartado no completa supuestos vacíos por semejanza de nombre.
- Un antecedente histórico es una comparación, no una fuente del alcance actual. Una estimación no ejecutada no se convierte en medición. No trasladar tarifas, márgenes ni descuentos de ejemplos al nuevo cliente.

## Bloque mínimo de entrega

Al cerrar un relevamiento completo, incluir este bloque en `RELEVAMIENTO.md` o en la respuesta. En un trabajo parcial, incluir solo lo relevante y marcar lo faltante, sin bloquear por ausencia de archivos accesorios.

| Campo | Contenido |
| --- | --- |
| Contrato | `relevamiento-presupuestos/v1`. |
| Proyecto y alcance | Nombre, versión/fecha del alcance y estado de aprobación; no confundir fecha de actualización con aprobación. |
| Fuentes | Rutas/enlaces exactos existentes o referencias a mensajes; sección/hoja/rango cuando se conozcan. Fuente elegida por dimensión y material excluido. |
| Modo de horas | `calcular`, `usar proporcionadas`, `omitir` o `pendiente de elección`; no elegir por mera existencia de un antecedente adjunto. |
| Unidades | Referencia al desglose canónico con IDs/padres, hojas estimables, agrupadores y trabajos compartidos, etapa y frente/superficie. |
| Base de esfuerzo | Criterios de terminado, tamaño, reutilización, factores técnicos, contexto del equipo y antecedentes comparables con límites de evidencia. |
| Valores aportados | Horas/costos/precios separados, con fuente, naturaleza (medida, aproximada, estimada, escenario), granularidad, inclusiones y período. Vacío no equivale a cero. |
| Pendientes | Estado global y por módulo: listo, condicionado o bloqueado; supuestos, preguntas, validación y efecto esperado. |
| Cambios | IDs afectados desde la versión anterior; estimaciones vigentes, pendientes de revisión o no disponibles. |
| Próxima acción | Lo pedido/autorizado por el usuario; no iniciar presupuesto ni publicar solo por completar el traspaso. |

## Consumo por presupuestos

1. Leer fuentes seleccionadas y contrastar alcance/versión con los números. Conservar decisiones resueltas; devolver solo discrepancias o faltantes materiales, por ID, sin reiniciar todo el discovery.
2. Estimar hojas, nunca sumar padre e hijos. Clasificar trabajo, no cantidad de desarrolladores: frontend web/mobile y backend pueden ser ejecutados por una persona fullstack sin duplicar sus horas. No repartir “ambas” 50/50. Contar transversales una sola vez y explicitar cobertura de QA/revisión/soporte.
3. En modo `usar proporcionadas`, mantener valores originales y granularidad. Si solo hay horas por área, registrarlas así; no repartirlas entre funcionalidades para aparentar trazabilidad. Separar el mapa funcional del agregado numérico y señalar la relación todavía no disponible. Revisar fórmulas/cifras no autoriza cambiarlas ni recalcular el archivo fuente.
4. En modo `calcular`, registrar para cada unidad el método, fuente comparable o juicio provisional, supuestos, cobertura y rango/valor justificado. Complejidad, story points, conteo de tareas y uso de IA no son conversiones automáticas a horas. No derivar duración sin disponibilidad y dependencias ni afirmar ahorro de IA no medido.
5. En `HORAS_HOMBRE.md`, registrar versión del alcance, modo y fuente, IDs cuando el desglose numérico exista, áreas/roles, total o subtotal conocido y partidas pendientes. Reconciliar con la planilla a su granularidad real. No cerrar un total de proyecto omitiendo silenciosamente partes bloqueadas.
6. Mantener esfuerzo, costo de construcción, costo operativo, precio comercial, margen/recargo y financiación separados. Si documento comercial y planilla difieren, conservar ambos valores con fuente; no sustituir uno por otro ni deducir la causa sin evidencia.

## Cambios y retorno a relevamiento

Si cambia una regla, dependencia o criterio, identificar IDs y versión afectados antes de actualizar horas/precio. Marcar la estimación anterior como pendiente de revisión, conservar sus valores históricos y recalcular solo con el modo y autorización correspondientes. No reescribir una planilla aportada para que coincida con un alcance nuevo.

Devolver una pregunta concreta y su efecto: por ejemplo, “RF-07: falta decidir cómo resolver duplicados offline; esto condiciona sincronización y QA”. Avanzar con unidades independientes. La respuesta validada actualiza la fuente canónica, no un segundo backlog del presupuestador.

## Comprobación de entrega

- Cada unidad incluida queda estimada, cubierta por un agregado explícito o pendiente; no se afirma desglose por ID cuando solo hay totales por área.
- No se suman agrupadores, alternativas excluyentes, evolución futura ni transversales repetidos.
- La naturaleza de las horas y la versión del alcance siguen visibles; no se trata una cotización histórica como productividad medida.
- El traspaso en sí no cambia modo de horas, valores suministrados ni permisos de publicación.
