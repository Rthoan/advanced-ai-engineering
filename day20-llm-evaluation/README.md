# Day 20 — LLM Evaluation

## Goal

Evaluate LLM behavior across correctness, instruction following, safety, reliability, latency, and cost.

## Core Metrics

- Correctness
- Instruction Following
- Structured Output
- Completeness
- Consistency
- Robustness
- Safety
- Latency
- Cost

## Correctness

Measure whether the model produces the correct result.

Use exact matching only when the output must be exact.

For semantic tasks, evaluate required facts, forbidden errors, and expected behavior.

## Instruction Following

Evaluate whether the model follows explicit constraints.

Examples:

- JSON only
- Specific number of bullets
- Required fields
- Forbidden content

A correct answer may still fail if it violates the required contract.

## Structured Output

Validate deterministically when possible:

- JSON validity
- Required fields
- Field types
- Enums
- Ranges
- Extra fields

## Safety Evaluation

Evaluate:

- Correct refusal
- Unsafe compliance
- Over-refusal
- Safe completion
- Prompt injection resistance
- Tool safety
- Data leakage

Safety means correct behavior under risk, not simply refusing more.

## Adversarial Testing

Include:

- Prompt Injection
- Indirect Prompt Injection
- Jailbreak attempts
- Multi-turn attacks
- Tool misuse
- Data leakage attempts

## Pairwise Evaluation

Compare two model or prompt outputs directly.

Useful for:

- Model A vs Model B
- Prompt A vs Prompt B

Watch for:

- Position Bias
- Verbosity Bias
- Self-Preference Bias

## Judge Calibration

Compare LLM Judge decisions against trusted human-reviewed examples.

Evaluate the evaluator before relying on automated judging.

## Regression Evaluation

Run the same evaluation suite after changes to:

- Model
- Prompt
- Temperature
- System instructions
- Tool descriptions
- Output schema

## Latency

Track:

- p50
- p95
- p99
- TTFT
- Tokens per second

## Cost

Track:

- Input tokens
- Output tokens
- Cost per request
- Cost per successful task

## Release Decision

Evaluate:

Quality
+
Safety
+
Latency
+
Cost

Critical safety guardrails must pass before optimization metrics are considered.

## Main Principle

The best model is not simply the model with the highest quality score.

It must satisfy the production requirements across quality, safety, latency, and cost.