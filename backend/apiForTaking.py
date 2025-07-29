from fastapi import FastAPI, Query
from vectorSearch import searchFromKeyword
from pydanticClass import SearchResponse
from fastapi.middleware.cors import CORSMiddleware 
from llmResponse import generate_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://52.23.247.167:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"msg": "Welcome here!"}

@app.get("/api/search", response_model=SearchResponse)
def search(query: str = Query(...)):
    hits = searchFromKeyword(query)
    payloads = [hit.payload for hit in hits]
    text_generated = generate_text(query, trekList)
    return {"result": text_generated}