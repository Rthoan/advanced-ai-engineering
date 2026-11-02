# Day 17 — Error Handling

## Goal

Design production-ready error handling for AI systems, APIs, tools, agents, and distributed workflows.

Topics:

- Error Taxonomy
- Retryable vs Non-Retryable Errors
- Timeouts and Deadlines
- Retry Policies
- Circuit Breakers
- Fallbacks
- Graceful Degradation
- Error Propagation
- Partial Failures
- Unknown Outcomes
- Compensation
- Fail Fast
- Fail Closed
- Manual Review
- Recovery Paths

---

## Error Taxonomy

Typical categories:

- Validation Error
- Authentication Error
- Authorization Error
- Business Rule Error
- Not Found
- Retryable Technical Error
- Non-Retryable Technical Error
- Unknown Outcome
- Partial Failure
- Fatal Error

Rule:

Classify first.
Retry second.

---

## Validation Errors

Example:

quantity = -3

Action:

Reject input.

Do not retry the same invalid request.

---

## Authentication Errors

Examples:

- Missing token
- Invalid token
- Expired token

Typical result:

401 Unauthorized

---

## Authorization Errors

The identity is known,
but the action is not permitted.

Typical result:

403 Forbidden

Rule:

Authorization failures are not retryable.

---

## Business Rule Errors

Example:

Return window expired.

The system works correctly,
but the requested action is not allowed.

This is not an internal server failure.

---

## Retryable Errors

Examples:

SERVICE_TIMEOUT
RATE_LIMIT
TEMPORARY_NETWORK_ERROR
TEMPORARY_UNAVAILABLE

Possible recovery:

Retry
+
Backoff
+
Jitter
+
Max Retries

---

## Non-Retryable Errors

Examples:

INVALID_INPUT
NOT_AUTHORIZED
UNSUPPORTED_FORMAT
INVALID_CONFIGURATION

Retrying the same request will normally not fix the problem.

---

## Unknown Outcome

A write operation may complete even when the response is lost.

Example:

issue_refund()
↓
TIMEOUT

Unknown does not mean failed.

Correct path:

Mark outcome UNKNOWN
↓
Verify external state
↓
Confirmed?
├── Success → Continue
├── Failure → Safe Retry / Stop
└── Still Unknown → Manual Review

---

## Idempotency

Write operations should support idempotency whenever possible.

Same logical request
+
Same idempotency key
→
Same final effect

Never repeat an unknown write blindly.

---

## Partial Failure

Example:

create_order ✅
charge_payment ✅
send_email ❌

Do not restart the entire workflow.

Instead:

Preserve successful results
↓
Recover only the failed step

---

## Retry Policies

A safe retry policy may include:

- Error classification
- Max retries
- Backoff
- Jitter
- Timeout
- Deadline
- Idempotency
- Retry ownership

---

## Backoff

Example:

Attempt 1
→ wait 1 second

Attempt 2
→ wait 2 seconds

Attempt 3
→ wait 4 seconds

Backoff reduces retry pressure.

---

## Jitter

Add small variation to retry delays.

This prevents many clients from retrying at exactly the same time.

---

## Timeout vs Deadline

Timeout:

Maximum duration of one operation.

Example:

Database timeout = 500ms

Deadline:

Total time budget for the complete request or workflow.

Example:

Request deadline = 3 seconds

---

## Retry Budget

Do not retry beyond the remaining execution budget.

Example:

Request deadline = 3 seconds

If only 500ms remain,
a 2-second retry should not start.

---

## Retry Ownership

Avoid retry amplification.

Bad:

Client retries 3x
API retries 3x
Service retries 3x

Worst case:

27 attempts

Rule:

Define one clear retry owner.

---

## Circuit Breaker

Circuit breakers stop calls to a dependency that is repeatedly failing.

States:

CLOSED
→ calls allowed

OPEN
→ calls blocked temporarily

HALF-OPEN
→ limited test calls

Purpose:

Fail fast and prevent cascading failures.

---

## Fallback

Fallback means using an alternate safe path.

Example:

Primary Model
↓ unavailable
Backup Model

Fallback must still satisfy:

- Safety
- Required functionality
- Acceptable quality

---

## Graceful Degradation

Continue with reduced functionality when an optional dependency fails.

Example:

Reranker unavailable
↓
Use Retriever ranking only

Record:

degraded_mode = true

---

## Required vs Optional Dependencies

Required:

- Authentication
- Authorization
- Payment validation
- Critical ownership checks

Failure:

Fail safely / fail closed

Optional:

- Analytics
- Recommendations
- Secondary email
- Reranker

Failure may allow graceful degradation.

---

## Fail Fast

Stop early when continuing is pointless.

Examples:

- Circuit breaker open
- Invalid configuration
- Unsupported format
- Known unavailable dependency

---

## Fail Closed

Deny the action when safety or permission cannot be verified.

Example:

Authorization Service unavailable
↓
Do not execute refund

Rule:

Security-critical uncertainty
→ Fail Closed

---

## Error Propagation

Translate errors between layers.

Example:

DatabaseTimeout
↓
RepositoryUnavailable
↓
OrderServiceUnavailable
↓
HTTP 503

Each layer should expose the right level of abstraction.

---

## Root Cause

Externally:

SERVICE_UNAVAILABLE

Internally:

Postgres timeout after 800ms

Rule:

Safe external error
+
Detailed internal diagnostics

---

## Error Ownership

Examples:

Validation Error
→ API Layer

Business Rule Error
→ Service Layer

Database Error
→ Repository / Infrastructure Layer

LLM Error
→ AI Service

Handle errors at the layer that understands them.

---

## Do Not Swallow Errors

Avoid:

try:
    ...
except Exception:
    pass

Silent failures create incorrect state and make debugging difficult.

---

## Recovery Paths

Recovery may include:

- Retry
- Fallback
- Graceful Degradation
- Compensation
- Resume from Checkpoint
- Manual Review
- Fail Safe

Recovery is broader than retry.

---

## Compensation

Example:

Reserve Inventory ✅
Payment ❌
↓
Release Inventory

Compensation handles the effects of earlier successful operations.

It is not always a perfect rollback.

---

## Manual Review

Use when automated recovery is unsafe.

Examples:

- High-value unknown payment
- Unknown refund status
- Failed compensation
- Critical state conflict
- Security incident

Possible state:

status = MANUAL_REVIEW

---

## Recovery State

Useful fields:

last_successful_step
failed_step
retry_count
error_code
recovery_action
verification_required
manual_review_required

---

## Error Response Design

Public response:

status = error
code = SERVICE_UNAVAILABLE
request_id = REQ-123

Internal logs may include:

dependency
timeout
attempt
stack trace
root cause

Do not expose internal infrastructure details to clients.

---

## Observability

Useful fields:

request_id
run_id
operation
dependency
attempt
error_code
recovery_action
final_status

Do not log secrets.

---

## Recovery Policy Example

SERVICE_TIMEOUT
→ Limited Retry

NOT_AUTHORIZED
→ Stop

RERANKER_UNAVAILABLE
→ Retriever Fallback

PAYMENT_OUTCOME_UNKNOWN
→ Verify

COMPENSATION_FAILED
→ Manual Review

---

## Main Principles

Never retry before classifying the error.

Unknown does not mean failed.

Recovery is broader than retry.

Critical uncertainty should fail closed.

Do not hide partial success.

Every important failure should have an explicit recovery path.

If automated recovery becomes unsafe, escalate.