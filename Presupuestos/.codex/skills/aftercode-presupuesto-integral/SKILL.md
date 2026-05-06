---
name: aftercode-presupuesto-integral
description: Crear y gestionar presupuestos comerciales de Aftercode de punta a punta. Usar cuando el usuario quiera relevar un proyecto, hacer un ping pong de preguntas y respuestas, analizar archivos o documentacion disponible, definir alcance y exclusiones, estimar horas por rol, redactar el presupuesto final siguiendo la plantilla del proyecto y, con confirmacion explicita, subirlo a Google Drive usando la plantilla "Presupuesto base".
---

# Aftercode Presupuesto Integral

Guiar el proceso en cuatro etapas con compuertas claras de confirmacion. Avanzar de una etapa a la siguiente solo cuando la informacion este suficientemente cerrada o el usuario confirme de forma explicita.

## Recursos a usar

- Leer `references/plantillas-presupuestos.md` para respetar la estructura de `Pagina web basica` o `Sistema complejo`.
- Si el usuario aporta archivos, notas, propuestas previas o documentacion, analizarlos antes de formular preguntas nuevas.
- Para la etapa de Google Drive, usar las capacidades del plugin `Google Drive` y, si hace falta editar el contenido del documento, seguir tambien el skill `google-drive:google-docs`.

## Flujo obligatorio

### Etapa 1: Descubrimiento y relevamiento

Entender el proyecto con precision antes de escribir archivos de salida.

#### Objetivo

Obtener una definicion clara de:

- finalidad del proyecto
- problema que resuelve
- tipo de proyecto: `Pagina web basica` o `Sistema complejo`
- funcionalidades incluidas
- funcionalidades excluidas
- integraciones
- restricciones
- actores o usuarios del sistema
- prioridades

#### Como trabajar

- Hacer un ping pong de preguntas y respuestas, en bloques cortos y concretos.
- Priorizar preguntas que cierren alcance y reduzcan ambiguedad.
- Si existen documentos, archivos, notas o presupuestos anteriores, leerlos y usarlos para evitar preguntas redundantes.
- Si detectas contradicciones o zonas grises, frenarlas y aclararlas antes de seguir.
- Cuando el proyecto sea complejo, resumir periodicamente lo entendido y pedir confirmacion parcial.
- No pasar a la etapa 2 hasta poder explicar con claridad que incluye el proyecto, que no incluye y cual es su objetivo.

#### Preguntas guia

Adaptar las preguntas al caso, sin usar siempre todas:

- Cual es el objetivo principal del proyecto
- Quien va a usar el sistema o sitio
- Que proceso actual se quiere mejorar o reemplazar
- Cuales son las funciones imprescindibles del primer alcance
- Que cosas seria bueno tener pero no son necesarias en esta etapa
- Hay panel administrador, roles o permisos
- Hay integraciones con terceros
- Hay restricciones de tiempo, presupuesto o tecnologia
- Hay contenido, branding o documentacion previa

#### Cierre de etapa

Cerrar la etapa solo cuando puedas redactar un resumen preciso del alcance y el usuario no tenga correcciones sustanciales sobre esa definicion.

### Etapa 2: Definicion funcional y estimacion

Crear una carpeta local del cliente y dejar por escrito el alcance funcional y la estimacion operativa.

#### Carpeta de trabajo

- Crear en la raiz del proyecto una carpeta con el nombre del cliente.
- Si ya existe, inspeccionar su contenido antes de escribir y continuar sin borrar archivos existentes.
- Usar nombres de archivo exactos:
  - `FUNCIONALIDADES.md`
  - `HORAS_HOMBRE.md`

#### Archivo `FUNCIONALIDADES.md`

Documentar como minimo:

- nombre del cliente
- tipo de proyecto
- objetivo general
- resumen del problema o necesidad
- alcance incluido
- exclusiones
- modulos o secciones
- funcionalidades detalladas
- usuarios, roles y permisos si aplican
- integraciones
- supuestos y dependencias
- dudas abiertas o decisiones pendientes

Escribirlo de manera util para luego presupuestar y eventualmente construir el proyecto.

#### Archivo `HORAS_HOMBRE.md`

Estimar esfuerzo considerando que el equipo trabaja con apoyo intensivo de IA y herramientas como Codex o Claude Code, por lo que las horas deben reflejar una ejecucion acelerada respecto de un proceso tradicional.

Incluir como minimo:

- criterio de estimacion
- supuestos de productividad con IA
- desglose por rol
- horas por rol
- total estimado
- riesgos que pueden aumentar o reducir el esfuerzo

Roles posibles, segun el caso:

- relevamiento funcional
- project management
- UX/UI
- frontend
- backend
- QA
- DevOps
- contenido o SEO

No forzar roles que no aporten. Si un rol no aplica, omitirlo.

#### Cierre de etapa

- Mostrar al usuario el contenido o un resumen fiel de `FUNCIONALIDADES.md` y `HORAS_HOMBRE.md`.
- Pedir confirmacion antes de pasar a la etapa 3.
- Si el usuario corrige funcionalidades o tiempos, actualizar ambos archivos antes de seguir.

