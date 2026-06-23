from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_documents(data_dir: Path):
    documents = []

    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    supported_files = list(data_dir.glob("*.txt")) + list(data_dir.glob("*.pdf"))

    if not supported_files:
        raise FileNotFoundError(
            "No .txt or .pdf files found in data/. Add telecom documents first."
        )

    for file_path in supported_files:
        if file_path.suffix.lower() == ".txt":
            loader = TextLoader(str(file_path), encoding="utf-8")
            documents.extend(loader.load())

        elif file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))
            documents.extend(loader.load())

    return documents
