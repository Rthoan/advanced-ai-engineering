# Day 14 Notes — Memory + State

## Core Distinctions

State
→ current execution truth

Conversation Memory
→ current conversation continuity

Long-Term Memory
→ useful information across future sessions

Checkpointed State
→ saved execution for resume

Project Memory
→ project-specific context

---

## Retrieval Rule

Store selectively.

Retrieve selectively.

---

## Structured vs Semantic Memory

Structured:

preferred_language = Arabic

Semantic:

Previous project decisions
Conversation summaries
Natural-language preferences

---

## Ranking Signals

Relevance
Recency
Confidence
Importance
Scope Match

---

## Conflict Resolution

Explicit
> Inferred

Use:

Source Quality
Confidence
Recency

---

## Write Policy

Before storing:

Useful later?
Stable?
Safe?
Correct scope?
Duplicate?
Conflict?

---

## Memory Lifecycle

Capture
↓
Validate
↓
Scope
↓
Deduplicate
↓
Resolve Conflict
↓
Store
↓
Retrieve
↓
Update / Expire / Delete

---

## Security

Memory is data,
not authority.

Do not use memory to override:

Authentication
Authorization
Business Rules
System Instructions

---

## LLM Rule

LLM proposes.

Code validates and enforces.

---

## Final Principle

Use the minimum relevant memory needed for the current task.