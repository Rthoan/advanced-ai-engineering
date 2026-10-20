# Day 08 — Embedding Strategy

## Goal

Learn how to choose, evaluate, and deploy an embedding model for a production RAG system.

Main decision flow:

Project Requirements
↓
Languages
↓
Domain
↓
Privacy
↓
Local vs API
↓
Candidate Models
↓
Benchmark
↓
Metrics
↓
Choose Model
↓
Version Index

---

## What is an Embedding?

An embedding converts text into a numerical vector.

Example:

"return policy"

→

[0.12, -0.44, 0.91, ...]

The main idea:

Similar meaning
→ Similar vectors

---

## Why Embeddings Matter in RAG

Embeddings directly affect retrieval quality.

Bad representation
↓
Bad retrieval
↓
Bad context
↓
Bad answer

The LLM cannot fix missing evidence if the retriever does not find the correct chunk.

---

## Semantic Similarity

Embeddings allow semantic search.

Example:

Query:

Can I return my phone?

Document:

Opened smartphones are not eligible for refund.

The words are different, but the meaning is related.

---

## Vector Dimensions

Embedding models may generate vectors with:

- 384 dimensions
- 768 dimensions
- 1024 dimensions
- 1536 dimensions
- or more

More dimensions do not automatically mean better retrieval.

Higher dimensions may require:

- More memory
- More storage
- More compute
- Larger indexes

Always evaluate retrieval quality.

---

## Similarity Metrics

Common similarity methods:

- Cosine Similarity
- Dot Product
- Euclidean Distance

Use the metric recommended for the embedding model and vector index.

Do not choose the similarity metric randomly.

---

## Similarity Threshold

A vector database can always return the closest result, even when the result is poor.

Therefore, a minimum relevance threshold can be useful.

Example:

Low similarity
↓
No reliable context
↓
Fallback

There is no universal threshold such as 0.8 for every model.

Thresholds must be tuned using evaluation data.

---

## Normalization

Some models or retrieval setups recommend normalized embeddings.

Example:

normalize_embeddings = True

Normalization can make vector comparisons more consistent.

Always follow the embedding model's recommended configuration.

---

## General Embeddings

Useful for general domains such as:

- FAQ
- E-commerce
- Company documentation
- Support systems
- General knowledge bases

---

## Domain-Specific Embeddings

May perform better in specialized domains such as:

- Legal
- Medical
- Financial
- Scientific

Example:

A legal embedding model may better understand terms such as:

- indemnification
- jurisdiction
- force majeure
- termination clause

However, domain-specific models should still be benchmarked on real project data.

---

## Multilingual Embeddings

Multilingual RAG systems require strong language support.

Example:

Arabic Query
↓
English Document

This requires cross-lingual retrieval.

Important tests:

Arabic Query → Arabic Document

Arabic Query → English Document

English Query → Arabic Document

English Query → English Document

A model may support Arabic but still perform poorly on Arabic-to-English retrieval.

---

## Multilingual vs Domain-Specific

Sometimes there is a trade-off.

Example:

Model A:
- Excellent legal English
- Weak Arabic support

Model B:
- Strong multilingual support
- General-domain model

The correct decision depends on:

- User languages
- Document languages
- Domain vocabulary
- Privacy
- Retrieval benchmark results

---

## Local Embeddings

Advantages:

- Data remains local
- More privacy
- More control
- No per-request API cost

Disadvantages:

- Infrastructure required
- Model serving responsibility
- Scaling responsibility
- Monitoring required

Useful when:

- Data is sensitive
- GPU infrastructure exists
- Privacy is important

---

## API Embeddings

Advantages:

- Easy to use
- Managed infrastructure
- Easy scaling
- Less operational work

Disadvantages:

- Data may leave the system
- Network latency
- API cost
- Provider dependency
- Rate limits

---

## Local vs API Decision

API Embeddings
=
Simplicity + Managed Scaling

Local Embeddings
=
Privacy + Control

The real decision depends on:

Privacy
+
Cost
+
Latency
+
Scale
+
Infrastructure
+
Operational Complexity

---

## Benchmarking Embedding Models

Do not choose a model from marketing claims.

Use a benchmark on your real data.

Example:

Model A
Model B
Model C

Use:

- Same documents
- Same chunks
- Same test queries
- Same top_k
- Same retrieval configuration

Then compare results.

---

## Evaluation Metrics

Important metrics include:

- Recall@K
- Hit Rate
- MRR
- Query embedding latency
- Cost
- Memory usage
- Index size
- Cross-lingual retrieval performance

---

## Example Benchmark

Model A:

Recall@5 = 88%
MRR = 0.71
Latency = 25 ms

Model B:

Recall@5 = 95%
MRR = 0.84
Latency = 80 ms

Model C:

Recall@5 = 93%
MRR = 0.82
Latency = 40 ms

A production decision may choose Model C because it gives a better balance between quality and speed.

---

## Controlled Experiments

When comparing embedding models, keep other variables fixed.

Do not change at the same time:

- Chunking strategy
- top_k
- Reranker
- Prompt
- LLM

Change one variable
↓
Measure
↓
Compare

This helps identify what caused the improvement.

---

## Embedding Model Versioning

Store information such as:

- embedding_model
- model_version
- dimension
- similarity_metric
- normalization
- index_version

Example:

embedding_model = multilingual_v2
dimension = 768
similarity_metric = cosine
normalized = true
index_version = v2

---

## Changing Embedding Models

Do not mix vector spaces.

Bad setup:

Old document vectors from Model A
+
New query vector from Model B

Instead:

New embedding model
↓
Re-embed documents
↓
Build new index
↓
Switch to new version

---

## Query vs Document Embeddings

Document embeddings are created during ingestion.

Query embeddings are created at query time.

Both must belong to the same vector space.

---

## Production Embedding Strategy

A good production decision should consider:

Language Fit
+
Domain Fit
+
Privacy
+
Retrieval Quality
+
Latency
+
Cost
+
Deployment Constraints

---

## Main Lesson

Best Embedding Model

does not mean:

Largest model

or

Highest dimensions

It means:

Best retrieval performance
for your real data and queries
under your real project constraints