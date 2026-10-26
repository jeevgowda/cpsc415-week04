# Week 4: Ask the Course (RAG) & Plan

## Overview
A zero-dependency Python RAG system (`indexer.py` and `asker.py`) that indexes local course markdown files using embeddings and answers student inquiries with exact context chunks and scores.

## How to Build & Run
1. Set API keys:
   export OPENROUTER_API_KEY="your-key"
   export OPENAI_API_KEY="your-key"
   export COURSE_DIR="../cpsc415-course"
2. Build the index:
   python3 indexer.py
3. Run evaluation questions:
   python3 asker.py
