# Day 09 Notes — Retrieval Strategies

## Dense Retrieval

Use for:

- Semantic meaning
- Natural language questions
- Synonyms

Rule:

Meaning
→ Dense

---

## Sparse Retrieval

Use for:

- IDs
- Codes
- Exact phrases
- Rare keywords

Rule:

Exact terms
→ Sparse

---

## Hybrid Search

Dense + Sparse

Use when the query contains:

Meaning
+
Exact identifier

---

## RRF

Reciprocal Rank Fusion.

Used to combine ranked lists such as:

Dense Ranking
+
BM25 Ranking

Useful because raw score scales may be different.

---

## Top-K

Small K:

May miss evidence.

Large K:

May add noise.

Production pattern:

Retrieve Broad
↓
Rerank
↓
Send Narrow

---

## Query Rewriting

Use for:

- Follow-up questions
- Ambiguous references
- Context-dependent queries

Example:

"What if I opened it?"

→

"Can the phone be returned after opening it?"

---

## Multi-Query

Use when:

- Vocabulary mismatch exists
- Recall is low
- Query is broad
- Several interpretations are possible

Trade-offs:

Recall ↑
Latency ↑
Cost ↑

---

## Metadata Filtering

Examples:

country
category
document_type
customer_id
version
status

Hard filter:

Strict requirement.

Soft preference:

Ranking preference.

---

## MMR

Maximal Marginal Relevance.

Goal:

Relevance
+
Diversity

Useful for broad multi-aspect questions.

---

## Deduplication

Remove repeated chunks before building final context.

Possible identifiers:

chunk_id
document_id
content_hash

---

## Reranker

Retriever:

Find candidates.

Reranker:

Improve candidate ordering.

Rule:

High Recall + Poor Ranking
→ Reranker

---

## Failure Diagnosis

Correct chunk missing:
→ Improve Retrieval

Correct chunk found but ranked low:
→ Reranker

Correct context reaches LLM but answer is wrong:
→ Prompt / Generation

Repeated results:
→ MMR / Deduplication

Exact ID missed:
→ Sparse / Hybrid

---

## Evaluation

Measure:

Recall@K
MRR
Hit Rate
Precision@K
Context Relevance
Duplicate Rate
Latency
Cost

---

## Core Decision

Semantic
→ Dense

Exact
→ Sparse

Semantic + Exact
→ Hybrid

Context-dependent
→ Query Rewriting

Vocabulary mismatch
→ Multi-Query

Broad question
→ MMR

Multiple ranked lists
→ RRF

Poor ranking
→ Reranker