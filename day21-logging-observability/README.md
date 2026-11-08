# Day 21 — Logging and Observability

## Goal

Build production observability for AI systems using logs, metrics, and traces.

## Observability

Observability combines:

- Logs
- Metrics
- Traces

AI systems also need:

- Model version
- Prompt version
- Token usage
- Retrieval metadata
- Tool calls
- Agent steps
- Fallback usage
- Cost

## Logging

Use structured logs.

Useful fields:

- timestamp
- level
- event
- request_id
- correlation_id
- run_id
- component
- operation
- error_code
- latency_ms
- status

Never log secrets.

## IDs

Request ID:
tracks one request.

Correlation ID:
links distributed operations across services.

Run ID:
tracks an agent or long-running workflow.

Trace ID:
links spans within a distributed trace.

## Metrics

Common metric types:

- Counter
- Gauge
- Histogram

Examples:

Counters:
- requests_total
- errors_total

Gauges:
- queue_depth
- active_workers

Histograms:
- request_latency
- llm_latency

## SLI and SLO

SLI:
actual measured service behavior.

SLO:
target service behavior.

Example:

SLI:
94% of requests under 3 seconds.

SLO:
95% of requests under 3 seconds.

## AI Metrics

Monitor:

- LLM latency
- TTFT
- Input tokens
- Output tokens
- Cost per request
- Fallback rate
- Empty retrieval rate
- Degraded mode rate
- Agent steps per run
- Tool error rate
- Manual review rate

HTTP success alone does not mean the AI system is healthy.

## Tracing

A Trace represents the full request journey.

A Span represents one operation inside the Trace.

Example:

API
├── Auth
├── Retriever
├── Reranker
├── LLM
└── Tool

## Distributed Tracing

Propagate trace context across services.

Useful span attributes:

- model_name
- prompt_version
- latency_ms
- tokens
- retry_count
- tool_name
- fallback_used

Do not store secrets or unnecessary sensitive content.

## Debugging Workflow

Metrics
→ detect the issue

Trace
→ locate the issue

Logs
→ understand the root cause

## OpenTelemetry

OpenTelemetry provides a standardized approach for collecting logs, metrics, and traces across distributed systems.

## Main Principle

Production AI observability must monitor both:

System Health
+
AI Quality