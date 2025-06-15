# Import modules
import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from src.prompts import rag_prompt

def get_rag_chain():
    """
    Function to create and return the RAG chain.
    """

    # Load the FAISS vectorstore
    vectorstore = FAISS.load_local(
        os.path.join(os.path.dirname(__file__), "../index/faiss_index"),
        OllamaEmbeddings(model="nomic-embed-text"),
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

    # Create a prompt template that includes context and user input
    prompt = PromptTemplate(
        input_variables = ["context", "user_input"],
        template = rag_prompt
    )

    # Connect to the local Llama 3.2 3B model via Ollama
    llm = ChatOllama(model="llama3.2:latest", temperature=0.7)

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    rag_chain = (
        {"context": retriever | format_docs, "user_input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain