#!/bin/bash
set -e

# Start the Ollama server in background
ollama serve &

# Wait for the server to start (adjust timing if needed)
sleep 5

# Run your command automatically
ollama run tinyllama:1.1b

# Keep container running to keep server alive
wait
