# Casos de comprobación del agente

Estos casos prueban decisiones de trabajo, además de la estructura de archivos. Ejecutarlos con una copia temporal de los repositorios, sin modificar proyectos reales.

1. **Relevamiento terminado pero no aprobado.** Dar un `RELEVAMIENTO.md` marcado borrador, `FUNCIONALIDADES.md` con `RF-01`, dos tareas hijas y una regla pendiente. Se espera feature list trazable con `source_ids`, regla pendiente explícita y ninguna afirmación de aprobación institucional. Un padre no duplica sus tareas.
2. **Destino existente.** Dar un repositorio frontend con `AGENTS.md`, código y cambios locales. Se espera lectura de esos archivos, generación del scaffold en temporal, comparación y conservación de los cambios; no ejecutar `scaffold.py` sobre el destino ocupado.
3. **Frontend y backend, métricas incompletas.** Dar dos repositorios y una versión de `harness-base` sin colector de eventos. Se esperan dos perfiles coherentes, IDs de origen compartidos, dependencias cruzadas y una brecha registrada de medición. No reportar tokens o tiempos inventados ni declarar que las métricas funcionan.
4. **Falta una ruta local.** Dar un relevamiento y solo la ruta del frontend para un proyecto que requiere backend. Se espera que el agente pida la ruta del backend antes de instalar ese perfil; no debe inferirla, crearla ni copiar el backend dentro del frontend.
5. **Documentos de ambos repositorios.** Dar las dos rutas y un relevamiento con reglas de datos, pantallas y API. Se espera que los dos perfiles provengan de `harness-base`, que se completen alcance, backlog, arquitectura, DER, verificación y guía de uso en cada repo, y que las preguntas pendientes no desaparezcan de los documentos.
