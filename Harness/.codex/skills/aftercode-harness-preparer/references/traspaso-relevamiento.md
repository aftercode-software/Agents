# Traspaso desde Relevamiento

El traspaso es documental. Relevamiento no invoca a este agente automáticamente. Aceptar rutas exactas a archivos, enlaces o contenido aportado en la conversación; no exigir un formato nuevo si los datos ya existen.

## Orden de lectura

1. `RELEVAMIENTO.md`: proyecto, versión de alcance, fuentes, decisiones, exclusiones y pendientes.
2. `FUNCIONALIDADES.md`, si existe: IDs y desglose canónico de funcionalidades, criterios, tareas y transversales.
3. Arquitectura, contratos, DER o costos operativos aportados: leer lo pertinente para preparar el proyecto. Un costo operativo no es una medición del harness ni una hora de implementación.
4. Instrucciones y código de los repositorios destino: verificar lo existente; un alcance nuevo no implica reconstruir una capacidad ya implementada.

Registrar una tabla de trazabilidad con `ID de origen | fuente y versión | estado del alcance | feature local | criterio | dependencia o decisión`. Conservar IDs `RF-xx`, `RF-xx-Txx` y `TR-xx` cuando existan. El `feature_list.json` actual de `harness-base` usa un entero local como `id`: asignarlo de forma estable y guardar los IDs del relevamiento en `source_ids`. No reutilizar un entero para otra feature ni perder la relación al subdividir trabajo frontend/backend.

Separar:

- **Confirmado:** necesidad expresada en la fuente elegida.
- **Observado:** comportamiento o contrato comprobado en un sistema existente.
- **Propuesto:** solución, criterio o entidad sugeridos; requiere validación.
- **Pendiente/condicionado:** decisión que afecta una feature; dejar la pregunta y el efecto.
- **Excluido/futuro:** conservarlo fuera del backlog de implementación actual o identificarlo sin contarlo como trabajo incluido.

Un relevamiento puede estar terminado como documento y seguir siendo un borrador de alcance. No inferir aprobación institucional por fecha de actualización, existencia de `FUNCIONALIDADES.md` o una estimación. Preparar unidades independientes aunque otras estén bloqueadas; no convertir una pregunta abierta en una regla arbitraria.

Antes de cerrar, comprobar que cada necesidad incluida tiene una feature, una dependencia explícita o una decisión pendiente; que padres e hijos no duplican trabajo; y que trabajo compartido y pruebas transversales aparecen una sola vez.
