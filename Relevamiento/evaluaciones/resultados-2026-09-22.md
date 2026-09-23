# Validación de antecedentes e integración — 2026-09-22

## Alcance

Cambios locales sin commit/push. Se evaluaron las instrucciones y el traspaso documental; no se ejecutó publicación en Drive, automatización entre agentes, cálculo de una nueva cotización ni desarrollo de los proyectos de referencia. Los PDFs/XLSX originales no se modificaron. Los cuatro documentos de ETRACK conservaron sus hashes y su estado staged previo.

## Comprobaciones estructurales

- `python3 -B Relevamiento/evaluaciones/validar_integracion.py`: pasó. Comprueba igualdad de las dos distribuciones de cada skill, las cuatro copias del contrato y los enlaces Markdown locales.
- `python3 -B -m unittest discover -s Relevamiento/evaluaciones -p 'test_*.py' -v`: seis pruebas aprobadas, incluidos drift entre agentes, contraparte faltante, espejo alterado y enlace roto, sobre fixtures temporales.
- `git diff --check`: sin errores.
- Frontmatter de las cuatro entradas: YAML parseado con Ruby/Psych, nombres, claves admitidas, longitudes y ausencia de placeholders comprobados.
- `skill-creator/scripts/quick_validate.py`: no pudo ejecutarse por `ModuleNotFoundError: No module named 'yaml'` en el Python disponible. No se instalaron dependencias ni se declara ese validador como aprobado; se usaron los controles alternativos anteriores.

## Evaluación de comportamiento

Dos evaluadores independientes leyeron las skills y referencias pertinentes, sin recibir la rúbrica de [casos.md](casos.md). Respondieron en conversación, sin escribir archivos ni usar servicios externos. Los pedidos base y criterios están en los casos 5–7; no se reejecutaron 1–4 en esta revisión.

| Prueba | Resultado observado |
| --- | --- |
| AfterAccess, caso 5 | Conservó 285 horas por área, PDF como alcance y Time sheet como cifras. Excluyó Hours, distinguió costo/fórmula/precio y declaró que usaba el registro, sin afirmar lectura nueva de originales ni ejecución del proyecto. |
| MCD, caso 6 | Trató dedicaciones como aproximadas; no usó 780 horas, no duplicó discovery/harness/fixes ni convirtió el precio hipotético con menos equipo en ahorro demostrado. Identificó falta de horas efectivas y costos atribuibles. |
| Turnos v1→v2, caso 7 | Conservó IDs, agregados 8/12/4 para v1 y excluyó invitaciones futuras. No asignó horas por tarea ni trasladó el total a v2. Devolvió preguntas sobre conflictos offline, permisos y evaluación del plazo por los IDs afectados. |
| Variante de caso 7, modo omitir | Conservó estimaciones v1 como antecedente y respetó la instrucción posterior de analizar v2 sin horas, sin presupuesto ni archivos. |

Se detectó una ambigüedad real: presupuestos hablaba de “Usar planilla proporcionada” y de crear carpeta aunque el pedido fuera una comprobación conversacional. Se cambió a “Usar horas proporcionadas”, incluyendo documentos/mensajes, y se explicitó la salida en conversación. El evaluador de integración releyó los archivos corregidos y no encontró un conflicto operativo aplicable al caso.

Las respuestas completas quedaron en los hilos de evaluación:

- Kepler, AfterAccess/MCD: `01a0c9cf-0081-75a2-ad0a-868087d4d696`.
- Helmholtz, integración y variante posterior: `01a0c9cf-00e6-7222-9e72-664e234452cc`.

## Identificación de la revisión

SHA-256 de entradas finales y contrato compartido:

- `Relevamiento/skills/relevamiento/SKILL.md`: `5d87df75dcda04d01b19d04addf0812edc82e98dae27ca0bb4e929f209feae88`.
- `Presupuestos/skills/aftercode-presupuesto-integral/SKILL.md`: `8cea0a9e697f585490d0444bd5baf74e0d04e1ecb82961162d66d4fd9bf573e3`.
- `references/traspaso-presupuestos.md` en las cuatro distribuciones: `75c9a9325e518f59a0c7554e730991bfc6cdd71f53ac759c013bab88b9db2959`.

Estas pruebas dan evidencia sobre los casos ejecutados, no garantizan calidad de todas las estimaciones futuras ni integración con aplicaciones externas.
