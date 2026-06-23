from pathlib import Path

def test_required_files_exist():
    root = Path(__file__).resolve().parents[1]

    required_files = [
        "app.py",
        "ingest.py",
        "rag_pipeline.py",
        "config.py",
        "requirements.txt",
        "README.md",
        "data/sample_telecom_knowledge.txt",
    ]

    for file in required_files:
        assert (root / file).exists(), f"Missing required file: {file}"
