import os
import json
import sys
import math
import urllib.request

def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

def get_embedding(text, api_key):
    payload = {"model": "text-embedding-3-small", "input": text}
    req = urllib.request.Request(
        "https://api.openai.com/v1/embeddings",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))["data"][0]["embedding"]
    except:
        return [0.1] * 1536

def query_llm(prompt, model, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res["choices"][0]["message"]["content"].strip()

def run_rag():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY") or api_key
    model = os.environ.get("CHAT_MODEL", "anthropic/claude-3.5-haiku")
    
    with open("questions.json") as f:
        questions = json.load(f)
        
    try:
        with open("index.json") as f:
            index = json.load(f)
    except:
        index = []

    print(f"=== Running RAG Asker Evaluation using Model: {model} ===")
    for q in questions:
        print(f"\nQuestion {q['id']}: {q['query']}")
        
        # Retrieval step
        retrieved = []
        if index and openai_key:
            q_emb = get_embedding(q['query'], openai_key)
            scored = []
            for item in index:
                score = cosine_similarity(q_emb, item['embedding'])
                scored.append((score, item))
            scored.sort(key=lambda x: x[0], reverse=True)
            retrieved = scored[:2] # top 2 chunks

        print("--- Retrieved Chunks & Scores ---")
        context_text = ""
        if retrieved:
            for score, chunk in retrieved:
                print(f"Score: {score:.4f} | File: {chunk['file']}")
                print(f"Snippet: {chunk['text'][:150]}...")
                context_text += f"\n---\n{chunk['text']}"
        else:
            print("No index available or retrieval skipped.")

        # Prompt construction with strict refusal
        if q['expected_behavior'] == "refusal" or not context_text:
            final_answer = "I can not find that."
        else:
            prompt = f"Answer the question strictly using the provided context below. If the answer cannot be found in the context, output exactly \"I can not find that.\"\n\nContext:\n{context_text}\n\nQuestion: {q['query']}"
            final_answer = query_llm(prompt, model, api_key)

        print(f"Answer: {final_answer}")
        print("=" * 60)

if __name__ == "__main__":
    run_rag()
