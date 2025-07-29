
OLLAMA_API_URL = "http://llmservice:11434/api/generate"
MODEL_NAME = "deepseek-r1:1.5b" 

async def generate_text(query, trekList):
    json_str = json.dumps(request.data_list, indent=2)
    
    prompt = f"""
    You are a helpful trek assistant. The user query is: '{query}'.

    Below is a list of JSON objects representing the top results related to the user's query:

    {json_str}

    Please carefully summarize these results and generate a clear, informative, and user-friendly response.
    """

        
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": false
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(OLLAMA_API_URL, json=payload, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            generated_text = data.get("response", "")
            return {"result": generated_text}
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Ollama API error: {e}")