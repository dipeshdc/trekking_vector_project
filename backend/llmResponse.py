import json
import httpx
from fastapi import HTTPException


OLLAMA_API_URL = "http://llmservice:11434/api/generate"
MODEL_NAME = "tinyllama:1.1b" 

async def generate_text(query, trekList):
    json_str = json.dumps(trekList, indent=2)
    
    prompt = f"""
    Summarize the trek data below in ~50 words. Be clear and informative. Don't mention the user. Answer according to query of user "{query}" taking inference from the below data.

    Data:
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