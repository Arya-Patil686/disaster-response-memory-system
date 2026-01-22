from qdrant_client import QdrantClient

client = QdrantClient(path="qdrant_data")

points, _ = client.scroll(
    collection_name="disasters",
    limit=50,
    with_payload=True
)

for p in points:
    new_importance = round(p.payload["importance"] * 0.9, 2)
    client.set_payload(
        collection_name="disasters",
        payload={"importance": new_importance},
        points=[p.id]
    )

print("Memory decay applied.")
