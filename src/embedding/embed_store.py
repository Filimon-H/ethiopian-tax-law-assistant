import os

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.ingestion.document_loader import load_and_chunk_pdfs

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load documents and chunked texts
documents = load_and_chunk_pdfs()

# Setup ChromaDB path
CHROMA_DB_DIR = "chroma_db"

# Create vectorstore and persist
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=CHROMA_DB_DIR
)

# Save the database to disk
vectorstore.persist()
print(f"✅ Chroma vector store saved to: {CHROMA_DB_DIR}")
