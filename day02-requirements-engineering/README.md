# Day 02 — Requirements Engineering

## Goal

Learn how to convert a vague client idea into clear, testable, and prioritized project requirements.

The workflow is:

Client Request
↓
Clarification Questions
↓
Business Goal
↓
Users
↓
Functional Requirements
↓
Non-Functional Requirements
↓
Constraints
↓
Data Sources
↓
User Stories
↓
Business Rules
↓
Acceptance Criteria
↓
Out of Scope
↓
Priorities

---

## Business Goal

The business goal explains why the project exists.

Example:

Reduce customer-support workload and help customers get answers faster.

---

## Functional Requirements

Functional requirements describe what the system must do.

Examples:

FR-01: The system shall answer customer questions using approved store data.

FR-02: The system shall display order status.

FR-03: The system shall allow customers to submit return requests.

FR-04: The system shall escalate to human support when it cannot answer.

---

## Non-Functional Requirements

Non-functional requirements describe how well the system should operate.

Examples:

NFR-01: Normal responses should be returned within a few seconds.

NFR-02: The system should support more than 1000 users.

NFR-03: Customer data must remain private.

NFR-04: The system should have high availability.

---

## Constraints

Constraints limit how the solution can be built.

Examples:

C-01: Answers must use approved store data only.

C-02: Customers must not access another customer's private data.

---

## Data Sources

Possible data sources:

- Product catalog
- Order database
- Shipping API
- Return policy documents
- Customer authentication system

---

## Clarification Questions

Before designing the system, ask:

1. Who will use the system?
2. Where does the data come from?
3. How are users authenticated?
4. What actions can the system perform?
5. What happens when the system cannot answer?
6. How many users are expected?
7. Which languages must be supported?
8. Will the system use a cloud LLM or local model?

Rule:

Never assume.
Ask first.

---

## User Stories

Format:

As a [user],
I want [goal],
so that [benefit].

Example:

As a customer,
I want to check my order status,
so that I know when my order will arrive.

---

## Business Rules

Business rules define the rules that control a feature.

Example:

BR-01: A return request can only be submitted within 14 days of delivery.

---

## Acceptance Criteria

Acceptance criteria explain how we verify that a requirement works correctly.

Example:

AC-01: The customer must be authenticated.

AC-02: The order must belong to the authenticated customer.

AC-03: The system must display the current order status.

AC-04: If no data is found, the system must return a clear message.

---

## Requirement vs Business Rule vs Acceptance Criterion

What?
→ Requirement

Under what rule?
→ Business Rule

How do we verify it?
→ Acceptance Criterion

---

## Traceability

A good project should allow us to trace:

Requirement
↓
Acceptance Criteria
↓
Implementation
↓
Test

Example:

FR-03
↓
AC-01, AC-02
↓
return_service.py
↓
test_return_service.py

---

## MoSCoW Prioritization

### Must Have
Required for the MVP.

### Should Have
Important but can be delayed.

### Could Have
Useful improvement.

### Won't Have for now
Outside the current release.

Example:

Must Have:
- Order status
- Return requests
- Data privacy

Should Have:
- Human support escalation
- Source citations

Could Have:
- Voice input
- Customer satisfaction rating

Won't Have for now:
- Payment processing
- Automatic refunds

---

## Main Lesson

Do not start with technology.

Start with:

Who?
What?
Why?
How well?
Under what rules?
How do we verify success?