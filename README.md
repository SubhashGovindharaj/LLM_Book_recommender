# LLM_Book_recommender

# 📚 LLM-Based Semantic Book Recommender

A powerful AI-powered book recommendation system built using **LangChain**, **ChromaDB**, and **OpenAI embeddings**. This app helps users discover books based on semantic similarity, emotional tone, and category — all through a clean UI built with **Streamlit** and **Gradio**.

---

## 🚀 Demo

> ⚡ Coming Soon: Deployed on Hugging Face / Streamlit Cloud  
> 🎥 Watch demo [link goes here]

---

## 🧠 Features

- ✅ Semantic Search with OpenAI Embeddings  
- ✅ Emotion-based filtering (Joy, Sadness, Surprise, etc.)  
- ✅ Category-based exploration  
- ✅ Beautiful UI with Streamlit & Gradio  
- ✅ Powered by LangChain + ChromaDB  
- ✅ NLP-driven real-time recommendations

---

## 🛠️ Tech Stack

- **LangChain** – LLM chaining logic  
- **OpenAI** – Embedding text  
- **ChromaDB** – Vector store for similarity search  
- **Gradio & Streamlit** – Frontend interface  
- **Pandas / NumPy** – Data wrangling

---

## 📁 Dataset

- `books_with_emotions.csv` → Contains book metadata + emotion scores  
- `tagged_description.txt` → Text source for vector embedding + search

---

## 🧪 How It Works

1. User types a query (e.g., _“A thrilling love story with emotional depth”_)  
2. LangChain converts the query to vector using OpenAI embeddings  
3. ChromaDB fetches semantically similar book chunks  
4. Emotion & category filters refine results  
5. Streamlit or Gradio displays books with thumbnails + summary

---

## 📦 Folder Structure
