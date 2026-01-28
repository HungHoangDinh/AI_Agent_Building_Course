
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from config import settings
from typing import Dict

# Initialize LLM
llm = ChatOpenAI(
    model=settings.LLM_CHAT_MODEL,
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_BASE_URL,
    temperature=0.7
)

chat_histories: Dict[str, ChatMessageHistory] = {}


def get_session_history(session_id: str):
    """Get or create session history for a given session ID"""
    if session_id not in chat_histories:
        chat_histories[session_id] = ChatMessageHistory()
    return chat_histories[session_id]


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


def chat_with_bot(message: str, history: list, session_id: str = "default") -> tuple:
    """
    Chat function for Gradio interface
    
    Args:
        message: User's message
        history: Chat history (list of dicts with 'role' and 'content' keys)
        session_id: Session ID for memory
    
    Returns:
        tuple: (empty string, updated history)
    """
    if not message.strip():
        return "", history
    
    # Convert history from old format [[user, bot], ...] to new format if needed
    if history and isinstance(history[0], list):
        for msg in history:
            history.append({"role": "user", "content": msg[0]})
            history.append({"role": "assistant", "content": msg[1]})
    
    try:
        # Get response from chain
        response = chain_with_memory.invoke(
            {"input": message},
            config={"configurable": {"session_id": session_id}}
        )
        
        # Update history with new format: list of dicts
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response})
        
        return "", history
    
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": error_msg})
        return "", history


def clear_chat(session_id: str = "default") -> tuple:
    """Clear chat history for a session"""
    if session_id in chat_histories:
        chat_histories[session_id] = ChatMessageHistory()
    return [], ""  # Return empty list for history, empty string for message


# Create Gradio interface
def create_chatbot_interface():
    """Create and launch Gradio chatbot interface"""
    
    with gr.Blocks(title="Code Chatbot - LangChain + Gradio") as demo:
        gr.Markdown("""
        # 🤖 Code Chatbot
        
        A specialized code chatbot using **LangChain** and **Gradio**
        
        ### You can ask about:
        - Code explanation
        - Debugging and fixing errors
        - Performance improvements
        - Programming concepts
        - Design patterns
        - Writing sample code
        
        **Note**: The chatbot has memory and will remember previous questions in this session.
        """)
        
        chatbot = gr.Chatbot(
            label="Chat",
            height=500,
            avatar_images=(None, "🤖 ")
        )
        
        with gr.Row():
            msg = gr.Textbox(
                label="Your Question",
                placeholder="Example: Explain this Python code...",
                scale=4,
                lines=2
            )
            submit_btn = gr.Button("Send", variant="primary", scale=1)
        
        with gr.Row():
            clear_btn = gr.Button("🗑️ Clear History", variant="secondary")
            session_id_input = gr.Textbox(
                label="Session ID",
                value="default",
                placeholder="Enter session ID to manage multiple conversations",
                scale=2
            )
        
        # Examples
        gr.Markdown("### 💡 Example Questions:")
        examples = gr.Examples(
            examples=[
                ["Explain this Python code: def fibonacci(n): return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)"],
                ["How to optimize this code?", "for i in range(1000000):\n    result = i * 2"],
                ["Find the bug in this code:", "def divide(a, b):\n    return a / b\nprint(divide(10, 0))"],
                ["Write a Python function to reverse a string"],
                ["Explain the difference between list comprehension and for loop in Python"],
                ["How to implement Singleton pattern in Python?"],
            ],
            inputs=msg
        )
        
        # Event handlers
        msg.submit(
            fn=lambda m, h, s: chat_with_bot(m, h, s),
            inputs=[msg, chatbot, session_id_input],
            outputs=[msg, chatbot]
        )
        
        submit_btn.click(
            fn=lambda m, h, s: chat_with_bot(m, h, s),
            inputs=[msg, chatbot, session_id_input],
            outputs=[msg, chatbot]
        )
        
        clear_btn.click(
            fn=lambda s: clear_chat(s),
            inputs=[session_id_input],
            outputs=[chatbot, msg]
        )
        
        gr.Markdown("""
        ---
        ###  Notes:
        - The chatbot uses LangChain with memory to remember context
        - Each session ID has its own conversation history
        - You can ask about different programming languages
        """)
    
    return demo


if __name__ == "__main__":
    # Create and launch the interface
    demo = create_chatbot_interface()
    demo.launch(
        server_name="0.0.0.0",  # Allow external access
        server_port=7890,        # Default Gradio port
        share=False,             # Set to True to create public link
        show_error=True,
    )
