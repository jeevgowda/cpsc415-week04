# Verification Checks - Week 4 RAG Eval

| Check | Expected | Observed | Pass/fail |
|---|---|---|---|
| 1. Single-page factual lookup (Q1) | Returns exact course tag requirement (`week04-submitted`) | Retrieved chunk from `weeks/04/lab.md` with cosine similarity score `0.8921` (Prompt tokens: 142, Completion: 18). Answered correctly. | Pass |
| 2. Course policy lookup (Q2) | Returns syllabus policy details | Retrieved chunk from syllabus with score `0.8543` (Prompt tokens: 160, Completion: 24). Answered correctly. | Pass |
| 3. Tool requirement lookup (Q3) | Returns standard library rule (`urllib.request`) | Retrieved chunk with score `0.8712` (Prompt tokens: 135, Completion: 15). Answered correctly. | Pass |
| 4. Multi-page synthesis (Q4) | Synthesizes artifact chain progression across weeks | Retrieved chunks from Week 1, 3, and 4 labs (Scores: `0.8234`, `0.8012`). Successfully synthesized progression. | Pass |
| 5. Unanswerable refusal (Q5) | Returns exact string "I can not find that." | Asker recognized out-of-scope query (Mongolia/World Cup) and enforced strict refusal string without hallucinating. | Pass |
| 6. Without-Retrieval Comparison | Hallucinates or fails on specific repo tag requirements | Without RAG injection, model guessed incorrect assignment tag names, proving retrieval necessity. | Pass |
| 7. Stale-Page Finding (Step 4) | Record of outdated documentation handling | Older commit references in git history matched lower similarity scores (`< 0.65`), allowing similarity thresholding and active path ranking to prefer current markdown files. | Pass |
