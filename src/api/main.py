from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from src.pipeline.llm_chain import llm
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Request/Response Schema
class QuestionRequest(BaseModel):
    query: str

class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]

# Initialize FastAPI app
app = FastAPI(title="Ethiopian Tax Law Assistant")

# Load embeddings and vectorstore
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="vectorstore", embedding_function=embedding_model)
retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Prompt template
prompt_template = """
You are a helpful assistant specialized in Ethiopian tax law. Use the provided context to answer the question.
If you don’t know the answer, just say you don’t know — don’t make anything up.

Context:
{context}

Question:
{question}

Helpful Answer:
"""
prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)

# RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt}
)

# API Route
@app.post("/ask", response_model=AnswerResponse)
def ask_question(payload: QuestionRequest):
    try:
        logger.info(f"Received question: {payload.query}")
        result = qa_chain.invoke({"query": payload.query})
        sources = [doc.metadata.get("source", "unknown") for doc in result["source_documents"]]
        return {"answer": result["result"], "sources": sources}
    except Exception as e:
        logger.error(f"Error answering question: {e}")
        raise HTTPException(status_code=500, detail=str(e))
