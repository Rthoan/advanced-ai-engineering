# Day 22 — Security

## Goal

Build secure AI systems using trusted authorization, least privilege, secure data handling, and defense in depth.

## Core Principle

LLM output is an untrusted proposal.

Trusted code decides.

## Threat Modeling

Identify:

- Assets
- Attack Surface
- Threat Actors
- Trust Boundaries
- Impact

Protect:

- User Data
- Secrets
- Private Documents
- Tools
- Payments
- Memory
- System Configuration

## Prompt Injection

Direct Prompt Injection comes from user input.

Indirect Prompt Injection comes from retrieved or external content.

Retrieved content must be treated as untrusted data.

Prompt-only security is not enough.

Use:

- Authorization
- Tool Restrictions
- Input Validation
- Allow Lists
- Business Rules
- Human Approval for high-risk actions

## Least Privilege

Give each user, service, and agent only the permissions required for its task.

Reduce tool exposure.

## Data Security

Use:

- Data Minimization
- Redaction
- Masking
- Encryption
- Retention Policies
- Deletion Policies

Never log or store secrets unnecessarily.

## Secret Management

Secrets include:

- API Keys
- Database Passwords
- Access Tokens
- Signing Keys

Store secrets in:

- Secret Managers
- Secure Environment Variables
- Vaults
- Cloud Secret Services

Do not store secrets in:

- Source Code
- GitHub
- Logs
- Prompts
- Memory
- Vector Databases

## Secure RAG

Apply authorization before retrieval.

Flow:

Authenticated User
→ Determine Access Scope
→ Apply ACL / Tenant Filter
→ Retrieve Authorized Documents
→ Rerank
→ Build Context
→ LLM

Prevent unauthorized retrieval before generation.

## Secure Memory

Memory must have explicit scope:

- User
- Conversation
- Project
- Organization
- Workflow

Never allow cross-user memory leakage.

## Authentication

Authentication answers:

Who are you?

## Authorization

Authorization answers:

What are you allowed to do?

## Object-Level Authorization

Object-level authorization answers:

Can you perform this action on this specific resource?

## RBAC and ABAC

RBAC uses roles.

ABAC uses attributes such as:

- Role
- Department
- Resource Owner
- Risk Level
- Amount

## Service Identity

Services must authenticate to other services.

Do not automatically trust internal network traffic.

Prefer:

- Short-lived credentials
- Workload identity
- Scoped tokens
- mTLS where appropriate

## Default Deny

If access is not explicitly allowed, deny it.

## Fail Closed

If sensitive authorization cannot be verified, do not execute the action.

## Defense in Depth

Use multiple independent security controls:

Prompt Guardrails
→ Authorization
→ Tool Validation
→ Business Rules
→ Audit

## Main Principles

LLM proposes.

Trusted code decides.

Relevant data must also be authorized and necessary.

Secrets belong in Secret Management, not AI Memory.

Prevent unauthorized retrieval before generation.

Use least privilege everywhere.