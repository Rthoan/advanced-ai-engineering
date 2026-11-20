import re
from dataclasses import dataclass

from app.rag.loader import DocumentChunk


STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "this",
    "to",
    "what",
    "when",
    "where",
    "which",
    "who",
    "with",
    "you",
    "your",
    "policy",
    "policies",
    "do",
    "does",
    "did",
    "done",
    "have",
    "has",
    "had",
    "can",
    "could",
    "should",
    "would",
    "will",
}


@dataclass
class RetrievalResult:
    chunk: DocumentChunk
    score: int


def tokenize(text: str) -> set[str]:
    tokens = set(re.findall(r"\b\w+\b", text.lower()))

    return {
        token
        for token in tokens
        if token not in STOP_WORDS
        and len(token) > 1
    }


def score_chunk(query: str, chunk: DocumentChunk) -> int:
    query_tokens = tokenize(query)

    chunk_tokens = tokenize(
        f"{chunk.title} {chunk.section} {chunk.content}"
    )

    return len(query_tokens & chunk_tokens)


def retrieve_chunks(
    query: str,
    chunks: list[DocumentChunk],
    top_k: int = 3,
    min_score: int = 1,
) -> list[RetrievalResult]:
    scored = [
        RetrievalResult(
            chunk=chunk,
            score=score_chunk(query, chunk),
        )
        for chunk in chunks
    ]

    scored = [
        result
        for result in scored
        if result.score >= min_score
    ]

    scored.sort(
        key=lambda result: result.score,
        reverse=True,
    )

    seen_chunk_ids: set[str] = set()
    deduplicated: list[RetrievalResult] = []

    for result in scored:
        if result.chunk.chunk_id in seen_chunk_ids:
            continue

        seen_chunk_ids.add(result.chunk.chunk_id)
        deduplicated.append(result)

    return deduplicated[:top_k]
