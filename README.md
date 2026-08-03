# perseus-action

GitHub Action that runs [Perseus](https://github.com/Perseus-Computing-LLC/perseus) to pre-render workspace context before AI assistants start work.

## Usage

```yaml
- uses: Perseus-Computing-LLC/perseus-action@main
  with:
    source: '.perseus/context.md'
    output: 'AGENTS.md'
    # Dangerous directives remain disabled unless explicitly required.
    allow_dangerous: 'false'
    provenance: 'AGENTS.md.provenance.json'
```

## What it does

Perseus resolves `@directives` in your context.md (services health, git state, memory search, skills listing) into a ready-to-consume markdown file that AI assistants read at session start. This action runs it in CI so context is always fresh.

## Safety and provenance

- Dangerous directives are **opt-in** through `allow_dangerous: 'true'`.
- `perseus-ctx` is installed at an exact version; review and update it deliberately.
- The action writes a hash-only provenance manifest beside the rendered context. It records the source/render digests, action revision, workspace revision, package version, dangerous-mode state, and completion status without copying raw context or secrets.
- For production workflows, pin the Action itself to a reviewed commit SHA rather than a moving branch such as `@main`.
