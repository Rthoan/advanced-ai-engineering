# Day 10 Notes — Reranking + Hybrid Search

## Hybrid

Dense
→ Meaning

BM25
→ Exact Terms

Hybrid
→ Meaning + Exact Terms

---

## RRF

Reciprocal Rank Fusion.

Purpose:

Merge ranked lists.

Useful when Dense and BM25 score scales are different.

---

## candidate_k

Number of candidates before / entering reranking.

Example:

candidate_k = 30

---

## final_k

Number of chunks kept for final context.

Example:

candidate_k = 30
↓
Reranker
↓
final_k = 5

---

## Reranker

Cross-Encoder:

Query + Chunk
↓
Relevance Score

Purpose:

Improve ranking precision.

---

## Diagnostic Rule

Low Recall
→ Improve Retrieval

High Recall + Low MRR
→ Reranker

Ranking gets worse after reranker
→ Reranker Problem

---

## MMR

Purpose:

Relevant + Diverse Results

Use mainly for broad or multi-aspect queries.

---

## Deduplication

Purpose:

Remove repeated candidates.

Possible keys:

chunk_id
document_id
content_hash

---

## Pipeline Order

Metadata Filter
↓
Dense + BM25
↓
RRF
↓
Reranker
↓
MMR
↓
Final Top-K

---

## Metrics

Recall@K
MRR
Precision@K
NDCG
Latency
Cost
Duplicate Rate

---

## Production Rule

Choose the best quality
within acceptable:

Latency
Cost
Complexity