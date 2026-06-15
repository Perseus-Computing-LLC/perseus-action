# perseus-action

GitHub Action that runs [Perseus](https://github.com/tcconnally/perseus) to pre-render workspace context before AI assistants start work.

## Usage

```yaml
- uses: tcconnally/perseus-action@main
  with:
    source: '.perseus/context.md'
    output: 'AGENTS.md'
```

## What it does

Perseus resolves `@directives` in your context.md (services health, git state, memory search, skills listing) into a ready-to-consume markdown file that AI assistants read at session start. This action runs it in CI so context is always fresh.
