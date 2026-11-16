# Day 24 — Production Architecture

## Goal

Design a production-ready AI system with clear responsibilities, security boundaries, failure recovery, observability, scalability, and safe deployment.

## Core Principle

Production architecture is not only about components.

It also requires:

- Responsibilities
- Trust Boundaries
- Failure Boundaries
- Scaling Boundaries
- Data Ownership
- Recovery Paths

## High-Level Architecture

Client
→ Gateway / Load Balancer
→ API
→ Authentication
→ Authorization
→ Application Layer
→ Agent / Workflow
→ RAG / Tools / Memory / LLM Gateway
→ Response

Background workloads:

API
→ Queue
→ Workers
→ Result Store

## API Layer

Keep the API thin.

Responsibilities:

- Request validation
- Authentication
- Request context
- Routing to application services
- Response formatting

## Agent and Workflow

Use deterministic workflows when the path is known.

Use agents only when decisions are genuinely dynamic.

The agent is not the entire system.

## RAG Service

Responsibilities:

- Query Processing
- ACL Filtering
- Retrieval
- Reranking
- Context Building
- Citations

Authorization must happen before retrieval.

## LLM Gateway

Centralize:

- Model Routing
- Timeouts
- Retries
- Fallback
- Rate Limits
- Cost Tracking
- Prompt Versioning
- Logging

## Tool Services

Use:

Agent
→ Tool
→ Service
→ Authorization
→ Business Rules
→ Database

Avoid direct agent access to transactional databases.

## Data Layer

Use appropriate storage:

- SQL DB for transactional truth
- Vector DB for semantic retrieval
- Cache for temporary reusable data
- Object Storage for files
- Queue for async jobs
- Memory Store for scoped AI memory

## Async Architecture

Use queues and workers for long-running workloads.

Return job IDs instead of holding HTTP requests open for long jobs.

## Stateless Services

Keep API and workers stateless when possible.

Externalize important state.

## Health Checks

Use:

- Liveness
- Readiness

Do not treat all optional dependency failures as total service failure.

## Reliability

Use:

- Timeouts
- Deadlines
- Bounded Retries
- Exponential Backoff
- Jitter
- Circuit Breakers
- Bulkheads
- Backpressure
- Graceful Degradation

## Required vs Optional Dependencies

Required dependency failure:

Fail safely.

Optional dependency failure:

Degrade gracefully.

## Scaling

API scaling signals may include:

- Request Rate
- Concurrency
- Latency
- CPU
- Memory

Worker scaling signals may include:

- Queue Depth
- Oldest Job Age
- Processing Time

## Deployment Strategies

Common strategies:

- Rolling Deployment
- Blue-Green Deployment
- Canary Deployment

## AI Canary

Monitor both infrastructure and AI quality:

- Error Rate
- Latency
- Groundedness
- Task Success
- Tool Accuracy
- Safety
- Fallback Rate
- Cost
- Token Usage

HTTP 200 does not mean AI quality is healthy.

## Rollback

Define rollback criteria before deployment.

## Database Migration

Prefer backward-compatible migrations.

Pattern:

Expand
→ Migrate
→ Contract

## Checkpoint Versioning

Long-running agents require graph and checkpoint version compatibility.

## Feature Flags

Use feature flags for gradual rollout and experimentation.

## Kill Switch

High-risk tools should support rapid disablement.

## Disaster Recovery

Use:

- Backups
- Restore Procedures
- Recovery Testing

RPO defines acceptable data loss.

RTO defines acceptable recovery time.

## Final Principle

Design failures to be containable, observable, recoverable, and safe.