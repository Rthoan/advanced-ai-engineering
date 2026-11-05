# Day 18 Notes — Testing Strategy

## Testing Levels

Unit
Integration
Contract
E2E
AI Evaluation

---

## Test Doubles

Stub
→ predefined output

Fake
→ lightweight working implementation

Mock
→ verifies interaction

---

## RAG

Test:

Retrieval
Ranking
Groundedness
Citations
No-answer behavior

---

## LLM

Test:

Structure
Constraints
Safety
Regression

---

## Agent

Test:

Tool Selection
Tool Arguments
State
Retry
Stop Condition

---

## Tool

Test:

Schema
Authorization
Business Rules
Side Effects
Idempotency

---

## Failure Injection

Simulate:

Timeout
Rate Limit
Crash
Duplicate Delivery
Dependency Failure

---

## Regression

Bug
→ Test
→ Fix
→ Keep Test

---

## Security

Test:

Cross-user access
Prompt Injection
Tool Abuse
Secret Leakage

---

## Performance

Load
Stress
Spike
Soak

Track:

p95
p99
throughput
errors
cost

---

## Core Rule

Test not only whether the system works.

Test how it fails.