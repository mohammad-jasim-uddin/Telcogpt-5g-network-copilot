import streamlit as st

from rag_pipeline import ask_telcogpt
from src.utils import format_sources

st.set_page_config(
    page_title="TelcoGPT - 5G Network Operations Copilot",
    page_icon="📡",
    layout="wide",
)

st.title("📡 TelcoGPT – 5G Network Operations Copilot")
st.caption("Hugging Face + LangChain + FAISS + Streamlit portfolio project")

with st.sidebar:
    st.header("About TelcoGPT")
    st.write(
        "TelcoGPT is a RAG assistant for LTE/5G network operations. "
        "It retrieves telecom knowledge from documents and generates practical troubleshooting answers."
    )

    st.subheader("Example Questions")
    st.markdown(
        '''
        - What causes RRC connection failure?
        - How do I troubleshoot high packet loss?
        - What is the eNodeB reset procedure?
        - Why does handover failure happen?
        - Generate an incident summary for a 5G site outage.
        '''
    )

    st.subheader("Workflow")
    st.write("1. Add documents to data/")
    st.write("2. Run python ingest.py")
    st.write("3. Run streamlit run app.py")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_area(
    "Ask a telecom network operations question:",
    placeholder="Example: What causes RRC connection failure?",
    height=100,
)

col1, col2 = st.columns([1, 5])

with col1:
    ask_button = st.button("Ask TelcoGPT", type="primary")

with col2:
    clear_button = st.button("Clear Chat")

if clear_button:
    st.session_state.chat_history = []
    st.rerun()

if ask_button:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching telecom knowledge base and generating answer..."):
            try:
                response = ask_telcogpt(question)
                answer = response.get("result", "")
                sources = response.get("source_documents", [])

                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": answer,
                        "sources": sources,
                    }
                )

            except Exception as exc:
                st.error(str(exc))

for item in reversed(st.session_state.chat_history):
    st.divider()
    st.subheader("Question")
    st.write(item["question"])

    st.subheader("TelcoGPT Answer")
    st.write(item["answer"])

    with st.expander("Retrieved Sources"):
        for label, content in format_sources(item["sources"]):
            st.markdown(f"**{label}**")
            st.write(content[:1200])
            st.divider()
