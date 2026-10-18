# Day 07 Notes

## Core Rule

Chunk boundaries should follow meaning whenever possible.

---

## Chunk Size

Small chunks:
→ Better precision
→ Less context

Large chunks:
→ More context
→ More noise

---

## Overlap

Overlap preserves context across boundaries.

Too much overlap:

→ Duplication
→ More storage
→ More embeddings
→ Higher cost
→ Repeated retrieval results

---

## Strategies

Fixed-size
→ Simple

Sentence / Paragraph
→ Natural boundaries

Section-based
→ Structured documents

Semantic
→ Topic-based splitting

Parent-Child
→ Small retrieval chunks + large generation context

Hierarchical
→ Large structured documents

Clause-based
→ Contracts / legal documents

Q&A based
→ FAQ

---

## Parent-Child Rule

Retrieval chunk
does not have to equal
generation context.

Search small
→ Answer with larger context

---

## Metadata

Useful fields:

document_id
chunk_id
source
page
section
version

---

## Evaluation

Measure:

Retrieval Hit Rate
MRR
Context Relevance
Faithfulness
Latency
Cost
Number of Chunks

---

## Experiment Rule

Change one variable
↓
Measure
↓
Compare

Do not change multiple architecture variables at the same time.