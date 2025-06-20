import streamlit as st
from ollama import Client

client = Client(host="http://localhost:11434")

st.title("💬 Llama 3.2 Chatbot (Ollama)")

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

usr = st.chat_input("Say something")
if usr:
    st.session_state.history.append({"role": "user", "content": usr})
    with st.spinner("Thinking…"):
        ai = client.chat(
            model="llama3.2", messages=st.session_state.history, stream=False
        )["message"]["content"]
    st.session_state.history.append({"role": "assistant", "content": ai})
    st.rerun()
