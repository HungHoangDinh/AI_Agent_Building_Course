"""
Entry: Gradio (hoặc CLI) chạy Agent Trợ lý Chuyển đổi Ngoại tệ & Tra cứu Lương.
Chạy ingest.py trước để ingest data/jobs.md vào vector_store trước khi dùng tool Job Retrieval.
"""
import os
import sys

# TODO: import gradio as gr
# TODO: from agent import create_agent


def run_agent(user_message: str, history: list) -> tuple:
    """
    Gửi user_message vào agent, trả về (output_string, updated_history).
    
    Args:
        user_message: Câu hỏi của user.
        history: Lịch sử chat (format Gradio: list of [user, bot] hoặc list of dict).
    
    Returns:
        tuple: (empty string để clear input, updated history).
    """
    # TODO: Load agent (create_agent), invoke với user message và thread_id
    raise NotImplementedError("TODO: implement run_agent")


def clear_chat() -> tuple:
    """Xóa lịch sử chat (và có thể reset memory)."""
    # TODO: Xóa memory và trả về empty history, empty message box
    return [], ""


# =========================
# Gradio Interface
# =========================

def create_interface():
    """Tạo giao diện Gradio cho agent."""
    # TODO: with gr.Blocks(title="Trợ lý Tỷ giá & Tra cứu Lương") as demo:
    # TODO:     gr.Markdown("# Trợ lý Chuyển đổi Ngoại tệ & Tra cứu Lương Rikkeisoft")
    # TODO:     gr.Markdown("Hỏi tỷ giá, quy đổi tiền tệ, hoặc tra cứu vị trí công việc.")
    # TODO:     chatbot = gr.Chatbot(...)
    # TODO:     msg = gr.Textbox(label="Câu hỏi", placeholder="VD: 1 USD bằng bao nhiêu VND? Tra cứu Frontend Developer...")
    # TODO:     submit_btn = gr.Button("Gửi")
    # TODO:     clear_btn = gr.Button("Xóa lịch sử")
    # TODO:     gr.Examples(examples=[["1 USD bằng bao nhiêu VND?"], ["Tra cứu vị trí Backend Developer tại Rikkeisoft"], ["Quy đổi 50 triệu VND sang USD theo tỷ giá hôm nay"]], inputs=msg)
    # TODO:     msg.submit(fn=run_agent, inputs=[msg, chatbot], outputs=[msg, chatbot])
    # TODO:     submit_btn.click(fn=run_agent, inputs=[msg, chatbot], outputs=[msg, chatbot])
    # TODO:     clear_btn.click(fn=clear_chat, inputs=[], outputs=[chatbot, msg])
    # TODO: return demo
    raise NotImplementedError("TODO: implement create_interface (Gradio)")


if __name__ == "__main__":
    # TODO: demo = create_interface()
    # TODO: demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
    print("TODO: Implement run_agent, create_interface and uncomment launch().")
    print("Chạy ingest.py trước để ingest data/jobs.md vào vector_store.")
