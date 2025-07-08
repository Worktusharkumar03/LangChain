import streamlit as st
from langchain_openrouter.openrouter import OpenRouterLLM
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# Load environment variables from .env
load_dotenv()

st.title("Chat with Any PDF (RAG)")
st.write("Upload a PDF and ask questions about its content!")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Extract text from PDF
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    # Chunk text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    # Embeddings (HuggingFace, free)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embeddings)
    retriever = vectorstore.as_retriever()
    # LLM
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    llm = OpenRouterLLM(
        model="deepseek/deepseek-chat-v3-0324:free",
        api_key=openrouter_api_key
    )
    # RetrievalQA chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )
    question = st.text_input("Ask a question about the PDF:")
    if question:
        answer = qa.run(question)
        st.markdown(f"**Answer:** {answer}")
else:
    st.info("Please upload a PDF to begin.")
