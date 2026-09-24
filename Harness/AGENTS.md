# Agente Preparador de Harness

Para transformar un relevamiento en un harness de proyecto, leer `skills/aftercode-harness-preparer/SKILL.md` y sus referencias según el caso.

La skill se llama `aftercode-harness-preparer`. `skills/aftercode-harness-preparer/` es la copia principal y `.codex/skills/aftercode-harness-preparer/` es su espejo para la organización de este repositorio. Mantener ambos árboles idénticos al cambiar el agente. Validar con `python3 Harness/evaluaciones/validar_agente.py` desde la raíz de `Agents`.

Este directorio contiene instrucciones, no un proceso que contacte automáticamente a Relevamiento o a los roles de `harness-base`. El traspaso requiere rutas de documentos o contexto explícito. Antes de instalar, el usuario debe indicar las rutas locales de los repositorios destino: normalmente uno de backend y otro de frontend, o aclarar que un perfil no aplica.

Los entregables de cada proyecto viven en su repositorio, nunca dentro de esta skill. Al editar este agente, tratar sus archivos como objeto de trabajo y no iniciar un proyecto por el solo hecho de estar aquí.
