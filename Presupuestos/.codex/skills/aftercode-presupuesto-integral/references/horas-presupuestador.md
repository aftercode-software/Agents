# Horas y Presupuestador base

Usar esta referencia durante la etapa 2 cuando se deban calcular horas desde requisitos o usar una planilla de horas proporcionada por el usuario.

Aplicar tambien [traspaso-presupuestos.md](traspaso-presupuestos.md) para conservar fuentes seleccionadas, IDs, granularidad y modo de horas. Las instrucciones de copia/carga siguientes aplican cuando se solicito trabajar en Sheets y existe autorizacion; una estimacion exclusivamente local no requiere escritura externa.

## Modos de trabajo

- **Calcular horas:** leer los requisitos y completar una copia de `Presupuestador base`.
- **Usar horas proporcionadas:** conservar las horas indicadas por el usuario en una planilla, documento o mensaje, sin recalcularlas ni modificar su fuente salvo pedido explícito.
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

Aplicar esta sección solo cuando el modo **Usar horas proporcionadas** usa una planilla. Para documentos o mensajes, registrar la fuente, valores y granularidad sin exigir planilla ni inventar pestañas/rangos.

1. Identificar el archivo exacto mediante su URL, ID o ubicación.
2. Leer sus metadatos antes de consultar rangos y confirmar las pestañas visibles.
3. Identificar la pestaña, el rango de la tabla de horas, las fórmulas, las validaciones y el total.
4. Tratar la planilla como fuente de solo lectura. No copiarla, editarla ni recalcularla salvo pedido explícito.
5. Usar las horas, roles, totales y supuestos disponibles para generar el presupuesto.
6. Registrar en `HORAS_HOMBRE.md` el enlace o ruta, pestaña, rango, total y cualquier dato faltante.

Respetar las pestañas/versiones elegidas y descartadas por el usuario. No mezclar un resumen por áreas con tareas de otro alcance. Conservar las horas por área cuando no existe desglose por funcionalidad; no reconstruirlo mediante reparto proporcional. Mantener el alcance documental y los valores numéricos con sus fuentes respectivas.

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
3. Para cada unidad estimable, buscar una referencia comparable por alcance, tipo de trabajo, rol, complejidad, reutilización, equipo y cobertura de entrega. Registrar si sus horas son medidas, aproximadas o solo presupuestadas.
4. Usar sus horas como punto de partida solo cuando la comparación sea defendible. Explicar ajustes y supuestos; no forzar un ejemplo lejano ni convertir baja/media/alta en una tabla fija de horas.
5. Un ejemplo llamado `Login` no alcanza para establecer equivalencia: comprobar recuperación, 2FA/SSO, permisos, servicios existentes, pruebas y revisión. El uso de IA no garantiza que su esfuerzo se reduzca.
6. Usar el mismo nivel de redondeo y granularidad que la plantilla. Evitar cifras arbitrarias o excesivamente precisas. Si no existe un ejemplo razonablemente comparable, marcar la estimación como provisional y explicar qué supuesto se utilizó.
7. Mapear el alcance seleccionado a IDs de unidades estimables, tareas, áreas/roles y horas. No sumar padres e hijos ni repetir transversales. Distinguir frontend web, mobile, backend y otras disciplinas pertinentes sin contar “fullstack” nuevamente como otra capa; explicitar cobertura de relevamiento, harness, revisión, QA y estabilización.
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
- versión del alcance, IDs vinculados y partidas condicionadas/bloqueadas; subtotal conocido cuando no se puede cerrar el total;
- naturaleza y granularidad de las horas; si son agregadas por área, declarar que no hay asignación aprobada por funcionalidad.
