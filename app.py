import os
import gradio as gr
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise Exception("GROQ_API_KEY not set in Hugging Face secrets")

client = Groq(api_key=api_key)

messages = [{"role": "system", "content": "You are a helpful assistant."}]

def chat_with_ai(message, history):
    messages.append({"role": "user", "content": message})
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )
        reply = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {str(e)}"

gr.ChatInterface(
    fn=chat_with_ai,
    chatbot=gr.Chatbot(),  # 🔧 FIXED: Removed type='messages'
    textbox=gr.Textbox(placeholder="Ask me anything..."),
    title="🌟 Free Groq AI Assistant",
    description="Chat with a powerful AI model (LLaMA 3). Built with Gradio + Groq.",
    theme="soft",
).launch(share=True)
