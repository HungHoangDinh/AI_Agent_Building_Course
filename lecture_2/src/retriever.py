from langchain_chroma import Chroma
from langchain_core.documents import Document
from src.embeddings import create_or_get_vector_store
from typing import List
def get_retriever(query: str)-> List[Document]:
    vectorstore = create_or_get_vector_store()
    return vectorstore.similarity_search(query, k=3)