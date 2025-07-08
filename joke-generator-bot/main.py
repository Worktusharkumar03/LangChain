import streamlit as st
from langchain_openrouter.openrouter import OpenRouterLLM
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Streamlit UI
st.title("Joke Generator Bot")
st.write("Pick a persona/job and get a custom joke!")

personas = ["Doctor", "Engineer", "HR", "Coder", "Mom", "Dad", "Teacher", "Chef", "Student", "Other"]
persona = st.selectbox("Choose a persona/job:", personas)
custom_persona = ""
if persona == "Other":
    custom_persona = st.text_input("Enter your custom persona/job:")
    persona = custom_persona if custom_persona else "Someone"

# LLM setup
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
llm = OpenRouterLLM(
    model="deepseek/deepseek-chat-v3-0324:free",
    api_key=openrouter_api_key
)

prompt = PromptTemplate(
    input_variables=["persona"],
    template="""
You are a professional comedian. Tell a joke as if you are a {persona}. Make it funny and relevant to the persona.
first setup the job second premise then the punchline.
"""
)

if persona:
    chain = prompt | llm
    response = chain.invoke({"persona": persona})
    st.markdown(f"**Joke:** {response}")
