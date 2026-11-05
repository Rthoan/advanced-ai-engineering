# Day 19 — RAG Evaluation

## Goal

Evaluate a RAG system across retrieval, context, answer quality, and production behavior.

## Retrieval Metrics

- Hit@K
- Recall@K
- Precision@K
- MRR
- NDCG

### Recall@K

Relevant retrieved / total relevant.

### MRR

Measures the rank of the first relevant result.

### NDCG

Evaluates ranking quality when relevance has multiple levels.

---

## Answer Metrics

- Groundedness
- Faithfulness
- Answer Relevance
- Completeness
- Correctness
- Citation Accuracy
- Citation Coverage

Groundedness asks whether claims are supported by retrieved context.

Correctness compares the final answer with ground truth.

Groundedness and correctness are not always the same.

---

## No-Answer Evaluation

The system should abstain when evidence is insufficient.

Monitor both:

- Hallucination
- Over-refusal

---

## Golden Dataset

A trusted evaluation dataset should include:

- Question
- Relevant documents
- Expected facts
- Expected behavior
- Language
- Difficulty
- Query type

Include:

- Easy
- Semantic
- Ambiguous
- Multi-hop
- Unsupported
- Hard-negative
- Multilingual
- Freshness cases

---

## Dev and Holdout

Use the Dev Set for tuning.

Use the Holdout Set for final evaluation.

Do not repeatedly optimize against the final test set.

---

## LLM-as-a-Judge

Useful for semantic evaluation such as:

- Groundedness
- Relevance
- Completeness

Use deterministic code checks whenever possible.

---

## Human Evaluation

Use human review for:

- Golden Set creation
- Critical cases
- Ambiguous cases
- Judge calibration

---

## Online Evaluation

Monitor:

- Quality
- Latency
- Cost
- Abstention
- Fallbacks
- Errors
- User feedback

---

## A/B Testing

Compare versions on real users.

## Shadow Evaluation

Run the new version on real production requests without showing its answers to users.

## Canary Release

Gradually increase traffic to a new version.

---

## Drift

Monitor:

- Query Drift
- Data Drift
- Policy Drift
- Model Behavior Drift

---

## Continuous Evaluation

Production Failure
↓
Human Review
↓
Regression Dataset
↓
Improve
↓
Re-evaluate
↓
Deploy

---

## Main Principle

A strong RAG evaluation system measures:

Retrieval Quality
+
Answer Quality
+
Safety
+
Latency
+
Cost