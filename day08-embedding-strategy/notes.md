# Day 08 Notes

## Core Rule

Best Embedding Model
=
Best fit for the project

Not:

Largest model
or
Most dimensions

---

## Selection Criteria

Check:

- Language support
- Cross-lingual retrieval
- Domain fit
- Privacy
- Local vs API
- Retrieval quality
- Latency
- Cost
- Memory
- License
- Deployment constraints

---

## Dimensions

More dimensions
≠
Better retrieval

Higher dimensions may increase:

- RAM usage
- Storage
- Index size
- Compute cost

---

## Similarity

Common metrics:

Cosine Similarity
Dot Product
Euclidean Distance

Use the metric recommended for the model.

---

## Threshold

There is no universal similarity threshold.

Tune it using real evaluation data.

---

## Multilingual

Test:

Arabic → Arabic

Arabic → English

English → Arabic

English → English

---

## Domain-Specific

General models:
→ general company docs
→ FAQ
→ e-commerce

Domain-specific:
→ legal
→ medical
→ financial
→ scientific

---

## Local vs API

Local:
→ Privacy
→ Control

API:
→ Simplicity
→ Managed scaling

---

## Benchmark Rule

Keep other variables fixed.

Same chunks
Same top_k
Same dataset
Same retrieval setup

Only change the embedding model.

---

## Core Metrics

Recall@K
Hit Rate
MRR
Latency
Cost
Memory
Index size
Cross-lingual performance

---

## Versioning

Store:

embedding_model
model_version
dimension
similarity_metric
normalization
index_version

---

## Model Change

New embedding model
→ Re-embed documents
→ Build new index

Do not mix vectors from different models.