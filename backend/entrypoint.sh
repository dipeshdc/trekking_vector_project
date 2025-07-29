#!/bin/bash
set -e

echo "Waiting for Qdrant..."

until curl -s http://qdrant:6333/collections > /dev/null; do
  sleep 1
done

echo "Qdrant is up. Running init script..."
python embed.py

echo "Starting FastAPI server..."
uvicorn apiForTaking:app --host 0.0.0.0 --port 8000
