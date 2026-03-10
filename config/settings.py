import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

# Vector database
CHROMA_DB_PATH = os.path.join("data", "chroma_db")

# Retrieval
TOP_K_RESULTS = 3

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# LLM model
LLM_MODEL = "llama-3.3-70b-versatile"