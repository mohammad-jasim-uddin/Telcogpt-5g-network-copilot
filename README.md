# TelcoGPT – 5G Network Operations Copilot

TelcoGPT is a portfolio-ready AI project for telecom network operations.  
It uses Hugging Face embeddings, FAISS vector search, LangChain, and Streamlit to answer LTE/5G troubleshooting questions from telecom documents.

## Why This Project Is Strong

This project connects directly with:

- MSc in Mobile & Personal Communications
- BSc in Computer Science & Engineering
- Generative AI / Hugging Face skills
- Telecom / Network Operations domain knowledge
- AI Engineer, GenAI Engineer, Data/AI and MLOps job applications

## Features

- Telecom-focused RAG assistant
- Hugging Face sentence-transformer embeddings
- FAISS vector database
- Streamlit chatbot interface
- Source-grounded answers
- Supports `.txt` and `.pdf` files
- Includes sample LTE/5G knowledge base
- Local fallback LLM mode
- Hugging Face endpoint mode
- Clean GitHub-ready structure

## Architecture

```text
Telecom Documents
        |
        v
Document Loader
        |
        v
Text Chunking
        |
        v
Hugging Face Embeddings
        |
        v
FAISS Vector Database
        |
        v
Retriever
        |
        v
LLM Answer Generator
        |
        v
Streamlit Chatbot
```

## Folder Structure

```text
telcogpt-5g-network-copilot/
│
├── app.py
├── ingest.py
├── rag_pipeline.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
│
├── data/
│   └── sample_telecom_knowledge.txt
│
├── vectorstore/
├── screenshots/
├── src/
│   ├── document_loader.py
│   ├── prompts.py
│   └── utils.py
│
└── tests/
    └── test_project_structure.py
```

## Installation

```bash
cd telcogpt-5g-network-copilot

python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Copy `.env.example` to `.env`.

Windows:

```bash
copy .env.example .env
```

Mac/Linux:

```bash
cp .env.example .env
```

Default mode is local:

```env
TELCOGPT_LLM_MODE=local
```

For Hugging Face endpoint mode:

```env
TELCOGPT_LLM_MODE=endpoint
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

## Build Vector Database

```bash
python ingest.py
```

## Run the App

```bash
streamlit run app.py
```

## Example Questions

```text
What causes RRC connection failure?
How do I troubleshoot high packet loss in an LTE site?
What is the eNodeB reset procedure?
Why does handover failure happen?
Generate an incident summary for a 5G site outage.
```

## Add Your Own Telecom Documents

Put your telecom `.txt` or `.pdf` files inside the `data/` folder, then rebuild the vector database:

```bash
python ingest.py
```

## Portfolio CV Description

**TelcoGPT – 5G Network Operations Copilot**  
Built a Hugging Face-powered Retrieval-Augmented Generation chatbot for telecom network operations. The system uses sentence-transformer embeddings, FAISS vector search, LangChain, and an LLM pipeline to answer LTE/5G troubleshooting questions from technical documents. Demonstrated practical skills in Generative AI, Hugging Face, RAG, vector databases, prompt engineering, Python, Streamlit, and telecom domain problem-solving.

## LinkedIn Post

```text
I built TelcoGPT – a 5G Network Operations Copilot using Hugging Face, LangChain, FAISS, and Streamlit.

The project helps telecom engineers:
- Explain LTE/5G alarms
- Troubleshoot RRC connection failures
- Analyse packet loss issues
- Search telecom documents using RAG
- Generate incident support answers

This project combines my MSc in Mobile & Personal Communications with modern Generative AI engineering.

Tech Stack:
Python | Hugging Face | LangChain | FAISS | Streamlit | RAG | LLMs

#GenerativeAI #HuggingFace #Telecom #RAG #LangChain #AIEngineer #MLOps
```

## Notes

The first run may take time because Hugging Face models are downloaded locally.
For low-resource computers, endpoint mode is recommended.
