# Day 03 — LLM vs RAG vs Agent

## Goal

Learn how to choose the simplest and most appropriate AI architecture for each project requirement.

The main rule is:

Requirement
↓
Need
↓
System Type
↓
Technology

---

## LLM

Use an LLM when the task is mainly:

- Text generation
- Summarization
- Translation
- Classification
- Text analysis
- Rewriting

Example:

User
↓
LLM
↓
Answer

---

## RAG

Use RAG when the answer depends on private or external knowledge.

Examples:

- Company documents
- University regulations
- Product manuals
- Internal policies
- Legal documents

Architecture:

Question
↓
Embedding
↓
Vector Search
↓
Relevant Chunks
↓
LLM
↓
Answer

---

## Tool

Use a Tool when the system needs to read structured data or perform an action.

Examples:

- Query a database
- Read order status
- Book an appointment
- Send an email
- Call an API

Example:

Order ID
↓
Order API
↓
Database
↓
Result

---

## Agent

Use an Agent when the system must decide which tool or path to use.

Example:

User
↓
Agent
├── RAG Tool
├── Order Tool
└── Support Tool

The Agent is useful when the system must make a decision.

---

## RAG + Agent

Use RAG + Agent when the system needs both:

- Private knowledge
- External actions or tools

Example:

"Can I return order #5821?"

The system may need:

1. Order Tool
2. RAG Tool
3. LLM
4. Return Tool

---

## Workflow

Use a normal workflow when the sequence is fixed.

Example:

Create Booking
↓
Booking Success
↓
Send Email
↓
Done

No Agent is required because the path is already known.

---

## LangGraph

Use LangGraph when the workflow has:

- Multiple steps
- State
- Branches
- Retries
- Loops
- Human approval

Example:

Start
↓
Check Order
↓
Eligible?
├── No → Explain
└── Yes
     ↓
Create Return
     ↓
Need Approval?
├── Yes → Human Review
└── No → Complete

---

## Decision Framework

Ask these questions in order:

1. Is this generation or text analysis?
   → LLM

2. Does it need private knowledge?
   → RAG

3. Does it need structured data or an external action?
   → Tool

4. Does the system need to choose between tools?
   → Agent

5. Is the sequence fixed?
   → Workflow

6. Does the workflow have state, retries, or branches?
   → LangGraph

---

## Avoid Overengineering

Do not use an Agent just because tools exist.

Do not use LangGraph for a simple fixed workflow.

Do not use RAG when a direct database query is enough.

Use the simplest architecture that satisfies the requirements.

Complexity increases:

- Cost
- Latency
- Debugging difficulty
- Testing difficulty
- Failure points

---

## Examples

### Example 1

Translate text:

LLM

### Example 2

Answer from 20,000 documents:

RAG

### Example 3

Get order status:

Tool

### Example 4

Choose between document search and order API:

Agent

### Example 5

Always send email after booking:

Workflow

### Example 6

Approval + retry + state:

LangGraph

---

## Main Lesson

Knowledge problem
→ RAG

Action problem
→ Tool

Decision problem
→ Agent

Fixed process
→ Workflow

Complex stateful process
→ LangGraph

Generation problem
→ LLM