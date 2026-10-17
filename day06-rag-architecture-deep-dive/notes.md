# Day 06 Notes

## Production RAG Flow

Question
→ Query Processing
→ Metadata Filtering
→ Hybrid Retrieval
→ Top-N
→ Reranking
→ Top-K
→ Context Builder
→ LLM
→ Answer
→ Citations

---

## Retrieval Rule

Retrieve broad
→ Rerank
→ Send narrow

---

## Metadata Example

country = Iraq
category = phones
document_type = return_policy

Metadata helps with:

- Filtering
- Citations
- Versioning
- Debugging

---

## Grounding Rule

Retrieved Context
= Source of Truth

Do not allow the LLM to invent missing policy information.

---

## Failure Types

Ingestion Failure
→ Data never entered correctly

Retrieval Failure
→ Correct chunk exists but was not retrieved

Reranking Failure
→ Correct chunk was retrieved but removed later

Context Failure
→ Final context is noisy or conflicting

Generation Failure
→ Correct context but wrong final answer

---

## Debugging Rule

Trace the evidence:

Source
→ Chunk
→ Retrieval
→ Reranking
→ Context
→ Answer

Do not change the LLM before identifying the actual failure point.

---

## Core Metrics

Retrieval Hit Rate
→ Did we retrieve the correct evidence?

Faithfulness
→ Is the answer supported by context?

Answer Relevance
→ Does the answer answer the question?

Citation Correctness
→ Does the cited source support the answer?

Latency
→ How fast is the system?

Cost
→ How expensive is each query?