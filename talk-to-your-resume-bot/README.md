# Talk to Your Resume Bot (OpenRouter + DeepSeek)

A hands-on project to learn Python, LangChain, and LLM integration by building a chatbot that answers questions about your resume using the free DeepSeek model via OpenRouter.

## 🚀 What You Learn
- **Python basics**: File I/O, environment variables, and functions
- **LangChain**: PromptTemplate, chaining, and LLM integration
- **OpenRouter**: Using free and open LLMs (DeepSeek)
- **Streamlit**: Building a simple web UI for your AI app
- **.env management**: Securely storing API keys
- **Debugging**: Handling dependency and compatibility issues

## 🛠️ How We Did It
1. **Project Setup**
   - Created a Python project with a clear folder structure
   - Added `.gitignore` and `.env` for security and privacy
2. **Resume Input**
   - Used a plain text file (`resume.txt`) for your resume
3. **LangChain Integration**
   - Used `PromptTemplate` to format questions and context
   - Chained the prompt with the LLM for dynamic answers
4. **OpenRouter LLM**
   - Switched from OpenAI to OpenRouter for free LLM access
   - Used the DeepSeek model: `deepseek/deepseek-chat-v3-0324:free`
5. **Streamlit UI**
   - Built a web interface for easy interaction
   - Input questions and display answers in real time
6. **Environment & Dependencies**
   - Managed dependencies in `requirements.txt`
   - Fixed compatibility issues (e.g., Pydantic version)
   - Loaded API keys from `.env` using `python-dotenv`

## 📝 How to Run
1. Add your `OPENROUTER_API_KEY` to `.env`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   streamlit run main.py
   ```
4. Ask questions about your resume in the browser!

## 💡 Next Steps
- Try with your own resume
- Experiment with different LLMs or prompts
- Add file upload or chat history features

---

**Learning by building is the best way to master AI!**
