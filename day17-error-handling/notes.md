# Day 17 Notes — Error Handling

## Core Flow

Failure
↓
Classify
↓
Choose Recovery Policy

---

## Error Classes

Validation
Authentication
Authorization
Business Rule
Retryable Technical
Non-Retryable Technical
Unknown Outcome
Partial Failure
Fatal

---

## Retry Rule

Retry only when:

Temporary
+
Retryable
+
Safe to repeat

---

## Retry Policy

Use:

Backoff
Jitter
Max Retries
Deadline
Idempotency

---

## Unknown Outcome

Unknown
≠
Failed

For writes:

Verify
or
retry safely using the same idempotency protection.

---

## Partial Failure

Preserve completed steps.

Recover only the failed part.

---

## Circuit Breaker

CLOSED
→ normal

OPEN
→ fail fast

HALF-OPEN
→ test recovery

---

## Fallback

Use a safe alternative when available.

---

## Graceful Degradation

Continue with reduced capability for optional dependency failures.

---

## Fail Closed

Use when authorization, safety, or high-impact state cannot be verified.

---

## Error Propagation

Low-Level Failure
↓
Domain/Application Error
↓
Public API Error

Keep root cause in logs.

---

## Recovery

Recovery may be:

Retry
Fallback
Degrade
Compensate
Verify
Manual Review
Fail Safe

---

## Final Principles

Classify first.

Retry second.

Unknown is not failure.

Recovery is broader than retry.

Important failures need explicit recovery paths.