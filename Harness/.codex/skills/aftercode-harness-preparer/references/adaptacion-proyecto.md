# Adaptación de harness-base al proyecto

## Inspección inicial

Recibir y verificar las rutas locales de `harness-base`, repositorio backend y repositorio frontend. Si uno no existe o no aplica, resolverlo expresamente con el usuario antes de instalar ese perfil. No buscar una carpeta de nombre parecido y asumir que es el destino.

Leer el `README.md`, `scripts/scaffold.py`, `scripts/validate.py`, `scaffold/common/`, perfiles y `harness.json` de la versión **real** de `harness-base`. Registrar commit/tag y si el árbol tiene cambios sin confirmar; una copia de trabajo en progreso no se presenta como versión publicada. Inspeccionar ambos repositorios destino y sus instrucciones antes de decidir archivos y comandos.

El scaffold observado al redactar esta guía elige un perfil `frontend` **o** `backend` y solo admite destinos vacíos. Volver a comprobarlo porque puede cambiar.

## Destinos

- **Repositorio nuevo y vacío:** ejecutar el generador con el perfil correspondiente y validar su salida antes de completar contenido.
- **Repositorio existente:** generar primero en un directorio temporal, comparar con instrucciones, arquitectura, tests y código existentes; llevar al proyecto solo los archivos o secciones compatibles. No ejecutar el generador directamente sobre un árbol ocupado ni sustituir archivos del proyecto.
- **Frontend y backend separados, caso habitual:** aplicar `scaffold/common/` y `scaffold/backend/` al backend; `scaffold/common/` y `scaffold/frontend/` al frontend. Preparar cada repositorio en su ruta indicada, conservar referencias a los mismos IDs de origen y documentar contratos y dependencias entre ambos. No duplicar una función completa en los dos backlogs: describir el resultado específico de cada lado.
- **Monorepo o perfil no soportado:** documentar la estructura elegida y adaptar la base común y skills pertinentes sin fingir que el generador soporta esa topología. Validar manualmente lo que el script no pueda verificar.

En todos los casos, trabajar en una rama de preparación cuando el repositorio destino sea Git y la tarea autorice cambios. Conservar archivos y modificaciones ajenas. Registrar versión o commit central, perfil aplicado, fecha y adaptaciones del proyecto; no mantener una rama permanente por proyecto en el repositorio central.

### Documentos comunes obligatorios

Al preparar los repositorios backend y frontend, copiar explícitamente desde la versión seleccionada de `harness-base` los cuatro documentos comunes de `docs/` a cada repositorio, antes de completarlos con información específica del proyecto:

- `harness-base/docs/architecture.md` → `<backend>/docs/architecture.md` y `<frontend>/docs/architecture.md`
- `harness-base/docs/conventions.md` → `<backend>/docs/conventions.md` y `<frontend>/docs/conventions.md`
- `harness-base/docs/specs.md` → `<backend>/docs/specs.md` y `<frontend>/docs/specs.md`
- `harness-base/docs/verification.md` → `<backend>/docs/verification.md` y `<frontend>/docs/verification.md`

Estos archivos son obligatorios en ambos repositorios, tanto si son nuevos como si ya existen. Adaptar cada copia al stack, arquitectura, convenciones, specs y comandos de verificación reales de ese repositorio. En un repositorio existente, conservar cambios compatibles del proyecto y adaptar el contenido después de copiarlo; no omitirlos por considerar que son documentos comunes. Si la versión real de `harness-base` usa otra ubicación o nombre, registrar la discrepancia y confirmar la ruta equivalente antes de continuar.

## Archivos a completar

| Archivo del proyecto | Resultado verificable |
| --- | --- |
| `docs/business_logic/functional-requirements.md` | Alcance, fuente/versiones, incluidos, excluidos y pendientes, con enlace al relevamiento canónico. |
| `feature_list.json` | Features acotadas con `source_ids`, aceptación observable, dependencias, prioridad fundada y estado inicial honesto. |
| `docs/business_logic/entity-relationship-diagram.md` | DER Mermaid y tabla que separa entidades/relaciones confirmadas, observadas y propuestas. |
| `docs/architecture.md` y `docs/conventions.md` | Estructura, integraciones y convenciones del repositorio real. |
| `docs/verification.md` | Comandos comprobados en el stack real y límites de entorno. |
| `docs/ui/DESIGN.md`, si hay frontend | Referencias y decisiones visuales aportadas; no inventar identidad aprobada. |
| `progress/` | Estado inicial y mecanismo de métricas del harness instalado. |
| `README.md` o `docs/harness.md` | Cómo iniciar/continuar una feature, aprobar specs, ejecutar verificación, consultar progreso y actualizar el harness. |

Completar estos archivos **en cada repositorio**, con contenido de backend o frontend según corresponda. En el backend, el DER detalla persistencia y relaciones; en el frontend, documenta el modelo de dominio consumido y señala el contrato/backend que gobierna esos datos, sin crear un modelo contradictorio. Revisar también `AGENTS.md`, `harness.json`, `docs/specs.md`, `docs/feature-list.md`, `docs/metrics.md` y el estado inicial de `progress/`; conservar las reglas generales del scaffold y sustituir las partes genéricas que requieran datos del proyecto. No inventar historial de trabajo ni eventos de features que todavía no ocurrieron.

No crear specs de todas las features durante la preparación. El flujo SDD prepara una feature por vez y conserva su aprobación humana antes del código.

## Comprobación final

Ejecutar `scripts/validate.py` de `harness-base` en cada instalación compatible. Comparar `source_ids` con el relevamiento, verificar dependencias, enlaces y que el DER no presente propuestas como hechos. Para repositorios existentes o monorepos, anotar comprobaciones manuales y límites del validador. Presentar el resultado por repo y los pendientes por ID.
