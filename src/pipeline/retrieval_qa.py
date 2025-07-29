from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from llm_chain import llm

# Load embedding model and vectorstore
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="vectorstore", embedding_function=embedding_model)

# Setup retriever
retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# 🧠 Custom Prompt Template
prompt_template = """
You are a helpful assistant specialized in Ethiopian tax law. Use the provided context to answer the question.
If you don’t know the answer, just say you don’t know — don’t make anything up.

Context:
{context}

Question:
{question}

Helpful Answer:
"""

custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)

# Build the RetrievalQA chain with custom prompt
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type="stuff",  # Keep default stuffing logic
    chain_type_kwargs={"prompt": custom_prompt}  # Inject custom prompt
)

# ✅ Test the chain
if __name__ == "__main__":
    query = "What is turnover tax in Ethiopia?"
    result = qa_chain.invoke({"query": query})
    print("\nAnswer:\n", result["result"])
    print("\nSources:\n", [doc.metadata.get("source", "unknown") for doc in result["source_documents"]])
