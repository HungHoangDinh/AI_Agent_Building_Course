"""
Code Chatbot using Streamlit and LangChain
This chatbot can answer questions about code, explain code, debug, and suggest improvements
"""
import streamlit as st
import uuid
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from config import settings
from typing import Dict

# Page configuration
st.set_page_config(
    page_title="Code Chatbot - LangChain + Streamlit",
    page_icon="🤖",
    layout="wide"
)

# Initialize LLM (cached to avoid re-initialization)
@st.cache_resource
def get_llm():
    """Initialize and cache LLM"""
    return ChatOpenAI(
        model=settings.LLM_CHAT_MODEL,
        api_key=settings.LLM_API_KEY,
        base_url=settings.LLM_BASE_URL,
        temperature=0.7
    )

llm = get_llm()

# Store for chat histories (session-based)
if "chat_histories" not in st.session_state:
    st.session_state.chat_histories: Dict[str, ChatMessageHistory] = {}

# Generate unique session ID for this Streamlit session
if "streamlit_session_id" not in st.session_state:
    st.session_state.streamlit_session_id = str(uuid.uuid4())


def get_session_history(session_id: str):
    """Get or create session history for a given session ID"""
    if session_id not in st.session_state.chat_histories:
        st.session_state.chat_histories[session_id] = ChatMessageHistory()
    return st.session_state.chat_histories[session_id]


# Create prompt template for code-related questions
code_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert programmer and code reviewer. 
You can:
- Explain code in detail and in an easy-to-understand way
- Find and fix bugs in code
- Suggest code improvements (performance, readability, best practices)
- Write sample code as requested
- Answer questions about programming concepts, algorithms, design patterns
- Support multiple programming languages: Python, JavaScript, Java, C++, etc.

Please provide detailed answers with concrete code examples when needed."""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Create chain with memory
chain = code_prompt | llm | StrOutputParser()

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)


def get_chat_response(message: str, session_id: str = "default") -> str:
    """
    Get response from chatbot
    
    Args:
        message: User's message
        session_id: Session ID for memory
    
    Returns:
        str: Bot's response
    """
    try:
        response = chain_with_memory.invoke(
            {"input": message},
            config={"configurable": {"session_id": session_id}}
        )
        return response
    except Exception as e:
        return f"Error: {str(e)}"


def clear_chat_history():
    """Clear chat history for current session"""
    session_id = st.session_state.streamlit_session_id
    if session_id in st.session_state.chat_histories:
        st.session_state.chat_histories[session_id] = ChatMessageHistory()
    if "messages" in st.session_state:
        st.session_state.messages = []


# Main UI
def main():
    """Main Streamlit app"""
    
    # Header
    st.title("🤖 Code Chatbot")
    
    # sidebar
    with st.sidebar:
        st.markdown("""Have a question about code? Ask me anything!""")
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question about code..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get bot response using auto-generated session ID
        session_id = st.session_state.streamlit_session_id
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_chat_response(prompt, session_id)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
