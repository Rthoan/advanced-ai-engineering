# Day 15 Notes — API Architecture

## Layer Responsibilities

API Layer
→ HTTP concerns

Service Layer
→ Business Logic

Repository Layer
→ Data Access

AI Layer
→ LLM / RAG / Agent

Worker
→ Long-running tasks

---

## Request Flow

Client
↓
Rate Limit
↓
Authentication
↓
Validation
↓
Authorization
↓
Endpoint
↓
Service
↓
Repository / AI / External API
↓
Response

---

## Auth

Authentication:
Who are you?

Authorization:
What can you do?

401:
Not authenticated

403:
Authenticated but forbidden

---

## API Models

Database Model
≠ API Request Model
≠ API Response Model

---

## Errors

Use stable error codes.

Do not expose internal stack traces or infrastructure details.

---

## Idempotency

Same logical write request
+
Same idempotency key
→
Same final effect

---

## Async

async def:
Non-blocking I/O

Background Job:
Runs outside request lifecycle

---

## Long Tasks

Use:

Queue
+
Worker
+
Job Status

Typical response:

202 Accepted

---

## Streaming

Streaming:

Connection stays open
and partial output is returned.

Background Job:

Request ends
and work continues separately.

---

## Reliability

Use:

Timeouts
Safe Retries
Circuit Breakers
Idempotency
Health Checks

---

## Final Rule

Keep transport, business logic, AI logic,
and data access clearly separated.