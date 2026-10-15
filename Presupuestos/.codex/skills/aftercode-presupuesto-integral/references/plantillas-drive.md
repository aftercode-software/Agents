# Plantillas en Google Drive

Las dos plantillas se identifican **por ID**, no por título ni ubicación. Si un
ID no responde o el archivo cambió de tipo, detenerse y pedir al usuario el
enlace vigente; no buscar sustitutos por nombre.

| Uso | Archivo | Tipo | ID |
| --- | --- | --- | --- |
| Interno: cálculo de horas (etapa 2) | `Presupuestador base` | Google Sheets | `1Y_cSckG3a_NuyMzuJ52oDlwNJR4SBvCvyYmkDXAIl3o` |
| Cliente: texto del presupuesto (etapa 4) | `Presupuesto Base Texto` | Google Docs | `1RaDB3tijHRfnLMhfuGt-rgsuh2HuV6ArGquFWLj058U` |

- El **Sheet es interno**: nunca se comparte ni se envía al cliente.
- El **Doc es lo que recibe el cliente**. Nunca editar ninguna de las dos
  plantillas: siempre trabajar sobre una copia.

## `Presupuestador base` (Sheets)

Pestañas conocidas: `Time sheet`, `Hours` (tabla `Horas`: `Número`, `Tarea`,
`Área`, `Complejidad` [Baja/Media/Alta], `Alcance`, `Horas`) y `Stats`
(protegida con advertencia). Confirmar igualmente con los metadatos antes de
escribir; si cambiaron, seguir lo que diga la planilla real.

## `Presupuesto Base Texto` (Docs)

La plantilla es un **presupuesto real ya completado** de otro cliente, con los
estilos de Aftercode. Su estructura es:

1. Cuerpo del presupuesto: secciones con estilo de encabezado (`Introducción`,
   `Objetivo del proyecto`, `Problema actual`, `Solución propuesta`,
   funcionalidades por perfil, `Entregables`, `Etapas de trabajo`,
   `Plazo estimado`, `Inversión`, `Forma de pago`, `Mantenimiento opcional`).
2. Bloque final **`Referencias de nuestros trabajos.`** con casos de Aftercode.

Al preparar el presupuesto de un cliente:

- Copiar el Doc a la carpeta del cliente con el nombre
  `Presupuesto <Nombre del cliente>`.
- **Reemplazar todo el cuerpo** (desde el inicio hasta antes de
  `Referencias de nuestros trabajos.`) con el contenido de `PRESUPUESTO.md`,
  usando sus títulos como encabezados reales y sus listas como listas nativas.
  No reutilizar frases, cifras, plazos ni funcionalidades del cliente de la
  plantilla.
- **Conservar intacto** el bloque `Referencias de nuestros trabajos.` y lo que
  le sigue, salvo pedido explícito del usuario.
- Verificación obligatoria antes de entregar: leer el Doc final y confirmar que
  no quede ningún resto del cliente de la plantilla (por ejemplo `enfermer`,
  `prestaciones`, `rendiciones`, `750 usd`, `250 dólares`, `6 a 8 semanas`),
  salvo que el nuevo proyecto los incluya de verdad.
