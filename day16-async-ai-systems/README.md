# Day 16 — Async AI Systems

## Goal

Design production-ready asynchronous AI systems that can safely handle:

- Concurrent I/O
- Long-running jobs
- Queues
- Workers
- Retries
- Backpressure
- Checkpoints
- Distributed workflows
- Partial failures
- Worker scaling

---

## Concurrency vs Parallelism

Concurrency:

Manage multiple tasks in overlapping time.

Parallelism:

Execute multiple tasks simultaneously.

Rule:

Concurrency
≠
Parallelism

---

## Async I/O

Async I/O is useful when the system is waiting for:

- LLM APIs
- Databases
- Vector databases
- HTTP APIs
- Object storage
- External tools

Example:

async def call_service():
    result = await async_http_call()
    return result

Important:

async def
+
blocking code
=
still blocking

---

## I/O-Bound vs CPU-Bound

I/O-Bound:

- LLM API calls
- HTTP calls
- Database queries
- Vector DB queries

CPU-Bound:

- Heavy document parsing
- Local inference
- Image processing
- Large computations

CPU-heavy work may require:

- Worker processes
- Dedicated services
- GPU workers

---

## Concurrent Independent Tasks

If tasks are independent:

Vector Search → 400 ms
User Profile → 200 ms
Order Lookup → 300 ms

Sequential:

~900 ms

Concurrent:

~400 ms

Rule:

Independent I/O tasks
→ run concurrently when safe.

---

## Dependency Graph

Do not run dependent tasks concurrently.

Example:

Authenticate User
↓
Load Private Orders

The second step requires the first.

---

## Bounded Concurrency

Never launch unlimited tasks.

Example:

max_concurrency = 20

This protects:

- LLM providers
- Databases
- Vector stores
- GPUs
- External APIs

Rule:

More concurrency
≠ more throughput.

---

## Queue

A Queue separates work intake from work execution.

Producer
↓
Queue
↓
Worker

Benefits:

- Load buffering
- Retry support
- Worker scaling
- Failure recovery
- Backpressure

---

## Producer

A Producer creates jobs.

Example:

FastAPI
→ document ingestion job

---

## Worker

A Worker processes jobs.

Example:

JOB-100
↓
Download Document
↓
Parse
↓
Chunk
↓
Embed
↓
Index
↓
COMPLETED

---

## Job States

Typical states:

QUEUED
PROCESSING
RETRYING
WAITING_FOR_APPROVAL
COMPLETED
FAILED
CANCELLED

---

## Job Payload

Avoid placing large files directly in queue messages.

Bad:

500 MB PDF in queue message

Better:

document_id = DOC-123
storage_key = files/doc123.pdf

The worker retrieves the file from storage.

---

## Retry Strategy

Retry only retryable failures.

Examples:

Retryable:

SERVICE_TIMEOUT
RATE_LIMIT
TEMPORARY_UNAVAILABLE

Non-Retryable:

INVALID_INPUT
NOT_AUTHORIZED
INVALID_DOCUMENT

---

## Backoff

Do not immediately retry failures repeatedly.

Example:

Attempt 1
→ wait 1 second

Attempt 2
→ wait 2 seconds

Attempt 3
→ wait 4 seconds

This reduces retry storms.

---

## Jitter

Add small randomness to retry delays.

Instead of all workers retrying after exactly 2 seconds:

1.7 s
2.1 s
2.4 s
1.9 s

This prevents synchronized retries.

---

## Max Retries

Every retry loop must have a limit.

Example:

max_retries = 3

Rule:

Retries without limits
are another form of failure.

---

## Dead Letter Queue

After repeated failure:

Attempt 1 ❌
Attempt 2 ❌
Attempt 3 ❌
↓
DLQ

DLQ jobs can be:

- Inspected
- Debugged
- Reprocessed
- Alerted

---

## Poison Messages

Some jobs always fail because the input itself is bad.

Example:

Corrupted document

Without limits:

Process
↓
Fail
↓
Requeue
↓
Fail forever

Solution:

Max retries
↓
DLQ

---

## Idempotent Workers

Queue systems may redeliver messages.

Therefore:

At-least-once delivery
+
Idempotent processing

is a common production design.

Example:

index_document(DOC-123)

Running it twice should not create uncontrolled duplicate chunks.

---

## Acknowledgement

After successful processing:

Worker
↓
ACK

If the worker crashes before ACK, the message may be delivered again.

This is another reason idempotency is important.

---

## Backpressure

Backpressure prevents work from entering the system faster than downstream capacity.

Example:

Incoming:
1000 jobs/sec

Processing:
100 jobs/sec

Without protection:

Queue Depth ↑
Queue Age ↑
Latency ↑

---

## Backpressure Strategies

Possible mechanisms:

- Rate limiting
- Bounded queues
- Concurrency limits
- Producer throttling
- Load shedding
- Priority queues
- Worker scaling

