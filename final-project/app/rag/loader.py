from dataclasses import dataclass
from pathlib import Path


@dataclass
class DocumentChunk:
    chunk_id: str
    document_id: str
    title: str
    section: str
    content: str
    source: str


def load_markdown_documents(directory: str) -> list[DocumentChunk]:
    base_path = Path(directory)
    chunks: list[DocumentChunk] = []

    for file_path in sorted(base_path.glob("*.md")):
        text = file_path.read_text(encoding="utf-8")

        document_id = file_path.stem
        title = document_id.replace("_", " ").title()

        current_section = "general"
        current_lines: list[str] = []
        section_index = 0

        def flush_chunk():
            nonlocal section_index, current_lines

            content = "\n".join(current_lines).strip()

            if not content:
                return

            section_index += 1

            chunks.append(
                DocumentChunk(
                    chunk_id=f"{document_id}-{section_index}",
                    document_id=document_id,
                    title=title,
                    section=current_section,
                    content=content,
                    source=str(file_path),
                )
            )

            current_lines = []

        for line in text.splitlines():
            stripped = line.strip()

            if stripped.startswith("## "):
                flush_chunk()
                current_section = stripped[3:].strip()
                continue

            if stripped.startswith("# "):
                continue

            current_lines.append(line)

        flush_chunk()

    return chunks
