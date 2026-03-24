"""
Tạo Agent với 3 tools (search, calculator, job_retrieval) và memory.
Tham khảo: lecture_3/main.ipynb (tools), lecture_2 (RAG).
"""
import os
import sys

# TODO: from langchain_google_genai import ChatGoogleGenerativeAI (hoặc model tương thích)
# TODO: from langchain.agents import create_react_agent, AgentExecutor
# TODO: from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# TODO: from langchain_community.chat_message_histories import ChatMessageHistory
# TODO: from langchain_core.chat_history import BaseChatMessageHistory
# TODO: from langchain_core.runnables.history import RunnableWithMessageHistory
# TODO: from prompt.prompt import CURRENCY_JOB_AGENT_SYSTEM_PROMPT
# TODO: from tools.search_tool import search_internet
# TODO: from tools.calculator_tool import calculate
# TODO: from tools.job_retrieval_tool import search_job_positions


def create_tools():
    """
    Tạo danh sách tools cho agent: search_internet, calculate, search_job_positions.
    
    Returns:
        List of LangChain Tool objects.
    """
    # TODO: Tạo list tools từ search_internet, calculate, search_job_positions (đã wrap @tool)
    raise NotImplementedError("TODO: implement create_tools")


def create_memory():
    """
    Tạo memory cho agent (dạng bài tập: lưu vài turn gần nhất).
    
    Returns:
        Object memory hoặc store cho session (session_id -> chat history).
    """
    # TODO: Lưu vài turn gần nhất vào memory
    raise NotImplementedError("TODO: implement create_memory")


def create_agent(llm=None, tools=None, memory=None):
    """
    Tạo agent (ReAct) với llm, tools, system prompt và memory.
    
    Args:
        llm: Chat model (ChatOpenAI hoặc tương thích).
        tools: List tools từ create_tools().
        memory: Memory từ create_memory() (optional).
    
    Returns:
        AgentExecutor hoặc chain có thể invoke (input: message, output: response).
    """
    # TODO: Tạo Agent với llm, tools, system prompt và memory.
    raise NotImplementedError("TODO: implement create_agent")
