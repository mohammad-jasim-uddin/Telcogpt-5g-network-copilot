from pathlib import Path

def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def format_sources(source_documents):
    formatted = []
    for i, doc in enumerate(source_documents, start=1):
        source = doc.metadata.get("source", "Unknown source")
        page = doc.metadata.get("page", None)
        label = f"Source {i}: {source}"
        if page is not None:
            label += f", page {page + 1}"
        formatted.append((label, doc.page_content))
    return formatted
