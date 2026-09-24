# Preparación de métricas

Las métricas pertenecen al harness de **cada repositorio destino**, en `progress/`, y su contrato común se mantiene en `harness-base`. El preparador usa los archivos y comandos de la versión elegida; no crea un segundo sistema incompatible dentro de su propia skill. La versión 0.2 inspeccionada incluye `docs/metrics.md` y `scripts/metrics.py`; volver a verificarlo al preparar un proyecto.

## Señales requeridas por feature

- Cambios pedidos a un spec no aprobado y posterior aprobación humana.
- Veredictos `CHANGES_REQUESTED` y `APPROVED` del reviewer, con intento/ciclo y hallazgos.
- Refactors pedidos, distinguiendo corrección técnica de mejora opcional.
- Cambios solicitados por el equipo o cliente, separados de defectos del implementer.
- Inicios/fines de fases, espera de aprobación y bloqueos con marca temporal para calcular duración transcurrida.
- Pruebas y resultados de verificación con referencia reproducible.
- Tokens de entrada/salida por modelo, turno y agente cuando el runtime los exponga, con fuente y cobertura.

Cada evento debería vincular `feature ID`, tipo, actor, fecha UTC, ciclo, motivo/categoría y referencia a spec, review, prueba o decisión. El resumen legible de `progress/` complementa el evento estructurado; no reemplaza su marca temporal ni su fuente.

La duración entre eventos es tiempo transcurrido, no horas humanas activas. Los tokens sin telemetría son **desconocidos**, nunca cero. Evitar sumar dos veces tokens de subagentes, caché o reintentos; conservar modelo y fuente. Una tasa alta de aprobación del reviewer no demuestra calidad por sí sola: usar pruebas, defectos posteriores y una muestra de revisión humana para calibrar el indicador.

Para aspirar a revisión humana por excepción, comenzar con una línea base de features comparables y una muestra humana periódica. Definir disparadores de revisión por caída en aprobación inicial, aumento de ciclos, defectos posteriores, falta de telemetría o cambios de alcance sensibles. Mantener la aprobación humana de specs prevista por el SDD mientras esa política no cambie explícitamente. No fijar umbrales arbitrarios sin datos del proyecto.

## Puerta de preparación

Antes del primer ciclo de implementación, comprobar con un caso controlado que un rechazo de spec, un rechazo del reviewer y un cambio solicitado por el equipo quedan diferenciados en el reporte por feature. Si el `harness-base` seleccionado aún no tiene eventos/lector de uso, registrar el faltante, su responsable y una acción concreta. Se puede preparar alcance y DER mientras tanto, pero no declarar lista la medición ni generar cifras a mano.
