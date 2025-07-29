import csv
from qdrant_client import QdrantClient,models
from sentence_transformers import SentenceTransformer


documents = []


with open("TrekData.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    seen_treks = set()
    for row in reader:
        row.pop("", None)
        trek_name = row.get("Trek", "").strip()
        if trek_name and trek_name not in seen_treks:
            seen_treks.add(trek_name)
            documents.append(row)

client = QdrantClient(url="http://localhost:6333")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

client.create_collection(
    collection_name="trekking_data",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),
        distance=models.Distance.COSINE,
    ),
)

client.upload_points(
    collection_name="trekking_data",
    points=[
        models.PointStruct(
            id=idx,
            vector=encoder.encode(
                f"Trek: {doc.get('Trek', '')}. "
                f"Cost: {doc.get('Cost', '')}. "
                f"Duration: {doc.get('Time', '')}. "
                f"Grade: {doc.get('Trip Grade', '')}. "
            ).tolist(),
            payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)
