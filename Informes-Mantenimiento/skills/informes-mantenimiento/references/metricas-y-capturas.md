# Métricas, capturas y acceso a Analytics

## Datos y períodos

Registrar cliente/dominio, fuente, propiedad si se conoce, intervalo exacto inclusivo, zona horaria, filtros/segmentos y fecha de consulta. Para GA4 usar la zona de la propiedad; la fecha de creación en Mendoza es independiente. Verificar que el cierre incluya el último día del mes y no sume el primer día del siguiente. Un mes todavía en curso es parcial y debe identificarse como tal; no compararlo como si fuera completo.

Las métricas mínimas de uso son las que existan en las fuentes: usuarios, sesiones/visitas y visualizaciones. Añadir canales, páginas principales, interacción, dispositivos o eventos cuando estén disponibles y ayuden a explicar el uso. No completar casilleros con valores inventados ni convertir un dato ausente en cero.

| Etiqueta | Distinción necesaria |
| --- | --- |
| Usuarios activos | Personas según la definición de GA4; no equivale a sesiones ni usuarios totales. |
| Sesiones / visitas | Sesiones de navegación. Si el usuario dice «visitas», aclarar qué indicador se está usando. |
| Visualizaciones | Vistas de páginas/pantallas, incluidas repeticiones; no son visitantes únicos. |
| Eventos | Acciones registradas; no todos son consultas, ventas o conversiones. |
| Tiempo de interacción | Conservar el nombre y denominador exactos de la fuente, por usuario activo o por sesión. |

No sumar usuarios únicos de páginas/canales/días para reconstruir el total mensual. No mezclar canales de adquisición de usuarios con adquisición de sesiones; conservar el alcance de la tabla fuente.

## Capturas como fuente

Usar las capturas que envíe el usuario tanto para extraer datos como para ilustrar el informe. Leer números, títulos, propiedad, fechas y filtros visibles. Interpretar separadores locales (`4.021` puede ser cuatro mil veintiuno; `2,14` puede ser decimal) y unidades. No adivinar cifras borrosas, porcentajes cortados ni períodos ocultos: solicitar la mínima aclaración o exportación que falte. Registrar que la fuente fue una captura, sin presentar la lectura como una consulta en vivo.

Si el usuario ya aportó todo, no volver a pedirlo. Si falta algo, indicar qué vistas serían útiles: resumen del mes informado y del mes anterior, adquisición de tráfico por canal y páginas principales. Esto no vuelve obligatorios todos los paneles para un informe que solo dispone de un resumen. Si hay capturas de arreglos o antes/después, ubicarlas con el trabajo correspondiente.

## Comparaciones y conclusiones

Comparar primero con el mes calendario inmediatamente anterior. Si solo existe un informe más antiguo, rotularlo como comparación histórica y dejar explícita la falta del mes anterior; no renombrarlo para cumplir la comparación.

Una base comparable requiere la misma propiedad/sitio, definición y unidad, zona, filtros, cobertura y estado completo/parcial. Dos meses calendario completos son comparables aunque tengan distinta cantidad de días; mostrar los intervalos y, si afecta la interpretación, el volumen medio diario adicional. Un intervalo de 47 días frente a un mes no es una comparación mensual equivalente. No normalizar usuarios únicos automáticamente por día.

- Diferencia absoluta: `actual - anterior`.
- Variación relativa: `(actual - anterior) / anterior × 100`, únicamente con base anterior positiva y compatible.
- Base cero: informar la diferencia y «sin base porcentual», nunca infinito o crecimiento de 100% arbitrario.
- Sin datos o sin compatibilidad: mantener los valores disponibles e indicar «sin datos comparables»; no calcular una variación engañosa.
- Tasas expresadas en porcentaje: distinguir **puntos porcentuales** de variación relativa.

No copiar porcentajes publicados sin verificarlos. Describir incrementos y caídas según el signo; no llamarlos mejora o deterioro automáticamente. Un cambio de tráfico no demuestra que un arreglo lo causó. Causas como campañas, bots, caídas de servicio o cambios de etiquetas requieren evidencia propia; si faltan, presentarlas como hipótesis. Evitar «tráfico 100% real», garantías SEO o conversiones deducidas de eventos genéricos.

### Calculadora local

`scripts/comparar_metricas.py` acepta por stdin o archivo una lista JSON de filas:

```json
[
  {"indicador":"Sesiones","actual":"1200","anterior":"1000","comparable":true},
  {"indicador":"Arreglos completados","actual":3,"anterior":0,"comparable":true},
  {"indicador":"Usuarios activos","actual":null,"anterior":500,"comparable":false}
]
```

Usar números sin separadores de miles y punto decimal. `comparable` es obligatorio y debe decidirse a partir de las fuentes, no del valor de los números. La calculadora sirve para cantidades o duraciones no negativas; calcular tasas en puntos porcentuales por separado. Devuelve diferencias y porcentajes con dos decimales, o un estado que explica por qué no corresponden. No consulta Drive/GA4, no identifica clientes ni valida períodos.

```bash
python3 scripts/comparar_metricas.py /ruta/al/archivo.json
```

## Lectura directa y futura automatización

Usar primero una integración de Analytics disponible con permisos de lectura o el navegador autenticado cuando permita ver la propiedad. Validar nombre/dominio, ID, fechas y filtros antes de extraer. No consultar APIs privadas, cookies ni credenciales del navegador. Si aparece bienvenida, acceso denegado o un selector sin la propiedad, detener la lectura de esa fuente y continuar con capturas/exportaciones; no pulsar «Empezar a medir» para resolverlo.

La automatización repetible puede hacerse con **Google Analytics Data API**, consultando `properties/<ID>:runReport` con autenticación autorizada y acceso a la propiedad. Para Nutriterra el ID aportado es `463601934`. El scope de lectura es `https://www.googleapis.com/auth/analytics.readonly`; la integración requiere acceso efectivo además del scope. Puede devolver totales de `activeUsers`, `sessions`, `screenPageViews`, `eventCount` y tablas por `sessionDefaultChannelGroup` o `pagePath`, verificando antes los nombres/compatibilidad actuales. Consultar totales sin dimensiones para evitar sumar usuarios duplicados. Conservar limitaciones de cobertura, umbrales o muestreo expuestas por la respuesta.

Esto es una vía posible, **no una integración implementada por esta skill**. No crear cuentas de servicio, claves, accesos, etiquetas o tareas programadas sin una solicitud específica. No guardar secretos en el repositorio.

Si el cliente no tiene Analytics, indicar «Métricas de uso no disponibles para este período» y completar los trabajos con las otras fuentes. Proponer configurar medición si es útil; no prometer reconstruir tráfico de un período no medido. Otras fuentes como estadísticas del hosting o Search Console deben nombrarse y no presentarse como sesiones de GA4.

Fuentes técnicas verificadas al crear el agente: [Inicio de Google Analytics API](https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart) y [dimensiones y métricas](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema). Revalidar documentación al implementar una integración.
