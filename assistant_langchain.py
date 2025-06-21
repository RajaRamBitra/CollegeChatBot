from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage, HumanMessage


class CollegeAssistantLC:
    def __init__(self):
        self.chat = ChatOllama(
            model="llama3.2:3b",
            base_url="http://localhost:11434",
            temperature=0.3,
            num_predict=150,
        )
        self.sys = SystemMessage(
            content=(
                "You are a helpful FAU assistant. "
                "Respond briefly and accurately about campus locations and services. "
                "Key locations: Registrar (Student Union 144), "
                "Library (S.E. Wimberly), Starbucks (Student Union food court)."
            )
        )

    def ask(self, user_msg: str) -> str:
        return self.chat.invoke([self.sys, HumanMessage(content=user_msg)]).content
