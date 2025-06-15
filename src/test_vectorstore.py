import os
from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings

# Load the FAISS vectorstore
vectorstore = FAISS.load_local(
    os.path.join(os.path.dirname(__file__), "../index/faiss_index"),
    OllamaEmbeddings(model="nomic-embed-text"),
    allow_dangerous_deserialization=True
)

# Test question
question = "How can we deal with patients falls?"

# Perform similarity search
results = vectorstore.similarity_search(question, k=5)

print("Top relevant documents for the question:")
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(doc.page_content)
    print(f"Metadata: {doc.metadata}")
    print('-' * 40)
