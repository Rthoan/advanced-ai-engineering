# Day 06 — RAG Architecture Deep Dive

## Goal

Understand how a production RAG system works beyond basic vector search.

Production RAG includes:

Documents
↓
Ingestion
↓
Retrieval
↓
Filtering
↓
Reranking
↓
Context Building
↓
Grounded Generation
↓
Citations
↓
Evaluation

---

## What is RAG?

RAG stands for:

Retrieval
+
Augmented
+
Generation

Instead of relying only on the LLM's internal knowledge, the system retrieves relevant external knowledge before generating an answer.

Question
↓
Retrieve Evidence
↓
Build Context
↓
LLM
↓
Grounded Answer

---

## Naive RAG

A simple RAG architecture:

Documents
↓
Chunking
↓
Embeddings
↓
Vector Store

Query:

Question
↓
Question Embedding
↓
Vector Search
↓
Top-K Chunks
↓
LLM
↓
Answer

This is useful for simple systems but may not be enough for production.

---

## Production RAG

A stronger architecture:

User Question
↓
Query Processing
↓
Query Rewriting
↓
Metadata Filtering
↓
Hybrid Retrieval
↓
Top-N Candidates
↓
Reranker
↓
Top-K Chunks
↓
Context Builder
↓
Grounded Prompt
↓
LLM
↓
Answer + Citations

---

## Query Rewriting

A user query may be vague.

Example:

"وشروطها؟"

After rewriting:

"ما شروط إرجاع اللابتوب؟"

This gives the retriever a clearer query.

---

## Query Expansion

The system may add related terms.

Example:

return
refund
exchange

This can improve retrieval coverage.

---

## Metadata Filtering

Metadata can reduce the search space.

Example:

country = Iraq
category = phones
document_type = return_policy

Then vector search is performed only inside the relevant subset.

---

## Hybrid Retrieval

Semantic search is not always enough.

Production systems may combine:

Semantic Search
+
Keyword Search

This is useful for exact IDs, names, product codes, and specialized terminology.

---

## Top-N and Top-K

The retriever may first return many candidates:

Top-N = 20

Then the reranker selects the best:

Top-K = 5

Flow:

Retriever
↓
Top-N Candidates
↓
Reranker
↓
Top-K Final Chunks

---

## Reranking

The reranker evaluates the relationship between:

Question
+
Chunk

It can improve the ordering of retrieved evidence.

---

## Context Building

Retrieved chunks should not be passed randomly to the LLM.

Good context should be:

- Relevant
- Ordered
- Deduplicated
- Traceable
- Small enough for the context window

Example:

Source: phones_policy.pdf
Page: 2
Section: Opened Products

Text:
Opened phones cannot be returned.

---

## Grounding

The LLM should answer using the retrieved context.

Example instruction:

Answer only from the provided context.

If the answer is not supported by the context, say that the information is unavailable.

Retrieved context should be treated as the source of truth.

---

## Citations

A RAG answer should include its evidence when appropriate.

Example:

Opened phones cannot be returned.

Source:
phones_policy.pdf
Page 2
Section: Opened Products

Metadata enables accurate citations.

---

## No-Answer Strategy

If retrieval confidence is too low:

Low Confidence
↓
No Reliable Context
↓
Do Not Hallucinate
↓
Fallback / Human Support

A safe no-answer is better than an invented answer.

---

## RAG Failure Types

### Ingestion Failure

The document was not processed correctly.

Examples:

- Parsing failed
- Empty extracted text
- Document not indexed

### Chunking Failure

The information was split in a way that destroyed meaning.

### Embedding Failure

The embedding representation does not capture the query/document relationship well.

### Retrieval Failure

The correct information exists but is not retrieved.

### Reranking Failure

The correct chunk is retrieved but removed from the final ranked results.

### Context Failure

The correct evidence exists but the final context contains noise, duplicates, or conflicting versions.

### Prompt Failure

The context is correct but instructions are weak or unclear.

### Generation Failure

The context and prompt are correct, but the LLM produces an unsupported answer.

---

## RAG Debugging

When an answer is wrong, trace the evidence:

Document
↓
Chunk
↓
Index
↓
Retrieval
↓
Reranking
↓
Context
↓
Prompt
↓
Answer

Ask:

1. Does the source contain the correct information?
2. Was it indexed?
3. Is the chunk correct?
4. Was it retrieved?
5. What rank did it receive?
6. Did the reranker keep it?
7. Did it enter the final context?
8. Was the prompt correct?
9. Did the LLM follow the evidence?

---

## Evaluation Metrics

### Retrieval Hit Rate

Did the system retrieve the correct source?

### Faithfulness

Is the generated answer supported by the retrieved context?

### Answer Relevance

Does the answer directly address the user's question?

### Citation Correctness

Does the cited source actually support the claim?

### Latency

How long does the complete request take?

### Cost

How much does each query cost?

---

## Production RAG Quality

RAG Quality depends on:

Data Quality
+
Chunking
+
Embeddings
+
Retrieval
+
Reranking
+
Context
+
Prompt
+
LLM
+
Evaluation

The LLM is only one component of the system.

---

## Main Lesson

Bad retrieval
→ Bad answer

Good retrieval
+
Good context
+
Grounded generation
→ Better RAG