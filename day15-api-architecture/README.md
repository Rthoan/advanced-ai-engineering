# Day 15 — API Architecture

## Goal

Design a production-ready API architecture for AI systems.

Topics:

- FastAPI Layer
- Request / Response Contracts
- API Versioning
- Authentication
- Authorization
- Validation
- Service Layer
- Repository Layer
- Error Mapping
- Idempotency
- Rate Limiting
- Async Boundaries
- Background Jobs
- Streaming
- Observability

---

## Core Architecture

Client
↓
HTTPS
↓
Rate Limit
↓
Authentication
↓
Validation
↓
Authorization
↓
FastAPI Endpoint
↓
Service Layer
↓
AI / Domain Logic
↓
Repository / External Services
↓
Database / Vector DB

---

## Thin API Layer

The API Layer should mainly handle:

- HTTP requests
- Request validation
- Authentication
- Authorization
- HTTP status codes
- Response serialization

Avoid placing business logic directly inside endpoints.

Rule:

Keep endpoints thin.
Keep business logic in services.

---

## Service Layer

The Service Layer contains application and business logic.

Examples:

ReturnService
OrderService
AssistantService

Responsibilities may include:

- Business validation
- Orchestration
- Calling repositories
- Calling tools
- Calling AI components
- Calling external services

---

## Repository Layer

Repositories handle data access.

Examples:

OrderRepository
ReturnRepository

Responsibilities:

- Database queries
- Persistence
- Data retrieval

Rule:

Repository
→ Data Access

Service
→ Business Logic

---

## Request Models

Request models define the public input contract.

Example:

CreateReturnRequest

Fields:

order_id
quantity
reason_code

Strong schemas improve:

- Validation
- Documentation
- Testing
- Safety

---

## Response Models

Response models define exactly what the API returns.

Do not expose the database model directly.

Rule:

Database Model
≠ API Response Model

---

## Error Contracts

Prefer stable structured errors.

Example:

status: error

error:
  code: ORDER_NOT_FOUND
  message: Order was not found.

Clients should branch on stable error codes,
not free-form messages.

---

## Domain Errors vs HTTP Errors

Domain:

OrderNotFound
ReturnNotEligible
AlreadyReturned

API Mapping:

OrderNotFound
→ 404

NotAuthenticated
→ 401

NotAuthorized
→ 403

ValidationError
→ 422

AlreadyReturned
→ 409

RateLimited
→ 429

DependencyUnavailable
→ 503

Rule:

Domain logic should not depend directly on HTTP.

---

## API Versioning

Example:

/v1/orders
/v1/returns
/v1/chat

Use a new version when making breaking changes.

Example:

/v2/returns

Breaking changes may include:

- Removing fields
- Changing field types
- Changing incompatible behavior

---

## Authentication

Authentication answers:

Who are you?

Examples:

JWT
API Key
Session
OAuth

---

## Authorization

Authorization answers:

What are you allowed to do?

Examples:

orders.read
returns.write
refunds.create

Authorization should be deterministic.

Never allow the LLM to decide permissions.

---

## 401 vs 403

401
→ identity was not established

403
→ identity is known but access is denied

---

## Resource Authorization

Permission checks should include resource ownership where needed.

Example:

Authenticated user:

USR-10

Order owner:

USR-20

Result:

Access denied.

---

## Least Privilege

Services and users should receive only the permissions they require.

Example:

order-reader-service

Allowed:

orders.read

Not required:

orders.delete
refunds.create
admin.*

---

## Idempotency

Write APIs may need idempotency protection.

Example:

POST /v1/returns

Header:

Idempotency-Key: abc-123

Same logical request
+
Same idempotency key
→
Same final effect

Do not create duplicate resources after retries.

---

## Idempotency Payload Safety

If the same idempotency key is used with a different request payload:

Reject the request.

Example:

Same Key
+
Different Payload
→ Conflict

---

