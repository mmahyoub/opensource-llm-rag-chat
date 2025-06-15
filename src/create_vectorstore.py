import os
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings

print("Creating vectorstore...")

# Path to the docs directory in parent directory
DOCS_DIR = os.path.join(os.path.dirname(__file__), "../docs")

# Load all PDF files from the Docs directory
all_docs = []
for filename in os.listdir(DOCS_DIR):
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(DOCS_DIR, filename))
        all_docs.extend(loader.load())

# Chunk the documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(all_docs)

# Post-process each chunk for readability
for doc in docs:
    # Strip leading/trailing whitespace
    text = doc.page_content.strip()
    # Replace single newlines (not part of double newlines) with spaces
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # Normalize multiple spaces
    text = re.sub(r' +', ' ', text)
    # Normalize multiple newlines to max two
    text = re.sub(r'\n{3,}', '\n\n', text)
    doc.page_content = text

# Create embeddings using Ollama's nomic-embed-text model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Create the FAISS vectorstore
vectorstore = FAISS.from_documents(docs, embeddings)

# Save the vectorstore to disk
vectorstore.save_local(os.path.join(os.path.dirname(__file__), "../index/faiss_index"))
print("Vectorstore created and saved to '../index/faiss_index' directory.")