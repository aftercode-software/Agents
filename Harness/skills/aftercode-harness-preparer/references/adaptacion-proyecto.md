# Adaptación de harness-base al proyecto

## Inspección inicial

Recibir y verificar las rutas locales de `harness-base`, repositorio backend y repositorio frontend. Si uno no existe o no aplica, resolverlo expresamente con el usuario antes de instalar ese perfil. No buscar una carpeta de nombre parecido y asumir que es el destino.

Leer el `README.md`, `scripts/scaffold.py`, `scripts/validate.py`, `scaffold/common/`, perfiles y `harness.json` de la versión **real** de `harness-base`. Registrar commit/tag y si el árbol tiene cambios sin confirmar; una copia de trabajo en progreso no se presenta como versión publicada. Inspeccionar ambos repositorios destino y sus instrucciones antes de decidir archivos y comandos.

Para el frontend, preguntar antes de armar el harness:

1. ¿Hay un repositorio que sirva de referencia técnica o documental? Pedir su ruta local o acceso, y precisar qué se quiere reutilizar: estructura, agentes, skills, guías, componentes o convenciones. Si no hay, registrarlo y usar la base y el repositorio destino como fuentes verificadas.
2. ¿Dónde está la referencia visual del proyecto? Pedir repositorio con UI, diseños, guía de marca o indicaciones para paleta, tipografías, formatos, componentes, espaciado, iconografía, estados y responsive. Puede ser el mismo repositorio de la pregunta anterior. Registrar qué está aprobado y qué sigue pendiente.

Inspeccionar las referencias indicadas antes de trasladar contenido. Contrastar su stack y vigencia con el frontend destino. Reutilizar patrones y documentación pertinentes con su procedencia; no trasladar reglas de negocio, rutas, credenciales ni decisiones visuales de otro proyecto como si pertenecieran a este. Si una referencia contradice `harness-base` o al proyecto, documentar la diferencia y resolver la elección con el usuario.

El scaffold observado al redactar esta guía elige un perfil `frontend` **o** `backend` y solo admite destinos vacíos. Volver a comprobarlo porque puede cambiar.

## Destinos

- **Repositorio nuevo y vacío:** ejecutar el generador con el perfil correspondiente y validar su salida antes de completar contenido.
- **Repositorio existente:** generar primero en un directorio temporal y comparar con instrucciones, arquitectura, tests y código existentes. Incorporar todos los archivos obligatorios del perfil; para rutas ya ocupadas, integrar el contenido compatible sin sustituir cambios ajenos y dejar el conflicto pendiente cuando no se pueda resolver. No ejecutar el generador directamente sobre un árbol ocupado ni omitir archivos por el solo hecho de que ya exista el directorio.
- **Frontend y backend separados, caso habitual:** aplicar `scaffold/common/` y `scaffold/backend/` al backend; `scaffold/common/` y `scaffold/frontend/` al frontend. Preparar cada repositorio en su ruta indicada, conservar referencias a los mismos IDs de origen y documentar contratos y dependencias entre ambos. No duplicar una función completa en los dos backlogs: describir el resultado específico de cada lado.
- **Monorepo o perfil no soportado:** documentar la estructura elegida y adaptar la base común y skills pertinentes sin fingir que el generador soporta esa topología. Validar manualmente lo que el script no pueda verificar.

En todos los casos, trabajar en una rama de preparación cuando el repositorio destino sea Git y la tarea autorice cambios. Conservar archivos y modificaciones ajenas. Registrar versión o commit central, perfil aplicado, fecha y adaptaciones del proyecto; no mantener una rama permanente por proyecto en el repositorio central.

### Integridad obligatoria del frontend

Usar la salida completa del generador de la versión seleccionada como inventario esperado de `scaffold/common/` + `scaffold/frontend/` (el perfil frontend prevalece cuando ambos contienen la misma ruta). Incluir directorios ocultos; en particular, los cuatro contratos de rol de `.agents/`, **todos** los archivos de cada `.agents/skills/`, `skills-lock.json`, los Markdown de `docs/` y `docs/ui/`, `AGENTS.md`, scripts, `harness.json`, `feature_list.json`, specs y `progress/`. No reconstruir los archivos a partir de un resumen ni copiar solo `SKILL.md` dejando fuera sus referencias, reglas o assets.

Copiar byte por byte los archivos reutilizables que no contienen datos del proyecto, incluidos los roles, skills y Markdown estáticos. Los documentos que sí requieren datos locales parten de la **versión íntegra** de la plantilla: conservar sus secciones y reglas reutilizables, y completar o corregir únicamente lo que exijan el relevamiento, el código y las referencias elegidas. `docs/ui/DESIGN.md` es una plantilla hasta que se incorporen fuentes visuales verificadas. Si el repo técnico de referencia aporta material adicional que falta en `harness-base`, incorporarlo tras comprobar compatibilidad y registrar origen y adaptación; no reemplazar por ello archivos obligatorios de la base.

