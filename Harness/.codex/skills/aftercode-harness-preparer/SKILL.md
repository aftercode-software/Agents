---
name: aftercode-harness-preparer
description: Preparar o adaptar el harness SDD de un proyecto Aftercode desde un relevamiento existente, usando harness-base y rutas locales explícitas de los repositorios frontend/backend. Usar para instalar perfiles, completar documentos, crear feature list y DER trazables y verificar la preparación; no para implementar funcionalidades.
---

# Preparador de Harness Aftercode

Convertir el relevamiento en una base de ejecución **revisable** dentro de los repositorios locales que indique el usuario. Normalmente se preparan un backend y un frontend. Trabajar con el usuario sobre decisiones que afecten alcance o arquitectura, y avanzar con las partes independientes. El resultado es un proyecto preparado para SDD, no un producto implementado ni un alcance aprobado por la institución.

## Entradas y fuentes

Antes de instalar, contar con: (1) rutas exactas de los documentos o carpeta de Relevamiento, (2) ruta local de `harness-base`, y (3) rutas locales **separadas y explícitas** de los repositorios destino backend y frontend. Si el proyecto usa un solo repositorio o un perfil no aplica, registrar esa excepción indicada por el usuario. Si falta la ruta de un repositorio requerido, pedirla; no deducirla por nombre ni crear un destino arbitrario. Leer [traspaso-relevamiento.md](references/traspaso-relevamiento.md) para conservar IDs, fuentes, decisiones y estado de aprobación. `FUNCIONALIDADES.md`, cuando existe, es el alcance canónico; no convertir una propuesta o un borrador en requisito aprobado.

Inspeccionar **cada** repositorio destino antes de escribir: instrucciones locales, estado Git, stack, código y contratos existentes. Leer el `README`, manifiesto, scaffold y scripts **actuales** de `harness-base` y fijar su commit o versión para cada repositorio. MCD inspiró la base operativa; no asumir que su UI o sus decisiones técnicas son las del proyecto. `harness-base` es la fuente obligatoria de los archivos y reglas iniciales.

Para el **frontend**, preguntar expresamente si existe un repositorio de referencia técnica o documental que convenga reutilizar y pedir su ruta o acceso. Preguntar también por la fuente visual: repositorio con UI, diseños, guía de marca o indicaciones de paleta, tipografías, componentes, formatos y comportamiento responsive. Una misma referencia puede cubrir ambos aspectos. Registrar qué fuente se usará y qué falta; no dar por completo `docs/ui/DESIGN.md` ni definir estilos como aprobados sin evidencia.

## Preparación

Seguir [adaptacion-proyecto.md](references/adaptacion-proyecto.md) para aplicar el perfil backend al repositorio backend y el perfil frontend al repositorio frontend, o documentar la excepción acordada. Generar en una rama de preparación de cada repositorio cuando corresponda; conservar cambios ajenos. Preparar ambos lados de un proyecto fullstack y mantener las dependencias entre ellos explícitas. No ejecutar dos perfiles sobre el mismo destino como si el scaffold actual admitiera esa combinación.

En el frontend, inventariar y trasladar **íntegros** los archivos aplicables de `scaffold/common/` y `scaffold/frontend/`, incluidos directorios ocultos: contratos de `.agents/`, árboles completos de `.agents/skills/`, documentos, guía de diseño, scripts y archivos de control. Copiar sin reescribir los roles, skills y Markdown estáticos; partir del contenido completo de las guías que requieran datos del proyecto y adaptar solo esas partes. Usar [auditar_frontend.py](scripts/auditar_frontend.py) para contrastar rutas y contenido con la versión de `harness-base` elegida antes de declarar el harness completo. Si un archivo existente entra en conflicto, conservarlo y resolver la integración de forma explícita; no omitir archivos silenciosamente.

En **cada repositorio destino**, completar los documentos y archivos que entrega `harness-base` con los datos del relevamiento que correspondan a su responsabilidad: alcance y fuentes, `feature_list.json`, arquitectura, convenciones, comandos de verificación, DER, guía de uso y decisiones pendientes. No dejar una plantilla genérica como si estuviera completa; si falta un dato, indicar la pregunta y su impacto en el propio documento. Mantener el mapa entre IDs `RF`/`TR` y los IDs locales del backlog. Un agrupador de negocio no se suma de nuevo a sus tareas; un trabajo transversal se registra una sola vez. Las relaciones y campos del DER inferidos se marcan como propuestas.

Antes de declarar listo el proyecto, aplicar [metricas.md](references/metricas.md): verificar que la versión instalada tenga un mecanismo real de eventos, tiempos, ciclos y uso por modelo. Si aún no está en `harness-base`, registrar esa brecha como pendiente de la base y no afirmar que las métricas funcionan.

Ejecutar los validadores del scaffold y revisar enlaces, trazabilidad de criterios, dependencias y referencias del DER. Entregar rutas, versión/commit del harness, estado por repositorio, dudas concretas y qué puede avanzar mientras otras unidades están condicionadas. Una prueba local no demuestra push, despliegue ni ejecución completa del flujo.

## Límites

- No implementar features, estimar horas comerciales, publicar ni desplegar por haber preparado el harness.
- No sobrescribir archivos o cambios existentes para forzar la plantilla. El generador vigente de `harness-base` requiere un destino vacío; en un repositorio ocupado, preparar una comparación en un directorio temporal y adaptar solo lo compatible.
- No autoaprobar specs ni resolver reglas de negocio sin fuente. La aprobación del spec sigue siendo una puerta humana del flujo SDD.
- No inferir tiempos ni tokens de resúmenes escritos por agentes: requieren eventos o telemetría del entorno.
- No crear ramas permanentes por proyecto en `harness-base`. Registrar la versión central usada y conservar la adaptación en el repositorio del proyecto.
