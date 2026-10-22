# Day 10 — Reranking + Hybrid Search

## Goal

Design a stronger production retrieval pipeline using:

- Dense Retrieval
- BM25 / Sparse Retrieval
- Reciprocal Rank Fusion
- Cross-Encoder Reranking
- MMR
- Controlled benchmarking

---

## Core Architecture

Metadata Filter
↓
Dense Retrieval + BM25
↓
RRF
↓
Unique Candidate Pool
↓
Cross-Encoder Reranker
↓
MMR if needed
↓
Final Top-K
↓
Context Builder
↓
LLM

---

## Dense Retrieval

Dense Retrieval uses embeddings.

Best for:

- Semantic meaning
- Natural language
- Synonyms
- Paraphrasing

Example:

Query:

Can I get my money back?

Document:

Customers may request a refund.

---

## Sparse Retrieval / BM25

Sparse Retrieval focuses on exact terms.

Best for:

- IDs
- SKU codes
- Policy numbers
- Error codes
- Names
- Rare terminology

Example:

SKU-X91

POL-2026-77

---

## Hybrid Search

Hybrid Search combines:

Dense Retrieval
+
Sparse Retrieval

Example:

What are the return conditions for POL-2026-77?

Semantic part:

return conditions

Exact part:

POL-2026-77

---

## Why Raw Scores Should Not Usually Be Added Directly

Dense scores and BM25 scores may use different scales.

Example:

Dense:

0.91
0.84
0.72

BM25:

13.4
9.1
5.8

These values are not directly comparable.

---

## Reciprocal Rank Fusion — RRF

RRF combines ranked result lists.

Instead of relying on raw scores, it uses ranking positions.

Example:

Dense:

A → Rank 1
B → Rank 2
C → Rank 3

BM25:

C → Rank 1
A → Rank 2
D → Rank 3

RRF can promote A and C because they rank highly in both systems.

Rule:

RRF
→ Merge ranked lists

---

## Weighted Fusion

Another option is:

Final Score
=
Dense Weight × Dense Score
+
Sparse Weight × Sparse Score

However, score normalization is normally required.

Weights should be tuned using evaluation data.

---

## Candidate Generation

The retriever should prioritize high recall.

Example:

Dense Top 20
+
BM25 Top 20
↓
Fusion
↓
30 Unique Candidates

These candidates are then sent to the reranker.

---

## candidate_k

candidate_k is the number of candidates available before or entering reranking.

Example:

candidate_k = 30

The correct evidence must be inside the candidate set before the reranker can promote it.

Rule:

Reranker cannot recover
what the Retriever did not retrieve.

---

## final_k

final_k is the number of final chunks kept for the context.

Example:

candidate_k = 30
↓
Reranker
↓
final_k = 5

---

## Cross-Encoder Reranker

A Cross-Encoder evaluates:

Query + Candidate Chunk

together.

It generates a relevance score and improves candidate ordering.

Rule:

Retriever
→ Find candidates

Reranker
→ Rank candidates more accurately

---

## Bi-Encoder vs Cross-Encoder

### Bi-Encoder

Query and document are encoded separately.

Advantages:

- Fast
- Scalable
- Suitable for initial retrieval

### Cross-Encoder

Query and document are processed together.

Advantages:

- Better relevance judgment
- Better final ranking

Disadvantage:

- Slower

Therefore:

Bi-Encoder
→ Retrieval

Cross-Encoder
→ Reranking

---

## Reranking Diagnosis

If:

Recall@30 is low

then:

Improve Retrieval

Possible causes:

- Weak embeddings
- Poor chunking
- Wrong metadata
- Weak query
- Wrong retriever
- candidate_k too small

If:

Recall@30 is high
but MRR is low

then:

Use or improve the Reranker

---

## Reranker Failure

If ranking becomes worse after reranking:

Before:

MRR = 0.82

After:

MRR = 0.64

Then investigate:

- Reranker model
- Language support
- Domain support
- Input formatting
- Truncation
- Configuration

---

## Multilingual Reranking

For systems with Arabic and English:

Arabic Query
↔
English Chunk

the reranker must support cross-lingual relevance.

---

## Domain-Specific Reranking

Specialized projects may require evaluation of domain-aware rerankers.

Examples:

- Legal
- Medical
- Financial
- Scientific

Do not assume a specialized model is automatically better.

Benchmark it.

---

## Deduplication

Dense and BM25 may return the same chunk.

Example:

Dense:
A B C

BM25:
A C D

The final candidate pool should contain:

A B C D

Use stable identifiers such as:

- chunk_id
- document_id
- content_hash

Rule:

Deduplication
→ Remove repeated candidates

---

## MMR

MMR improves diversity after relevance has been established.

Example:

Reranker results:

1. Return period
2. Return period
3. Return period
4. Opened products
5. Receipt

MMR can produce:

1. Return period
2. Opened products
3. Receipt
4. Refund method
5. Exceptions

Rule:

Reranker
→ Relevance

MMR
→ Diversity

---

## Recommended Ordering

Filter
↓
Retrieve
↓
Fuse
↓
Rerank
↓
Diversify
↓
Final Context

Example:

Metadata Pre-filter
↓
Dense + BM25
↓
RRF
↓
Cross-Encoder Reranker
↓
MMR
↓
Final Top-K

---

## Benchmarking

Compare controlled configurations.

Example:

Config A:
Dense only

Config B:
Hybrid + RRF

Config C:
Hybrid + RRF + Reranker

Config D:
Hybrid + RRF + Reranker + MMR

Keep fixed:

- Documents
- Chunks
- Embeddings
- Metadata
- Test queries
- Final K

---

## Evaluation Metrics

Use:

- Recall@K
- Precision@K
- MRR
- NDCG
- Latency
- Cost
- Duplicate Rate
- Context Relevance

---

## Segmented Evaluation

Do not rely only on overall averages.

Evaluate:

- Semantic queries
- Exact queries
- Mixed queries
- Broad queries
- Cross-lingual queries

---

## Production Selection

The highest metric does not automatically mean the best production system.

Choose:

Best quality
within acceptable
Latency + Cost + Complexity

---

## Failure Diagnosis

Low Recall
→ Improve Retrieval

High Recall + Low MRR
→ Improve Ranking / Reranker

Performance Drops After Reranking
→ Reranker Problem

Relevant but Repetitive Results
→ MMR / Diversity

High Latency
→ Profile Each Stage

---

## Main Lesson

Retrieval
→ Maximize Candidate Recall

Fusion
→ Combine Retrieval Signals

Reranking
→ Improve Precision and Ranking

MMR
→ Improve Useful Diversity