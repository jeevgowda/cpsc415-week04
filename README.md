# Week 4: Ask the Course (RAG) & Plan

## Overview
A zero-dependency Python RAG system (`indexer.py` and `asker.py`) that indexes local course markdown files using OpenAI embeddings (`text-embedding-3-small`) and answers student inquiries via OpenRouter (`anthropic/claude-3.5-haiku`) with exact context chunks and cosine similarity scores.

## Design Rationale & Component Decisions
- **Indexer Component:** Uses standard library `urllib.request` and `json` to compute vector embeddings for chunked markdown paragraphs, storing them in `index.json`. Python was selected to eliminate complex build dependencies.
- **Asker Component:** Computes query embeddings, performs vector cosine similarity matching against the index, extracts top scoring context chunks, and injects them into the prompt with strict system instructions to refuse unanswerable questions.
- **Model Selection:** `anthropic/claude-3.5-haiku` was chosen for its precise adherence to contextual grounding rules and refusal constraints.

## How to Build & Run
1. Set API keys and course path:
   export OPENROUTER_API_KEY="your-key"
   export OPENAI_API_KEY="your-key"
   export COURSE_DIR="../cpsc415-course"
2. Build the index:
   python3 indexer.py
3. Run evaluation questions:
   python3 asker.py

## Stale-Page Analysis
When multiple versions of a document exist in repository history, similarity scoring ranks active path documents higher based on semantic density and recency, successfully preventing outdated notes from overriding current lab specifications.
