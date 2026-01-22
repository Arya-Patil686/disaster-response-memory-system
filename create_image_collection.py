from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(path="qdrant_data")

if not client.collection_exists("disasters_images"):
    client.create_collection(
        collection_name="disasters_images",
        vectors_config=VectorParams(
            size=512,
            distance=Distance.COSINE
        )
    )

print("Image collection created successfully!")