Antes del cierre, ejecutar `python3 <ruta-de-esta-skill>/scripts/auditar_frontend.py --base <ruta-harness-base> --destino <ruta-frontend>`. Compara recursivamente las rutas esperadas y exige igualdad de bytes para `.agents/`, `docs/feature-list.md`, `docs/metrics.md` y `docs/specs.md`. Revisar además cualquier otro Markdown que sea estático en la versión elegida; para los documentos adaptados, comprobar que no se hayan perdido secciones ni reglas de la base y que cada decisión específica tenga fuente. Si falta un archivo, una skill está incompleta o una colisión sigue abierta, corregirla o declarar el frontend pendiente con la ruta y la decisión necesaria. El validador general del scaffold no sustituye esta comparación. Si se modifica deliberadamente un archivo estático por una necesidad del proyecto, registrar la excepción y su fuente; el auditor seguirá señalando la diferencia para revisión.

### Documentos comunes obligatorios

Al preparar los repositorios backend y frontend, incluir explícitamente los cuatro documentos de `docs/` del perfil efectivo de la versión seleccionada de `harness-base`, antes de completarlos con información específica del proyecto. En la versión inspeccionada, `scaffold/backend/docs/` y `scaffold/frontend/docs/` prevalecen sobre los archivos de igual nombre en `scaffold/common/docs/`:

- `scaffold/<perfil>/docs/architecture.md` → `<destino>/docs/architecture.md`
- `scaffold/<perfil>/docs/conventions.md` → `<destino>/docs/conventions.md`
- `scaffold/<perfil>/docs/specs.md` → `<destino>/docs/specs.md`
- `scaffold/<perfil>/docs/verification.md` → `<destino>/docs/verification.md`

Estos archivos son obligatorios en ambos repositorios, tanto si son nuevos como si ya existen. Partir de cada documento completo y adaptar sus partes específicas al stack, arquitectura, convenciones, specs y comandos de verificación reales de ese repositorio. En un repositorio existente, conservar cambios compatibles del proyecto; no omitirlos por considerar que son documentos comunes. Si la versión real de `harness-base` usa otra ubicación o nombre, registrar la discrepancia y confirmar la ruta equivalente antes de continuar.

## Archivos a completar

| Archivo del proyecto | Resultado verificable |
| --- | --- |
| `docs/business_logic/functional-requirements.md` | Alcance, fuente/versiones, incluidos, excluidos y pendientes, con enlace al relevamiento canónico. |
| `feature_list.json` | Features acotadas con `source_ids`, aceptación observable, dependencias, prioridad fundada y estado inicial honesto. |
| `docs/business_logic/entity-relationship-diagram.md` | DER Mermaid y tabla que separa entidades/relaciones confirmadas, observadas y propuestas. |
| `docs/architecture.md` y `docs/conventions.md` | Estructura, integraciones y convenciones del repositorio real. |
| `docs/verification.md` | Comandos comprobados en el stack real y límites de entorno. |
| `docs/ui/DESIGN.md`, si hay frontend | Fuente visual y estado de aprobación; paleta, tipografías, formatos, componentes, estados y responsive derivados de esa fuente. Dejar preguntas pendientes donde falte definición, sin inventar identidad aprobada. |
| `progress/` | Estado inicial y mecanismo de métricas del harness instalado. |
| `README.md` o `docs/harness.md` | Cómo iniciar/continuar una feature, aprobar specs, ejecutar verificación, consultar progreso y actualizar el harness. |

Completar estos archivos **en cada repositorio**, con contenido de backend o frontend según corresponda. En el backend, el DER detalla persistencia y relaciones; en el frontend, documenta el modelo de dominio consumido y señala el contrato/backend que gobierna esos datos, sin crear un modelo contradictorio. Revisar también `AGENTS.md`, `harness.json`, `docs/specs.md`, `docs/feature-list.md`, `docs/metrics.md` y el estado inicial de `progress/`; conservar las reglas generales del scaffold y sustituir las partes genéricas que requieran datos del proyecto. No inventar historial de trabajo ni eventos de features que todavía no ocurrieron.

No crear specs de todas las features durante la preparación. El flujo SDD prepara una feature por vez y conserva su aprobación humana antes del código.

## Comprobación final

Ejecutar `scripts/validate.py` de `harness-base` en cada instalación compatible. En el frontend, añadir la comparación recursiva y de archivos estáticos descrita arriba. Comparar `source_ids` con el relevamiento, verificar dependencias, enlaces y que el DER no presente propuestas como hechos. Para repositorios existentes o monorepos, anotar comprobaciones manuales y límites del validador. Presentar el resultado por repo y los pendientes por ID.
