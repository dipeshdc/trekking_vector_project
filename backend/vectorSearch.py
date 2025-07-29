from qdrant_client import QdrantClient,models
from sentence_transformers import SentenceTransformer

client = QdrantClient(url="http://qdrant:6333")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

def searchFromKeyword(keyword):
    hits = client.query_points(
        collection_name="trekking_data",
        query=encoder.encode(keyword).tolist(),
        limit=3,
    ).points
    return hits
