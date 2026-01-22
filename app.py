from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from fastapi import FastAPI
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer

app = FastAPI(title="Disaster Response Memory System")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

client = QdrantClient(path="qdrant_data")
model = SentenceTransformer("all-MiniLM-L6-v2")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/search")
def search_disasters(query: str, location: str):
    try:
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

        if not results or not results.points:
            return {
                "query": query,
                "location": location,
                "results": [],
                "message": "No matching disaster records found"
            }

        cleaned_results = []

        for r in results.points:
            payload = r.payload or {}

            cleaned_results.append({
                "text": payload.get("text", "N/A"),
                "type": payload.get("type", "N/A"),
                "location": payload.get("location", "N/A"),
                "importance": payload.get("importance", 0.0),
                "modality": payload.get("modality", "text")
            })

        cleaned_results = sorted(
            cleaned_results,
            key=lambda x: x["importance"],
            reverse=True
        )

        return {
            "query": query,
            "location": location,
            "results": cleaned_results
        }

    except Exception as e:
        return {
            "error": "Search failed",
            "details": str(e)
        }