---

## Queue Metrics

Monitor:

queue_depth
oldest_job_age
processing_time
success_rate
failure_rate
retry_count
DLQ_size

Queue depth alone is not enough.

A small queue with very old jobs can still indicate a serious problem.

---

## Long-Running Agents

Do not keep HTTP requests or workers blocked for hours.

Example:

POST /v1/agent-runs
↓
202 Accepted
↓
RUN-123
↓
Queue
↓
Agent Worker
↓
LangGraph

---

## Human Approval

If the workflow requires human approval:

Agent Worker
↓
Approval Required
↓
Save Checkpoint
↓
Release Worker

Later:

Approval Event
↓
Resume Job
↓
Worker
↓
Load Checkpoint
↓
Revalidate
↓
Continue

Rule:

Do not keep workers blocked while waiting for humans.

---

## Durable Execution

Long-running workflows should persist their state.

Execute Step
↓
Persist State
↓
Process Can Stop
↓
Resume Later

The workflow should not depend on one process staying alive forever.

---

## Queue vs Checkpoint

Queue:

What work should execute?

Checkpoint:

Where did the workflow stop and what was its state?

Both are useful in long-running AI workflows.

---

## Revalidation

A checkpoint preserves previous workflow state.

It does not freeze external reality.

After a long pause:

Resume
↓
Revalidate Critical Data
↓
Continue

---

## Distributed Workflows

Example:

Agent Service
↓
Order Service
↓
Payment Service
↓
Email Service

Distributed workflows must expect partial failures.

---

## Partial Failure

Example:

Booking Created ✅
Payment Charged ✅
Email Sent ❌

Do not restart the entire workflow.

Instead:

Preserve successful results
↓
Retry only failed step

---

## Compensation

If a later step fails permanently, an earlier successful action may need compensation.

Example:

Reserve Inventory ✅
Payment ❌
↓
Release Inventory

Rule:

Compensation
≠ always perfect rollback.

---

## Saga Concept

A distributed workflow can use a sequence of actions and compensating actions.

Example:

Reserve Inventory
↓
Charge Payment
↓
Create Shipment

If shipment creation fails:

Refund / compensate payment
↓
Release inventory

---

## Unknown Write Outcome

Example:

charge_payment()
↓
TIMEOUT

Do not assume failure.

Use:

Verify Status

or:

Retry using the same idempotency key.

---

## Events

Command:

CREATE_RETURN

Meaning:

Do this action.

Event:

RETURN_CREATED

Meaning:

This already happened.

---

## Event-Driven Resume

Example:

APPROVAL_GRANTED
↓
Queue
↓
Resume Agent Worker
↓
Load Checkpoint
↓
Continue

---

## Duplicate Events

Events may be delivered more than once.

Consumers should therefore be idempotent.

---

## Worker Scaling

Workers can scale based on demand.

Signals may include:

- Queue Depth
- Queue Age
- Processing Latency
- CPU
- Memory
- GPU Utilization

But worker scaling cannot remove downstream bottlenecks.

---

## Bulkhead Pattern

Separate workloads into independent resource pools.

Example:

Chat Workers
Document Workers
Embedding Workers
Notification Workers

This prevents one overloaded workload from consuming every worker.

---

## Load Shedding

During overload, rejecting lower-priority work can be safer than allowing the whole system to fail.

Examples:

429 Too Many Requests

503 Service Unavailable

---

## Priority Queues

Possible priorities:

High
Normal
Batch

Protect interactive user traffic from large batch workloads.

Avoid starvation of low-priority jobs.

---

## Production Architecture

Client
↓
API Gateway
↓
Rate Limiting
↓
FastAPI
↓
Async Boundary
├── Interactive Path
│   ├── Async I/O
│   ├── Bounded Concurrency
│   └── Streaming
│
└── Long-Running Path
    ↓
    Queue
    ↓
    Worker Pools
    ├── Agent Workers
    ├── Document Workers
    ├── Embedding Workers
    └── Notification Workers
    ↓
    External Dependencies

Supporting components:

- Job State Store
- Checkpoint Store
- DLQ
- Observability
- Circuit Breakers
- Autoscaling

---

## Production Checklist

Before shipping:

- Concurrency bounded?
- Queue bounded?
- Retries bounded?
- Backoff configured?
- Jitter configured?
- DLQ available?
- Workers idempotent?
- Checkpoints durable?
- Dependencies isolated?
- Autoscaling bounded?
- Queue age monitored?
- Queue depth monitored?
- Write retries safe?
- Partial failures handled?

---

## Main Principles

Independent I/O can run concurrently.

More concurrency does not automatically mean more throughput.

Retries must be bounded.

Every queue needs observability.

Every write path needs idempotency.

Long-running workflows need durable state.

Distributed systems must expect partial failure.