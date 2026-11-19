# Day 26 — Project Skeleton + FastAPI + Core Contracts

## Overview

Day 26 marks the beginning of the implementation phase of the final project:

**Production AI Customer Support Assistant**

The goal of this day was to create the initial project skeleton, start the FastAPI application, define the first production-oriented API contracts, add request tracing through request IDs, implement structured error handling, and build the first deterministic routing layer.

This day establishes the foundation that the RAG pipeline, order tools, return workflow, security controls, observability, and evaluation system will build on in the next stages.

---

## Goals

The main goals for Day 26 were:

- Create a clean project structure
- Initialize the FastAPI application
- Add a health endpoint
- Define Pydantic request and response contracts
- Create structured application errors
- Add a unique request ID to every request
- Implement a deterministic request router
- Validate incoming user messages
- Add initial unit tests
- Verify that the API works locally

---

## Project Structure

The project currently follows this structure:

```text
final-project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── errors.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── router.py
│   │
│   ├── rag/
│   │   └── __init__.py
│   │
│   ├── tools/
│   │   └── __init__.py
│   │
│   ├── security/
│   │   └── __init__.py
│   │
│   └── observability/
│       └── __init__.py
│
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   └── test_router.py
│   └── integration/
│
├── docs/
│   ├── day25/
│   └── day26/
│       └── README.md
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Architecture Principle

The API layer should remain thin.

The main architectural rule used today is:

```text
API Layer
→ HTTP concerns

Service Layer
→ Application and business logic
```

The FastAPI endpoints should not become responsible for all routing, business rules, retrieval, authorization, and external integrations.

Instead, these responsibilities will gradually move into dedicated modules.

---

## FastAPI Application

The application is initialized in:

```text
app/main.py
```

Current application configuration:

```python
app = FastAPI(
    title="Production AI Customer Support Assistant",
    version="0.1.0",
)
```

The application currently includes:

- API routes
- Request ID middleware
- Structured application error handling
- Health endpoint

---

## Health Endpoint

The first endpoint implemented was:

```http
GET /health
```

Example response:

```json
{
  "status": "ok",
  "service": "production-ai-customer-support"
}
```

This endpoint provides a basic service health check.

Later, the project can separate health checks into:

```text
/health/live
/health/ready
```

for production deployment.

---

## API Documentation

FastAPI automatically provides interactive API documentation.

After starting the application, Swagger UI is available at:

```text
http://127.0.0.1:8000/docs
```

The OpenAPI schema is also generated automatically.

---

## Running the Application

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Start the development server:

```bash
uvicorn app.main:app --reload
```

The application runs locally at:

```text
http://127.0.0.1:8000
```

Test the health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "production-ai-customer-support"
}
```

---

## Python Virtual Environment

The project uses a dedicated Python virtual environment instead of installing packages globally.

The environment was created using:

```bash
python3 -m venv .venv
```

Activated with:

```bash
source .venv/bin/activate
```

Dependencies are installed using:

```bash
python -m pip install -r requirements.txt
```

This avoids modifying the system Python environment.

---

## Current Dependencies

The initial `requirements.txt` contains:

```text
fastapi
uvicorn[standard]
pydantic
pydantic-settings
httpx
pytest
```

These dependencies provide:

- FastAPI for the API layer
- Uvicorn as the ASGI server
- Pydantic for validation and schemas
- Pydantic Settings for future configuration management
- HTTPX for HTTP testing and integrations
- Pytest for automated testing

---

## Core API Contracts

The project defines API contracts using Pydantic models inside:

```text
app/models/schemas.py
```

Current models include:

```text
ErrorDetails
ErrorResponse
HealthResponse
ChatRequest
Citation
ChatResponse
ToolResult
```

Using explicit schemas provides:

- Input validation
- Predictable API responses
- Automatic OpenAPI documentation
- Easier testing
- Stable contracts between components

---

## Chat Request

The current chat request contract is:

```json
{
  "message": "Where is order ORD-100?"
}
```

Represented by:

```python
class ChatRequest(BaseModel):
    message: str
```

---

## Chat Response

The current chat response includes:

```json
{
  "request_id": "8307e5f9-8e56-4dd5-89c2-3c4014ce5e23",
  "answer": "Route detected successfully.",
  "route": "order_lookup",
  "citations": []
}
```

The response provides:

- Request ID
- Temporary response message
- Selected route
- Citation list

The temporary answer will later be replaced by real RAG, tool, and workflow responses.

---

## Request ID Middleware

Every HTTP request receives a unique request ID.

The request ID can either:

- Be provided by the client through `X-Request-ID`
- Be generated automatically by the API

Example:

```text
X-Request-ID: 8307e5f9-8e56-4dd5-89c2-3c4014ce5e23
```

The ID is stored inside:

```python
request.state.request_id
```

and returned in the response headers.

This provides a foundation for future:

- Logging
- Distributed tracing
- Error investigation
- Request correlation
- User support debugging

---

## Structured Error Handling

Application errors use a custom `AppError` class.

Example:

```python
raise AppError(
    code="INVALID_REQUEST",
    message="Message must contain at least 3 characters.",
    status_code=422,
    retryable=False,
)
```

The API converts the error into a structured response.

Example:

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Message must contain at least 3 characters.",
    "retryable": false,
    "request_id": "..."
  }
}
```

This is preferred over generic errors such as:

```text
Something went wrong.
```

because structured errors are easier for clients, logs, tests, and monitoring systems to process.

---

## Error Contract

The current error response contains:

```text
code
message
retryable
request_id
```

The `retryable` field will become important later when the system handles:

- LLM provider failures
- Database failures
- Rate limits
- Network timeouts
- Temporary dependency failures

---

## Input Validation

The `/v1/chat` endpoint currently rejects messages shorter than three characters.

Example invalid request:

```json
{
  "message": "a"
}
```

Example error:

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Message must contain at least 3 characters.",
    "retryable": false,
    "request_id": "..."
  }
}
```

