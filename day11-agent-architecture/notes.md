# Day 11 Notes — Agent Architecture

## Core Definitions

Tool
→ Executes one capability

Workflow
→ Fixed sequence

Agent
→ Dynamically chooses the next action

---

## ReAct

Reason
→ Act
→ Observe
→ Repeat

Use when the next step depends on the previous result.

---

## Plan-and-Execute

Plan
↓
Execute
↓
Replan if required

Use for longer and more complex tasks.

---

## Router

Chooses the correct path or domain.

Example:

RAG
Orders
Returns
Booking

---

## Single Agent

Default starting point.

One Agent
+
Several well-designed Tools

---

## Multi-Agent

Use only when there are real separate specialties.

Costs:

- More LLM calls
- More latency
- More state synchronization
- More debugging complexity

---

## State

Current execution truth.

Examples:

order_id
tool_results
retry_count
step_count
completion_status

---

## Context

Information visible to the model now.

---

## Memory

Persistent information useful for future tasks.

---

## Tool Design

Good Tool:

Clear Responsibility
+
Structured Input
+
Structured Output
+
Explicit Errors
+
Safe Permissions

---

## Read Tool

Reads state.

Examples:

get_order
search_policy

---

## Write Tool

Changes state.

Examples:

create_return
cancel_order
refund

Needs stronger validation.

---

## Idempotency

Same logical request
+
Same idempotency key
→
Same final effect

Important for Write Tools and retries.

---

## Failure Handling

Retryable:
→ Retry with limit

Non-Retryable:
→ Stop / alternate path

Unknown Write Outcome:
→ Verify before retrying

Secondary Failure:
→ Do not repeat successful core action

Agent Loop:
→ Detect + Stop

---

## Guardrails

Use:

Authorization
Business Rules
Tool Permissions
Human Approval
Rate Limits
Audit Logs

---

## Fail Closed

Security check unavailable
→ Deny / Stop

---

## Core Rule

Agent proposes.

Trusted service validates and enforces.

---

## Design Rule

LLM for ambiguity.

Code for certainty.

---

## Complexity Rule

Direct Tool
→ Workflow
→ Single Agent
→ Multi-Agent

Use the simplest architecture that works.