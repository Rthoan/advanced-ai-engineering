# Project Requirements

## Functional Requirements

### FR-1
Answer trusted policy questions using RAG.

### FR-2
Return current order status using a structured order service.

### FR-3
Create eligible return requests.

### FR-4
Abstain when trusted evidence is unavailable.

### FR-5
Prevent users from accessing resources they do not own.

## Non-Functional Requirements

### NFR-1
Target p95 latency below 3 seconds for standard interactive requests.

### NFR-2
Critical authorization violations must be zero.

### NFR-3
RAG answers must contain citations.

### NFR-4
Every request must be traceable.

### NFR-5
Writes must be auditable.

### NFR-6
No secrets may be stored in source code.

### NFR-7
LLM cost must be measurable per request.

## Return Eligibility Baseline

An order is eligible when:

- It is delivered
- It is within 30 days
- It has no existing active return

## Out of Scope

- Real payment processing
- Admin dashboard
- Real customer PII
- Complex multi-agent architecture
- Kubernetes