from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(path="qdrant_data")

if not client.collection_exists("disasters_audio"):
    client.create_collection(
        collection_name="disasters_audio",
        vectors_config=VectorParams(
            size=384,   # SAME as text embeddings
            distance=Distance.COSINE
        )
    )

print("Audio collection ready!")
