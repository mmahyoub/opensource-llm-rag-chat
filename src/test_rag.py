# Test for RAG chain using the same question as in test_vectorestore.py
from src.rag import get_rag_chain

print("Testing RAG chain...")
print("-" * 40)

rag_chain = get_rag_chain()
question = "How can we deal with patients falls?"
print("Question:", question)

response = rag_chain.invoke(question)
print("\nRAG Chain Response:\n", response)


