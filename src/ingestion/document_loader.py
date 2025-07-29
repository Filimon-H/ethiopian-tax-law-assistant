import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_pdfs():
    # Get absolute path to /data/raw from the current file
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    pdf_folder = os.path.join(PROJECT_ROOT, "data", "raw")

    all_chunks = []

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            print(f"Loading: {file_path}")
            loader = PyPDFLoader(file_path)
            documents = loader.load()

            # ✅ Add source metadata to each page
            for doc in documents:
                doc.metadata["source"] = filename

            # Chunk the documents with overlap
            splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
            chunks = splitter.split_documents(documents)

            all_chunks.extend(chunks)

    return all_chunks

# Run to test
if __name__ == "__main__":
    chunks = load_and_chunk_pdfs()
    print(f"Total chunks: {len(chunks)}")
    print("Example chunk metadata:", chunks[0].metadata)

print(chunks[0].page_content)
