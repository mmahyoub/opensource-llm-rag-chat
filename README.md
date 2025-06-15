# Open-source LLM RAG Chat

A lightweight, open-source Retrieval-Augmented Generation (RAG) chatbot scaffold that lets you chat with your own documents using open-source LLMs. Designed for rapid prototyping and educational use, it features:
- Local LLM and embedding model support via Ollama
- Simple Streamlit web interface
- Example use case: Nurse Guide Chatbot for healthcare document Q&A
- Containerization for easy deployment
- Modular code for RAG, vectorstore, and prompt logic

> Chat with your data using open-source technology.
> 
> Example application: Nurse Guide Chatbot.
> 
> The purpose here is to provide a scaffold for RAG-based chat with your own documents. Features like chat history, prompt engineering, guardrails, evaluation, and inference optimization are out of scope for this project.
---

## Prerequisites

- **Ollama**: [Download & Install](https://ollama.com/download)
- **uv**: [Install Instructions](https://docs.astral.sh/uv/#installation)
- **Docker**: [Get Started](https://www.docker.com/get-started/)

---

## Local Setup

1. **Install dependencies**
   ```sh
   uv sync
   ```

2. **Pull LLM and Embeddings Model**
   ```sh
   uv run setup_ollama.py
   ```

3. **Run the Streamlit app**
   ```sh
   uv run streamlit run app.py
   ```

---

### Project Structure

- `app.py` — Main Streamlit app
- `src/` — Source code (RAG, prompts, vectorstore, etc.)
- `docs/` — Example healthcare nursing guidance policy PDFs (synthetic documents)
- `index/faiss_index/` — FAISS vector index files
- `containerize/` — Dockerfile and entrypoint script for containerization

---

### Usage

Once running, open the provided local URL in your browser to chat with your data using the open-source LLM.

If you would like to recreate the index, test the vectorestore, and or optimize the rag, teh follwing commadands are useful 

1. create the index 
```sh
uv run -m src.create_vectorstore
```

2. test vectorstore 
```sh
uv run -m src.test_vectorstore
```

3. test rag chain 
```sh
uv run -m src.test_rag
```
---
## Containerization
For deployment on a server or cloud environment.

1. **Build the Docker Image**
    ```sh
    docker build -f containerize/Dockerfile -t nurseguideapp .
    ```

2. **Run the Docker Container**
    ```sh
    # GPU
    docker run --gpus all -p 8000:8000 nurseguideapp

    # No GPU
    docker run -p 8000:8000 nurseguideapp
    ```

---
## License

MIT License