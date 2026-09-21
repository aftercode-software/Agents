# Archivos de salida

Usar esta referencia para mantener consistencia entre presupuestos.

## `FUNCIONALIDADES.md`

Estructura sugerida:

```md
# Funcionalidades

## Cliente

## Tipo de proyecto

## Objetivo general

## Problema o necesidad

## Alcance incluido

## Exclusiones

## Modulos o secciones

## Funcionalidades detalladas

## Roles y permisos

## Integraciones

## Supuestos y dependencias

## Pendientes abiertos
```

## `HORAS_HOMBRE.md`

Estructura sugerida:

```md
# Horas Hombre

## Cliente

## Modo de estimacion

## Criterio de estimacion

## Supuestos de productividad con IA

## Desglose por rol

## Total estimado

## Riesgos y variaciones posibles
```

Dentro de `Desglose por rol`, listar cada rol con:

- objetivo del rol
- tareas principales
- horas estimadas
- comentarios o supuestos

Cuando se use `Presupuestador base`, agregar tambien:

```md
## Documento de requisitos utilizado

## Presupuestador base

## Enlace a la copia

## Pestaña y rango completados

## Total reconciliado con la hoja

## Referencias de estimacion

Para cada tarea estimada, registrar el ejemplo de `Presupuestador base` utilizado como referencia, sus horas base y cualquier ajuste aplicado.
```

En el modo `Usar planilla proporcionada`, reemplazar las referencias de `Presupuestador base` por la fuente real utilizada. En el modo `Omitir horas`, indicar que la estimacion fue omitida a pedido del usuario y listar los datos pendientes.

## `PRESUPUESTO.md`

- Elegir la estructura leyendo `references/plantillas-presupuestos.md`.
- Copiar solo la plantilla que corresponda al tipo de proyecto.
- Completar cada seccion con informacion concreta del cliente.
- Mantener `Inversion`, `Forma de pago`, `Consideraciones y exclusiones` y `Proximos pasos` hacia el final del documento.
- Escribir siempre con ortografia correcta en español, respetando tildes y acentos.
- Al llevar el contenido a Google Docs, convertir los encabezados en estilos de encabezado y las listas en listas nativas.
- Al finalizar la edición en Google Docs, eliminar los espacios en blanco innecesarios entre párrafos.
