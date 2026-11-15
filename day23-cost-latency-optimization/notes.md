# Day 23 Notes — Cost + Latency Optimization

## Core Rule

Measure before optimizing.

## Cost

Track:

- Tokens
- LLM Calls
- Model Cost
- Retries
- Agent Steps
- Cost per Request
- Cost per Successful Task

## Latency

Break total latency into component spans.

Optimize the dominant bottleneck.

## Context

Use only relevant, authorized, and necessary context.

## Caching

Avoid repeating reusable work.

Cache keys must preserve security scope.

## Batching

Combine multiple workloads to improve throughput.

Batching may increase waiting latency.

## Routing

Use smaller models for simpler tasks when quality allows.

## Parallelism

Parallelize independent operations.

## Guardrails

Never improve cost and latency by silently damaging quality or safety.

## Final Rule

Measure
→ Optimize
→ Measure again