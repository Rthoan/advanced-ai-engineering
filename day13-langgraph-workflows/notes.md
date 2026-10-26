# Day 13 Notes — LangGraph Workflows

## Core Concepts

State
→ execution truth

Node
→ unit of work

Edge
→ fixed transition

Conditional Edge
→ state-based transition

Checkpoint
→ saved workflow state

Human-in-the-loop
→ controlled human decision

---

## State Rule

Good State:

Minimal
Structured
Typed
Single Source of Truth
Execution Relevant

---

## Routing Rule

Routing decides.
Nodes execute.
State carries truth.

---

## Retry Rule

Retry only when:

retryable == true

and

retry_count < max_retries

Every loop needs an exit condition.

---

## Error Classes

Validation
Authorization
Business
Retryable Technical
Unknown Write Outcome
Fatal

Each may need a different path.

---

## Human Approval

Use for:

High-risk
High-value
Sensitive
Irreversible

---

## Checkpoint Rule

Checkpoint saves execution state.

It does not freeze external systems.

After long pauses:

Revalidate critical external data.

---

## LangGraph vs Tools

LangGraph:
Controls workflow.

Tools:
Perform actions.

---

## Deterministic vs LLM

Code for certainty.

LLM for ambiguity.

---

## Final Rule

Use Graphs to make control flow explicit.