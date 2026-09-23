# Preparar evidencia para estimar esfuerzo

El relevamiento explica qué trabajo hay y qué factores lo hacen variar. Presupuestos transforma esa información en horas y condiciones comerciales. Registrar las horas aportadas por el usuario sin recalcularlas ni inventar un reparto más detallado.

## Ficha proporcional por unidad estimable

Ampliar las tareas de `FUNCIONALIDADES.md` con los datos que realmente cambian su esfuerzo. Compartir contexto a nivel de proyecto y heredar del padre para evitar fichas repetitivas.

| Dato | Qué debe permitir entender |
| --- | --- |
| Tipo de trabajo | Nuevo, modificación, configuración, integración, migración o retiro. |
| Tamaño observable | Flujos y variantes, reglas, estados, entidades, contratos, pantallas o reportes distintos. Indicar cantidades solo si están relevadas; no convertir pantallas en horas. |
| Frente y superficie | Frontend web, cliente mobile, backend u otra disciplina; tareas separadas cuando corresponde. “Fullstack” es un perfil de persona, no otro frente que se suma a frontend y backend. |
| Reutilización | Qué ya existe, evidencia de que sirve, qué se adapta y qué se debe verificar. Distinguir hipótesis de reutilización de implementación comprobada. |
| Factores técnicos | Permisos, aislamiento, concurrencia, operación offline, sincronización, volumen, integraciones y datos heredados, solo cuando apliquen. |
| Alcance de entrega | Diseño, implementación, pruebas propias, revisión, integración, documentación y publicación necesarias. Indicar qué queda en tareas compartidas. |
| Dependencias | Contratos entre capas, tareas previas, accesos, datos o decisiones del cliente. Separar espera externa de horas de trabajo. |
| Evidencia e incertidumbre | Fuentes, supuestos, complejidad justificada, preguntas abiertas, efecto y validación que las resuelve. |
| Base de comparación | Antecedente comparable, tipo de sus horas y diferencias relevantes. Si no existe, decirlo. |

Relevar contexto del equipo cuando afecte la estimación: stack conocido, experiencia, disponibilidad efectiva, herramientas, harness existente y proceso de revisión/QA. La duración calendario requiere capacidad y dependencias; no se obtiene dividiendo por cantidad de personas sin esos datos.

## Trabajo que suele quedar oculto

Revisar si el alcance necesita discovery, harness, diseño, coordinación, revisión de PR, pruebas integradas, infraestructura, publicación, capacitación o estabilización. No son recargos obligatorios: registrar su cobertura y contar cada trabajo una vez. Si ya está incluido en las horas de desarrollo, no volver a sumarlo como transversal.

Distinguir correcciones previas a entrega, garantía/estabilización posterior y mantenimiento contratado. Indicar período, responsable y dedicación cuando se conozcan. No imputar una suscripción compartida completa a cada proyecto; conservar costo bruto y criterio de asignación, o declarar pendiente la porción atribuible.

## Calidad de la evidencia histórica

Cada cifra debe indicar fuente, período, alcance/versionado, unidad, rol o área y naturaleza:

- **Medida:** horas registradas con cobertura conocida. Documentar si incluye revisión, QA y soporte.
- **Reportada aproximada:** recuerdo o dedicación orientativa del equipo; no elevarlo a medición.
- **Estimada:** esfuerzo previsto, ejecutado o no el proyecto. Una planilla presupuestada no demuestra productividad.
- **Escenario retrospectivo:** lo que hoy se haría o cobraría distinto; no describe un resultado realizado.

Conservar la granularidad original. Un total por área no respalda horas por funcionalidad. No repartirlo por número de tareas, commits, pantallas ni con porcentajes arbitrarios para completar una tabla. Si el usuario necesita ese desglose, tratarlo como una nueva estimación explícita, separada del dato original.

Al comparar un antecedente, comprobar alcance, complejidad, reutilización, equipo, stack y definición de terminado. No extrapolar horas de un proyecto entero a una función pequeña. Los casos de [casos-aftercode.md](casos-aftercode.md) ayudan a detectar omisiones; no son una tarifa ni una tabla de velocidad.

## Lectura de repositorios

Git permite rastrear cambios, PR, revisiones y estados del backlog, no medir horas por sí solo. Distinguir fecha de implementación, primera integración a main, cierre formal y entrega al cliente. Explicar rama/corte, identidad de tareas, renumeraciones y cierres agrupados si se cuentan eventos.

No equiparar una entrada de `feature_list` con una funcionalidad comercial uniforme. Un PR integrado no garantiza aceptación o cierre; un estado pendiente tampoco demuestra que no exista implementación. La cadencia recordada y los días con cierres no son una tasa universal de producción.

## Salida para presupuestos

Mantener alcance y unidades en `FUNCIONALIDADES.md`. Dejar contexto del equipo, fuentes numéricas y límites de evidencia en `RELEVAMIENTO.md`. Enlazar ambos en el bloque de traspaso de [traspaso-presupuestos.md](traspaso-presupuestos.md), sin crear otra lista de funcionalidades.

No aplicar conversiones fijas complejidad→horas, puntos→horas ni descuentos automáticos por IA. Registrar posibles ahorros por automatización como hipótesis hasta contar con evidencia; revisión, validación y retrabajo siguen siendo esfuerzo humano. Si faltan datos, entregar tareas estimables condicionadas o bloqueadas en lugar de una precisión ficticia.
