# Galeria de mockups

Usar esta galeria unicamente despues de aprobar la imagen principal. Las bases estan en `assets/mockups/`, el catalogo tecnico en `assets/mockups/manifest.json` y el compositor en `scripts/componer_mockup.swift`.

Todas las salidas deben medir exactamente **1080 x 1350 px**.

## Seleccion

- `monitor`: capturas de sitios, dashboards, software de escritorio o contenido panoramico.
- `notebook`: producto digital, trabajo remoto, equipos y escenas de uso profesional.
- `telefono`: aplicaciones mobile, retratos verticales o contenido pensado para pantalla angosta.
- `navegador`: sitios web y capturas donde convenga hacer evidente el contexto web.

Elegir una base segun el tema, la orientacion de la imagen y sus colores. Si hay una opcion claramente adecuada, recomendarla y mostrar la composicion. Si hay dos o tres buenas alternativas, componerlas y permitir que el usuario elija. No mostrar las 31 opciones salvo que el usuario pida ver la galeria completa.

Cuando el usuario pida ver la galeria completa, mostrar `assets/mockups/catalogo.png`.

## Composicion

Ejecutar:

```bash
swift -module-cache-path /private/tmp/linkedin-swift-cache scripts/componer_mockup.swift \
  --template ID_DEL_MANIFEST \
  --input /ruta/imagen-aprobada.png \
  --output /ruta/mockup-final.png \
  --focus center
```

`--focus` admite `center`, `top`, `bottom`, `left` y `right`. Elegir `top` para retratos cuando sea necesario proteger rostros y `center` para capturas de producto.

El compositor debe:

- conservar la proporcion de la imagen;
- recortar solo lo necesario para llenar la pantalla;
- aplicar perspectiva en telefonos inclinados;
- preservar marcos, fondos, barras del navegador, notch y Dynamic Island;
- reemplazar por completo el texto `Drop or Paste`;
- no alterar la base grafica;
- exportar PNG en 1080 x 1350.

Si el entorno aislado impide a Core Image renderizar, volver a ejecutar el mismo comando con aprobacion de permisos; no cambiar de compositor ni degradar la calidad.

Conservar tambien la imagen aprobada sin mockup. No usar como base las composiciones de ejemplo que ya contienen sitios o fotografias.
