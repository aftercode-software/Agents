# Agentes de Aftercode

Repositorio de agentes de trabajo (no es una aplicación). Cada carpeta es un
agente con su skill; las reglas de cada uno viven en su `AGENTS.md` y en su
`skills/<nombre>/SKILL.md`. Este archivo solo orienta a Claude.

| Agente | Skill (`/nombre`) | Para qué |
| --- | --- | --- |
| `Relevamiento/` | `relevamiento` | Bajar una idea a tierra: alcance, arquitectura, costos operativos |
| `Presupuestos/` | `aftercode-presupuesto-integral` | Presupuestos comerciales de punta a punta, con horas y Drive |
| `Harness/` | `aftercode-harness-preparer` | Instalar el harness SDD (`harness-base`) en repos de un proyecto |
| `Informes-Mantenimiento/` | `informes-mantenimiento` | Informe mensual de mantenimiento de un cliente en Drive (en desarrollo) |
| `Linkedin/` | `linkedin` | Posts para el perfil personal de LinkedIn de Matías |
| `Instagram/` | `instagram` | Contenido semanal de Instagram de Aftercode |
| `Nicho/` | — (solo `AGENTS.md`) | Análisis de negocio y procesos de un nicho |

## Reglas para Claude

- Las skills se exponen vía `.claude/skills/` (symlinks a `<Agente>/skills/<nombre>/`).
  La copia principal es `<Agente>/skills/`; `.codex/skills/` es su espejo para
  Codex. **Al editar un agente, mantener ambos árboles idénticos** y validar:
  `python3 Relevamiento/evaluaciones/validar_integracion.py` y
  `python3 Harness/evaluaciones/validar_agente.py`.
- Editar o revisar un agente no inicia su trabajo (no arrancar un relevamiento,
  presupuesto o informe por estar en su carpeta).
- Los entregables de clientes nunca se guardan dentro de las carpetas de skills.
- Google Drive, Docs y Sheets: usar los conectores de claude.ai. Si no están
  disponibles o autorizados, avisar antes de empezar en vez de improvisar
  archivos locales como reemplazo.
- Claude no genera imágenes: en LinkedIn e Instagram, avisar y entregar prompts
  listos salvo que haya una herramienta de generación conectada.
