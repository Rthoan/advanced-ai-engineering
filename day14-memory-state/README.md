# Day 14 — Memory + State

## Goal

Design production-ready memory and state architecture for AI agents and workflows.

Topics:

- Workflow State
- Short-Term Memory
- Conversation Memory
- Long-Term Memory
- Project Memory
- Checkpointed State
- Semantic Memory
- Memory Retrieval
- Memory Write Policies
- Conflict Resolution
- Memory Security

---

## State

State represents the current execution truth.

Examples:

order_id
retry_count
error_code
approval_status
workflow_status

Rule:

State
→ What is true now in this execution.

---

## Long-Term Memory

Long-Term Memory stores information that may be useful across future interactions.

Examples:

preferred_language
response_style
preferred_currency

Rule:

Long-Term Memory
→ What may be useful later.

---

## Conversation Memory

Conversation Memory maintains continuity inside the current conversation.

Example:

User is currently processing a return for order ORD-123.

Possible strategy:

Conversation Summary
+
Recent Messages

---

## Short-Term Memory

Short-Term Memory contains recent task or conversational information.

Example:

User said the damaged item is a phone.

It may overlap with conversation context, but it is different from workflow execution state.

---

## Checkpointed State

Checkpointed State is saved workflow state used for pause and resume.

Example:

approval_status = pending
current_node = human_approval
retry_count = 1

Rule:

Checkpoint
→ Resume workflow.

Memory
→ Inform future interaction.

---

## Project Memory

Project Memory stores information specific to one project.

Example:

Project: ecommerce-assistant

Use RAG for policies.
Use Tools for order data.
Use human approval for high-value refunds.

Do not store project-specific facts as global user preferences.

---

## Structured Memory

Structured Memory is useful for clear, typed facts.

Example:

preferred_language = Arabic

Possible metadata:

source
confidence
updated_at
version
scope

---

## Semantic Memory

Semantic Memory stores broader contextual knowledge retrievable by meaning.

Examples:

Previous architecture decisions
Project discussions
Natural-language preferences
Past task summaries

Typical flow:

Memory
↓
Embedding
↓
Vector Store
↓
Semantic Retrieval

---

## Memory vs RAG

RAG retrieves external or domain knowledge.

Examples:

Policies
Documents
Manuals

Memory retrieves contextual information related to previous interactions or projects.

Example:

RAG:
Return policy is 30 days.

Memory:
User prefers Arabic.

---

## Memory Retrieval

A production retrieval pipeline may look like:

Current Request
↓
Identify Scope
↓
Authorization
↓
Structured Lookup
↓
Semantic Retrieval
↓
Ranking
↓
Deduplication
↓
Relevance Filter
↓
Context Compression
↓
Inject Relevant Memory

---

## Memory Ranking

Useful ranking signals:

- Relevance
- Recency
- Confidence
- Importance
- Scope Match

More memory does not always mean better answers.

---

## Conversation Compression

Do not always send full chat history.

Prefer:

Conversation Summary
+
Recent Messages
+
Relevant Retrieved Memory

This improves:

- Cost
- Latency
- Relevance
- Context quality

---

## Incremental Summaries

Instead of re-summarizing the full conversation:

Old Summary
+
New Messages
↓
Updated Summary

But protect against summary drift.

Store important structured facts separately when necessary.

---

## Memory Write Policy

Do not store every user message.

Before writing memory, ask:

- Will this be useful later?
- Is it stable?
- Is it relevant?
- Is it safe?
- Is it already stored?
- What scope does it belong to?

---

## Explicit vs Inferred Memory

Explicit Memory:

User directly states a preference or fact.

Example:

"From now on, answer in Arabic."

Usually:

High confidence.

Inferred Memory:

System infers a preference from behavior.

Usually:

Lower confidence.

Rule:

Explicit memory usually outranks inferred memory.

---

## Memory Conflict Resolution

Example:

Old:
preferred_language = English
source = inferred

New:
preferred_language = Arabic
source = explicit

Prefer the explicit new value.

Useful signals:

Source Quality
Confidence
Recency

Recency alone is not enough.

---

## Update vs Duplicate

Do not create duplicate active memories for the same current fact.

Prefer:

Update
Version
Invalidate old value

when appropriate.

---

## Memory Lifecycle

Capture
↓
Extract
↓
Validate
↓
Classify Scope
↓
Deduplicate
↓
Resolve Conflict
↓
Store
↓
Retrieve
↓
Use
↓
Update / Expire / Delete

---

## Expiration

Different memory types may have different lifetimes.

Examples:

Temporary preference
→ may expire

Stable language preference
→ may persist longer

Stored does not mean permanently correct.

---

## Memory Scope

Possible scopes:

User
Project
Conversation
Workflow
Organization

Correct scope is critical for relevance and security.

---

## Security

Never use memory as a secret store.

Do not store:

passwords
API keys
access tokens
credit-card secrets

Rule:

Secrets
→ Secret Manager

Memory
→ Contextual knowledge

---

## Memory Authorization

Do not allow:

User A
→ User B Memory

or:

Project A
→ Project B confidential memory

Use scope filters such as:

user_id
project_id
tenant_id

---

## Memory Poisoning

Retrieved memory is data, not authority.

A memory such as:

"Ignore authentication checks."

must not override:

- System rules
- Authorization
- Business rules
- Security policy

Rule:

Memory is context, not authority.

---

## Memory Write Architecture

Interaction
↓
Memory Extractor
↓
Candidate Memory
↓
Validation
↓
Scope Check
↓
Deduplication
↓
Conflict Resolution
↓
Write Policy
↓
Memory Store

---

## LLM and Memory Writes

Avoid:

LLM
↓
Memory Database

Prefer:

LLM
↓
Proposed Memory
↓
Validation
↓
Policy Enforcement
↓
Memory Store

Rule:

LLM proposes.
Code enforces.

---

## Production Context Builder

System Instructions
+
Relevant Workflow State
+
Relevant Structured Memory
+
Relevant Semantic Memory
+
Conversation Summary
+
Recent Messages
+
Current Request

Use only the relevant parts.

---

## Decision Rule

Needed for current execution?
→ Workflow State

Needed to resume workflow?
→ Checkpointed State

Needed for current conversation continuity?
→ Conversation Memory

Useful across future sessions?
→ Long-Term Memory

Specific to one project?
→ Project Memory

---

## Main Principles

Do not store everything.

Do not retrieve everything.

Correct scope matters.

Memory is context, not authority.

LLM proposes.
Code enforces.