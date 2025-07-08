import streamlit as st
from langchain_openrouter.openrouter import OpenRouterLLM
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Streamlit UI
st.title("AI Chef Bot")
st.write("Enter your available ingredients and get a creative recipe!")

ingredients = st.text_area("List your available ingredients (comma separated):")

# LLM setup
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
llm = OpenRouterLLM(
    model="deepseek/deepseek-chat-v3-0324:free",
    api_key=openrouter_api_key
)

prompt = PromptTemplate(
    input_variables=["ingredients"],
    template="""
You are a world-class chef. Given these ingredients: {ingredients}, create a delicious, creative recipe. Include a name, ingredients list, and step-by-step instructions.
"""
)

if ingredients:
    chain = prompt | llm
    response = chain.invoke({"ingredients": ingredients})
    st.markdown(f"**Recipe:**\n{response}")
