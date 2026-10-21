# Day 09 — Retrieval Strategies

## Goal

Learn how to design and evaluate retrieval strategies for production RAG systems.

The main idea:

Query Type
↓
Choose Retrieval Strategy
↓
Retrieve Candidates
↓
Rank / Filter / Diversify
↓
Build Final Context

---

## Retrieval Strategies

### Dense Retrieval

Dense retrieval uses embeddings and vector similarity.

Best for:

- Natural language questions
- Semantic similarity
- Synonyms
- Different wording with similar meaning

Example:

Query:

Can I get my money back?

Document:

Customers may request a refund within 14 days.

Dense retrieval can identify the semantic relationship.

---

## Sparse Retrieval

Sparse retrieval such as BM25 focuses on exact words and terms.

Best for:

- IDs
- Product codes
- Policy numbers
- Error codes
- Names
- Rare technical terms

Example:

RET-2026-04

or:

SKU-X91

---

## Dense vs Sparse

Dense:

Meaning

Sparse:

Exact words

Rule:

Semantic meaning
→ Dense

Exact identifier
→ Sparse

---

## Hybrid Search

Hybrid Search combines:

Dense Retrieval
+
Sparse Retrieval

Useful when the query contains both meaning and exact terms.

Example:

What is the return policy for SKU-X91?

Semantic part:

return policy

Exact part:

SKU-X91

Architecture:

Query
↓
Dense Search + BM25 Search
↓
Merge Results
↓
Deduplicate
↓
Fusion
↓
Rerank
↓
Final Results

---

## Reciprocal Rank Fusion — RRF

Dense and BM25 scores often use different scales.

Example:

Dense:

0.91
0.83
0.76

BM25:

12.4
8.2
5.1

Raw scores should not normally be compared directly.

RRF combines ranked result lists using their positions rather than raw score scales.

Example:

Dense Ranking:

A → Rank 1
B → Rank 2
C → Rank 3

BM25 Ranking:

C → Rank 1
A → Rank 2
D → Rank 3

RRF produces a combined ranking.

---

## Top-K

Top-K controls how many results the retriever returns.

Example:

top_k = 5

Low K:

Risk of missing useful evidence.

High K:

More noise, latency, tokens, and cost.

Rule:

Low K
→ Higher risk of missing evidence

High K
→ Higher risk of noisy context

---

## Candidate K vs Final K

Production systems often use:

candidate_k = 20 or 30

then:

Reranker
↓
final_k = 5

Pattern:

Retrieve Broad
↓
Rerank
↓
Send Narrow Context

---

## Recall vs Precision

Recall asks:

Did we retrieve the important evidence?

Precision asks:

How much of the retrieved evidence is actually relevant?

Increasing K often improves recall but may reduce precision.

---

## Query Rewriting

Query Rewriting transforms a weak or context-dependent query into a clearer search query.

Example:

User:

What about if I opened it?

Rewritten:

Can the phone be returned after the package has been opened?

Goal:

Preserve user intent
+
Improve retrieval

---

## Multi-Query Retrieval

Multi-Query generates multiple search formulations.

Example:

Original:

Can I return an opened phone?

Queries:

1. opened phone return policy
2. smartphone refund after opening
3. return rules for unsealed electronics

Pipeline:

Multiple Queries
↓
Retrieve
↓
Merge
↓
Deduplicate
↓
Rerank

Multi-Query can improve recall but increases latency and cost.

---

## Metadata Filtering

Metadata can limit search to the correct scope.

Example:

country = Iraq
category = phones
document_type = return_policy
status = active

Pipeline:

Query
↓
Metadata Filter
↓
Retriever

---

## Pre-filter vs Post-filter

Pre-filter:

Filter before search.

Example:

country = Iraq
↓
Search only Iraq documents

Post-filter:

Search first
↓
Remove invalid results afterward

Pre-filter is usually preferred when strict metadata constraints are known.

---

## Hard Filters

Hard filters must not be violated.

Examples:

customer_id = current_user

country = Iraq

status = active

Security boundaries should be enforced before retrieval.

---

## Soft Preferences

