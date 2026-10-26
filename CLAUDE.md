# CLAUDE.md Guidelines - Week 4
- Standard library Python only (`json`, `os`, `urllib`, `math`, `pathlib`).
- No API keys committed to git.
- `index.json` is excluded via `.gitignore` and rebuilt locally via `indexer.py`.
- All evaluation runs must output exact similarity scores for retrieved chunks and enforce strict refusal ("I can not find that.").
