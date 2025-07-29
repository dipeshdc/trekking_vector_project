import json
import httpx
from fastapi import HTTPException


OLLAMA_API_URL = "http://llmservice:11434/api/generate"
MODEL_NAME = "tinyllama:1.1b" 

async def generate_text(query, trekList):
    json_str = json.dumps(trekList, indent=2)
    
    prompt = f"""
    Generate a concise and informative summary (around 50 words) of the following trek data. The response should be clear, engaging, and not reference any user or query. Focus on key highlights and usefulness.

    Trek Information:
    {json_str}
    """

        
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(OLLAMA_API_URL, json=payload, timeout=90.0)
            response.raise_for_status()
            data = response.json()
            generated_text = data.get("response", "")
            return {"result": generated_text}
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Ollama API error: {e}")