## Rate Limiting

Rate limits protect the system from:

- Abuse
- Cost spikes
- Overload
- Excessive AI usage

Possible dimensions:

- IP
- User ID
- API Key
- Tenant
- Endpoint

Typical response:

429 Too Many Requests

---

## AI-Aware Rate Limiting

AI systems may also monitor:

- Token usage
- Tool calls
- Model calls
- Compute cost
- Expensive endpoints

Request count alone may not represent real cost.

---

## Request IDs

Use a request identifier for tracing.

Example:

request_id = REQ-123

Propagate it through:

API
↓
Service
↓
Agent
↓
Tools
↓
External Services

---

## Correlation IDs

Useful across multiple services.

Example:

API Gateway
↓
AI Service
↓
Order Service
↓
Payment Service

All logs can be linked through one correlation ID.

---

## Structured Logging

Useful fields:

request_id
user_id
endpoint
status_code
latency
error_code

Never log unnecessary secrets.

---

## Timeouts

Dependencies should have explicit timeouts.

Examples:

LLM
Database
Vector Store
External API

Rule:

No Timeout
→ Resource Exhaustion Risk

---

## Retry Policy

Retry only when appropriate.

Read timeout:
→ may be retryable

Write timeout:
→ verify outcome or retry with idempotency protection

Never retry write operations blindly.

---

## Circuit Breaker

If a dependency repeatedly fails:

Failures exceed threshold
↓
Open Circuit
↓
Temporarily stop calls

This helps prevent cascading failures.

---

## Async Boundaries

Not every operation should complete inside one HTTP request.

Long-running operations may use:

API
↓
Job Queue
↓
Worker
↓
Heavy Processing

---

## 202 Accepted

Use when the request was accepted but processing continues asynchronously.

Example:

POST /v1/documents
→ 202 Accepted

Response:

job_id
status = queued

---

## Background Jobs

Good use cases:

- Document ingestion
- Embedding generation
- Batch evaluation
- Report generation
- Long-running AI workflows
- Notifications

---

## Job States

Typical states:

QUEUED
PROCESSING
COMPLETED
FAILED
CANCELLED
RETRYING

---

## async def vs Background Job

async def
→ non-blocking I/O

Background Job
→ work continues outside the HTTP request lifecycle

These are not the same thing.

---

## I/O-bound vs CPU-bound

I/O-bound examples:

- HTTP calls
- Database calls
- LLM API calls
- Vector DB calls

CPU-bound examples:

- Heavy document processing
- Local inference
- Image processing

CPU-heavy jobs may require separate workers.

---

## Streaming

Streaming keeps the connection open and sends partial output.

Useful for:

AI chat responses

Streaming improves perceived latency.

Streaming
≠ Background Processing

---

## Long-Running Agents

Long-running Agent workflows should usually not keep HTTP connections open for hours.

Example:

POST /v1/agent-runs
↓
202 Accepted
↓
run_id
↓
Worker / LangGraph
↓
Checkpoint
↓
Resume

---

## Health Endpoints

Examples:

/health
/liveness
/readiness

Liveness:
Is the process alive?

Readiness:
Can the service safely serve traffic?

---

## Production Folder Example

app/
├── api/
│   ├── routes/
│   ├── schemas/
│   └── dependencies/
├── services/
├── repositories/
├── agents/
├── rag/
├── workers/
├── models/
└── main.py

---

## Production Checklist

Before shipping an API:

- Versioned endpoints
- Strong schemas
- Authentication
- Authorization
- Rate limiting
- Idempotency
- Timeouts
- Safe retries
- Error mapping
- Request IDs
- Structured logging
- Async jobs where needed
- Health checks
- No secrets in code
- Tests

---

## Main Principles

Keep endpoints thin.

Domain logic should not depend on HTTP.

Never retry write operations blindly.

Long-running work should not block HTTP requests.

Production APIs need explicit contracts and boundaries.