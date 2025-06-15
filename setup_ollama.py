'''
Pull the LLM model/models and embeddings model from Ollama.

You can pull specific models by changing the model names in the subprocess commands.

Dependencies:
# ollama
'''

import subprocess
subprocess.run(["ollama", "pull", "nomic-embed-text"], check=True)
subprocess.run(["ollama", "pull", "llama3.2:latest"], check=True)