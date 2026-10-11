# Day 04 Notes

## Core Architecture Rule

Requirements
↓
Components
↓
Responsibilities
↓
Data Sources
↓
Flows
↓
Failure Paths
↓
Final Architecture

---

## Responsibility Map

FastAPI
→ HTTP layer

Authentication
→ User identity and permissions

Validation
→ Input validation

Agent
→ Path / tool selection

RAG Service
→ Knowledge retrieval

LLM Service
→ Language generation and analysis

Order Service
→ Order business logic

Return Service
→ Return business logic

Ticket Service
→ Ticket business logic

Email Service
→ Email sending

---

## Important Rule

Do not let every component access every database directly.

Prefer:

Agent
↓
Order Service
↓
Orders DB

Instead of:

Agent
↓
Orders DB

---

## Data Ownership

One data domain should have one clear owner.

Examples:

Orders → Order Service

Returns → Return Service

Tickets → Ticket Service

Documents → RAG Service

---

## Validation vs Business Logic

Invalid input format:

date = "abc"

→ Validation Error

Valid date but no available appointment:

date = "2026-10-20"

→ Business Logic

---

## Failure Handling

Success Path
+
Failure Path
+
Fallback
=
Better Architecture

---

## Partial Failure

If the main action succeeds and a secondary action fails:

Keep the main action successful.

Example:

Ticket created
+
Email failed

→ Ticket remains created
→ Retry email
→ Log error

---

## AI Rule

Do not route every request through the LLM.

Use normal services for:

- Database reads
- Permission checks
- API calls
- Fixed business rules

Use LLM only when language understanding or generation is needed.