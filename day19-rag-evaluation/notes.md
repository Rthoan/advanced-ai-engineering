# Day 19 Notes — RAG Evaluation

## Retrieval

Hit@K
Recall@K
Precision@K
MRR
NDCG

---

## Answer

Groundedness
Faithfulness
Relevance
Completeness
Correctness
Citation Accuracy

---

## Important

Groundedness != Correctness

A response can be grounded in stale context and still be factually outdated.

---

## Dataset

Golden Set

Dev Set

Holdout Set

Avoid evaluation overfitting.

---

## Evaluation Methods

Deterministic Checks
LLM-as-a-Judge
Human Review

---

## Production

A/B Testing
Shadow Evaluation
Canary
Thresholds
Drift Monitoring

---

## Final Rule

Do not evaluate only the final answer.

Evaluate the complete RAG pipeline.