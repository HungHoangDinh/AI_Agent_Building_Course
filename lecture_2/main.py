"""
RAG Chatbot Demo using Gradio
Uses RAG chain to answer questions based on ingested documents
"""
import gradio as gr
from src.rag_chain import chat_with_rag


def chat_with_rag_bot(message: str, history: list) -> tuple:
    """
    Chat function for Gradio interface using RAG
    
    Args:
        message: User's message/question
        history: Chat history (list of dicts with 'role' and 'content' keys)
    
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
        rag_response, retrieved_docs = chat_with_rag(message)
        response_text = rag_response.answer
        if retrieved_docs:
            all_sources_list = []
            for i, doc in enumerate(retrieved_docs, 1):
                source_path = doc.metadata.get("source", "Unknown") 
            all_sources_str = "\n".join([f"  • {s}" for s in all_sources_list])
            response_text += f"\n\n📚 All Retrieved Sources:\n{all_sources_str}"
            
            # Also show sources used in answer (if different)
            if rag_response.sources:
                used_sources_list = []
                for source in rag_response.sources:
                    page_info = f", Page {source.page}" if source.page is not None else ""
                    used_sources_list.append(f"Document {source.document}: {source.source}{page_info}")
                used_sources_str = "\n".join([f"  • {s}" for s in used_sources_list])
                response_text += f"\n\n✅ Sources Used in Answer:\n{used_sources_str}"
        else:
            response_text += "\n\n📚 Sources: None"
        
        # Update history with new format: list of dicts
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response_text})
        
        return "", history
    
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": error_msg})
        return "", history


def clear_chat() -> tuple:
    """Clear chat history"""
    return [], ""


# Create Gradio interface
def create_rag_chatbot_interface():
    """Create and launch RAG chatbot interface"""
    
    with gr.Blocks(title="RAG Chatbot - LangChain + Gradio") as demo:
        gr.Markdown("""
        # 🤖 RAG Chatbot
        
        A chatbot powered by **Retrieval-Augmented Generation (RAG)** using **LangChain** and **Gradio**
        
        ### Features:
        - Answers questions based on your ingested documents
        - Retrieves relevant context from vector database
        - Prevents hallucination by only using provided context
        
        **Note**: Make sure you have ingested documents into the vector store before asking questions.
        """)
        
        chatbot = gr.Chatbot(
            label="Chat",
            height=500,
            avatar_images=(None, "🤖")
        )
        
        with gr.Row():
            msg = gr.Textbox(
                label="Your Question",
                placeholder="Ask a question about your documents...",
                scale=4,
                lines=2
            )
            submit_btn = gr.Button("Send", variant="primary", scale=1)
        
        with gr.Row():
            clear_btn = gr.Button("🗑️ Clear History", variant="secondary")
        
        # Examples
        gr.Markdown("### 💡 Example Questions:")
        examples = gr.Examples(
            examples=[
                ["What information is available in the documents?"],
                ["Summarize the main topics"],
                ["Tell me about the key points"],
            ],
            inputs=msg
        )
        
        # Event handlers
        msg.submit(
            fn=chat_with_rag_bot,
            inputs=[msg, chatbot],
            outputs=[msg, chatbot]
        )
        
        submit_btn.click(
            fn=chat_with_rag_bot,
            inputs=[msg, chatbot],
            outputs=[msg, chatbot]
        )
        
        clear_btn.click(
            fn=clear_chat,
            inputs=[],
            outputs=[chatbot, msg]
        )
        
        gr.Markdown("""
        ---
        ### 📝 Notes:
        - The chatbot uses RAG to retrieve relevant documents and answer based on them
        - If information is not in the documents, the chatbot will say "I don't know"
        - Make sure documents are ingested into the vector store before use
        """)
    
    return demo


if __name__ == "__main__":
    # Create and launch the interface
    demo = create_rag_chatbot_interface()
    demo.launch(
        server_name="0.0.0.0",  
        server_port=7880,       
        share=False,           
    )
