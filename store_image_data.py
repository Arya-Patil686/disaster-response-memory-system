from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from image_embeddings import image_to_vector

client = QdrantClient(path="qdrant_data")

image_vector = image_to_vector("images/flood_pune.jpg")

point = PointStruct(
    id=100,
    vector=image_vector,
    payload={
        "type": "Flood",
        "location": "Pune",
        "modality": "image",
        "importance": 1.0,
        "description": "Satellite image showing flood damage in Pune"
    }
)

client.upsert(
    collection_name="disasters_images",
    points=[point]
)

print("Image disaster memory stored successfully!")
