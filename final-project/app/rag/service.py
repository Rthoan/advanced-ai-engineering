from app.models.schemas import Citation
from app.rag.loader import load_markdown_documents
from app.rag.retriever import retrieve_chunks


class RAGResult:
    def __init__(
        self,
        answer: str,
        citations: list[Citation],
    ):
        self.answer = answer
        self.citations = citations


class RAGService:
    def __init__(
        self,
        policy_directory: str = "data/policies",
    ):
        self.chunks = load_markdown_documents(policy_directory)

    def answer(
        self,
        query: str,
        top_k: int = 3,
    ) -> RAGResult:
        results = retrieve_chunks(
            query=query,
            chunks=self.chunks,
            top_k=top_k,
            min_score=1,
        )

        if not results:
            return RAGResult(
                answer=(
                    "I could not find enough trusted information "
                    "in the knowledge base to answer this question."
                ),
                citations=[],
            )

        context = "\n\n".join(
            result.chunk.content
            for result in results
        )

        citations = [
            Citation(
                document_id=result.chunk.document_id,
                section=result.chunk.section,
            )
            for result in results
        ]

        return RAGResult(
            answer=context,
            citations=citations,
        )
