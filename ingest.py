from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from config import DATA_DIR, VECTOR_DIR, EMBEDDING_MODEL
from src.document_loader import load_documents
from src.utils import ensure_directory

def create_vectorstore():
    print("Loading telecom documents...")
    documents = load_documents(DATA_DIR)

    print(f"Loaded {len(documents)} document pages/files.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} text chunks.")

    print("Loading Hugging Face embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    ensure_directory(VECTOR_DIR)

    print("Creating FAISS vector database...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(str(VECTOR_DIR))

    print("Vector database created successfully.")
    print(f"Saved to: {VECTOR_DIR}")

if __name__ == "__main__":
    create_vectorstore()
