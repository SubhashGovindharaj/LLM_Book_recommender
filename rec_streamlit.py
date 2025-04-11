import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

# Title
st.set_page_config(page_title="📚 Semantic Book Recommender", layout="wide")
st.title("📚 Semantic Book Recommender")

# Load data
books = pd.read_csv("books_with_emotions.csv")

books["large_thumbnail"] = books["thumbnail"] + "&fife=w800"
books["large_thumbnail"] = np.where(
    books["large_thumbnail"].isna(),
    "cover-not-found.jpg",
    books["large_thumbnail"],
)

# Load & Split documents
raw_documents = TextLoader("tagged_description.txt").load()
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=0, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)

# Embed & Create ChromaDB
db_books = Chroma.from_documents(documents, OpenAIEmbeddings())

# Categories and tones
categories = ["All"] + sorted(books["categories"].dropna().unique())
tones = ["All", "Happy", "Surprising", "Angry", "Suspenseful", "Sad"]

# Input UI
st.markdown("### 📝 Describe your preferred book")
query = st.text_input("Please enter a description of a book:", placeholder="e.g., A story about forgiveness")

category = st.selectbox("Select a category:", categories, index=0)
tone = st.selectbox("Select an emotional tone:", tones, index=0)

submit = st.button("🔍 Find Recommendations")


# Function to get recommendations
def retrieve_semantic_recommendations(query, category=None, tone=None, initial_top_k=50, final_top_k=16):
    recs = db_books.similarity_search(query, k=initial_top_k)
    books_list = [int(rec.page_content.strip('"').split()[0]) for rec in recs]
    book_recs = books[books["isbn13"].isin(books_list)].head(initial_top_k)

    if category != "All":
        book_recs = book_recs[book_recs["categories"] == category].head(final_top_k)
    else:
        book_recs = book_recs.head(final_top_k)

    if tone == "Happy":
        book_recs.sort_values(by="joy", ascending=False, inplace=True)
    elif tone == "Surprising":
        book_recs.sort_values(by="surprise", ascending=False, inplace=True)
    elif tone == "Angry":
        book_recs.sort_values(by="anger", ascending=False, inplace=True)
    elif tone == "Suspenseful":
        book_recs.sort_values(by="fear", ascending=False, inplace=True)
    elif tone == "Sad":
        book_recs.sort_values(by="sadness", ascending=False, inplace=True)

    return book_recs


# Display Results
if submit and query:
    with st.spinner("Searching books for you..."):
        recommendations = retrieve_semantic_recommendations(query, category, tone)
        if recommendations.empty:
            st.warning("No recommendations found.")
        else:
            st.markdown("### 🎯 Recommended Books")
            cols = st.columns(4)
            for idx, (_, row) in enumerate(recommendations.iterrows()):
                with cols[idx % 4]:
                    st.image(row["large_thumbnail"], use_column_width=True)
                    authors = row["authors"]
                    description = row["description"]
                    truncated = " ".join(description.split()[:30]) + "..."
                    st.caption(f"📖 **{row['title']}** by *{authors}*  \n{truncated}")