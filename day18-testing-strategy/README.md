# Day 18 — Testing Strategy

## Goal

Build a production-ready testing strategy for AI systems.

Topics:

- Unit Testing
- Integration Testing
- Contract Testing
- End-to-End Testing
- Test Doubles
- Mocks
- Stubs
- Fakes
- RAG Testing
- LLM Testing
- Agent Testing
- Tool Testing
- Failure Injection
- Regression Testing
- Security Testing
- Performance Testing

---

## Testing Layers

### Unit Tests

Test small isolated components.

Examples:

- Validation
- Business rules
- Error classification
- Ranking logic

### Integration Tests

Test multiple components together.

Examples:

- Service + Database
- Retriever + Vector DB
- Agent + Tool Registry

### Contract Tests

Verify interface and schema stability.

Examples:

- API response schema
- Tool input/output schema

### End-to-End Tests

Test complete user workflows.

---

## Testing Pyramid

Prefer:

Many Unit Tests

Some Integration Tests

Few End-to-End Tests

Test at the lowest layer that can reliably detect the problem.

---

## Test Doubles

### Stub

Returns predefined responses.

### Fake

Lightweight working implementation.

### Mock

Verifies interactions and calls.

---

## Dependency Injection

Dependencies should be replaceable.

Production:

Real service

Testing:

Fake / Mock / Stub

---

## RAG Testing

Test:

- Recall@K
- MRR
- NDCG
- Groundedness
- Citation Accuracy
- Unsupported Question Handling

Do not test only the final answer.

---

## LLM Testing

Test:

- Structured output
- Required fields
- Constraints
- Safety
- Groundedness
- Regression

Avoid exact string matching when multiple valid answers exist.

---

## Agent Testing

Test:

- Tool Selection
- Tool Arguments
- Stop Conditions
- State Transitions
- Retry Behavior
- Unauthorized Tool Calls
- Loop Prevention

---

## Tool Testing

Test:

- Input Schema
- Output Schema
- Happy Path
- Validation
- Authorization
- Business Rules
- Side Effects
- Idempotency
- Timeout Behavior

---

## Golden Dataset

Maintain a fixed evaluation dataset with:

- Easy cases
- Hard cases
- Unsupported cases
- Adversarial cases
- Multilingual cases
- Tool-use cases

Use it for regression testing.

---

## Failure Injection

Intentionally simulate:

- Timeouts
- Rate Limits
- Network Errors
- Database Failures
- Queue Redelivery
- Worker Crashes
- External API Failures

Verify recovery behavior.

---

## Regression Testing

Workflow:

Bug found
↓
Create failing test
↓
Fix bug
↓
Keep test forever

Regression tests prevent old failures from returning.

---

## Security Testing

Test:

- Authentication
- Authorization
- Cross-user access
- Prompt Injection
- Indirect Prompt Injection
- Tool Abuse
- Secret Leakage
- Data Isolation

Critical security failures should block deployment.

---

## Performance Testing

### Load Testing

Test expected production load.

### Stress Testing

Find system breaking point.

### Spike Testing

Test sudden traffic increases.

### Soak Testing

Detect long-term degradation.

Monitor:

- p50
- p95
- p99
- Throughput
- Error Rate
- CPU
- Memory
- Queue Depth
- Cost

---

## AI Metrics

Useful metrics:

- Retrieval Recall@K
- Groundedness
- Tool Selection Accuracy
- Tool Argument Accuracy
- Citation Accuracy
- Safety Violation Rate
- Latency
- Cost per Request

---

## Main Principles

Test behavior, not implementation details.

Do not mock everything.

Test failures intentionally.

Keep regression datasets.

Security tests should fail closed.

Every production bug should become a test.