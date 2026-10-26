# Day 13 — LangGraph Workflows

## Goal

Design production-ready workflows using:

- State
- Nodes
- Edges
- Conditional Edges
- Routing
- Retry Loops
- Checkpoints
- Human-in-the-loop
- Error Paths

---

## Core Graph Model

START
↓
Node
↓
State Update
↓
Condition
├── Path A
├── Path B
└── END

---

## State

State represents the current execution truth.

Example:

order_id
order_data
policy_data
return_eligible
return_id
retry_count
error_code
status

Rule:

Store only execution-relevant data.

---

## State vs Context vs Memory

State:
Current workflow truth.

Context:
What the model sees now.

Memory:
Information that may persist across future interactions.

---

## Good State Design

Good State should be:

- Minimal
- Structured
- Typed
- Clear
- Single source of truth

Avoid:

data
result
temp
flag
x

Prefer:

order_id
return_eligible
retry_count
last_error_code

---

## Node

A Node performs one unit of work.

Examples:

load_order
retrieve_policy
check_eligibility
create_return
verify_return

Rule:

One Node
→ One Clear Responsibility

---

## Edge

An Edge is a fixed transition.

Example:

load_order
↓
check_eligibility

---

## Conditional Edge

A Conditional Edge chooses the next path based on State.

Example:

eligible?
├── Yes → create_return
└── No  → explain_not_eligible

---

## Routing

Routing decides where execution goes next.

Routing should not perform business actions.

Rule:

Routing decides.
Nodes execute.
State carries truth.

---

## Deterministic Routing

Use code when the decision is certain.

Examples:

NOT_AUTHORIZED
→ stop

SERVICE_TIMEOUT
→ retry policy

---

## LLM Routing

Use an LLM when intent is ambiguous.

Example:

User message
↓
classify intent
├── POLICY
├── ORDER_STATUS
├── RETURN
└── UNKNOWN

Rule:

Code for certainty.
LLM for ambiguity.

---

## Retry Loops

Example:

get_order
↓
SERVICE_TIMEOUT
↓
can_retry?
├── Yes → get_order
└── No  → handle_failure

State:

retry_count
max_retries
retryable
error_code

Rule:

Every loop needs an exit condition.

---

## Error Routing

Example:

error_type?
├── validation → request_input
├── authorization → security_stop
├── business → explain_rule
├── retryable → retry_handler
├── unknown_write → verify_operation
└── fatal → fail_safe

---

## Human-in-the-loop

Use when an action is:

- High impact
- Financially sensitive
- Security sensitive
- Irreversible
- Legally important

Example:

refund_amount > limit?
├── No → issue_refund
└── Yes → human_approval

---

## Human Approval State

approval_required = true
approval_status = pending

Possible values:

pending
approved
rejected

---

## Checkpoints

A Checkpoint saves workflow state.

Use cases:

- Long-running workflows
- Human approval
- Crash recovery
- Pause and resume

Rule:

Checkpoint saves workflow state,
not external reality.

---

## Resume Safety

After a long pause:

Resume
↓
Revalidate critical external state
↓
Still valid?
├── Yes → Execute
└── No  → Stop or Re-route

---

## Unknown Write Outcome

Example:

create_return
↓
TIMEOUT
↓
Outcome unknown
↓
verify_return

Then:

return_exists?
├── Yes → success
└── No  → safe_retry

Never assume a write timeout means failure.

---

## Production Return Workflow

START
↓
validate_request
↓
load_order
↓
result?
├── NOT_FOUND → explain_not_found → END
├── TIMEOUT → retry_router
└── SUCCESS
      ↓
retrieve_return_policy
      ↓
check_eligibility
      ↓
eligible?
├── No → explain_not_eligible → END
└── Yes
      ↓
approval_required?
├── No → create_return
└── Yes → human_approval
              ↓
          CHECKPOINT
              ↓
          approved?
       ├── No → END
       └── Yes
             ↓
      revalidate_order
             ↓
        create_return

---

## Tools and LangGraph

LangGraph:

- Orchestration
- State
- Routing
- Retry control
- Checkpoints
- Control flow

Tools:

- Read data
- Write data
- Call services
- Perform actions

Rule:

LangGraph controls the workflow.
Tools perform the work.

---

## RAG in the Graph

Example:

retrieve_return_policy
↓
RAG Retrieval
↓
Relevant Policy
↓
Store policy_data in State

---

## Agent inside a Graph

An Agent may be a Node.

Example:

agent_router
↓
next_action?
├── RAG
├── Order Tool
├── Return Workflow
└── Finish

Use an Agent only when decisions are dynamic.

---

## Hybrid Architecture

Strong production systems often use:

Deterministic Workflow
+
Agent Decision Nodes

Example:

START
↓
authenticate
↓
validate
↓
agent_router
├── RAG
├── Order Flow
└── Return Flow

---

## Observability

Useful trace fields:

request_id
node_name
start_time
end_time
latency
result
error_code
retry_count

---

## Debugging

When a Graph fails, inspect:

1. Initial State
2. Executed Nodes
3. Selected Edges
4. Tool Results
5. State Updates
6. Retry Loops
7. Final Node

---

## Anti-Patterns

Avoid:

- Huge State
- One giant Node
- LLM decides everything
- Infinite retries
- Missing error paths
- Resume without revalidation
- Write retries without idempotency

---

## Main Principle

Use Graphs to make control flow explicit.