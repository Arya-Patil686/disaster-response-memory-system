from qdrant_client import QdrantClient
from image_embeddings import image_to_vector

client = QdrantClient(path="qdrant_data")

query_vector = image_to_vector("images/flood_pune.jpg")

results = client.query_points(
    collection_name="disasters_images",
    query=query_vector,
    limit=3
)

print("\nImage-based search results:\n")
for r in results.points:
    print(r.payload)
