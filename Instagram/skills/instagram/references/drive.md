# Google Drive

## Destino esperado

El contenido de Instagram debe subirse a Google Drive en una carpeta llamada:

`instagram`

La carpeta debe estar ubicada al lado de la carpeta:

`linkedin`

Es decir, ambas deben compartir el mismo padre.

## Flujo con conector Google Drive

1. Buscar carpetas llamadas `linkedin`.
2. Si hay una sola carpeta clara, usar su carpeta padre.
3. Buscar o crear una carpeta hermana llamada `instagram`.
4. Dentro de `instagram`, crear una carpeta por semana con el mismo nombre que la carpeta local.
5. Subir:
   - `PLAN.md`
   - `HISTORIAS.md`
   - `POST.md`
   - `REEL.md`
   - `IMAGENES.md`
   - `FUENTES.md`, si existe
   - imagenes generadas, si existen
6. Registrar enlaces en `DRIVE.md`.

## Casos ambiguos

Si aparecen varias carpetas `linkedin`, pedir confirmacion antes de crear `instagram`.

Si no aparece `linkedin`, preguntar cual es la carpeta padre correcta o pedir un enlace/id de Drive.

Si el conector de Drive no esta disponible, crear todos los archivos locales y dejar `DRIVE.md` con el estado:

`Pendiente: falta acceso al conector Google Drive o confirmacion de carpeta destino.`

## Nombres de carpeta

Usar:

`YYYY-MM-DD-semana-instagram-tema`

Ejemplo:

`2026-06-28-semana-instagram-automatizacion-procesos`
