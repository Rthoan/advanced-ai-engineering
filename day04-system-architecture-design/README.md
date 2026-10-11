# Day 04 — System Architecture Design

## Goal

Learn how to transform project requirements into a clear system architecture before writing code.

Main flow:

Requirements
↓
System Boundaries
↓
Components
↓
Responsibilities
↓
Data Sources
↓
Main Flows
↓
Failure Paths
↓
External Services
↓
Final Architecture

---

## System Architecture

System architecture describes:

- Who uses the system
- Which components exist
- What each component is responsible for
- How components communicate
- Where data comes from
- Which services are external
- What happens when something fails

---

## System Boundaries

Separate internal components from external systems.

### Internal

- FastAPI
- Authentication
- Validation
- Agent / Router
- RAG Service
- Ticket Service
- Email Service
- LLM Service

### External

- Cloud LLM Provider
- Email Provider
- External APIs

---

## Layers

A common architecture can be divided into:

Presentation Layer
↓
API Layer
↓
Application Layer
↓
AI Layer
↓
Data Layer

### API Layer

Responsible for:

- HTTP requests
- HTTP responses
- Routing
- Status codes

### Application Layer

Responsible for business logic.

Examples:

- Order Service
- Return Service
- Ticket Service

### AI Layer

Responsible for:

- RAG
- Agent
- LLM
- Embeddings

### Data Layer

Examples:

- PostgreSQL
- Vector Store
- Redis
- External APIs

---

## Separation of Responsibilities

Each component should have one clear main responsibility.

Examples:

FastAPI
→ HTTP request / response

Authentication
→ Identify user and permissions

Validation
→ Validate input structure

Agent
→ Choose the correct tool or path

RAG Service
→ Retrieve private knowledge

Order Service
→ Manage order data and logic

Return Service
→ Manage return logic

Ticket Service
→ Manage support tickets

LLM Service
→ Generate or analyze language

Email Service
→ Send email messages

---

## Data Ownership

Each data source should have a clear owner.

Orders DB
→ Order Service

Returns DB
→ Return Service

Ticket DB
→ Ticket Service

Vector Store
→ RAG Service

User Identity
→ Authentication Service

---

## Main Flow Example

Policy Question:

User
↓
FastAPI
↓
Authentication
↓
Validation
↓
Agent
↓
RAG Service
↓
Vector Store
↓
Relevant Context
↓
LLM Service
↓
Answer

---

## Structured Data Flow

Ticket Status:

User
↓
FastAPI
↓
Authentication
↓
Validation
↓
Agent
↓
Ticket Service
↓
Ticket Database
↓
Status
↓
Response

LLM is not required if the result can be returned directly.

---

## Action Flow

Create Ticket:

User
↓
FastAPI
↓
Authentication
↓
Validation
↓
Agent
↓
Ticket Service
↓
Ticket Database
↓
Email Service
↓
Email Provider
↓
Confirmation

---

## Failure Paths

A production architecture must include failure handling.

Examples:

Authentication Failure
→ 401 Unauthorized

Permission Failure
→ 403 Forbidden

Resource Not Found
→ 404 Not Found

Database Unavailable
→ 503 Service Unavailable

RAG Finds No Context
→ Do not hallucinate
→ Fallback / Human Support

LLM Timeout
→ Retry / Fallback

Email Failure After Core Action
→ Keep core action successful
→ Retry email
→ Log failure

---

## Partial Failure

Example:

Return Request Created ✅
Email Failed ❌

Do not mark the entire operation as failed.

Instead:

- Keep the return request
- Retry email
- Log the error
- Return success for the core action

---

## Avoid Overengineering

Do not use AI when normal software logic is enough.

Examples:

Get order status
→ Service + Database

Send confirmation email
→ Email Service

Simple fixed flow
→ Workflow

Use Agent only when a decision between tools is required.

Use LangGraph only when the workflow has:

- State
- Branches
- Retries
- Loops
- Human approval

---

## Architecture Review Checklist

Before implementation, check:

1. Does every requirement have a component?
2. Does every component have a clear responsibility?
3. Does every data source have an owner?
4. Is the happy path clear?
5. Are failure paths defined?
6. Are external services visible?
7. Is AI used only where needed?
8. Is the architecture unnecessarily complex?

---

## Main Lesson

Architecture is not just boxes.

Architecture =

Components
+
Responsibilities
+
Data Ownership
+
Flows
+
Failure Paths
+
External Services