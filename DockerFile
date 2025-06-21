FROM ollama/ollama:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install --no-cache-dir streamlit ollama \
    langchain langchain-community langchain-ollama

RUN ollama pull llama3.2:3b

WORKDIR /app
COPY requirements.txt assistant_langchain.py chat_ui.py ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["bash", "-c", "ollama serve & streamlit run chat_ui.py --server.port 8080 --server.address 0.0.0.0"]
