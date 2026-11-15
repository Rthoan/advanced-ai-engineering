# Day 23 — Cost + Latency Optimization

## Goal

Reduce AI system cost and latency without breaking quality, correctness, safety, or reliability.

## Core Principle

Measure
→ Optimize
→ Measure again

## Cost Breakdown

Important cost drivers:

- Input Tokens
- Output Tokens
- Number of LLM Calls
- Model Choice
- Retries
- Agent Loops
- Tool Schemas
- Context Size

Measure:

- Cost per request
- Cost per successful task

## Latency Breakdown

Break latency into:

- API
- Retrieval
- Reranking
- LLM
- Tools
- Database

Optimize the dominant bottleneck first.

## LLM Calls

Remove unnecessary LLM calls.

Use:

LLM for ambiguity.

Code for certainty.

## Context Optimization

Send only:

- Relevant
- Authorized
- Necessary

Use reranking, deduplication, summaries, and context budgets.

More context is not automatically better context.

## Prompt Compression

Remove:

- Repetition
- Redundant examples
- Unnecessary wording

Always run regression tests after prompt compression.

## Caching

Caching avoids repeating reusable work.

Types:

- Response Cache
- Embedding Cache
- Retrieval Cache
- Tool Result Cache
- Prompt Prefix Cache

## Cache Safety

Cache keys must preserve authorization scope.

Personalized data requires personalized cache scope.

Use:

- TTL
- Invalidation
- Versioning

## Cache Stampede

Prevent repeated recomputation using:

- Single-flight
- Request Coalescing
- Locks
- Staggered TTL

## Batching

Batching processes multiple items together.

Useful for:

- Embeddings
- Reranking
- Ingestion
- Offline Evaluation
- Database Operations

Batching improves throughput but may increase latency.

## Model Routing

Simple tasks can use smaller and faster models.

Complex tasks may use stronger models.

Measure escalation rate when using cascaded models.

## Parallelism

Run independent operations concurrently when it improves latency.

Parallelism can reduce latency while increasing cost.

## Retries and Agent Loops

Retries and agent steps add cost and latency.

Use:

- Retry classification
- Retry limits
- Max steps
- Deadlines

## Latency Budget

Define target latency per component.

Example:

API
Retrieval
Reranking
LLM
Tools
Buffer

## Quality Guardrails

Optimization must respect minimum quality thresholds.

Examples:

- Groundedness
- Tool Accuracy
- Safety
- Task Success

## Optimization Order

1. Remove unnecessary LLM calls
2. Remove unnecessary context
3. Cache safe repeated work
4. Batch suitable workloads
5. Route to the right model
6. Parallelize independent work
7. Optimize lower-level infrastructure

## Final Principle

Optimize the system, not just the model.