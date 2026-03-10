import streamlit as st

from agent.memory_manager import MemoryManager
from agent.retriever import MemoryRetriever
from models.llm_model import LLMModel
from database.vector_store import VectorStore


# -----------------------------
# Initialize components safely
# -----------------------------
@st.cache_resource
def load_components():
    memory_manager = MemoryManager()
    retriever = MemoryRetriever()
    llm = LLMModel()
    vector_store = VectorStore()
    return memory_manager, retriever, llm, vector_store


memory_manager, retriever, llm, vector_store = load_components()


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Personal Knowledge Agent",
    page_icon="🧠",
    layout="wide"
)


# -----------------------------
# App title
# -----------------------------
st.title("🧠 Personal Knowledge Agent")
st.write("An AI assistant that remembers information about you.")


# -----------------------------
# Session state for chat
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -----------------------------
# Sidebar Memory Panel
# -----------------------------
st.sidebar.title("🧠 Memory Panel")

memories = vector_store.get_all_memories()

if st.sidebar.button("Show Stored Memories"):

    if memories:
        st.sidebar.write("### Stored Memories")

        for m in memories:
            st.sidebar.write("•", m)

    else:
        st.sidebar.write("No memories stored yet.")


if st.sidebar.button("Clear Memory"):

    vector_store.clear_memories()
    st.sidebar.success("Memory cleared.")
    st.rerun()


st.sidebar.markdown("---")
st.sidebar.write(f"Total Memories: {len(memories)}")


# -----------------------------
# Display chat history
# -----------------------------
for role, message in st.session_state.chat_history:

    with st.chat_message(role):
        st.write(message)


# -----------------------------
# Chat input
# -----------------------------
user_input = st.chat_input("Ask me something...")


# -----------------------------
# Process user message
# -----------------------------
if user_input:

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Store memory if relevant
    memory_manager.process_input(user_input)

    # Retrieve memories
    retrieved_memories = retriever.retrieve(user_input)

    # Generate response
    response = llm.generate_answer(user_input, retrieved_memories)

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)

    # Save to chat history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))