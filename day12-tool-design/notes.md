# Day 12 Notes — Tool Design

## Core Rule

Good Tool
=
Clear Responsibility
+
Strong Schema
+
Structured Output
+
Explicit Errors
+
Safe Permissions
+
Controlled Side Effects
+
Idempotency
+
Testing
+
Observability

---

## Responsibility

Avoid:

manage_order(action)

Prefer:

get_order()
cancel_order()
create_return()

---

## Read vs Write

Read:
→ Observes state

Write:
→ Changes state

Write Tools need more protection.

---

## Input Validation

Use:

Strong types
Required fields
Optional fields
Enums
Range checks
Unknown-field rejection

---

## Schema vs Business Validation

Schema:
→ Is the input valid?

Business:
→ Is the action allowed?

---

## Output

Return structured facts.

Not natural-language-only responses.

---

## Error Contract

Use:

error_code
retryable
field
reason

when appropriate.

---

## Idempotency

Same logical request
+
Same idempotency key
→
Same final effect

Especially important for Write Tools.

---

## Write Timeout

Timeout
≠ definite failure

Verify outcome
or
retry safely with same idempotency key.

---

## Safe Write Flow

Validate
↓
Authenticate
↓
Authorize
↓
Preconditions
↓
Idempotency
↓
Execute
↓
Verify
↓
Audit

---

## Testing

Test:

Happy Path
Validation
Authorization
Business Rules
Not Found
Timeouts
Retries
Idempotency
Partial Failures
Side Effects
Contracts
Security

---

## Final Rule

LLM can be probabilistic.

Tool interfaces should be deterministic.