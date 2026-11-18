# Day 25 — Full Project Definition

## Project

Production AI Customer Support Assistant

## Goal

Build a production-oriented AI support system that combines:

- RAG
- Tools
- Deterministic Workflows
- Security
- Evaluation
- Observability
- Cost and Latency Controls

## Core Capabilities

The system can:

- Answer policy questions
- Answer shipping questions
- Look up order status
- Create return requests
- Refuse unsupported answers
- Prevent cross-user access

## Architecture Principle

Use the LLM where intelligence is required.

Use deterministic systems where correctness is required.

## Routing

Supported routes:

- rag
- order_lookup
- create_return
- fallback

Start with deterministic routing.

## Data Ownership

Orders:
Transactional Database

Returns:
Transactional Database

Policies:
Document Source

Semantic Search:
Vector Index

## Security

The LLM never enforces authorization.

Trusted application and service code enforce:

- Authentication
- Authorization
- Object-Level Authorization
- Business Rules
- Idempotency

## Definition of Done

By Day 30:

- API works
- RAG works
- Order lookup works
- Return workflow works
- Cross-user access is blocked
- Errors are structured
- Tests pass
- Observability exists
- Evaluation exists
- Docker works
- Documentation is complete
- No secrets are committed