Soft preferences influence ranking but do not completely remove other results.

Example:

Prefer newer documents.

---

## MMR

MMR stands for:

Maximal Marginal Relevance

It balances:

Relevance
+
Diversity

Normal similarity search may return multiple chunks containing the same information.

MMR tries to select relevant chunks that add new information.

Example:

Without MMR:

- Return period
- Return period
- Return period
- Return period
- Receipt requirement

With MMR:

- Return period
- Exceptions
- Receipt requirement
- Opened products
- Refund method

---

## Deduplication

Duplicate results waste context window and token budget.

Duplicates can be:

- Exact duplicates
- Semantic duplicates

Possible methods:

- document_id
- chunk_id
- content_hash
- similarity-based deduplication

---

## Reranking

The retriever finds candidate documents.

The reranker improves their ordering.

Pattern:

Retriever
↓
Top 30 Candidates
↓
Reranker
↓
Top 5

Rule:

Retriever
→ Find candidates

Reranker
→ Order candidates better

---

## Bi-Encoder vs Cross-Encoder

### Bi-Encoder

Query and documents are encoded separately.

Fast and scalable.

Best for:

Initial retrieval.

### Cross-Encoder

Query and candidate chunk are processed together.

Usually more accurate but slower.

Best for:

Reranking a small candidate set.

---

## RRF vs Reranker

RRF:

Combines multiple ranked lists.

Reranker:

Re-evaluates candidate relevance to the query.

Rule:

RRF
→ Combine rankings

Reranker
→ Improve ranking quality

---

## Reranker vs MMR

Reranker:

Focuses mainly on relevance.

MMR:

Focuses on relevance and diversity.

---

## Retrieval Failure Diagnosis

### Low Recall

Correct evidence is missing from candidates.

Possible causes:

- Weak embedding model
- Poor chunking
- Wrong query
- Wrong retrieval method
- Bad metadata
- Candidate K too small

Action:

Improve Retrieval

---

### High Recall + Poor Ranking

Correct evidence exists but ranks too low.

Action:

Use or improve a Reranker

---

### Good Retrieval + Bad Answer

Correct evidence reaches the LLM but the final answer is incorrect.

Possible causes:

- Context building
- Prompt
- LLM generation

This is not primarily a retrieval problem.

---

## Retrieval Debugging Workflow

1. Is the source document present?
2. Was it indexed?
3. Is the correct chunk well formed?
4. Is metadata correct?
5. Does retrieval return the chunk?
6. What is its rank?
7. Does reranking keep it?
8. Is it present in final context?
9. Does the LLM use it correctly?

---

## Production Retrieval Pipeline

A possible architecture:

User Query
↓
Query Classification
↓
Query Rewriting if needed
↓
Metadata Pre-filter
↓
Retriever Selection
├── Dense
├── Sparse
└── Hybrid
↓
Candidate Retrieval
↓
Merge
↓
Deduplicate
↓
RRF
↓
Reranker
↓
MMR if needed
↓
Final Top-K
↓
Context Builder
↓
LLM

Not every query needs every stage.

---

## Query Strategy Examples

Semantic question:

What are the return conditions?

→ Dense

Exact identifier:

RET-2026-04

→ Sparse

Mixed query:

What are the conditions in RET-2026-04?

→ Hybrid

Follow-up:

What if I opened it?

→ Query Rewriting

Broad question:

Explain the full return policy including exceptions and refund methods.

→ Multi-Query / MMR

---

## Evaluation Metrics

Important retrieval metrics:

- Recall@K
- Precision@K
- MRR
- Hit Rate
- Context Relevance
- Duplicate Rate
- Latency
- Cost

---

## Main Diagnostic Rule

Low Recall
→ Improve Retrieval

High Recall + Poor Ranking
→ Reranker

Good Retrieval + Bad Answer
→ Context / Prompt / Generation

---

## Main Lesson

There is no single best retriever.

The best retrieval strategy depends on:

- Query type
- Data type
- Exact identifiers
- Languages
- Metadata
- Latency requirements
- Cost
- Retrieval quality

Use the simplest strategy that satisfies the project requirements.