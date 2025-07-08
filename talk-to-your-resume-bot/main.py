import streamlit as st
from langchain_openrouter.openrouter import OpenRouterLLM
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from pypdf import PdfReader

# Load environment variables from .env
load_dotenv()

# PDF or resume.txt loader
resume_text = ""

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        # Read PDF
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text() or ""
    else:
        # Read TXT
        resume_text = uploaded_file.read().decode("utf-8")
else:
    # Fallback to local resume.txt
    if os.path.exists("resume.txt"):
        with open("resume.txt", "r") as file:
            resume_text = file.read()

# 2. Set up the LLM (OpenRouter with DeepSeek model)
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
llm = OpenRouterLLM(
    model="deepseek/deepseek-chat-v3-0324:free",
    api_key=openrouter_api_key
)

# 3. Create a prompt template
prompt = PromptTemplate(
    input_variables=["question", "resume"],
    template="""
You are an expert career assistant. Given the following resume:

{resume}

Answer the user's question: {question}
"""
)

# Streamlit UI
st.title("Talk to Your Resume Bot (OpenRouter)")
st.write("Ask any question about your resume!")

if not resume_text:
    st.warning("Please upload a PDF or TXT resume, or ensure resume.txt exists.")
else:
    question = st.text_input("Your question:")
    if question:
        chain = prompt | llm
        response = chain.invoke({"question": question, "resume": resume_text})
        st.markdown(f"**AI:** {response}")
