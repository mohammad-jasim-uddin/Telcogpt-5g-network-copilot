from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

from config import (
    VECTOR_DIR,
    EMBEDDING_MODEL,
    LOCAL_LLM_MODEL,
    HF_ENDPOINT_MODEL,
    TELCOGPT_LLM_MODE,
    HF_TOKEN,
)
from src.prompts import TELCOGPT_SYSTEM_PROMPT

PROMPT_TEMPLATE = """
{system_prompt}

Retrieved telecom context:
{context}

Question:
{question}

Answer:
"""

def _build_prompt():
    return PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"],
        partial_variables={"system_prompt": TELCOGPT_SYSTEM_PROMPT},
    )

def _load_local_llm():
    tokenizer = AutoTokenizer.from_pretrained(LOCAL_LLM_MODEL)
    model = AutoModelForSeq2SeqLM.from_pretrained(LOCAL_LLM_MODEL)

    text_generation_pipeline = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.2,
        do_sample=False,
    )

    return HuggingFacePipeline(pipeline=text_generation_pipeline)

def _load_endpoint_llm():
    if not HF_TOKEN:
        raise ValueError(
            "HUGGINGFACEHUB_API_TOKEN is missing. Add it to your .env file or use TELCOGPT_LLM_MODE=local."
        )

    return HuggingFaceEndpoint(
        repo_id=HF_ENDPOINT_MODEL,
        temperature=0.2,
        max_new_tokens=512,
        huggingfacehub_api_token=HF_TOKEN,
    )

def load_rag_chain():
    index_file = Path(VECTOR_DIR) / "index.faiss"

    if not index_file.exists():
        raise FileNotFoundError(
            "Vector database not found. Run this first: python ingest.py"
        )

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    db = FAISS.load_local(
        str(VECTOR_DIR),
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retriever = db.as_retriever(search_kwargs={"k": 4})

    if TELCOGPT_LLM_MODE == "endpoint":
        llm = _load_endpoint_llm()
    else:
        llm = _load_local_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": _build_prompt()},
        return_source_documents=True,
    )

    return qa_chain

def ask_telcogpt(question: str):
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    chain = load_rag_chain()
    return chain.invoke({"query": question})
