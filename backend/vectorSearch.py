from qdrant_client import QdrantClient,models
from sentence_transformers import SentenceTransformer

client = QdrantClient(url="http://localhost:6333")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

def searchFromKeyword(keyword):
    hits = client.query_points(
        collection_name="trekking_data",
        query=encoder.encode(keyword).tolist(),
        limit=3,
    ).points
    return hits

# hits = client.query_points(
#     collection_name="trekking_data",
#     query=encoder.encode("What is the most expensive one?").tolist(),
#     limit=3,
# ).points

# for hit in hits:
#     print("ID:", hit.id)
#     print("Payload:", hit.payload)
#     print("Score:", hit.score)
#     print("-" * 40)

