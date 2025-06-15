import streamlit as st
from src.rag import get_rag_chain

# Initialize the RAG chain
chain = get_rag_chain()


# Define avatars for chat boxes
avatars = {
    "user": ":material/person:",
    "assistant": ":material/assistant_on_hub:"
}

st.header("NurseGuideBot :material/chat:")

# Session variables 
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add initial assistant greeting only once
    st.session_state.messages.append({"role": "assistant", "content": "Hello, how can I help you?"})

# Add sidebar button for new session
if st.sidebar.button("Start New Session"):
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hello, how can I help you?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=avatars[message["role"]]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help?"):
    # Display user message in chat message container
    with st.chat_message("user", avatar=avatars["user"]):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        with st.spinner("Thinking ..."):
            response = st.write_stream(chain.stream(prompt))

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})