# Day 22 Notes — Security

## Core Rule

LLM is not a security boundary.

## Prompt Injection

Retrieved content is untrusted data.

Do not let documents become instructions.

## Authorization

Authentication
→ Who are you?

Authorization
→ What can you do?

Object-Level Authorization
→ Can you do it to this resource?

## Least Privilege

Minimum permissions only.

## Secure RAG

Filter by tenant / ACL before retrieval.

## Secure Memory

Use strict user / project / organization scope.

## Secrets

Use Secret Manager.

Never store secrets in prompts, logs, GitHub, memory, or vector databases.

## Service Security

Use service identity.

Use scoped and short-lived credentials.

## Final Rules

Default Deny.

Fail Closed.

Defense in Depth.

LLM proposes.

Trusted code decides.