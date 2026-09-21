# Horas y Presupuestador base

Usar esta referencia durante la etapa 2 cuando se deban calcular horas desde requisitos o usar una planilla de horas proporcionada por el usuario.

## Modos de trabajo

- **Calcular horas:** leer los requisitos y completar una copia de `Presupuestador base`.
- **Usar planilla proporcionada:** leer una planilla existente como fuente de horas, sin recalcularla ni modificarla salvo pedido explícito.
- **Omitir horas:** no ejecutar este flujo; registrar que la estimación fue omitida y marcar como pendientes los datos dependientes.

## Documento de requisitos `.docx`

1. Leer el documento completo antes de formular preguntas redundantes.
2. Revisar párrafos, títulos, listas y tablas; no limitarse a una extracción parcial de texto.
3. Extraer como mínimo:
   - objetivo y problema del proyecto;
   - módulos y funcionalidades;
   - usuarios, roles y permisos;
   - integraciones y dependencias;
   - restricciones, supuestos y exclusiones;
   - puntos ambiguos o pendientes.
4. Usar el documento como fuente de requisitos, pero dar prioridad a una instrucción explícita y posterior del usuario si existe una contradicción.
5. Registrar en `HORAS_HOMBRE.md` el nombre o ruta del documento utilizado y cualquier ambigüedad que afecte la estimación.

Si el `.docx` está en Google Drive, localizarlo primero con el flujo de Google Drive y descargarlo como archivo no nativo para leerlo. No convertirlo a Google Docs salvo que el usuario lo solicite.

## Planilla proporcionada por el usuario

Aplicar esta sección solo en el modo **Usar planilla proporcionada**.

1. Identificar el archivo exacto mediante su URL, ID o ubicación.
2. Leer sus metadatos antes de consultar rangos y confirmar las pestañas visibles.
3. Identificar la pestaña, el rango de la tabla de horas, las fórmulas, las validaciones y el total.
4. Tratar la planilla como fuente de solo lectura. No copiarla, editarla ni recalcularla salvo pedido explícito.
5. Usar las horas, roles, totales y supuestos disponibles para generar el presupuesto.
6. Registrar en `HORAS_HOMBRE.md` el enlace o ruta, pestaña, rango, total y cualquier dato faltante.

Si la planilla no respalda algún dato necesario para el presupuesto, pedir solamente ese dato o marcarlo como pendiente. No completar los huecos con una estimación silenciosa.

## Plantilla de Google Sheets

La plantilla de horas es un archivo nativo de Google Sheets titulado `Presupuestador base`, ubicado en la raíz de My Drive. No confundirlo con el Google Doc `Presupuesto base`, que se usa en la etapa 4.

1. Buscar el archivo por título y verificar que esté en la raíz de My Drive.
2. Si no existe, hay varias coincidencias o la ubicación no es clara, detenerse y pedir confirmación.
3. Leer primero los metadatos del spreadsheet y los nombres exactos de sus pestañas.
4. Copiar el spreadsheet completo a un archivo nuevo; no editar el original ni reconstruir la plantilla desde cero.
5. Crear la copia en la raíz de My Drive con el nombre `Presupuestador <Nombre del cliente>`, salvo que el usuario indique otro nombre. Si ya existe un archivo con ese nombre, pedir confirmación antes de sobrescribir o crear una variante.
6. Verificar que el ID de la copia sea diferente al ID de `Presupuestador base`.

La copia y la escritura son una mutación externa. Antes de ejecutarlas, mostrar el documento de requisitos identificado, la plantilla encontrada, el nombre de la copia y el plan de carga. Una solicitud explícita del usuario para copiar y completar el presupuestador cuenta como autorización; si el usuario solo pidió preparar una estimación local, pedir confirmación antes de escribir en Drive.

## Carga de la tabla de horas

1. En la copia, identificar la pestaña y el rango real de la tabla de horas mediante sus metadatos y encabezados. No asumir `Sheet1`, una pestaña llamada `Horas` ni rangos fijos.
2. Leer encabezados, filas de ejemplo, fórmulas, formato, validaciones y cualquier total existente antes de escribir.
3. Para cada requisito, buscar primero en la plantilla el ejemplo existente más parecido por tipo de tarea, rol, alcance, complejidad e integraciones. Usar sus horas como referencia de calibración.
4. Partir de las horas del ejemplo más cercano y conservarlas cuando la nueva tarea tenga un alcance equivalente. Ajustarlas solo si hay una diferencia concreta de alcance o complejidad, y registrar el motivo.
5. Ejemplo: si la plantilla estima `Login` en 4 horas, un nuevo flujo de login equivalente debe estimarse en torno a 4 horas. Solo aumentar o reducir esa base si incorpora diferencias verificables, como recuperación de contraseña, 2FA, SSO, roles adicionales o una integración externa.
6. Usar el mismo nivel de redondeo y granularidad que la plantilla. Evitar cifras arbitrarias o excesivamente precisas. Si no existe un ejemplo razonablemente comparable, marcar la estimación como provisional y explicar qué supuesto se utilizó.
7. Mapear los requisitos del `.docx` a módulos, tareas, roles y horas. Mantener separadas las horas de relevamiento, gestión, UX/UI, frontend, backend, QA, DevOps, contenido/SEO u otros roles que realmente apliquen.
8. Completar únicamente las celdas de entrada de la tabla. Preservar fórmulas, validaciones, formato, congelamiento y estructura nativa de la plantilla.
9. Si hace falta agregar filas, hacerlo con la estructura nativa existente y sin convertir la tabla en un rango de valores plano. Si el esquema no permite representar una funcionalidad sin romper la plantilla, detenerse y consultar.
10. Verificar mediante una lectura posterior las celdas escritas, las fórmulas y los totales. El total de la hoja debe coincidir con `HORAS_HOMBRE.md`.
11. Revisar la hoja renderizada o sus metadatos visuales para detectar celdas cortadas, columnas ilegibles, fórmulas dañadas o cambios fuera del rango solicitado.

Seguir el skill `google-drive:google-sheets` para la búsqueda, copia, lectura de rangos, escritura y verificación. Usar lecturas acotadas y nombres exactos de pestañas; no hacer búsquedas sobre toda la grilla sin necesidad.

## Registro local

En `HORAS_HOMBRE.md` incluir:

- documento de requisitos utilizado;
- nombre y enlace de la copia de `Presupuestador base`;
- nombre de la pestaña y rango de la tabla completada;
- criterio de asignación de horas;
- ejemplo o fila de la plantilla usada como referencia para cada tarea;
- horas base tomadas del ejemplo y ajuste aplicado, si corresponde;
- desglose por rol y total;
- fórmulas o supuestos relevantes;
- riesgos, pendientes y diferencias entre el documento y la planilla.