### Etapa 3: Redaccion del presupuesto

Convertir lo definido en un presupuesto estructurado y presentable.

#### Archivo de salida

- Crear o actualizar `PRESUPUESTO.md` dentro de la carpeta del cliente.

#### Estructura obligatoria

- Elegir la plantilla adecuada leyendo `references/plantillas-presupuestos.md`.
- Si el proyecto es un sitio institucional, landing o web de complejidad baja a media, usar `Plantilla 1: Pagina web basica`.
- Si el proyecto es software a medida, portal operativo, CRM, ERP, backoffice o sistema con logica de negocio, usar `Plantilla 2: Sistema complejo`.
- Respetar los titulos y el orden de la plantilla elegida.

#### Contenido del presupuesto

Redactar cada seccion del presupuesto a partir de lo validado en etapas anteriores. Incluir:

- objetivo del proyecto
- alcance real
- exclusiones
- entregables o modulos segun corresponda
- plazos estimados
- inversion, si el usuario ya la definio
- forma de pago, si el usuario ya la definio
- proximos pasos

Si faltan datos comerciales criticos, hacer preguntas puntuales antes de cerrar el documento.

#### Cierre de etapa

- Presentar `PRESUPUESTO.md` al usuario.
- Esperar feedback y hacer ajustes.
- No pasar a la etapa 4 hasta recibir confirmacion explicita de que el presupuesto esta aprobado para subirse.

### Etapa 4: Publicacion en Google Drive

Subir el presupuesto final a la estructura comercial de Google Drive respetando la plantilla base.

#### Precondicion

Solo ejecutar esta etapa con confirmacion explicita del usuario.

#### Flujo en Google Drive

1. Buscar en la raiz de Google Drive la carpeta `Cuentas`.
2. Dentro de `Cuentas`, buscar una carpeta con el nombre del cliente.
3. Si existe mas de una candidata o el nombre no coincide claramente, preguntar al usuario cual corresponde.
4. Si no existe, proponer crearla y confirmar con el usuario antes de hacerlo.
5. Buscar el Google Doc `Presupuesto base` dentro de `Cuentas/Presupuestos generales`.
6. Copiar ese documento dentro de la carpeta del cliente.
7. Nombrar la copia `Presupuesto <Nombre del cliente>`.

#### Edicion del documento

- Llevar el contenido de `PRESUPUESTO.md` al Google Doc copiado.
- Respetar todos los títulos y subtítulos del markdown.
- Aplicar estilos de encabezado reales en Google Docs para todos los títulos y subtítulos, usando la herramienta de Google Drive.
- Aplicar formato de lista real en todas las listas, usando la herramienta de Google Drive.
- Si al copiar contenido quedan guiones sueltos simulando listas, eliminarlos y reconstruir la lista con formato de lista nativo.
- Eliminar los espacios en blanco sobrantes entre párrafos para que el documento quede compacto y consistente.
- Conservar los estilos existentes de `Presupuesto base`.
- No remaquetar el documento manualmente si eso rompe los estilos originales.
- Mantener intacto cualquier bloque de referencias o cierre que deba preservarse según la plantilla base existente en Drive.
- Revisar cuidadosamente ortografía, acentuación y tildes antes de dar el documento por finalizado.

#### Verificaciones finales

- Confirmar que el documento quedó en la carpeta correcta.
- Verificar que no queden placeholders ni texto genéricamente redactado.
- Verificar que todos los encabezados sean consistentes con `PRESUPUESTO.md` y tengan estilo de encabezado aplicado.
- Verificar que todas las listas tengan formato de lista aplicado y que no queden guiones sueltos donde debería haber viñetas o numeración real.
- Verificar que no queden líneas o espacios en blanco innecesarios entre párrafos.
- Verificar que el documento final conserve correctamente todas las tildes y caracteres en español.

## Reglas de calidad

- Ser extremadamente preciso con inclusiones y exclusiones.
- No inventar funcionalidades, horas, integraciones ni cifras faltantes.
- Si algo no esta confirmado, marcarlo como pendiente.
- Priorizar claridad comercial y operativa por encima del lenguaje ornamental.
- Reutilizar informacion ya validada; no reabrir decisiones cerradas salvo contradiccion.
- Si el usuario cambia el alcance, actualizar primero `FUNCIONALIDADES.md` y `HORAS_HOMBRE.md` antes de tocar `PRESUPUESTO.md`.
- Tratar como requisito critico la correcta escritura en español, incluyendo tildes, acentos y caracteres especiales.
- En Google Docs, no dejar títulos como texto plano ni listas simuladas con guiones.
- No dejar espacios en blanco sobrantes entre párrafos en el documento final.

## Formato esperado de los archivos

Si necesitas una guia concreta para redactar los archivos locales, leer `references/archivos-salida.md` y `references/plantillas-presupuestos.md`.

## Entrega al usuario

Al terminar cada etapa, informar:

- que etapa se completo
- que archivos se crearon o actualizaron
- que decisiones quedaron confirmadas
- que falta para pasar a la siguiente etapa
