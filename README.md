Perfect, thanks for pasting the full one. I see what you want:
We’ll polish it up so the README is more **professional, polished, and GitHub-ready** with:

* Cleaner formatting
* Proper image embedding (your screenshots will **display inline** instead of looking broken)
* A slightly improved workflow section
* Removal of duplicate/placeholder sections
* Extra clarity for someone who lands on your repo

Here’s the enhanced **README.md**:

---

````markdown
# 🕷️ AI Web Crawler + RAG Pipeline

This project is an **AI-powered web crawler and knowledge extraction pipeline**.  
It can **crawl websites**, extract clean text, **embed** it using **Qwen embeddings**, store the vectors in **ChromaDB**, and then use **Retrieval-Augmented Generation (RAG)** to answer user questions.  

It also ships with a **Streamlit frontend** where you can:  
✅ Crawl and extract knowledge from any website  
✅ Save structured knowledge as JSON  
✅ Generate embeddings and store in a vector database  
✅ Ask natural-language questions and get AI-powered answers  

---

## 🚀 Features

- 🌐 **Website Crawling** → Powered by [Crawl4AI](https://github.com/unclecode/crawl4ai)  
- 📄 **Clean Text Extraction** → Converts raw HTML into human-readable text  
- 🧠 **Embeddings with Qwen** → Alibaba’s Qwen embedding API  
- 🗂️ **Vector Store with ChromaDB** → Fast similarity search across crawled data  
- 🔍 **RAG Question Answering** → Combines retrieval with generative answers  
- 💾 **Export JSON** → Download extracted knowledge before embeddings  
- 🖥️ **Streamlit UI** → Easy-to-use interactive frontend  

---

## 📂 Project Structure

```bash
project_root/
│── scripts/
│   ├── run_pipeline.py      # CLI pipeline runner
│── app/
│   ├── streamlit_app.py     # Streamlit frontend
│── core/
│   ├── crawler.py           # Crawl4AI-based crawler
│   ├── embedder.py          # Qwen embedding functions
│   ├── vector_store.py      # ChromaDB vector store
│   ├── rag.py               # Retrieval + QA logic
│── outputs/
│   ├── extracted_data.json  # Sample extracted JSON
│── requirements.txt
│── README.md
````

---

## 🔧 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/ai-web-crawler-rag.git
   cd ai-web-crawler-rag
   ```

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

📸 Example output:

![CLI Example](https://github.com/ArunMandava3030/web_crawler_ai-agent/blob/d4f92a6f761215adc197f3ee9db8e678106f1c51/Screenshot%202025-08-17%20110231.png)

---

### 2. Run Streamlit frontend

Launch the interactive dashboard:

```bash
streamlit run app/streamlit_app.py
```

📸 Streamlit UI:

![Streamlit Example](https://github.com/ArunMandava3030/web_crawler_ai-agent/blob/d4f92a6f761215adc197f3ee9db8e678106f1c51/Screenshot%202025-08-17%20110513.png)

---

## 🧩 Example Workflow

1. Enter a website URL in the Streamlit UI
2. Crawl + extract readable content
3. JSON output is generated (downloadable)
4. Embeddings are created using Qwen
5. ChromaDB stores vectors
6. Ask questions → AI answers with RAG

---

## ⚡ Tech Stack

* [Python 3.10+](https://www.python.org/)
* [Crawl4AI](https://github.com/unclecode/crawl4ai) - Web crawling
* [Qwen API](https://dashscope.aliyuncs.com/) - Embeddings
* [ChromaDB](https://www.trychroma.com/) - Vector database
* [Streamlit](https://streamlit.io/) - Frontend

---

## 🛠️ Troubleshooting

* **Crawl4AI fails** → Some sites block bots. Try adding headers, delays, or testing another site.
* **Qwen API 404** → Ensure your API key is valid and endpoint is correct.
* **Chroma dimension mismatch** → Clear database if embedding dimensions changed.
* **Empty JSON** → The site may be heavily JavaScript-based; try alternate scraping config.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Arun Mandava**
