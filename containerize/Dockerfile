# Use official Python 3.13 image
FROM python:3.13-slim

# Set environment variables
ENV PATH="/root/.local/bin:${PATH}"

# Install curl (build-time)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl

# Install Ollama
RUN echo "Installing Ollama..." && \
    curl -fsSL https://ollama.com/install.sh | sh && \
    echo "Ollama installation script finished." && \
    echo "Verifying ollama command is available..." && \
    (ollama help || (echo "Error: 'ollama' command failed. Ollama might not be installed correctly or not in PATH." && exit 1))

# Install uv
RUN echo "Installing uv..." && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    echo "uv installation script finished." && \
    export PATH=$PATH:/root/.local/bin && \
    echo "Verifying uv command is available..." && \
    (uv --version || (echo "Error: 'uv' command failed. uv might not be installed correctly or not in PATH." && exit 1))

# Clean up build-time system dependencies
RUN apt-get purge -y --auto-remove curl && rm -rf /var/lib/apt/lists/*

# Install curl again so it's available at runtime for entrypoint.sh
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy uv configuration files from the parent directory
COPY ../uv.lock /app/uv.lock
COPY ../pyproject.toml /app/pyproject.toml
COPY ../.python-version /app/.python-version

# Install Python dependencies
RUN uv sync

# Copy the rest of the application code, artifacts, and faiss_index into the working directory

COPY ../index/faiss_index /app/index/faiss_index
COPY ../app.py /app/app.py
COPY ../src/rag.py /app/src/rag.py
COPY ../src/prompts.py /app/src/prompts.py
COPY ../containerize/entrypoint.sh /app/entrypoint.sh

# Expose the port your Streamlit application will run on
EXPOSE 8000

# Use entrypoint script to start Ollama, pull models, and run Streamlit
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]