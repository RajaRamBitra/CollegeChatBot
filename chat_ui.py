import streamlit as st
from assistant_langchain import CollegeAssistantLC

assistant = CollegeAssistantLC()
st.title("💬 FAU Assistant — LangChain + Ollama")

for m in st.session_state.get("history", []):
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

question = st.chat_input("Ask me anything about FAU…")
if question:
    st.session_state.setdefault("history", []).append(
        {"role": "user", "content": question}
    )
    with st.spinner("Thinking…"):
        answer = assistant.ask(question)
    st.session_state.history.append({"role": "assistant", "content": answer})
    st.rerun()
