# Day 20 Notes — LLM Evaluation

## Correctness

Is the answer correct?

## Instruction Following

Did the model follow the constraints?

## Structured Output

Validate schemas with deterministic code.

## Safety

Measure:

Unsafe Compliance
Over-Refusal
Safe Completion
Tool Safety
Data Leakage

## Pairwise Evaluation

Compare A vs B directly.

## Judge Calibration

Compare LLM Judge results with human-reviewed examples.

## Regression

Every important prompt or model change should run the full regression suite.

## Latency

Track:

p50
p95
p99
TTFT

## Cost

Track:

Tokens
Cost per Request
Cost per Successful Task

## Final Rule

Guardrails first.

Optimization second.