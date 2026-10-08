# Day 03 Notes

## Core Decision Map

Generation / Analysis
→ LLM

Private Knowledge
→ RAG

Structured Data / Action
→ Tool

Choose Between Tools
→ Agent

Fixed Sequence
→ Workflow

State + Branches + Retries
→ LangGraph

---

## Important Rule

A Tool does not automatically require an Agent.

Example:

Booking Success
↓
Email Tool

This is a fixed workflow.

---

## RAG vs Database

Documents / unstructured knowledge
→ RAG

Structured live data
→ Database / API Tool

Example:

Return policy
→ RAG

Order status
→ Order API

---

## Agent Rule

Use an Agent when the system must decide:

Which tool should I use?

---

## LangGraph Rule

Use LangGraph when the system needs:

- State
- Retry
- Branching
- Multi-step logic
- Human approval
- Loops

---

## Overengineering

Always ask:

Can this be solved with a simpler architecture?

Prefer:

Simple
→ Reliable
→ Testable
→ Cheap

before:

Complex
→ Agent everywhere
→ LangGraph everywhere