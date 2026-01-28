import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from typing import List, Tuple
from pydantic import BaseModel, Field
from config import settings
from src.retriever import get_retriever
from prompt.prompt import RAG_SYSTEM_PROMPT
# Output structure definition
class Source(BaseModel):
    """Source information"""
    document: int = Field(description="Document number")
    source: str = Field(description="Source file path or link")
    page: int = Field(description="Page number in the source document", default=None)
class RAGResponse(BaseModel):
    """Structured output for RAG responses"""
    answer: str = Field(description="The answer to the question based on context documents")
    sources: List[Source] = Field(description="List of sources with document number, source path, and page number")


def _format_documents(docs: List[Document]) -> str:
    """Format retrieved documents into JSON string format"""
    documents_list = []
    for i, doc in enumerate(docs, 1):
        doc_dict = {
            "document": i,
            "source": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", None),
            "content": doc.page_content.strip()
        }
        documents_list.append(doc_dict)
    
    return json.dumps(documents_list, ensure_ascii=False, indent=2)


# Create output parser
output_parser = PydanticOutputParser(pydantic_object=RAGResponse)

RAG_PROMPT = ChatPromptTemplate.from_messages([
    ("system", RAG_SYSTEM_PROMPT),
    ("human", "{question}")
])


def chat_with_rag(query: str) -> Tuple[RAGResponse, List[Document]]:
    llm = ChatOpenAI(
        api_key=settings.LLM_API_KEY,
        model=settings.LLM_CHAT_MODEL,
        base_url=settings.LLM_BASE_URL,
        temperature=0.1
    )
    
    docs = get_retriever(query)
    context = _format_documents(docs)
    
    # Chain with structured output parser
    chain = RAG_PROMPT | llm | output_parser
    
    result = chain.invoke({"question": query, "context": context})
    return result, docs