This is the first validation rule in the project.

Additional validation will be added as the project grows.

---

## Deterministic Router

The first routing system is implemented in:

```text
app/services/router.py
```

The router currently supports four routes:

```text
rag
order_lookup
create_return
fallback
```

The design intentionally starts with deterministic routing instead of an LLM router.

---

## Why Deterministic Routing First?

A deterministic router is currently preferred because it is:

```text
Faster
Cheaper
Predictable
Testable
Observable
```

An LLM router will only be introduced later if real ambiguity requires it.

The general principle is:

```text
LLM for ambiguity.

Code for certainty.
```

---

## Current Routing Logic

### RAG Route

Questions containing concepts such as:

```text
policy
shipping
faq
refund
```

are routed to:

```text
rag
```

Example:

```text
What is your return policy?
```

Result:

```json
{
  "route": "rag"
}
```

---

## Order Lookup Route

Messages containing an order ID and order tracking intent are routed to:

```text
order_lookup
```

Example:

```text
Where is order ORD-100?
```

Result:

```json
{
  "route": "order_lookup"
}
```

---

## Create Return Route

Messages requesting a return for a specific order are routed to:

```text
create_return
```

Example:

```text
I want to return ORD-100
```

Result:

```json
{
  "route": "create_return"
}
```

---

## Fallback Route

Requests that do not match the supported capabilities are routed to:

```text
fallback
```

Example:

```text
Tell me a joke.
```

Result:

```json
{
  "route": "fallback"
}
```

---

## Current Request Flow

The project currently follows this request flow:

```text
Client
↓
FastAPI
↓
Request ID Middleware
↓
Pydantic Validation
↓
Chat Endpoint
↓
Deterministic Router
├── rag
├── order_lookup
├── create_return
└── fallback
↓
Structured ChatResponse
```

The real implementations behind these routes will be added in the following days.

---

## Testing

The project currently contains unit tests for the deterministic router.

Test file:

```text
tests/unit/test_router.py
```

The tests verify:

- Order lookup routing
- Return routing
- RAG routing
- Fallback routing

Current tests:

```python
def test_order_lookup_route():
    route = detect_route("Where is order ORD-100?")
    assert route == Route.ORDER_LOOKUP
```

```python
def test_create_return_route():
    route = detect_route("I want to return ORD-100")
    assert route == Route.CREATE_RETURN
```

```python
def test_rag_route():
    route = detect_route("What is your return policy?")
    assert route == Route.RAG
```

```python
def test_fallback_route():
    route = detect_route("Tell me a joke")
    assert route == Route.FALLBACK
```

---

## Running Tests

Run the current test suite with:

```bash
PYTHONPATH=. python -m pytest -q
```

Current result:

```text
4 passed
```

---

## Why `PYTHONPATH=.` Is Currently Used

The project currently uses:

```bash
PYTHONPATH=. python -m pytest -q
```

so Python recognizes the project root and can import:

```python
from app.services.router import Route, detect_route
```

A cleaner project configuration can be added later so the environment does not require setting `PYTHONPATH` manually.

---

## Current Completed Features

At the end of Day 26, the following components are working:

```text
FastAPI Application ✅
Health Endpoint ✅
Virtual Environment ✅
Pydantic Contracts ✅
Request ID Middleware ✅
Structured Errors ✅
Input Validation ✅
Deterministic Router ✅
RAG Route Detection ✅
Order Route Detection ✅
Return Route Detection ✅
Fallback Route Detection ✅
Unit Tests ✅
```

---

## What Is Not Implemented Yet?

The current routing layer only identifies where a request should go.

The following components are intentionally not implemented yet:

```text
Actual RAG retrieval
Embeddings
Vector search
Reranking
LLM generation
Order database
Order authorization
Return workflow
Idempotency
Caching
Production logging
Tracing
Metrics
Evaluation pipeline
Docker
```

These will be added progressively from Day 27 onward.

---

## Next Step

Day 27 will implement the first real AI capability:

# RAG Pipeline

The planned pipeline is:

```text
Policy Documents
↓
Chunking
↓
Indexing
↓
User Question
↓
Retrieval
↓
Top-K Context
↓
Citation Builder
↓
Answer
```

The first goal will be to make the current:

```text
route = rag
```

actually retrieve trusted policy information instead of returning the temporary message:

```text
Route detected successfully.
```

---

## Key Engineering Lessons

### 1. Start with clear contracts

Define request, response, and error structures before adding complex AI behavior.

### 2. Keep endpoints thin

FastAPI endpoints should coordinate HTTP concerns and delegate application logic.

### 3. Do not use an LLM unnecessarily

Deterministic routing is currently sufficient for the known project routes.

### 4. Make errors observable

Structured errors and request IDs make production debugging easier.

### 5. Test deterministic components early

The router is simple, but testing it now prevents regressions as the project grows.

---

## Final Architecture Principle

```text
API receives the request.

Schemas validate it.

Router determines the path.

Services perform the work.

Trusted code enforces rules.

AI is added only where intelligence is required.
```

---

## Day 26 Status

**Day 26 — Project Skeleton + FastAPI + Core Contracts: COMPLETE ✅**

Current test result:

```text
4 passed
```

Next:

**Day 27 — RAG Pipeline**