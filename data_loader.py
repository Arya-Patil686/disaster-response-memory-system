from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer

client = QdrantClient(path="qdrant_data")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create collection if not exists
if not client.collection_exists("disasters"):
    client.create_collection(
        collection_name="disasters",
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

disasters = [
    {
        "id": 1,
        "text": "Severe flooding in Pune caused hospital shortages",
        "location": "Pune",
        "type": "Flood",
        "year": 2023,
        "importance": 1.0
    },
    {
        "id": 2,
        "text": "Earthquake in Turkey damaged transport routes",
        "location": "Turkey",
        "type": "Earthquake",
        "year": 2022,
        "importance": 0.8
    }
]

points = []
for d in disasters:
    vector = model.encode(d["text"]).tolist()
    points.append(
        PointStruct(
            id=d["id"],
            vector=vector,
            payload=d
        )
    )

client.upsert(collection_name="disasters", points=points)

print("Initial disaster memory loaded!")
