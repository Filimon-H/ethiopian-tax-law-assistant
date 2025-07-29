# src/pipeline/llm_chain.py

import os


from langchain_groq import ChatGroq

from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM (LLaMA 3.1 8B model)
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,  # adjust for more or less creativity
    api_key=GROQ_API_KEY
)
