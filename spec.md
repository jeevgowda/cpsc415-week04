# Specification: Ask the Course Component

## Component 1: Indexer
- **Language/Library Decision:** Python 3 standard library (`json`, `os`, `pathlib`) with `urllib` for OpenAI/OpenRouter embedding requests.
- **Embedding Model:** `text-embedding-3-small` (or standard open-router embedding model alternative).
- **Role:** Scans the local course clone directory, chunks text documents, computes embeddings, and writes `index.json`.

## Component 2: Asker
- **Language/Library Decision:** Python 3 standard library.
- **Chat Model:** `anthropic/claude-3.5-haiku` via OpenRouter (Alternative: `nvidia/nemotron-3-ultra-550b-a55b:free`).
- **Role:** Computes query embedding, performs cosine similarity search against `index.json`, prints top retrieved chunks with scores, and injects context into prompt with strict refusal instructions.

## Numbered Behaviors
1. **Behavior 1 (Single-page factual lookups):** Questions answerable from a specific lecture page return exact course facts.
2. **Behavior 2 (Spread-out concepts):** Questions requiring synthesis across multiple pages aggregate relevant chunks.
3. **Behavior 3 (Unanswerable refusal):** When questions fall outside course scope, the system responds with "I can not find that."

## External Dependencies
- OpenRouter API (via standard library `urllib` and `json`, zero external pip dependencies).
