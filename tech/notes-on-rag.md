---
title: Notes on RAG
parent: Tech
nav_order: 1
---

# Notes on RAG

> Dummy note. The code block below shows that syntax highlighting works out
> of the box.

A retrieval-augmented generation system is mostly an exercise in *not*
embarrassing yourself at retrieval time. The model is rarely the bottleneck;
the chunking and ranking usually are.

## Minimal loop

```python
def answer(query, store, llm):
    chunks = store.search(query, k=5)      # retrieval
    context = "\n\n".join(c.text for c in chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}"
    return llm.complete(prompt)            # generation
```

## Things that actually move the needle

- **Chunk boundaries** that respect document structure, not fixed token counts.
- **Reranking** the top-k before it hits the prompt.
- **Evals** you trust, so you can tell whether a change helped.

## To revisit

- Hybrid search (dense + BM25) vs. pure dense — when is the complexity worth it?
