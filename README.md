# 🧠 RAG Agent

A Retrieval-Augmented Generation (RAG) application that answers questions from your own PDF documents using semantic search and OpenAI.

Instead of sending an entire document to an LLM, the system retrieves only the most relevant chunks from a vector database, improving accuracy, reducing token usage, and minimizing hallucinations.

---

## 🚀 Features

- 📄 Extract text from PDFs
- ✂️ Intelligent document chunking
- 🧩 Generate semantic embeddings using Sentence Transformers
- 🗂️ Store embeddings in Qdrant Vector Database
- 🔎 Semantic similarity search
- 🤖 Context-aware answer generation with OpenAI GPT
- 📚 Support for multiple documents
- ⚡ Modular, extensible architecture

---

## 🛠 Tech Stack

- Python
- OpenAI API
- Sentence Transformers (all-MiniLM-L6-v2)
- Qdrant Vector Database
- PyMuPDF
- Docker

---

## 📂 Project Flow

```
PDF
   │
   ▼
Extract Text
   │
   ▼
Chunk Document
   │
   ▼
Generate Embeddings
   │
   ▼
Store in Qdrant
   │
   ▼
User Query
   │
   ▼
Semantic Search
   │
   ▼
Retrieve Relevant Chunks
   │
   ▼
OpenAI GPT
   │
   ▼
Final Answer
```

---

## 📁 Project Structure

```
app/
│
├── services/
│   ├── pdf_reader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_db.py
│   ├── search.py
│   └── generator.py
│
├── models/
│
└── main.py
```

---

## ⚙️ Setup

```bash
git clone <repo-url>

cd rag_agent

pip install -r requirements.txt

docker compose up -d
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Run:

```bash
python -m app.services.generator
```

---

## 💬 Example

```
Query:
How does top management demonstrate leadership?

Answer:
• Establish an information security policy and objectives.
• Align security objectives with strategic direction.
• Promote continual improvement.
• Support personnel responsible for the ISMS.
```

---

## 🎯 Future Improvements

- FastAPI backend
- Web interface
- Source citations
- Conversation history
- Cloud deployment
- Hybrid search
- Streaming responses

---

Built to understand documents, not just read them.
