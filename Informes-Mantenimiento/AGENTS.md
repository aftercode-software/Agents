# Agente Informes Mantenimiento

Para elaborar un informe mensual de mantenimiento de un cliente, leer `skills/informes-mantenimiento/SKILL.md` y las referencias que correspondan.

El nombre visible es **Informes Mantenimiento** y la skill se invoca como `$informes-mantenimiento`. La copia principal vive en `skills/informes-mantenimiento/`; mantener idéntico su espejo en `.codex/skills/informes-mantenimiento/`. El enlace de descubrimiento en la raíz, `.agents/skills/informes-mantenimiento`, apunta a la copia principal.

Editar o revisar este agente no inicia un informe de cliente. Los informes se guardan en Google Drive dentro de `Cuentas/<cliente>/<fecha actual>/`, nunca dentro de la skill. Este rol no ejecuta mantenimiento ni instala Analytics: documenta trabajos y propone mejoras.
