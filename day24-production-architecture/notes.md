# Day 24 Notes — Production Architecture

## Core Idea

Production architecture combines:

- Components
- Clear ownership
- Security
- Reliability
- Observability
- Scaling
- Deployment safety
- Recovery

## Agent

Agent orchestrates.

Trusted services enforce.

Database stores truth.

## RAG

Authorization-aware retrieval.

ACL filtering before retrieval.

## LLM Gateway

Centralize model access and operational controls.

## Reliability

Use timeouts, bounded retries, circuit breakers, bulkheads, and backpressure.

## Deployment

Use rolling, blue-green, or canary deployment.

Monitor AI quality, not only HTTP health.

## Disaster Recovery

Backup alone is not enough.

Restore must be tested.

## Final Rule

Production systems are designed for failure, not for perfect conditions.