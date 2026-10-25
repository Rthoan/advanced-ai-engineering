# Day 12 — Tool Design

## Goal

Design production-ready tools for AI agents.

A good Tool should be:

- Clear
- Focused
- Structured
- Safe
- Testable
- Observable

---

## Tool Responsibility

Each Tool should have one clear responsibility.

Bad:

manage_order(action)

Better:

get_order()
cancel_order()
create_return()

Rule:

One Tool
→ One Clear Responsibility

---

## Tool Granularity

Avoid Tools that are too broad.

Bad:

manage_everything()

Also avoid unnecessary fragmentation.

Bad:

get_order_status()
get_order_date()
get_order_category()

If these values are usually needed together, prefer:

get_order()

---

## Read vs Write Tools

### Read Tools

Observe system state.

Examples:

get_order()
search_policy()
check_inventory()

### Write Tools

Change system state.

Examples:

create_return()
cancel_order()
book_appointment()
issue_refund()

Write Tools require stronger:

- Validation
- Authorization
- Idempotency
- Audit logging

---

## Strong Input Schemas

Avoid free-text Tool inputs when structured fields are possible.

Bad:

input: "return order 123 because damaged"

Better:

order_id: string
quantity: integer
reason_code: enum
customer_note: optional string

---

## Required vs Optional Fields

Required:

Tool cannot execute without the value.

Optional:

Tool can continue without it.

Example:

order_id: required
reason_code: required
customer_note: optional

Never invent missing required values.

---

## Type Validation

Examples:

quantity: integer
refund_amount: number
currency: enum

Strong types reduce ambiguity.

---

## Range Validation

Valid type does not always mean valid value.

Example:

quantity = -2

Integer type is valid,
but the value is invalid.

Rule:

quantity >= 1

---

## Enum Fields

Enums provide predictable values.

Example:

reason_code:

- DAMAGED
- WRONG_ITEM
- NOT_NEEDED
- OTHER

Enums can be combined with free-text notes.

---

## Schema Validation vs Business Validation

Schema Validation asks:

Is the input structurally valid?

Example:

quantity must be integer
quantity >= 1

Business Validation asks:

Is the action allowed?

Example:

Is the order still inside the return window?

---

## Tool Input Flow

Tool Request
↓
Schema Validation
↓
Authentication
↓
Authorization
↓
Business Validation
↓
Execution

---

## Structured Output

Tools should return structured data.

Bad:

"Everything worked."

Better:

status: success
return_id: RET-900
order_id: ORD-123
created_at: ...

---

## Success Contract

Use a predictable success structure.

Example:

status: success
data: ...
error: null

---

## Error Contract

Use stable error codes.

Example:

status: error
data: null
error:
  code: ORDER_NOT_FOUND
  retryable: false

---

## Common Error Codes

Examples:

VALIDATION_ERROR
ORDER_NOT_FOUND
NOT_AUTHORIZED
NOT_ELIGIBLE
ALREADY_RETURNED
SERVICE_TIMEOUT
RATE_LIMITED

---

## Retryable Errors

Examples:

SERVICE_TIMEOUT
RATE_LIMIT
TEMPORARY_UNAVAILABLE

Possible action:

Retry with limits.

---

## Non-Retryable Errors

Examples:

ORDER_NOT_FOUND
NOT_AUTHORIZED
NOT_ELIGIBLE

Do not retry blindly.

---

## Tool Output vs User Response

Tool:

status: success
return_id: RET-900

Agent:

"Your return request was created successfully. Return ID: RET-900."

Rule:

Tool
→ Structured Facts

Agent
→ Natural Language

---

## Side Effects

Write Tools may create side effects.

Example:

create_return()

May cause:

- Return record creation
- Order state change
- Shipping workflow
- Notification

These side effects should be known and controlled.

---

## Preconditions

Before Write Tool execution:

Order exists?
↓
User authorized?
↓
Action allowed?
↓
Already completed?
↓
Execute

---

## Postconditions

After execution, verify the expected system state.

Example:

cancel_order()

Postcondition:

order.status == cancelled

---

## Idempotency

Write Tools should be designed to avoid duplicate effects.

Example:

create_return(
  order_id,
  idempotency_key
)

Same logical request
+
Same idempotency key
→
Same final effect

---

## Unknown Write Outcome

A timeout does not necessarily mean failure.

Example:

create_return()
↓
TIMEOUT

The server may have completed the action.

Correct response:

Verify operation state
or
Retry with the same idempotency key

---

## Safe Write Tool Pattern

Validate Input
↓
Authenticate
↓
Authorize
↓
Check Preconditions
↓
Check Idempotency
↓
Execute
↓
Verify Postcondition
↓
Return Structured Result
↓
Audit

---

## Partial Failure

Example:

Return created
↓
Email failed

Do not repeat the successful core action.

Store:

return_created = true
email_sent = false

Retry only the failed secondary action.

---

## Compensating Actions

In distributed systems, a later failure may require a compensating action.

Example:

Reserve inventory
↓
Payment fails
↓
Release inventory

---

## Permissions

Tools should require explicit scopes.

Examples:

orders.read
returns.write
refunds.small
refunds.large

Apply least privilege.

---

## Tool Testing

Production Tools require more than a happy-path test.

Test:

- Success path
- Validation failures
- Authorization failures
- Business-rule failures
- Not-found cases
- Timeouts
- Idempotency
- Partial failures
- Retry limits
- Side effects
- Security boundaries

---

## Unit Tests

Test Tool logic in isolation.

Examples:

- Validation
- Error mapping
- Idempotency logic

---

## Integration Tests

Test integration between:

Tool
+
Business Service
+
Database / External API

---

## End-to-End Tests

Test:

User Request
↓
Agent
↓
Tool
↓
Service
↓
Database
↓
Result
↓
Agent Response

---

## Tool Selection Tests

Also test that the Agent selects the correct Tool.

Example:

"Where is my order?"

Expected:

get_order()

Not:

create_return()

---

## Tool Misuse Tests

Example:

"What happens if I cancel my order?"

Expected:

No cancel_order() execution.

The user asked for information, not an action.

---

## Observability

Useful fields:

request_id
tool_name
latency
result_status
error_code

Do not log unnecessary secrets or sensitive data.

---

## Production Tool Checklist

Before shipping a Tool, verify:

- Clear responsibility
- Strong input schema
- Defined required fields
- Predictable output
- Stable error codes
- Authorization
- Known side effects
- Idempotency
- Tests
- Observability

---

## Main Principle

LLM output may be probabilistic.

Tool boundaries must be deterministic.