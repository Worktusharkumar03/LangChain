# Chat with Any PDF

A LangChain project where you can upload any PDF (e.g., contract, research paper, resume) and chat with it using Retrieval-Augmented Generation (RAG), embeddings, and a vector store.

## 🚀 What You Learn
- How to load and chunk PDF documents in Python
- How to create and use embeddings for semantic search
- How to build a vector store for fast retrieval
- How to use RetrievalQA (RAG) with LangChain and OpenRouter LLMs
- How to build a Streamlit UI for document Q&A

## 🛠️ What We Do
1. Upload a PDF file
2. Extract and chunk the text
3. Create embeddings for each chunk
4. Store embeddings in a vector store
5. User asks questions; relevant chunks are retrieved and sent to the LLM
6. LLM answers based on the PDF content

## 📝 How to Run
1. Add your `OPENROUTER_API_KEY` to `.env`
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   streamlit run main.py
   ```
4. Upload a PDF and start chatting!

---

**Learn RAG, embeddings, and vector search by chatting with your own documents!**
