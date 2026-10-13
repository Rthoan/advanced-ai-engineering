# Day 05 Notes

## Core Pipeline

Upload
→ Validate
→ Extract
→ Clean
→ Chunk
→ Metadata
→ Embed
→ Store

---

## Ingestion vs Query

Ingestion:
Prepare and store knowledge.

Query:
Use stored knowledge to answer.

---

## Structured Data Rule

Documents / unstructured knowledge
→ RAG

Structured live data
→ Service + Database / API

---

## Metadata

Useful metadata:

source
page
section
document_id
version
updated_at

---

## Update Rule

If checksum is unchanged:

Skip

If checksum changed:

Delete old chunks
→ Reprocess
→ Store new version

---

## Idempotency

Same input
→ Same final state

Do not duplicate data.

---

## Incremental Processing

Process only what changed.

This reduces:

- Cost
- Compute
- Time
- Embedding calls

---

## Failure Handling

If one document fails:

Do not stop the entire pipeline.

Instead:

Log
→ Mark FAILED
→ Continue
→ Retry later

---

## Status Tracking

PENDING
PROCESSING
COMPLETED
FAILED

---

## Good Data Pipeline

Correct Data
+
Traceable Data
+
Updatable Data
+
Recoverable Failures
+
Scalable Processing