# Day 05 — Data Pipeline Design

## Goal

Learn how to design a reliable and scalable data pipeline for AI systems.

Main flow:

Data Source
↓
Ingestion
↓
Validation
↓
Cleaning
↓
Transformation
↓
Chunking
↓
Metadata
↓
Embeddings
↓
Storage / Indexing
↓
Updates
↓
Monitoring

---

## Data Sources

Common data sources:

- PDF
- DOCX
- TXT
- CSV
- Database
- API
- Web pages
- User uploads

Each source may require a different pipeline.

---

## RAG Ingestion Pipeline

A typical RAG ingestion pipeline:

File Upload
↓
Validation
↓
Text Extraction
↓
Cleaning
↓
Chunking
↓
Attach Metadata
↓
Embeddings
↓
Vector Store

---

## Query Pipeline

The query pipeline is different:

User Question
↓
Validation
↓
Question Embedding
↓
Vector Search
↓
Relevant Chunks
↓
Prompt Construction
↓
LLM
↓
Answer

---

## Ingestion vs Query

Ingestion
= Prepare knowledge

Query
= Use knowledge

Important rule:

Documents are embedded during ingestion.

Questions are embedded during query time.

---

## Data Validation

Validation checks if the data is usable.

Examples:

- Required columns exist
- IDs are present
- Values have correct types
- Files are readable
- Data is not corrupted

Example:

student_id missing
→ Validation Error

---

## Cleaning

Cleaning removes unnecessary or corrupted content.

Examples:

- Extra spaces
- Duplicate text
- HTML tags
- Broken characters
- Repeated headers and footers

---

## Transformation

Transformation converts data into a useful format.

Example:

Database row

→

Structured object

or

Normalized text

---

## Metadata

Do not store text without context.

Useful metadata:

- source
- page
- section
- document_id
- version
- created_at
- updated_at

Metadata helps with:

- Citations
- Filtering
- Debugging
- Versioning
- Updates

---

## Structured Data vs RAG

Do not convert all structured data into embeddings.

Example:

Return Policy PDF
→ RAG

Order Status
→ Order Service + Database Query

Exam Schedule Database
→ Exam Schedule Service + Structured Query

Student CSV
→ Validate + Clean + Transform + Database

---

## Updates

When a document changes:

Updated Document
↓
Detect Change
↓
Find Old Version
↓
Delete Old Chunks
↓
Reprocess
↓
Create New Embeddings
↓
Update Vector Store

This prevents old and new versions from existing together.

---

## Idempotency

Running the same pipeline multiple times should not create duplicate data.

Useful identifiers:

- document_id
- checksum
- version

Example:

Same checksum
→ Skip

New checksum
→ Reprocess

---

## Incremental Processing

If only a few documents change, process only those documents.

Example:

5000 documents
20 changed

Do not reprocess all 5000.

Use:

Incremental Processing

Benefits:

- Lower cost
- Faster processing
- Less compute
- Fewer embedding calls

---

## Batch vs Real-Time

### Batch

Process data at scheduled times.

Example:

Nightly document sync

### Real-Time

Process immediately after upload.

Example:

User uploads a new policy PDF
→ Process now

---

## Failure Handling

One failed document should not stop the entire pipeline.

Example:

Document Failed
↓
Log Error
↓
Mark FAILED
↓
Continue Other Documents
↓
Retry Later

---

## Pipeline Status

Useful statuses:

- PENDING
- PROCESSING
- COMPLETED
- FAILED

Example:

document_001 → COMPLETED
document_002 → FAILED
document_003 → PROCESSING

---

## Retry Strategy

Use limited retries.

Example:

Retry 1
↓
Retry 2
↓
Retry 3
↓
Mark FAILED

Avoid infinite retries.

---

## Scalable Pipeline

A larger system may use:

Upload
↓
Create Job
↓
Queue
↓
Worker
↓
Process
↓
Vector Store

This is useful for long-running document processing.

---

## Observability

Track metrics such as:

- documents_processed
- documents_failed
- processing_time
- chunks_created
- embedding_calls

---

## Main Lesson

A good data pipeline should be:

Correct
+
Traceable
+
Updatable
+
Idempotent
+
Recoverable
+
Scalable