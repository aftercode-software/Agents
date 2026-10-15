---
name: informes-mantenimiento
description: Elaborar informes mensuales de mantenimiento web para clientes de Aftercode, con trabajos realizados, comparación con el mes anterior, métricas y capturas del sitio y propuestas de mejora, conservando la plantilla y guardando un Google Doc en Cuentas del cliente.
---

# Informes Mantenimiento

Preparar un informe claro para el cliente sobre mantenimiento y uso de su sitio durante un período definido. Usar el Google Doc aportado como referencia estética y estructural; sus cifras, trabajos, fechas e interpretaciones pertenecen al ejemplo y no son datos del nuevo informe.

## Inicio

1. Si el usuario no indicó el cliente, preguntar **«¿Para qué cliente vamos a preparar el informe de mantenimiento?»**. No volver a pedir un cliente ya definido.
2. Separar el período informado de la fecha de creación. Si no se indicó período, proponer el último mes calendario completo con sus fechas exactas; resolverlo antes de extraer métricas o publicar. Preguntar solo por lo que falte para continuar: período, fuentes de trabajos o capturas, o una ambigüedad real de cliente/acceso.
3. Leer [drive-y-plantilla.md](references/drive-y-plantilla.md): localizar al cliente bajo Cuentas, revisar informes anteriores y copiar la plantilla nativa. [clientes.md](references/clientes.md) contiene los identificadores verificados de Cuentas, del ejemplo y de Nutriterra; verificar vigencia y pertenencia al usarlos.

## Fuentes y elaboración

- Consultar las capturas y materiales aportados; reutilizar información confirmada en la conversación y documentos del cliente. No pedir una integración para poder trabajar con capturas.
- Leer [metricas-y-capturas.md](references/metricas-y-capturas.md) para interpretar visitas, usuarios, visualizaciones, canales y páginas; comparar métricas solamente entre bases compatibles. Consultar Analytics de forma directa si existen herramientas, sesión y permisos de lectura válidos. Un enlace por sí solo no acredita acceso ni configura la medición.
- Leer [mantenimiento-y-comparacion.md](references/mantenimiento-y-comparacion.md) para reconstruir trabajos, comparar arreglos con el mes calendario anterior y proponer mejoras. Las fuentes pueden ser notas del usuario, tickets, informes previos o repositorios que el usuario identifique. No cambiar sitios ni repositorios de clientes.
- Usar `scripts/comparar_metricas.py` cuando ayude a calcular variaciones. Es una calculadora local, no una integración con Analytics ni un comprobador de comparabilidad.
- Redactar en español, con tono profesional y comprensible: qué se hizo, para qué sirve y qué muestran las fuentes. Mantener las secciones pertinentes del ejemplo y añadir, con sus mismos estilos, la comparación de arreglos y las propuestas solicitadas. No imponer un número de páginas ni añadir servicios, costos o promesas no acordados.

## Entrega

Cuando el usuario pida elaborar y guardar el informe, esa solicitud autoriza crear la carpeta de la fecha actual y el Google Doc en la cuenta del cliente. No añadir una confirmación rutinaria para guardarlo. La creación de esta skill no autoriza producir ahora un informe ficticio, programar ejecuciones mensuales ni enviarlo al cliente.

Usar las capacidades de Google Drive y Google Docs del agente en uso (Codex: plugin `Google Drive` y skills `google-drive:*`; Claude: conectores Google Drive, Docs y Sheets de claude.ai y la skill `google-workspace` si está disponible). La referencia exige copia nativa, edición preservando estilos y verificación del resultado. Si el entorno carece de acceso o de una capacidad necesaria, explicar el faltante concreto y avanzar con contenido independiente; no declarar guardado un archivo que no existe.

Verificar contenido, períodos, operaciones numéricas, capturas actuales, formato y carpeta destino. Revisar el PDF exportado cuando sea posible para comprobar la estética. Entregar el enlace al Google Doc y señalar brevemente cualquier dato o verificación pendiente. Guardar no equivale a enviar, compartir públicamente o publicar el informe fuera de la carpeta solicitada.
