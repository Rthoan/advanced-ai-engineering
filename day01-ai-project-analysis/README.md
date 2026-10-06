# Day 01 — AI Project Analysis

## Goal

Learn how to analyze an AI project before writing code.

The main workflow is:

Problem
↓
Requirements
↓
Constraints
↓
Architecture
↓
Data Flow
↓
Technology Selection
↓
Implementation
↓
Testing
↓
Evaluation

---

## LLM vs RAG vs Agent

### LLM

Use an LLM when the task only requires generation, reasoning, summarization, or transformation.

Examples:

- Generate marketing content
- Summarize text
- Rewrite text

Architecture:

User
↓
LLM
↓
Answer

---

### RAG

Use RAG when the answer depends on private or external documents.

Examples:

- Company documents
- University regulations
- Product documentation

Architecture:

Question
↓
Retrieval
↓
Relevant Context
↓
LLM
↓
Answer

---

### Agent

Use an Agent when the system must choose or execute tools.

Examples:

- Check order status
- Book an appointment
- Send an email
- Query a database

Architecture:

User
↓
Agent
↓
Tool
↓
Result

---

### RAG + Agent

Use both when the system needs private knowledge and external actions.

Example:

Can I return order #5821?

The system may need:

Order Tool
+
RAG
+
LLM

---

## Requirements vs Constraints

### Requirements

Describe what the system must do.

Example:

- Answer product questions
- Answer shipping questions
- Answer return-policy questions
- Check order status

### Constraints

Describe limitations or conditions.

Example:

- Protect customer data
- Support many users
- Reduce LLM cost
- Keep private data secure

---

## Engineering Rule

Always think:

Requirement
↓
Capability
↓
Component
↓
Technology

Do not choose technologies before understanding the requirement.

Example:

Need to answer from documents
↓
Knowledge Retrieval
↓
RAG Component
↓
FAISS / Vector DB

---

## Ingestion Pipeline

Documents
↓
Document Parsing
↓
Text Cleaning
↓
Chunking
↓
Embeddings
↓
Vector Store

---

## Query Pipeline

User Question
↓
API
↓
Validation
↓
Agent
↓
Tool Selection
↓
LLM
↓
Answer

---

## Main Lesson

Do not start an AI project by asking:

"What library should I use?"

Start by asking:

"What problem am I solving?"