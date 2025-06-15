import os
import pandas as pd
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings

def build_vector_store(data_path="./data/realistic_restaurant_reviews.csv",
                       db_location="./chroma_langchain_db"):

    df = pd.read_csv(data_path)
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    add_documents = not os.path.exists(db_location)

    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )

    if add_documents:
        documents = [
            Document(
                page_content=row["Title"] + " " + row["Review"],
                metadata={"rating": row["Rating"], "date": row["Date"]},
                id=str(i)
            )
            for i, row in df.iterrows()
        ]
        ids = [str(i) for i in range(len(documents))]
        vector_store.add_documents(documents=documents, ids=ids)

    return vector_store

def get_retriever():
    return build_vector_store().as_retriever(search_kwargs={"k": 5})
