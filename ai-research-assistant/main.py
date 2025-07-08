import streamlit as st
from langchain_openrouter.openrouter import OpenRouterLLM
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

st.title("AI Research Assistant")
st.write("Ask a research question and get summarized, referenced answers!")

# LLM setup
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
llm = OpenRouterLLM(
    model="deepseek/deepseek-chat-v3-0324:free",
    api_key=openrouter_api_key
)

# Search tool (DuckDuckGo, no API key needed)
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Useful for answering questions about current events or general knowledge."
    )
]

# Agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True
)

question = st.text_input("Ask your research question:")

# Add QA feedback
feedback = None

if question:
    with st.spinner("Researching..."):
        try:
            answer = agent.run(question)
        except Exception as e:
            st.error(f"Agent failed to answer due to output parsing error. Try rephrasing your question.\nError: {e}")
            answer = None
    if answer:
        st.markdown(f"**Answer:** {answer}")
        feedback = st.radio(
            "Was this answer helpful?",
            ("👍 Yes, perfect!", "👎 No, needs improvement."),
            index=None
        )
        if feedback:
            st.success(f"Thank you for your feedback: {feedback}")
            if feedback == "👎 No, needs improvement.":
                st.info("Trying to improve the answer...")
                with st.spinner("Researching again..."):
                    try:
                        improved_answer = agent.run(question)
                        st.markdown(f"**Improved Answer:** {improved_answer}")
                    except Exception as e:
                        st.error(f"Still unable to answer. Error: {e}")
