# Plan: Week 4 RAG Indexer and Asker

## Files to Create
- `intent/ask-the-course.md`: Defining RAG system goals.
- `spec.md`: Defining Indexer and Asker components, models, and behaviors.
- `indexer.py`: Scans course dir, chunks files, generates embeddings, and saves `index.json`.
- `asker.py`: Loads index, queries embeddings, computes cosine similarity, retrieves top chunks, prints scores, and prompts LLM.
- `questions.json`: 5 evaluation test cases (3 single-page, 1 multi-page, 1 unanswerable).
- `CHECKS.md`: Evaluation results with/without retrieval and stale-page analysis.
- `README.md` & `CLAUDE.md`

## Build Order
1. Commit pre-code artifacts (`intent/`, `spec.md`, `plan.md`).
2. Implement `indexer.py` to build local embeddings from course content.
3. Implement `asker.py` and `questions.json`.
4. Run evaluation matrix with and without RAG retrieval, document findings in `CHECKS.md`.

## Risks & Mitigations
- **Risk:** Large index file size or missing course path.
  - **Mitigation:** Add `index.json` to `.gitignore` or provide clear build instructions in `README.md`.

## Proof & Evaluation Strategy
- Run `asker.py` across `questions.json` with retrieval enabled vs disabled, comparing answer precision and refusal behavior.
