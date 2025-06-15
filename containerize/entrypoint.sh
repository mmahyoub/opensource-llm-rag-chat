#!/bin/bash
set -e

# Start Ollama server in the background
ollama serve &

# Wait for Ollama server to be ready
until curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama server to start..."
  sleep 2
done

echo "Ollama server is up. Pulling models..."
ollama pull nomic-embed-text
ollama pull llama3.2:latest

echo "Starting Streamlit app..."
exec uv run streamlit run app.py --server.port 8000