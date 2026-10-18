# Day 07 — Chunking Strategies

## Goal

Learn how to split documents into meaningful chunks that improve retrieval quality in RAG systems.

Main idea:

Document
↓
Chunking Strategy
↓
Chunks
↓
Embeddings
↓
Retrieval
↓
Context
↓
Answer

---

## Why Chunking Matters

Chunking affects:

- Retrieval precision
- Context quality
- Embedding quality
- Latency
- Cost
- Faithfulness

Bad chunks can produce bad retrieval even when the LLM and embedding model are strong.

---

## Chunk Size

Small chunks:

- More precise retrieval
- Less context
- More chunks
- More storage

Large chunks:

- More context
- More noise
- More tokens
- Potentially lower retrieval precision

There is no universal best chunk size.

---

## Overlap

Overlap preserves context across chunk boundaries.

Example:

chunk_size = 500
overlap = 75

Too little overlap may lose context.

Too much overlap causes:

- Duplicate chunks
- More embeddings
- More storage
- Repeated retrieval results
- Higher cost

---

## Fixed-Size Chunking

Example:

500 tokens per chunk

Advantages:

- Simple
- Fast
- Easy to implement

Disadvantage:

May split sentences or ideas at bad boundaries.

---

## Sentence and Paragraph Chunking

Split according to natural language boundaries.

Useful when:

- Paragraphs are meaningful
- Document structure is simple
- Preserving meaning matters

---

## Section-Based Chunking

Useful for structured documents.

Example:

Shipping
Returns
Warranty
Payments

Each section becomes its own logical area.

If a section is too large:

Section
↓
Internal chunking
↓
Small overlap

---

## Semantic Chunking

Semantic chunking splits when the topic or meaning changes.

Useful for:

- Long reports
- Research papers
- Transcripts
- Documents without clear headings

Advantages:

- Better semantic coherence

Disadvantages:

- More complex
- More expensive to process

---

## Parent-Child Chunking

Use small chunks for retrieval and larger chunks for generation.

Example:

Parent = 800 tokens

Children:
- 200 tokens
- 200 tokens
- 200 tokens
- 200 tokens

Flow:

Question
↓
Search Child Chunks
↓
Find Relevant Child
↓
Return Parent Context
↓
LLM

Main idea:

Search small
↓
Read large

---

## Hierarchical Chunking

Preserve document hierarchy:

Document
↓
Chapter
↓
Section
↓
Subsection
↓
Paragraph

Useful for large and complex documents.

---

## Clause-Based Chunking

Useful for:

- Contracts
- Legal documents
- Regulations

Each clause is treated as a logical unit.

Context expansion can include:

Previous Clause
+
Current Clause
+
Next Clause

---

## Q&A Chunking

Useful for FAQ datasets.

Example:

Question
+
Answer
=
One Chunk

---

## Metadata

Each chunk should contain metadata such as:

- document_id
- chunk_id
- source
- page
- section
- version

Metadata helps with:

- Filtering
- Citations
- Debugging
- Versioning
- Retrieval analysis

---

## Context Expansion

After retrieving a chunk, we may also retrieve neighboring chunks.

Example:

Retrieved Chunk 12

Context:

Chunk 11
Chunk 12
Chunk 13

This adds useful context without retrieving the full document.

---

## Choosing a Strategy

Structured document:
→ Section-based

Large structured sections:
→ Section-based + internal chunking

Unstructured long text:
→ Semantic chunking

Precise retrieval + larger context:
→ Parent-Child

Contracts:
→ Clause-based

FAQ:
→ Q&A based

---

## Evaluation

Do not choose chunking settings by intuition alone.

Compare configurations.

Example:

Config A:
chunk_size = 300
overlap = 50

Config B:
chunk_size = 500
overlap = 75

Config C:
Parent-Child

Evaluate using:

- Retrieval Hit Rate
- MRR
- Context Relevance
- Faithfulness
- Latency
- Cost
- Number of chunks

---

## Controlled Experiments

Change one variable at a time.

Do not change:

- Chunking
- Embeddings
- Retrieval
- Prompt
- LLM

all at once.

Instead:

Change chunking
↓
Measure
↓
Compare

This helps identify what caused the improvement.

---

## Main Lesson

Best Chunking Strategy

does not mean:

one fixed chunk size for every project.

It means:

Strategy suited to the document
+
Appropriate chunk size
+
Appropriate overlap
+
Useful metadata
+
Evaluation on real questions