# Tasker XML Format Lock

Codex must not break Tasker format.

## Forbidden

- Do not convert runtime XML to JSON.
- Do not convert runtime XML to YAML.
- Do not output snippets as final runtime.
- Do not output documentation-only build.
- Do not strip plugin bundle data.
- Do not strip private/local settings.
- Do not strip key task.
- Do not strip sheet IDs.
- Do not reformat in a way that changes Tasker import behavior.
- Do not output `.prj.xml` unless explicitly instructed.
- Do not create partial/truncated XML.
- Do not wrap XML in markdown fences.

## Required

- Full `.xml`
- XML declaration
- `<TaskerData ...>`
- complete tasks/profiles/scenes/projects
- valid UTF-8
- valid XML parse
- importable into Tasker

## Raw reference preservation

The raw XML in `REFERENCE_RAW_DO_NOT_REFORMAT` is copied byte-for-byte.
Use it as source reference.
Do not alter raw reference file.
