# Day 16 Notes — Async AI Systems

## Core Concepts

Concurrency
→ overlapping tasks

Parallelism
→ simultaneous execution

Async I/O
→ do not block while waiting

Queue
→ buffers work

Worker
→ executes work

Backpressure
→ prevents overload

---

## Independent Tasks

Independent I/O tasks can run concurrently.

Dependent tasks must preserve execution order.

---

## Retry Policy

Retry only retryable errors.

Use:

Backoff
Jitter
Max Retries

Then:

DLQ

if the job still fails.

---

## Worker Rule

Workers should be idempotent because jobs may be redelivered.

---

## Long-Running Agents

Use:

Queue
+
Worker
+
Checkpoint

Do not keep HTTP requests or workers open while waiting for humans.

---

## Partial Failure

Do not restart successful steps.

Retry only the failed step when safe.

---

## Compensation

Compensation handles the effects of previously successful distributed actions.

---

## Backpressure

Incoming demand must not exceed processing capacity indefinitely.

Use:

Rate Limits
Bounded Queues
Concurrency Limits
Load Shedding
Worker Scaling

---

## Scaling Rule

More Workers
≠
More Throughput

if the downstream dependency is already saturated.

---

## Bulkheads

Separate worker pools by workload.

Example:

Chat
Documents
Embeddings
Notifications

---

## Observability

Monitor:

queue_depth
oldest_job_age
processing_latency
retry_count
failure_rate
DLQ_size
worker_utilization

---

## Final Principles

Retries must be bounded.

Writes must be idempotent.

Queues must be observable.

Long-running state must be durable.

Distributed workflows must expect partial failure.