from fastapi import FastAPI
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer

app = FastAPI(title="Disaster Response Memory System")

client = QdrantClient(path="qdrant_data")
model = SentenceTransformer("all-MiniLM-L6-v2")


@app.get("/")
def home():
    return {"message": "Disaster Response Memory System is running"}


@app.get("/search")
def search_disasters(query: str, location: str):
    query_vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name="disasters",
        query=query_vector,
        limit=5,
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="location",
                    match=MatchValue(value=location)
                )
            ]
        )
    )

    reinforced_results = []

    for r in results.points:
        current_importance = r.payload["importance"]

        # Reinforcement: increase importance
        new_importance = round(min(current_importance + 0.1, 2.0), 2)

        client.set_payload(
            collection_name="disasters",
            payload={"importance": new_importance},
            points=[r.id]
        )

        r.payload["importance"] = new_importance
        reinforced_results.append(r)

    sorted_results = sorted(
        reinforced_results,
        key=lambda x: x.payload["importance"],
        reverse=True
    )

    return {
        "query": query,
        "location": location,
        "results": [r.payload for r in sorted_results]
    }

