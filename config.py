from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
VECTOR_DIR = BASE_DIR / "vectorstore"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Local model is small enough for demos. You can change this to a stronger model if your computer supports it.
LOCAL_LLM_MODEL = "google/flan-t5-base"

# Endpoint model for Hugging Face hosted inference.
HF_ENDPOINT_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

TELCOGPT_LLM_MODE = os.getenv("TELCOGPT_LLM_MODE", "local").lower()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")
