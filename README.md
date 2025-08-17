# 🕷️ AI Web Crawler + RAG Pipeline

This project is an **AI-powered web crawler and knowledge extraction pipeline** that can crawl websites, extract clean text, embed it using **Qwen embeddings**, store it in **ChromaDB**, and perform **Retrieval-Augmented Generation (RAG)** to answer user questions.  

It also includes a **Streamlit frontend** where users can:
- Crawl and extract structured knowledge from a website  
- Store knowledge in a vector database  
- Ask questions and get AI-powered answers  
- Download the extracted knowledge as a JSON file  

---

## 🚀 Features

- 🌐 **Website Crawling** → Powered by [Crawl4AI](https://github.com/unclecode/crawl4ai)  
- 📄 **Clean Text Extraction** → Extracts readable content instead of raw HTML  
- 🧠 **Embeddings with Qwen** → Uses Alibaba’s Qwen embedding API  
- 🗂️ **Vector Store with ChromaDB** → Stores embeddings for efficient similarity search  
- 🔍 **RAG Question Answering** → Retrieves relevant chunks + generates answers  
- 💾 **Export JSON** → Download extracted website knowledge before embedding  
- 🖥️ **Streamlit UI** → Simple interactive frontend  

---

## 📂 Project Structure

```

project\_root/
│── scripts/
│   ├── run\_pipeline.py      # CLI pipeline runner
│── app/
│   ├── streamlit\_app.py     # Streamlit frontend
│── core/
│   ├── crawler.py           # Crawl4AI-based crawler
│   ├── embedder.py          # Qwen embedding functions
│   ├── vector\_store.py      # ChromaDB vector store
│   ├── rag.py               # Retrieval + QA logic
│── outputs/
│   ├── extracted\_data.json  # Sample extracted JSON
│── requirements.txt
│── README.md

````

---

## 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/ai-web-crawler-rag.git
   cd ai-web-crawler-rag
````

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   Create a `.env` file in the project root:

   ```ini
   QWEN_API_KEY=your_api_key_here
   ```

---

## ▶️ Usage

### 1. Run pipeline from CLI

Crawl a website, embed it, and store in ChromaDB:

```bash
python scripts/run_pipeline.py https://www.chrismytton.com/plain-text-websites/
```

### 2. Run Streamlit frontend

Launch the interactive dashboard:

```bash
streamlit run app/streamlit_app.py
```

---

## 🧩 Example Workflow

1. Enter a website URL in the Streamlit UI
2. The system crawls and extracts text
3. JSON output is generated → downloadable before embedding
4. Embeddings are created with Qwen
5. ChromaDB stores vectors
6. Ask questions → Answers are generated with RAG

---

## 📸 Screenshots (Optional)

*Add screenshots of the Streamlit app UI, crawling process, and Q\&A here.*

---

## ⚡ Tech Stack

* [Python 3.10+](https://www.python.org/)
* [Crawl4AI](https://github.com/unclecode/crawl4ai) - Web crawling
* [Qwen API](https://dashscope.aliyuncs.com/) - Embeddings
* [ChromaDB](https://www.trychroma.com/) - Vector database
* [Streamlit](https://streamlit.io/) - Frontend

---

## 🛠️ Troubleshooting

* **Crawl4AI fails** → Check if site blocks bots (use headers or delays).
* **Qwen API 404** → Make sure the embedding endpoint is correct and API key is valid.
* **FAISS/Chroma dimension mismatch** → Ensure embeddings are stored with consistent dimensions.
* **Empty JSON output** → Site may have dynamic JS content. Use a different crawler config.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Arun Mandava**

* 🌐 [LinkedIn](https://linkedin.com/in/arun-mandava)
* 💻 Data Scientist | AI & Web Crawling Enthusiast

