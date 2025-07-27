import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load the API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file!")

# Initialize LLM
llm = ChatGroq(model="llama3-8b-8192", api_key=api_key)

# Setup a basic conversation
conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory())

# Test query
response = conversation.predict(input="Hello! What is VAT in Ethiopia?")
print("Response:", response)
