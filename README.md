# rag-first
hackathon rag app

# 🍕 Pizza Review RAG Demo

This is a simple Retrieval-Augmented Generation (RAG) demo using LangChain + Ollama locally.

## 🚀 Setup

### 1. Install Requirements
```bash
pip install langchain langchain-core langchain-community pandas
```

### 2. Install Ollama
Go to [https://ollama.com](https://ollama.com) and install it.

### 3. Pull the Models
```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

### 4. Add Data
Place your `realistic_restaurant_reviews.csv` file into a `./data/` folder.

### 5. Run the App
```bash
python main.py
```

## 💡 What This Does
- Embeds pizza reviews with `mxbai-embed-large`
- Stores them in a Chroma vector DB
- Uses `llama3.2` to answer questions based on retrieved context

## 🧠 RAG Explained
You ask a question → relevant reviews are retrieved → the LLM is prompted with both → it gives an answer based on that context.

---

Feel free to customize the prompt, model, or documents!
