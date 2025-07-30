# 📟 Ethiopian Tax Law Assistant

A RAG-based legal chatbot that helps users query the Ethiopian tax code—including VAT, Turnover Tax, and Income Tax—by retrieving relevant chunks from legal PDFs and generating accurate, cited answers using Groq’s LLaMA3-8B model. Built using LangChain, FastAPI, Streamlit, and ChromaDB.

---

## 📌 Project Overview

**Goal:** To make Ethiopian tax regulations more accessible and understandable to professionals, citizens, and businesses by providing an AI-powered legal assistant.

**Problem:** Navigating Ethiopia's complex tax codes is time-consuming and requires legal expertise.

**Solution:** A Retrieval-Augmented Generation (RAG) chatbot that accepts natural language tax-related questions and responds with answers grounded in official legal documents.

---

## 🧠 Architecture & Tools

| Layer            | Technology              | Purpose                     |
| ---------------- | ----------------------- | --------------------------- |
| LLM              | Groq (LLaMA3-8B)        | Answer generation           |
| Chunking         | LangChain               | Semantic text splitting     |
| Embedding        | Sentence Transformers   | Dense vector representation |
| Vector Store     | ChromaDB                | Document similarity search  |
| Backend API      | FastAPI                 | Handles `/ask` endpoint     |
| Frontend UI      | Streamlit               | Simple chat interface       |
| Containerization | Docker & Docker Compose | Reproducible deployment     |

---

## 📂 Project Structure

```bash
.
├── docker-compose.yml
├── .env.example
├── requirements.txt
├── src/
│   ├── api/main.py                 # FastAPI app
│   ├── config/load_config.py      # Loads .env & API keys
│   ├── ingestion/document_loader.py  # PDF loader & chunker
│   ├── embedding/embed_store.py   # Embedding and vector store
│   └── pipeline/retrieval_qa.py   # RAG logic
├── streamlit_app/app.py           # Streamlit UI
```

---

## 🥪 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ethiopian-tax-law-assistant.git
cd ethiopian-tax-law-assistant
```

### 2. Set Up Environment Variables

Get your **Groq API key** from [https://console.groq.com](https://console.groq.com) and add it to your local `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run in Development Mode

```bash
# Step 1: Load API key and config
python src/config/load_config.py

# Step 2: Load and chunk legal PDFs
python src/ingestion/document_loader.py

# Step 3: Embed chunks and store in ChromaDB
python src/embedding/embed_store.py

# Step 4: Start FastAPI server
python src/api/main.py
```

In a **separate terminal**, once FastAPI is running:

```bash
# Step 5: Launch Streamlit interface
streamlit run streamlit_app/app.py
```

---

## 🐳 Run with Docker

### 1. Build Images

```bash
docker-compose build
```

### 2. Run Services

```bash
docker-compose up
```

Access the app at: [http://localhost:8501](http://localhost:8501)
API available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ Example Questions

* "What is the turnover tax threshold in Ethiopia?"
* "Is VAT applicable to educational institutions?"
* "When should income tax be filed?"

---

## 📊 Evaluation

| Metric             | Description                            | Result |
| ------------------ | -------------------------------------- | ------ |
| RAG Quality        | Manual check for relevance & citations | ✅ High |
| UI Usability       | Simple, accessible sidebar and layout  | ✅ Easy |
| API Latency        | Fast (hosted via Groq inference)       | ✅ Fast |
| Dockerization      | Multi-service with `docker-compose`    | ✅ Done |
---

## 🚀 Future Work

* ✅ Add Source File Viewer in Streamlit
* ✅ Implement Query Retry on Failure
* 🔒 Add Auth for Admin View
* 🌐 Add Amharic LLM Support

---

## 📜 License

MIT License. See [LICENSE](LICENSE) file.

---

## ✨ Credits

Made by [Filimon Hailemariam]

