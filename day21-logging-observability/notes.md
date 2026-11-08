# Day 21 Notes — Logging and Observability

## Logs

Detailed events.

Use structured logging.

Never log secrets.

## Metrics

Aggregated system behavior.

Counter:
increases over time.

Gauge:
current changing value.

Histogram:
distribution such as latency.

## SLI

Actual measured value.

## SLO

Target value.

## AI Metrics

Latency
TTFT
Tokens
Cost
Fallback Rate
Degraded Mode Rate
Agent Steps
Tool Errors

## Tracing

Trace
→ complete request journey.

Span
→ one operation.

## IDs

Request ID

Correlation ID

Run ID

Trace ID

## Debugging

Metrics
→ Trace
→ Logs

## Final Rule

HTTP 200 does not automatically mean the AI system is healthy.